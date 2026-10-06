#!/usr/bin/env bash
# Build DOCX (6x9), print PDF, and EPUB from chapters/ + back_matter.md into OUT (default: ../output).
set -euo pipefail
T="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$T/../output}"
mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
SLUG="my-ceo-husband-gave-her-my-corner-office"
AUTHOR="Shawn J Dean"
TITLE="My CEO Husband Gave Her My Corner Office"
WORK="$(mktemp -d)"

python3 "$T/make_build_md.py" "$WORK/book.md"

# DOCX (verified TOC, page numbers, mirror margins, copyright page) and PDF
(cd "$T" && NODE_PATH=/opt/node22/lib/node_modules node build_docx.js "$WORK/book.md" "$OUT/$SLUG.docx" --author "$AUTHOR" --trim 6x9)
(cd "$WORK" && timeout 300 soffice --headless --convert-to pdf --outdir "$WORK" "$OUT/$SLUG.docx" >/dev/null 2>&1)
cp "$WORK/$SLUG.pdf" "$OUT/$SLUG.pdf"

# EPUB: preprocess, add a copyright section after the title page, then pandoc
node "$T/build_epub_source.js" "$WORK/book.md" "$WORK/epub_src.md" --author "$AUTHOR"
python3 - "$WORK/epub_src.md" "$T/copyright.json" <<'PY'
import json, sys, html
src, cj = sys.argv[1], sys.argv[2]
lines = json.load(open(cj))["lines"][1:]
block = "# Copyright {.visually-hidden}\n\n<div class=\"copyright\">\n" + "\n".join(
    f"<p>{html.escape(l, quote=False)}</p>" for l in lines) + "\n</div>\n\n"
s = open(src).read()
i = s.index("\n# Chapter 1")
open(src, "w").write(s[:i + 1] + block + s[i + 1:])
PY
cat > "$WORK/meta.xml" <<EOF
<dc:title>$TITLE</dc:title>
<dc:creator opf:role="aut">$AUTHOR</dc:creator>
<dc:language>en-US</dc:language>
<dc:rights>Copyright © 2026 by $AUTHOR. All rights reserved.</dc:rights>
EOF
pandoc "$WORK/epub_src.md" -f markdown+smart -t epub3 -o "$OUT/$SLUG.epub" \
  --css="$T/epub_template/style.css" --epub-title-page=false --split-level=1 \
  --epub-metadata="$WORK/meta.xml" --metadata title="$TITLE" --toc --toc-depth=1

# Verify
pdfinfo "$OUT/$SLUG.pdf" | grep -E "Pages|Page size"
pdffonts "$OUT/$SLUG.pdf" | awk 'NR>2 && $(NF-4)!="yes"{bad=1; print "NOT EMBEDDED:", $0} END{if(!bad) print "fonts: all embedded"}'
python3 -c "
from epubcheck import EpubCheck
r = EpubCheck('$OUT/$SLUG.epub'); print('epubcheck valid:', r.valid)
for m in r.messages: print(' ', m)"
rm -rf "$WORK"
