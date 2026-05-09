#!/usr/bin/env bash
# ai-trace-scan.sh — 扫描文档中的 AI 套话与学术八股
# 来源：references/ai-trace-checklist.md
# 用法：./ai-trace-scan.sh <file.md>
#       ./ai-trace-scan.sh path/to/paper/  (递归扫描目录)

set -euo pipefail

if [ $# -lt 1 ]; then
    cat <<EOF
用法：$0 <file.md | directory>

扫描以下两类问题：
  1. 高频套话（出现即标记）——值得注意的是 / 不难发现 / 综上所述 等
  2. 过度堆砌的连接词（>3 次警告）——此外 / 同时 / 另外 等

输出：每条匹配的行号 + 行内容
EOF
    exit 1
fi

INPUT="$1"
[ -e "$INPUT" ] || { echo "路径不存在：$INPUT" >&2; exit 1; }

# 高频套话（出现即标记）— 与 references/ai-trace-checklist.md 同步
SINGLE_PATTERNS=(
    "值得注意的是"
    "不难发现"
    "这引发了我们的思考"
    "综上所述"
    "总而言之"
    "填补了.*空白"
    "具有重要的理论和实践意义"
    "本文旨在"
    "鉴于此"
    "该.*被广泛运用于"
    "被认为是"
    "诚然.*但是"
)

# 频次警告（超阈值才提示）
FREQUENCY_PATTERNS=(
    "此外"
    "同时"
    "另外"
    "与此同时"
    "进一步来说"
    "在此基础上"
)
FREQ_THRESHOLD=3

# grep 参数：递归 + 只看 .md
if [ -d "$INPUT" ]; then
    GREP_OPTS="-rn --include=*.md"
else
    GREP_OPTS="-n"
fi

echo "=== AI 痕迹扫描 · $INPUT ==="
echo ""

found_any=0

echo "## 一、高频套话（出现即审视）"
echo ""
for pat in "${SINGLE_PATTERNS[@]}"; do
    if matches=$(grep $GREP_OPTS -E "$pat" "$INPUT" 2>/dev/null); then
        found_any=1
        echo "▶ 「$pat」"
        echo "$matches" | sed 's/^/    /'
        echo ""
    fi
done

echo "## 二、连接词频次警告（阈值 >$FREQ_THRESHOLD 次/文件）"
echo ""
for word in "${FREQUENCY_PATTERNS[@]}"; do
    if [ -d "$INPUT" ]; then
        count=$(grep -rh --include=*.md "$word" "$INPUT" 2>/dev/null | wc -l | tr -d ' ')
    else
        count=$(grep -h "$word" "$INPUT" 2>/dev/null | wc -l | tr -d ' ')
    fi
    if [ "$count" -gt "$FREQ_THRESHOLD" ]; then
        echo "⚠ 「$word」出现 $count 次（阈值 $FREQ_THRESHOLD）"
        grep $GREP_OPTS "$word" "$INPUT" 2>/dev/null | sed 's/^/    /' | head -5
        [ "$count" -gt 5 ] && echo "    ... (仅显示前 5 处)"
        echo ""
        found_any=1
    fi
done

if [ "$found_any" -eq 0 ]; then
    echo "✅ 未发现明显 AI 痕迹或八股套话"
else
    echo ""
    echo "---"
    echo "💡 排查原则：每一处都问自己——这是我有意选择的表达，还是无意识的默认？"
    echo "   详见 references/ai-trace-checklist.md"
fi
