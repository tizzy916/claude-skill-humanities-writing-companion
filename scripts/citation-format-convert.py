#!/usr/bin/env python3
"""
citation-format-convert.py — 引用格式转换 / Citation format converter

Converts a bibliography (BibTeX or simple structured input) between four major
academic citation styles used in the humanities:

    Chicago (Author-Date) ↔ MLA ↔ APA 7 ↔ GB/T 7714 (顺序编码制 / numeric sequential system)

用法 / Usage:
    python3 citation-format-convert.py <input.bib> --to <chicago|mla|apa|gb7714>
    python3 citation-format-convert.py <input.bib> --to apa --out output.txt

Supported entry types: @book, @article, @incollection, @inbook, @inproceedings, @thesis.

Design notes:
    - Not a replacement for BibLaTeX / CSL. Use those if your tooling supports them.
    - This script is for the in-flight case: you have a draft with mixed inline citation
      hints, and you want a clean references list in one specific style for submission.
    - Crucially, the script does NOT change inline citations within the prose itself —
      that requires understanding the document structure. Use it for the reference list.
    - Balanced-brace parser: handles nested braces (title = {The {DNA} Story}),
      single-line entries, and quoted values. Entries that cannot be parsed are
      REPORTED on stderr and skipped — never silently merged or corrupted.

Exit codes:
    0 — all entries parsed and converted
    1 — some entries could not be parsed (reported on stderr; output contains the rest)
    2 — no entries parsed at all, or input file unreadable

诚实声明 / Honest disclaimer:
    Each style has many subtle rules and journal-specific variants. This converter
    handles the common cases. ALWAYS check the output against your target journal's
    style guide before submission. Treat output as a starting draft, not final copy.
"""

import argparse
import re
import sys
from pathlib import Path


# ----------------------------- BibTeX parsing -----------------------------

_ENTRY_HEAD_RE = re.compile(r'@(\w+)\s*\{')
_FIELD_NAME_RE = re.compile(r'([\w\-]+)\s*=\s*')

# Non-bibliographic BibTeX constructs — skipped, they are not entries
_NON_ENTRIES = {"comment", "string", "preamble"}


def _clean_value(raw):
    """Normalize a field value: collapse whitespace, drop BibTeX grouping braces
    (they protect capitalization; the content stays: {The {DNA} Story} → The DNA Story)."""
    value = re.sub(r'\s+', ' ', raw).strip()
    return value.replace('{', '').replace('}', '').strip()


def _parse_fields(body):
    """Parse 'name = value' pairs from an entry body using balanced-brace counting.
    Handles {nested {braces}}, "quoted values", and bare values (year = 2020).
    Raises ValueError with a description when the body cannot be parsed."""
    fields = {}
    k, n = 0, len(body)
    while k < n:
        while k < n and (body[k].isspace() or body[k] == ','):
            k += 1
        if k >= n:
            break
        m = _FIELD_NAME_RE.match(body, k)
        if not m:
            raise ValueError(f"cannot parse field near: {body[k:k+40]!r}")
        name = m.group(1).lower()
        k = m.end()
        if k >= n:
            raise ValueError(f"field '{name}' has no value")
        c = body[k]
        if c == '{':
            depth, k = 1, k + 1
            start = k
            while k < n and depth > 0:
                if body[k] == '{':
                    depth += 1
                elif body[k] == '}':
                    depth -= 1
                k += 1
            if depth != 0:
                raise ValueError(f"unbalanced braces in field '{name}'")
            fields[name] = _clean_value(body[start:k - 1])
        elif c == '"':
            k += 1
            start = k
            depth = 0
            while k < n:
                ch = body[k]
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                elif ch == '"' and depth == 0:
                    break
                k += 1
            if k >= n:
                raise ValueError(f"unterminated quoted value in field '{name}'")
            fields[name] = _clean_value(body[start:k])
            k += 1
        else:
            m2 = re.match(r'[^,\n]+', body[k:])
            fields[name] = _clean_value(m2.group(0))
            k += m2.end()
    return fields


