#!/usr/bin/env zsh
# ai-trace-scan.sh — Scan documents for AI clichés and academic boilerplate
# NOTE: requires zsh — macOS's bundled bash 3.2 mis-handles the multibyte pattern arrays under `set -u`
# Source: references/ai-trace-checklist.md
# Usage: ./ai-trace-scan.sh <file.md>
#        ./ai-trace-scan.sh path/to/paper/  (recursively scan a directory)

set -euo pipefail

if [ $# -lt 1 ]; then
    cat <<EOF
Usage: $0 <file.md | directory>

Scans for two categories of issues:
  1. High-frequency clichés (flagged on any occurrence) — 值得注意的是 / 不难发现 / 综上所述 etc.
  2. Overused connectors (warning at >3 occurrences) — 此外 / 同时 / 另外 etc.
     Frequency is counted by OCCURRENCE, not by line — four 此外 in one
     paragraph (one line) trigger the threshold just like four lines do.

Output: line number + line content for each match
EOF
    exit 1
fi

INPUT="$1"
[ -e "$INPUT" ] || { echo "Path does not exist: $INPUT" >&2; exit 1; }

# High-frequency clichés (flagged on any occurrence) — kept in sync with references/ai-trace-checklist.md
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

# Frequency warning (only flagged above the threshold)
FREQUENCY_PATTERNS=(
    "此外"
    "同时"
    "另外"
    "与此同时"
    "进一步来说"
    "在此基础上"
)
FREQ_THRESHOLD=3

# grep options as a zsh ARRAY — a plain string would not be word-split by zsh,
# and an unquoted literal --include=*.md would trip zsh's NOMATCH globbing.
if [ -d "$INPUT" ]; then
    grep_opts=(-r -n --include='*.md')
    grep_opts_nofn=(-r -h --include='*.md')   # no filename/line prefix, for counting
else
    grep_opts=(-n)
    grep_opts_nofn=(-h)
fi

echo "=== AI trace scan · $INPUT ==="
echo ""

found_any=0

echo "## 1. High-frequency clichés (review on any occurrence)"
echo ""
for pat in "${SINGLE_PATTERNS[@]}"; do
    if matches=$(grep "${grep_opts[@]}" -E "$pat" "$INPUT" 2>/dev/null); then
        found_any=1
        echo "▶ 「$pat」"
        echo "$matches" | sed 's/^/    /'
        echo ""
    fi
done

echo "## 2. Connector frequency warning (threshold >$FREQ_THRESHOLD occurrences)"
echo ""
for word in "${FREQUENCY_PATTERNS[@]}"; do
    # Count OCCURRENCES (grep -o), not matching lines — Chinese markdown often
    # keeps a whole paragraph on one line, so line-count systematically undercounts.
    count=$( (grep "${grep_opts_nofn[@]}" -o -- "$word" "$INPUT" 2>/dev/null || true) | wc -l | tr -d ' ')
    if [ "$count" -gt "$FREQ_THRESHOLD" ]; then
        echo "⚠ 「$word」 appears $count times (threshold $FREQ_THRESHOLD)"
        # `|| true` guards the SIGPIPE that `head` sends upstream under pipefail
        { grep "${grep_opts[@]}" -- "$word" "$INPUT" 2>/dev/null || true; } | sed 's/^/    /' | head -5
        if [ "$count" -gt 5 ]; then
            echo "    ... (showing first 5 matching lines only)"
        fi
        echo ""
        found_any=1
    fi
done

if [ "$found_any" -eq 0 ]; then
    echo "✅ No obvious AI traces or boilerplate clichés found"
else
    echo ""
    echo "---"
    echo "💡 Review principle: for each hit, ask yourself — is this a deliberate choice of wording, or an unconscious default?"
    echo "   See references/ai-trace-checklist.md for details"
fi
