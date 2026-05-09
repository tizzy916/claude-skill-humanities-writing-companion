#!/usr/bin/env bash
# pending-checks.sh — 提取论文项目中所有待核对 / 待讨论 / AI 不确定的标记
# 用法：./pending-checks.sh <path>   # path 可以是单个文件或论文项目目录

set -euo pipefail

INPUT="${1:-.}"

[ -e "$INPUT" ] || { echo "路径不存在：$INPUT" >&2; exit 1; }

if [ -d "$INPUT" ]; then
    GREP_OPTS="-rn --include=*.md"
else
    GREP_OPTS="-n"
fi

echo "=== 待办标记汇总 · $INPUT ==="
echo ""

scan_marker() {
    local label="$1"
    local pattern="$2"
    local desc="$3"

    echo "## $label"
    echo "_${desc}_"
    echo ""
    if matches=$(grep $GREP_OPTS -E "$pattern" "$INPUT" 2>/dev/null); then
        echo "$matches" | sed 's/^/  /'
    else
        echo "  （无）"
    fi
    echo ""
}

scan_marker "🔴 [待核对]" \
    "\[待核对\]" \
    "AI 凭记忆引用、未核实的事实、未确认的数据等——必须在投稿前清零"

scan_marker "🟡 ❓ 待讨论" \
    "❓ ?待讨论" \
    "需要作者本人决定的论证选择、理论方向问题"

scan_marker "🟢 [AI 草稿，待作者审阅]" \
    "\[AI 草稿，待作者审阅\]" \
    "AI 起草的段落，作者尚未审阅过——审阅后请删除标记"

scan_marker "🔵 >>> AI 不确定" \
    ">>>" \
    "AI 起草时拿不准的地方（概念理解 / 论证方向 / 引用选择）"

scan_marker "🟣 [作者微调]" \
    "\[作者微调\]" \
    "作者对 AI 修改建议的二次调整——是最精确的风格信号，应回写到写作风格档案"

# 汇总统计
echo "## 📊 汇总"
total=0
for marker in "\[待核对\]" "❓ ?待讨论" "\[AI 草稿，待作者审阅\]" ">>>" "\[作者微调\]"; do
    if [ -d "$INPUT" ]; then
        c=$(grep -rh --include=*.md -E "$marker" "$INPUT" 2>/dev/null | wc -l | tr -d ' ')
    else
        c=$(grep -h -E "$marker" "$INPUT" 2>/dev/null | wc -l | tr -d ' ')
    fi
    [ "$c" -gt 0 ] && total=$((total + c))
done
echo "  共 $total 处待办项"