def parse_bibtex(text):
    """Parse BibTeX with balanced-brace scanning (nested braces and single-line
    entries both work). Returns (entries, problems):
        entries  — list of dicts (one per successfully parsed entry)
        problems — list of human-readable strings for entries that could NOT be
                   parsed. They are reported, never silently dropped or merged."""
    entries = []
    problems = []
    i, n = 0, len(text)
    while True:
        at = text.find('@', i)
        if at == -1:
            break
        line_no = text.count('\n', 0, at) + 1
        m = _ENTRY_HEAD_RE.match(text, at)
        if not m:
            # '@' that does not open a brace-delimited entry (e.g. an email in a
            # comment, or the unsupported @entry(...) paren form) — note and move on.
            frag = text[at:at + 30].split('\n')[0]
            problems.append(f"L{line_no}: '@' is not a parsable entry header ({frag!r}) — skipped")
            i = at + 1
            continue
        etype = m.group(1).lower()
        if etype in _NON_ENTRIES:
            # @comment/@string/@preamble: skip the balanced block silently
            depth, j = 1, m.end()
            while j < n and depth > 0:
                if text[j] == '{':
                    depth += 1
                elif text[j] == '}':
                    depth -= 1
                j += 1
            i = j
            continue
        depth, j = 1, m.end()
        while j < n and depth > 0:
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
            j += 1
        if depth != 0:
            problems.append(f"@{etype} at L{line_no}: unbalanced braces to end of file — entry skipped")
            # Resync at the next line starting with '@' to salvage later entries
            nxt = text.find('\n@', at)
            if nxt == -1:
                break
            i = nxt + 1
            continue
        body = text[m.end():j - 1]
        comma = body.find(',')
        if comma == -1:
            key, field_src = body.strip(), ""
        else:
            key, field_src = body[:comma].strip(), body[comma + 1:]
        if not key:
            problems.append(f"@{etype} at L{line_no}: missing citation key — entry skipped")
            i = j
            continue
        try:
            fields = _parse_fields(field_src)
        except ValueError as exc:
            problems.append(f"@{etype}{{{key}}} at L{line_no}: {exc} — entry skipped (not silently merged)")
            i = j
            continue
        entry = {"_type": etype, "_key": key}
        entry.update(fields)
        entries.append(entry)
        i = j
    return entries, problems


def parse_authors(author_str):
    """Split 'A and B and C' or 'A; B; C' into list of (last, first) tuples.
    Handles 'Last, First' and 'First Last' formats."""
    if not author_str:
        return []
    parts = re.split(r'\s+and\s+|;\s*', author_str)
    out = []
    for p in parts:
        p = p.strip()
        if "," in p:
            last, first = [s.strip() for s in p.split(",", 1)]
        else:
            tokens = p.split()
            if len(tokens) == 1:
                last, first = tokens[0], ""
            else:
                last = tokens[-1]
                first = " ".join(tokens[:-1])
        out.append((last, first))
    return out


def initials(first_name):
    """John Andrew → J. A."""
    if not first_name:
        return ""
    return " ".join(t[0] + "." for t in first_name.split() if t)


# ----------------------------- Formatters -----------------------------

def format_authors_chicago(authors, paper_type="book"):
    """Chicago Author-Date: first author Last, First; others First Last; & before last."""
    if not authors:
        return ""
    formatted = []
    for i, (last, first) in enumerate(authors):
        if i == 0:
            formatted.append(f"{last}, {first}".rstrip(", "))
        else:
            formatted.append(f"{first} {last}".strip())
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f"{formatted[0]}, and {formatted[1]}"
    return ", ".join(formatted[:-1]) + ", and " + formatted[-1]


def format_authors_mla(authors):
    """MLA: first author Last, First; others First Last; et al. if 3+."""
    if not authors:
        return ""
    first = authors[0]
    first_str = f"{first[0]}, {first[1]}".rstrip(", ")
    if len(authors) == 1:
        return first_str
    if len(authors) == 2:
        second = authors[1]
        return f"{first_str}, and {second[1]} {second[0]}".strip()
    return f"{first_str}, et al."


def format_authors_apa(authors):
    """APA 7: all authors Last, F. M.; & before last (up to 20)."""
    if not authors:
        return ""
    formatted = []
    for last, first in authors:
        inits = initials(first)
        formatted.append(f"{last}, {inits}".rstrip(", "))
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f"{formatted[0]}, & {formatted[1]}"
    return ", ".join(formatted[:-1]) + ", & " + formatted[-1]


