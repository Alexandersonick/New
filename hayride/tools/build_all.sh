#!/usr/bin/env bash
# Build DOCX (6x9 print master), EPUB3 and print PDF from manuscript/chapters/.
# Usage: tools/build_all.sh [OUT_DIR]   (default: build/)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
OUT="${1:-$ROOT/build}"
NAME="Two_Tickets_to_the_Haunted_Hayride"
TITLE="Two Tickets to the Haunted Hayride"
SUBTITLE="A Sweet Halloween Second-Chance Romance"
AUTHOR="Shawn J Dean"
mkdir -p "$OUT"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT

python3 "$HERE/assemble.py"
SRC="$ROOT/manuscript/canonical/$NAME.md"

# 1. DOCX (two-pass verified TOC, 6x9 mirror margins, copyright page)
node "$HERE/build_manuscript_docx.js" "$SRC" "$OUT/$NAME.docx" \
  --author "$AUTHOR" --trim 6x9 --copyright "$HERE/copyright.txt" > "$WORK/docx.log"

# 2. EPUB3: source + copyright section injected after the title page
node "$HERE/build_epub_source.js" "$SRC" "$WORK/epub_src.md" --author "$AUTHOR" > "$WORK/epub.log"
python3 - "$WORK/epub_src.md" "$HERE/copyright.txt" <<'PY'
import sys, html
src, cp = sys.argv[1], sys.argv[2]
s = open(src).read()
paras = [p.strip() for p in open(cp).read().split('\n\n') if p.strip()]
block = '# Copyright {.visually-hidden}\n\n<div class="copyright">\n' + \
        '\n'.join(f'<p>{html.escape(p)}</p>' for p in paras) + '\n</div>\n\n'
i = s.index('# Chapter 1')
open(src, 'w').write(s[:i] + block + s[i:])
PY
cat > "$WORK/meta.yaml" <<EOF
---
title:
  - type: main
    text: "$TITLE"
  - type: subtitle
    text: "$SUBTITLE"
creator:
  - role: author
    text: "$AUTHOR"
lang: en-US
rights: "Copyright © 2026 $AUTHOR. All rights reserved."
---
EOF
cp "$HERE/style.css" "$WORK/style.css"
cat >> "$WORK/style.css" <<'EOF'
div.copyright { margin-top: 3em; font-size: 0.8em; text-align: center; }
div.copyright p { text-indent: 0; margin-bottom: 0.8em; }
EOF
(cd "$WORK" && pandoc -f markdown+smart -t epub3 --split-level=1 --toc --toc-depth=1 \
  --css style.css --metadata-file meta.yaml epub_src.md -o "$OUT/$NAME.epub")

# 3. Print PDF from the DOCX
soffice --headless --convert-to pdf --outdir "$WORK" "$OUT/$NAME.docx" > /dev/null 2>&1
# LibreOffice exports 6x9 as 432 x 649.16 pt; trim the box to exactly 432 x 648 (top-anchored, so only bottom margin loses 1.2 pt)
python3 - "$WORK/$NAME.pdf" "$OUT/${NAME}_print_6x9.pdf" <<'PY'
import sys
from pypdf import PdfReader, PdfWriter
r = PdfReader(sys.argv[1]); w = PdfWriter()
for pg in r.pages:
    top = float(pg.mediabox.top)
    for box in (pg.mediabox, pg.cropbox, pg.trimbox, pg.bleedbox):
        box.lower_left = (0, top - 648); box.upper_right = (432, top)
    w.add_page(pg)
w.add_metadata({"/Title": "Two Tickets to the Haunted Hayride", "/Author": "Shawn J Dean"})
w.write(sys.argv[2])
PY

# Checks
EPUBCHECK_JAR="$(python3 -c 'import epubcheck,os;print(os.path.join(os.path.dirname(epubcheck.__file__),"epubcheck.jar"))')"
echo "== epubcheck"; java -jar "$EPUBCHECK_JAR" "$OUT/$NAME.epub" 2>&1 | grep -E "Messages:|ERROR|WARNING" || true
echo "== pdfinfo";   pdfinfo "$OUT/${NAME}_print_6x9.pdf" | grep -E "Pages|Page size"
echo "== pdffonts";  pdffonts "$OUT/${NAME}_print_6x9.pdf"
ls -la "$OUT"
