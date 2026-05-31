#!/usr/bin/env bash
# pending-checks.sh — Extract all "to verify" / "to discuss" / "AI uncertain" markers in a paper project
# Usage: ./pending-checks.sh <path>   # path can be a single file or a paper project directory

set -euo pipefail

INPUT="${1:-.}"

[ -e "$INPUT" ] || { echo "Path does not exist: $INPUT" >&2; exit 1; }

if [ -d "$INPUT" ]; then
    GREP_OPTS="-rn --include=*.md"
else
    GREP_OPTS="-n"
fi

echo "=== Pending-marker summary · $INPUT ==="
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
        echo "  (none)"
    fi
    echo ""
}

scan_marker "🔴 [待核对] (to verify)" \
    "\[待核对\]" \
    "AI quotes from memory, unverified facts, unconfirmed data, etc. — must be cleared to zero before submission"

scan_marker "🟡 ❓ 待讨论 (to discuss)" \
    "❓ ?待讨论" \
    "Argumentation choices and theoretical-direction questions that the author must decide"

scan_marker "🟢 [AI 草稿，待作者审阅] (AI draft, pending author review)" \
    "\[AI 草稿，待作者审阅\]" \
    "Paragraphs drafted by AI that the author has not yet reviewed — remove the marker once reviewed"

scan_marker "🔵 >>> AI 不确定 (AI uncertain)" \
    ">>>" \
    "Spots where the AI was unsure while drafting (concept understanding / line of argument / choice of citation)"

scan_marker "🟣 [作者微调] (author tweak)" \
    "\[作者微调\]" \
    "The author's second-pass adjustments to AI suggestions — the most precise style signal; should be written back to the writing-style profile"

# Summary statistics
echo "## 📊 Summary"
total=0
for marker in "\[待核对\]" "❓ ?待讨论" "\[AI 草稿，待作者审阅\]" ">>>" "\[作者微调\]"; do
    if [ -d "$INPUT" ]; then
        c=$(grep -rh --include=*.md -E "$marker" "$INPUT" 2>/dev/null | wc -l | tr -d ' ')
    else
        c=$(grep -h -E "$marker" "$INPUT" 2>/dev/null | wc -l | tr -d ' ')
    fi
    [ "$c" -gt 0 ] && total=$((total + c))
done
echo "  $total pending item(s) total"