def format_authors_gb7714(authors, max_show=3):
    """GB/T 7714: all authors Last F. (no comma between last and first initials);
    , (separator); 等 / et al. if more than max_show."""
    if not authors:
        return ""
    formatted = []
    for last, first in authors[:max_show]:
        inits = initials(first).replace(".", "").replace(" ", "")
        formatted.append(f"{last} {inits}".strip())
    s = ", ".join(formatted)
    if len(authors) > max_show:
        s += ", 等"
    return s


# ----------------------------- Entry formatters per style -----------------------------

def chicago(entry):
    """Chicago Author-Date reference-list format."""
    authors = parse_authors(entry.get("author", ""))
    auth = format_authors_chicago(authors)
    year = entry.get("year", "n.d.")
    title = entry.get("title", "").strip("{}")
    t = entry["_type"]
    if t == "book":
        place = entry.get("address", "")
        pub = entry.get("publisher", "")
        return f"{auth}. {year}. *{title}*. {place}: {pub}.".replace(" : ", ": ")
    if t == "article":
        journal = entry.get("journal", "")
        vol = entry.get("volume", "")
        num = entry.get("number", "")
        pages = entry.get("pages", "")
        loc = f"{vol}" + (f", no. {num}" if num else "") + (f": {pages}" if pages else "")
        return f'{auth}. {year}. "{title}." *{journal}* {loc}.'
    if t in ("incollection", "inbook"):
        booktitle = entry.get("booktitle", "")
        editor = entry.get("editor", "")
        pages = entry.get("pages", "")
        place = entry.get("address", "")
        pub = entry.get("publisher", "")
        ed_str = f", edited by {editor}" if editor else ""
        return f'{auth}. {year}. "{title}." In *{booktitle}*{ed_str}, {pages}. {place}: {pub}.'
    return f"{auth}. {year}. {title}."


def mla(entry):
    """MLA 9 works-cited format."""
    authors = parse_authors(entry.get("author", ""))
    auth = format_authors_mla(authors)
    title = entry.get("title", "").strip("{}")
    t = entry["_type"]
    year = entry.get("year", "")
    if t == "book":
        place = entry.get("address", "")
        pub = entry.get("publisher", "")
        return f"{auth}. *{title}*. {pub}, {year}."
    if t == "article":
        journal = entry.get("journal", "")
        vol = entry.get("volume", "")
        num = entry.get("number", "")
        pages = entry.get("pages", "")
        loc = f"vol. {vol}" + (f", no. {num}" if num else "") + (f", {year}" if year else "") + (f", pp. {pages}" if pages else "")
        return f'{auth}. "{title}." *{journal}*, {loc}.'
    if t in ("incollection", "inbook"):
        booktitle = entry.get("booktitle", "")
        editor = entry.get("editor", "")
        pages = entry.get("pages", "")
        pub = entry.get("publisher", "")
        ed_str = f"edited by {editor}, " if editor else ""
        return f'{auth}. "{title}." *{booktitle}*, {ed_str}{pub}, {year}, pp. {pages}.'
    return f"{auth}. {title}. {year}."


def apa(entry):
    """APA 7 reference-list format."""
    authors = parse_authors(entry.get("author", ""))
    auth = format_authors_apa(authors)
    year = entry.get("year", "n.d.")
    title = entry.get("title", "").strip("{}")
    t = entry["_type"]
    if t == "book":
        pub = entry.get("publisher", "")
        return f"{auth} ({year}). *{title}*. {pub}."
    if t == "article":
        journal = entry.get("journal", "")
        vol = entry.get("volume", "")
        num = entry.get("number", "")
        pages = entry.get("pages", "")
        loc = f"*{vol}*" + (f"({num})" if num else "") + (f", {pages}" if pages else "")
        return f'{auth} ({year}). {title}. *{journal}*, {loc}.'
    if t in ("incollection", "inbook"):
        booktitle = entry.get("booktitle", "")
        editor = entry.get("editor", "")
        pages = entry.get("pages", "")
        pub = entry.get("publisher", "")
        ed_str = f"In {editor} (Ed.), " if editor else "In "
        pp_str = f" (pp. {pages})" if pages else ""
        return f'{auth} ({year}). {title}. {ed_str}*{booktitle}*{pp_str}. {pub}.'
    return f"{auth} ({year}). {title}."


