#!/usr/bin/env bash
# Build the distributable zip for a marketplace upload: one top-level folder (workdocs/) with SKILL.md at its root.
# Output: dist/workdocs-<version>.zip (version read from SKILL.md metadata). Refuses to overwrite an existing zip.
#   bash scripts/package.sh
set -eu
SKILL="$(cd "$(dirname "$0")/.." && pwd)"; NAME="$(basename "$SKILL")"
VER="$(sed -n 's/^  version: *"\{0,1\}\([0-9][0-9.]*\)"\{0,1\}.*/\1/p' "$SKILL/SKILL.md" | head -1)"
command -v zip >/dev/null || { echo "zip is required" >&2; exit 1; }
mkdir -p "$SKILL/dist"; OUT="$SKILL/dist/$NAME-${VER:-dev}.zip"
[ -e "$OUT" ] && { echo "already exists: $OUT - remove or rename it first" >&2; exit 1; }
( cd "$SKILL/.." && zip -r -X "$OUT" "$NAME" -x "$NAME/dist/*" "$NAME/docs/*" "$NAME/demo/*" "$NAME/.bak/*" "$NAME/CLAUDE.md" "$NAME/.git/*" "$NAME/.gitignore" "$NAME/.claude/*" "$NAME/.playwright-cli/*" "*.DS_Store" "*/__pycache__/*" "*.pyc" >/dev/null )
echo "built $OUT"
unzip -l "$OUT" | awk 'NR > 3 && $4 != "" { print "  " $4 }' | grep -v '/$'
