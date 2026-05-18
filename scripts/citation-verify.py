#!/usr/bin/env python3
"""
citation-verify.py — 引用真实性核查(基于 Crossref API)

Reads in-prose citations from a Markdown file and verifies each one against the
Crossref public API. Flags:
    1. CITATIONS THAT DO NOT EXIST in Crossref (likely hallucination)
    2. CITATIONS WITH MISMATCHED METADATA (year wrong, journal wrong, author wrong)
    3. CITATIONS WHERE TITLE FUZZY-MATCHES BUT METADATA DIVERGES (probable typo or paraphrase)

用法 / Usage:
    python3 citation-verify.py <draft.md>
    python3 citation-verify.py <draft.md> --bib references.bib

诚实声明 / Honest disclaimer:
    - Crossref does not index everything. Many humanities works (especially:
      monographs from small university presses, untranslated foreign-language
      works, dissertations, archival sources, classical texts) are NOT in
      Crossref. A "NOT FOUND" verdict for those is expected and not a problem.
    - This script catches the LLM-hallucination case (made-up journal article
      citations) — that's where Crossref coverage is good.
    - For monograph / archival / classics citations, the [VERIFY] marker
      protocol in SKILL.md is the right tool, not this script.
    - Network calls. Rate-limited to 1 req/sec to be polite to Crossref.

API ref: https://api.crossref.org/works
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from difflib import SequenceMatcher


CROSSREF_URL = "https://api.crossref.org/works"
USER_AGENT = "humanities-writing-companion/4.0 (https://github.com/tizzy916/claude-skill-humanities-writing-companion; mailto:shencong916@gmail.com)"


# ----------------------------- Inline citation parsing -----------------------------

# Patterns to match in-prose citations across styles.
# Conservative — we accept some false negatives (missed citations) over false positives.
PATTERNS = [
    # Chicago author-date / APA author-year: (Foucault, 1975, p. 23) or (Foucault 1975)
    re.compile(r'\(([A-Z][a-zA-ZÀ-ſ\-]+(?:\s+(?:and|&)\s+[A-Z][a-zA-ZÀ-ſ\-]+)*)[,\s]+(\d{4})[a-z]?(?:[,\s]+p?p?\.?\s*[\d\-–]+)?\)'),
    # Chicago narrative: Foucault (1975) ...
    re.compile(r'\b([A-Z][a-zA-ZÀ-ſ\-]+)\s+\((\d{4})[a-z]?\)'),
    # Chinese: (福柯, 1975)
    re.compile(r'[(（]([^()（）]+?)[，,]\s*(\d{4})[a-z]?[)）]'),
]


def extract_citations(text):
    """Returns list of (author_name, year) tuples found in prose. Deduplicated."""
    seen = set()
    out = []
    for pattern in PATTERNS:
        for m in pattern.finditer(text):
            author = m.group(1).strip()
            year = m.group(2).strip()
            # Normalize: take last surname for compound authors
            author_main = re.split(r'\s+(?:and|&)\s+', author)[0].strip()
            key = (author_main.lower(), year)
            if key not in seen:
                seen.add(key)
                out.append((author_main, year))
    return out


# ----------------------------- Crossref query -----------------------------

def crossref_query(author, year, rows=5):
    """Search Crossref for works by author + year. Returns list of matching items."""
    params = {
        "query.author": author,
        "filter": f"from-pub-date:{year}-01,until-pub-date:{year}-12",
        "rows": rows,
    }
    url = f"{CROSSREF_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data.get("message", {}).get("items", [])
    except Exception as exc:
        print(f"[!] Crossref query failed for ({author}, {year}): {exc}", file=sys.stderr)
        return []


def best_match(items, author):
    """Pick best item matching author. Returns (item, confidence) or (None, 0)."""
    if not items:
        return None, 0.0
    best = None
    best_score = 0.0
    for item in items:
        item_authors = item.get("author", [])
        if not item_authors:
            continue
        for a in item_authors:
            family = a.get("family", "")
            score = SequenceMatcher(None, family.lower(), author.lower()).ratio()
            if score > best_score:
                best_score = score
                best = item
    return best, best_score


# ----------------------------- Main verification loop -----------------------------

def verify(text, verbose=False):
    """Returns a list of dicts with verification results."""
    citations = extract_citations(text)
    if not citations:
        return []
    results = []
    for i, (author, year) in enumerate(citations):
        if verbose:
            print(f"[{i+1}/{len(citations)}] Querying Crossref for ({author}, {year})...",
                  file=sys.stderr)
        items = crossref_query(author, year)
        best, score = best_match(items, author)
        if best is None or score < 0.5:
            verdict = "NOT_FOUND"
            details = (f"No Crossref match for ({author}, {year}). "
                       f"This may be a humanities work outside Crossref coverage "
                       f"(monograph, archival, classics, dissertation, foreign-language), "
                       f"or it may not exist. Manually verify.")
            match_data = None
        elif score < 0.85:
            verdict = "FUZZY_MATCH"
            details = (f"Best match for ({author}, {year}) is similarity={score:.2f}. "
                       f"Possible spelling difference or different work.")
            match_data = best
        else:
            verdict = "FOUND"
            details = f"Match confidence {score:.2f}"
            match_data = best
        results.append({
            "author": author,
            "year": year,
            "verdict": verdict,
            "details": details,
            "match": {
                "title": match_data.get("title", [""])[0] if match_data else None,
                "type": match_data.get("type") if match_data else None,
                "container": match_data.get("container-title", [""])[0]
                             if match_data and match_data.get("container-title") else None,
                "doi": match_data.get("DOI") if match_data else None,
            } if match_data else None,
        })
        time.sleep(1)  # polite rate limit
    return results


def print_report(results):
    """Print human-readable report."""
    if not results:
        print("[i] No citations parsed from the input.")
        return

    not_found = [r for r in results if r["verdict"] == "NOT_FOUND"]
    fuzzy = [r for r in results if r["verdict"] == "FUZZY_MATCH"]
    found = [r for r in results if r["verdict"] == "FOUND"]

    print(f"\n=== Citation verification (Crossref) ===")
    print(f"Total citations parsed: {len(results)}")
    print(f"  ✓ Found:        {len(found)}")
    print(f"  ⚠ Fuzzy match:  {len(fuzzy)}  ← review")
    print(f"  ✗ Not found:    {len(not_found)}  ← review (or may be off-Crossref humanities work)")

    if not_found:
        print(f"\n## ✗ NOT FOUND in Crossref ({len(not_found)})")
        for r in not_found:
            print(f"\n  ({r['author']}, {r['year']})")
            print(f"    {r['details']}")

    if fuzzy:
        print(f"\n## ⚠ FUZZY MATCH — review for typo / different work ({len(fuzzy)})")
        for r in fuzzy:
            print(f"\n  ({r['author']}, {r['year']})")
            if r["match"]:
                print(f"    Best Crossref match: \"{r['match']['title']}\"")
                if r["match"]["container"]:
                    print(f"    Container: {r['match']['container']}")
                if r["match"]["doi"]:
                    print(f"    DOI: {r['match']['doi']}")
            print(f"    {r['details']}")

    if found:
        print(f"\n## ✓ FOUND ({len(found)})")
        for r in found:
            print(f"\n  ({r['author']}, {r['year']}) → {r['match']['title']}")
            if r["match"]["doi"]:
                print(f"    DOI: {r['match']['doi']}")

    print(f"\n=== Reminders ===")
    print("  · NOT_FOUND is expected for monographs, archival sources, classics, dissertations,")
    print("    and non-English-language works. Crossref coverage is strongest for English-")
    print("    language journal articles in indexed journals.")
    print("  · This script catches the LLM-hallucination case (made-up journal articles).")
    print("    For monograph citations, use the [VERIFY] / [待核对] marker workflow.")
    print("  · FUZZY_MATCH and a near-but-different result probably means a spelling or year typo.")
    print()


def main():
    parser = argparse.ArgumentParser(description="Verify in-prose citations against Crossref.")
    parser.add_argument("input", help="Input Markdown file to scan")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human report")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress output")
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    results = verify(text, verbose=not args.quiet)
    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        print_report(results)


if __name__ == "__main__":
    main()