def gb7714(entry):
    """GB/T 7714 顺序编码制 / numeric sequential system reference-list format."""
    authors = parse_authors(entry.get("author", ""))
    auth = format_authors_gb7714(authors)
    year = entry.get("year", "")
    title = entry.get("title", "").strip("{}")
    t = entry["_type"]
    type_marker = {
        "book": "[M]",
        "article": "[J]",
        "incollection": "[M]//",
        "inbook": "[M]//",
        "inproceedings": "[C]//",
        "thesis": "[D]",
        "phdthesis": "[D]",
        "mastersthesis": "[D]",
        "report": "[R]",
        "online": "[EB/OL]",
    }.get(t, "[Z]")
    if t == "book":
        place = entry.get("address", "")
        pub = entry.get("publisher", "")
        return f"{auth}. {title}{type_marker}. {place}: {pub}, {year}."
    if t == "article":
        journal = entry.get("journal", "")
        vol = entry.get("volume", "")
        num = entry.get("number", "")
        pages = entry.get("pages", "")
        vn = f"{year},{vol}" + (f"({num})" if num else "") + (f":{pages}" if pages else "")
        return f"{auth}. {title}{type_marker}. {journal}, {vn}."
    if t in ("incollection", "inbook"):
        booktitle = entry.get("booktitle", "")
        editor = entry.get("editor", "")
        pages = entry.get("pages", "")
        place = entry.get("address", "")
        pub = entry.get("publisher", "")
        ed_str = f"{editor}. " if editor else ""
        return f"{auth}. {title}{type_marker}{ed_str}{booktitle}. {place}: {pub}, {year}: {pages}."
    return f"{auth}. {title}{type_marker}. {year}."


FORMATTERS = {
    "chicago": chicago,
    "mla": mla,
    "apa": apa,
    "gb7714": gb7714,
}


# ----------------------------- CLI -----------------------------

def main():
    parser = argparse.ArgumentParser(description="Convert BibTeX bibliography to one of: chicago, mla, apa, gb7714")
    parser.add_argument("input", help="Input .bib file")
    parser.add_argument("--to", choices=list(FORMATTERS.keys()), required=True,
                        help="Target citation style")
    parser.add_argument("--out", default=None, help="Output file (default: stdout)")
    parser.add_argument("--sort", default="author", choices=["author", "year", "key", "input"],
                        help="Sort order (default: by first author)")
    args = parser.parse_args()

    path = Path(args.input)
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"[!] Input file does not exist: {path}", file=sys.stderr)
        sys.exit(2)
    except IsADirectoryError:
        print(f"[!] Input is a directory, expected a .bib file: {path}", file=sys.stderr)
        sys.exit(2)
    except OSError as exc:
        print(f"[!] Cannot read input file {path}: {exc}", file=sys.stderr)
        sys.exit(2)

    entries, problems = parse_bibtex(text)
    for p in problems:
        print(f"[!] {p}", file=sys.stderr)
    if not entries:
        print("[!] No entries parsed. Check input formatting.", file=sys.stderr)
        sys.exit(2)

    if args.sort == "author":
        entries.sort(key=lambda e: parse_authors(e.get("author", ""))[0][0]
                     if e.get("author") else "")
    elif args.sort == "year":
        entries.sort(key=lambda e: e.get("year", ""))
    elif args.sort == "key":
        entries.sort(key=lambda e: e["_key"])

    fmt = FORMATTERS[args.to]
    lines = []
    for e in entries:
        try:
            lines.append(fmt(e))
        except Exception as exc:
            print(f"[!] Error formatting {e.get('_key', '?')}: {exc}", file=sys.stderr)

    output = "\n\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(output, encoding="utf-8")
        print(f"[✓] Wrote {len(lines)} entries to {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(output)

    if problems:
        print(f"[!] {len(problems)} entr{'y' if len(problems) == 1 else 'ies'} could not be parsed "
              f"(listed above) and are NOT in the output.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
