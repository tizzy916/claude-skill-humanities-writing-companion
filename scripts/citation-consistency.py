#!/usr/bin/env python3
"""
citation-consistency.py — 引用格式一致性扫描

用法：
    python3 citation-consistency.py <file.md>

检查项：
    1. 括号类型混用（半角 () vs 全角 （））
    2. 引用内逗号混用（半角 , vs 全角 ，）
    3. 多作者连接词不统一（& / and / 与 / 和）
    4. 同一文献被引用时姓名形式不一致（中文译名 vs 英文原姓）
    5. 页码格式不统一（p. X / p.X / 第 X 页）

注意：
    - 这是一个启发式扫描器，可能有少量误报（尤其是不规则引用）
    - 仅检查"格式不一致"，不检查"是否符合特定引用规范"（APA / Chicago / GB/T 7714）
    - 全文/规范层面的检查，请配合 references/project-management.md 中的引用格式速查使用
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

    issues.append(f"引用统计：英文形式 (Author, year) {en_hits} 处 / 中文形式 （作者，年份） {zh_hits} 处")
    issues.append("")

    if en_hits > 0 and zh_hits > 0:
        minority = min(en_hits, zh_hits)
        majority = max(en_hits, zh_hits)
        ratio = minority / majority if majority > 0 else 0
        if ratio > 0.05:
            issues.append(f"⚠ 括号类型混用：少数派占比 {ratio:.1%}（建议全文统一为一种）")

    for i, line in enumerate(lines, 1):
        for m in MIX_HALF_PAREN_FULL_COMMA.finditer(line):
            issues.append(f"  L{i}: 半角括号 + 全角逗号 → {m.group(0)}")
        for m in MIX_FULL_PAREN_HALF_COMMA.finditer(line):
            issues.append(f"  L{i}: 全角括号 + 半角逗号 → {m.group(0)}")

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
        issues.append(f"⚠ 多作者连接词不统一：{used}")
        issues.append("  建议根据所选引用格式（APA 用 & / GB/T 7714 用 ， 等）统一全文")

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
        issues.append("⚠ 同一年份的引用被混用中英文姓名（可能是同一文献的不同写法）：")
        for year, refs in name_lang_conflicts[:5]:
            issues.append(f"  {year}: {sorted(refs)}")
        if len(name_lang_conflicts) > 5:
            issues.append(f"  ... 共 {len(name_lang_conflicts)} 个年份有此问题")

    page_formats = {
        'p. X':   len(re.findall(r'\bp\.\s+\d', text)),
        'pp. X-Y': len(re.findall(r'\bpp\.\s+\d', text)),
        'p.X (无空格)':  len(re.findall(r'\bp\.\d', text)),
        '第 X 页': len(re.findall(r'第\s*\d+\s*页', text)),
        '第 X-Y 页': len(re.findall(r'第\s*\d+\s*[-–]\s*\d+\s*页', text)),
    }
    used_pages = {k: v for k, v in page_formats.items() if v > 0}
    if len(used_pages) > 1:
        issues.append("")
        issues.append(f"⚠ 页码格式不统一：{used_pages}")

    return issues


def main():
    if len(sys.argv) < 2:
        print(f"用法：{sys.argv[0]} <file.md>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"文件不存在：{filepath}", file=sys.stderr)
        sys.exit(1)

    issues = scan(text)

    print(f"=== 引用格式一致性扫描 · {filepath} ===\n")

    issue_count = sum(1 for line in issues if line.startswith('⚠') or '→' in line)

    if issues:
        for line in issues:
            print(line)

    print()
    if issue_count == 0:
        print("✅ 未发现明显的格式不一致")
    else:
        print(f"共发现约 {issue_count} 处需要审查的格式问题")
    print()
    print("注：此扫描仅检测'不一致'，不评判'是否符合特定规范'。")
    print("    全文规范检查请对照 _writing-config/引用格式速查.md。")


if __name__ == '__main__':
    main()
