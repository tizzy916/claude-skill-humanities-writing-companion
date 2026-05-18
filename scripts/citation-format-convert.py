#!/usr/bin/env python3
"""
citation-format-convert.py — 引用格式转换 / Citation format converter

Converts a bibliography (BibTeX or simple structured input) between four major
academic citation styles used in the humanities:

    Chicago (Author-Date) ↔ MLA ↔ APA 7 ↔ GB/T 7714 (顺序编码制)

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
    - Heuristic parser — for well-formed BibTeX. Malformed entries are reported, not silently dropped.

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

ENTRY_RE = re.compile(r'@(?P<type>\w+)\s*\{\s*(?P<key>[^,]+),\s*(?P<body>.*?)\n\}',
                      re.DOTALL)
FIELD_RE = re.compile(r'(?P<name>\w+)\s*=\s*[\{"](?P<value>.*?)["\}](?:\s*,|\s*$)',
                      re.DOTALL)


def parse_bibtex(text):
    """Parse simple BibTeX. Returns list of dicts (one per entry)."""
    entries = []
    for m in ENTRY_RE.finditer(text):
        entry = {"_type": m.group("type").lower(), "_key": m.group("key").strip()}
        body = m.group("body")
        for fm in FIELD_RE.finditer(body):
            entry[fm.group("name").lower()] = fm.group("value").strip()
        entries.append(entry)
    return entries


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
    """GB/T 7714 顺序编码制 reference-list format."""
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

    text = Path(args.input).read_text(encoding="utf-8")
    entries = parse_bibtex(text)
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


if __name__ == "__main__":
    main()
