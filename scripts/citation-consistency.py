#!/usr/bin/env python3
"""
citation-consistency.py — Citation-format consistency scan

Usage:
    python3 citation-consistency.py <file.md>

Checks:
    1. Mixed parenthesis types (half-width () vs full-width （））
    2. Mixed commas inside citations (half-width , vs full-width ，)
    3. Inconsistent multi-author connectors (& / and / 与 / 和)
    4. Inconsistent name forms for the same reference (Chinese translated name vs English surname)
    5. Inconsistent page-number formats (p. X / p.X / 第 X 页)

Notes:
    - This is a heuristic scanner and may produce a few false positives (especially for irregular citations)
    - It only checks for "format inconsistency", not "conformance to a specific citation style" (APA / Chicago / GB/T 7714)
    - For full-text / style-level checks, use this alongside the citation-format quick reference in references/project-management.md
"""

import re
import sys
from collections import defaultdict


EN_INLINE = re.compile(r'\(([A-Z][\w\-\.\s&,]+?),?\s+(\d{4}[a-z]?)(?:,\s*p?p?\.?\s*[\d\-–]+)?\)')
ZH_INLINE = re.compile(r'（([^（）]+?)[，,]\s*(\d{4}[a-z]?)(?:[，,]\s*第?\s*[\d\-–]+\s*页?)?）')

MIX_HALF_PAREN_FULL_COMMA = re.compile(r'\(([^()]+?)，(\d{4})\)')
MIX_FULL_PAREN_HALF_COMMA = re.compile(r'（([^（）]+?),\s*(\d{4})）')


def scan(text):
    issues = []
    lines = text.split('\n')

    en_hits = sum(len(EN_INLINE.findall(line)) for line in lines)
    zh_hits = sum(len(ZH_INLINE.findall(line)) for line in lines)

    issues.append(f"Citation counts: English form (Author, year) {en_hits} / Chinese form （作者，年份） {zh_hits}")
    issues.append("")

    if en_hits > 0 and zh_hits > 0:
        minority = min(en_hits, zh_hits)
        majority = max(en_hits, zh_hits)
        ratio = minority / majority if majority > 0 else 0
        if ratio > 0.05:
            issues.append(f"⚠ Mixed parenthesis types: minority share {ratio:.1%} (recommend unifying to one form throughout)")

    for i, line in enumerate(lines, 1):
        for m in MIX_HALF_PAREN_FULL_COMMA.finditer(line):
            issues.append(f"  L{i}: half-width parens + full-width comma → {m.group(0)}")
        for m in MIX_FULL_PAREN_HALF_COMMA.finditer(line):
            issues.append(f"  L{i}: full-width parens + half-width comma → {m.group(0)}")

    connectors = {
        '&':   len(re.findall(r'\([^()]*&[^()]*\d{4}', text)),
        'and': len(re.findall(r'\([^()]*\sand\s[^()]*\d{4}', text)),
        '与':  len(re.findall(r'（[^（）]*与[^（）]*\d{4}', text)),
        '和':  len(re.findall(r'（[^（）]*和[^（）]*\d{4}', text)),
        '、':  len(re.findall(r'\([^()]*、[^()]*\d{4}', text))
              + len(re.findall(r'（[^（）]*、[^（）]*\d{4}', text)),
    }
    used = {k: v for k, v in connectors.items() if v > 0}
    if len(used) > 1:
        issues.append("")
        issues.append(f"⚠ Inconsistent multi-author connectors: {used}")
        issues.append("  Recommend unifying throughout per the chosen citation style (APA uses & / GB/T 7714 uses ， etc.)")

    year_to_names = defaultdict(set)
    for line in lines:
        for m in EN_INLINE.finditer(line):
            year_to_names[m.group(2)].add(('EN', m.group(1).strip()))
        for m in ZH_INLINE.finditer(line):
            year_to_names[m.group(2)].add(('ZH', m.group(1).strip()))

    name_lang_conflicts = []
    for year, refs in sorted(year_to_names.items()):
        langs = set(lang for lang, _ in refs)
        if len(langs) > 1:
            name_lang_conflicts.append((year, refs))

    if name_lang_conflicts:
        issues.append("")
        issues.append("⚠ Citations for the same year mix Chinese and English names (possibly different spellings of the same reference):")
        for year, refs in name_lang_conflicts[:5]:
            issues.append(f"  {year}: {sorted(refs)}")
        if len(name_lang_conflicts) > 5:
            issues.append(f"  ... {len(name_lang_conflicts)} years have this issue in total")

    page_formats = {
        'p. X':   len(re.findall(r'\bp\.\s+\d', text)),
        'pp. X-Y': len(re.findall(r'\bpp\.\s+\d', text)),
        'p.X (no space)':  len(re.findall(r'\bp\.\d', text)),
        '第 X 页': len(re.findall(r'第\s*\d+\s*页', text)),
        '第 X-Y 页': len(re.findall(r'第\s*\d+\s*[-–]\s*\d+\s*页', text)),
    }
    used_pages = {k: v for k, v in page_formats.items() if v > 0}
    if len(used_pages) > 1:
        issues.append("")
        issues.append(f"⚠ Inconsistent page-number formats: {used_pages}")

    return issues


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.md>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File does not exist: {filepath}", file=sys.stderr)
        sys.exit(1)

    issues = scan(text)

    print(f"=== Citation-format consistency scan · {filepath} ===\n")

    issue_count = sum(1 for line in issues if line.startswith('⚠') or '→' in line)

    if issues:
        for line in issues:
            print(line)

    print()
    if issue_count == 0:
        print("✅ No obvious format inconsistencies found")
    else:
        print(f"About {issue_count} format issue(s) need review")
    print()
    print("Note: this scan only detects 'inconsistency', it does not judge 'conformance to a specific style'.")
    print("    For full-text style checks, compare against _writing-config/引用格式速查.md.")


if __name__ == '__main__':
    main()
