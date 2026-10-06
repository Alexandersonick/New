"""Apply all five books' edits plus the production fixes, then build DOCX, print PDF and EPUB.
usage: python3 build.py [--books 1,2,3,4,5] [--no-render]"""
import re, sys, os, shutil, zipfile, subprocess, html
from common import *
OUT = os.path.abspath(os.path.join(HERE, '..', 'manuscript'))
BUILD = SCR + '/build'
NAME = 'Vows_and_Betrayals'
SRC_DOCX = SCR + '/in/ms.docx'
PEN = 'Marlowe Ashwood'
books = [int(b) for b in (sys.argv[sys.argv.index('--books') + 1].split(',') if '--books' in sys.argv else '12345') if b]

x, ms = load_xml(); errs = []
REP, DELE, INS = {}, set(), {}
for b in books:
    r, d, i = resolve(b, ms, errs)
    REP.update(r); DELE |= d
    for k, v in i.items(): INS.setdefault(k, []).extend(v)
if errs:
    for e in errs: print('ERR', e)
    sys.exit(1)

BODY_PPR = '<w:pPr><w:widowControl/><w:spacing w:after="0" w:before="0" w:line="254" w:lineRule="exact"/><w:ind w:firstLine="288"/><w:jc w:val="both"/></w:pPr>'
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def runs(text):
    out = []
    for k, seg in enumerate(re.split(r'\*([^*]+)\*', text)):
        if not seg: continue
        rpr = '<w:rPr><w:i/><w:iCs/></w:rPr>' if k % 2 else '<w:rPr><w:i w:val="false"/><w:iCs w:val="false"/></w:rPr>'
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(seg)}</w:t></w:r>')
    return ''.join(out)

# ---- production text fixes (PR-01): exact paragraph texts, formatting kept ----
FRONT_TEXT = {5: ('[PEN NAME]', PEN), 8: ('Copyright © [YEAR] [PEN NAME]', f'Copyright © 2026 {PEN}'),
              11: ('five complete, separately titled novels', 'five complete, separately titled short novels'),
              12: ('First edition: [MONTH YEAR]', 'First edition: October 2026'),
              6496: ('[PEN NAME]', PEN)}
FRONT_DELETE = {13}  # optional ISBN line: KDP assigns the ebook ASIN; no own ISBN supplied
NOTE_6495 = (f'If you would like to know when the next book is out, search for {PEN} on Amazon, '
             'open the author page, and tap Follow.')
CONTENT_NOTE = ('Content note: The Winter We Never Spoke Of concerns the stillbirth of a child and the '
                'grief that follows. All five stories are closed-door romances.')

out = [x[:ms[0].start()]]; last = ms[0].start()
for i, m in enumerate(ms):
    out.append(x[last:m.start()]); last = m.end(); p = m.group(0)
    if i in DELE or i in FRONT_DELETE: pass
    elif i in REP:
        ppr = re.search(r'<w:pPr>.*?</w:pPr>', p, re.S); ppr = ppr.group(0) if ppr else BODY_PPR
        out.append(f'<w:p>{ppr}{runs(REP[i])}</w:p>')
    elif i in FRONT_TEXT:
        a, b = FRONT_TEXT[i]
        assert esc(a) in p, (i, a); out.append(p.replace(esc(a), esc(b)))
    elif i == 6495:
        assert '[NEWSLETTER OR WEBSITE LINK GOES HERE]' in p
        out.append(p.replace('[NEWSLETTER OR WEBSITE LINK GOES HERE]', esc(NOTE_6495)))
    else: out.append(p)
    if i == 11:  # content note on the copyright page, same formatting as ¶11
        out.append(re.sub(r'<w:t xml:space="preserve">[^<]*</w:t>', f'<w:t xml:space="preserve">{esc(CONTENT_NOTE)}</w:t>', p))
    for t in INS.get(i, []): out.append(f'<w:p>{BODY_PPR}{runs(t)}</w:p>')
out.append(x[last:])
doc = ''.join(out)
# PR-03: footer distance 0.208 in -> 0.375 in (540 twips); bottom margin stays 0.6 in
doc = doc.replace('w:footer="300"', 'w:footer="540"')
assert '[' not in ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', doc)), 'placeholder bracket left'

# PR-04: one Normal style, one definition per heading ID
sty = open(SCR + '/ms_x/word/styles.xml', encoding='utf-8').read()
for sid in ('Heading1', 'Heading2'):
    defs = list(re.finditer(rf'<w:style w:type="paragraph" w:styleId="{sid}">.*?</w:style>', sty, re.S))
    if len(defs) > 1:  # drop the earlier blue template definitions, keep the book's own
        for d in reversed(defs[:-1]): sty = sty[:d.start()] + sty[d.end():]
if 'w:styleId="Normal"' not in sty:
    normal = ('<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/>'
              '<w:pPr><w:widowControl/><w:spacing w:after="0" w:before="0" w:line="254" w:lineRule="exact"/></w:pPr>'
              '<w:rPr><w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" w:hAnsi="Times New Roman"/>'
              '<w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr></w:style>')
    sty = sty.replace('</w:latentStyles>', '</w:latentStyles>' + normal, 1) if '</w:latentStyles>' in sty \
        else re.sub(r'(<w:style )', normal + r'\1', sty, count=1)
core = open(SCR + '/ms_x/docProps/core.xml', encoding='utf-8').read().replace('[PEN NAME]', PEN)

os.makedirs(BUILD, exist_ok=True); os.makedirs(OUT, exist_ok=True)
def package(docxml):
    import xml.dom.minidom
    xml.dom.minidom.parseString(docxml.encode()); xml.dom.minidom.parseString(sty.encode())
    zi = zipfile.ZipFile(SRC_DOCX); dst = f'{BUILD}/{NAME}.docx'
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            d = {'word/document.xml': docxml, 'word/styles.xml': sty, 'docProps/core.xml': core}.get(it.filename)
            zo.writestr(it, d.encode() if d is not None else zi.read(it.filename))
    return dst
LABELS = ['BOOK ONE', 'BOOK TWO', 'BOOK THREE', 'BOOK FOUR', 'BOOK FIVE', 'A Note Before You Go']
TITLES = ['The Cottage His Family Sold', 'He Wasn’t There When It Counted', 'My Husband Told My Best Friend Everything',
          'The Year He Decided Without Me', 'The Winter We Never Spoke Of', 'A Note Before You Go']
def render(dst):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', BUILD, dst], capture_output=True, timeout=900)
    pdf = f'{BUILD}/{NAME}.pdf'
    n = int(subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout.split('Pages:')[1].split()[0])
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout.split('\f')
    pages = {}
    for pno, t in enumerate(txt, 1):
        L = [l.strip() for l in t.splitlines() if l.strip()]
        for title, label in zip(TITLES, LABELS):
            if title in pages or pno < 4: continue
            if L and L[0] == label: pages[title] = pno
    return n, pages
TOC_RX = r'(<w:t xml:space="preserve">{t}</w:t></w:r></w:hyperlink><w:r><w:rPr>(?:(?!</w:rPr>).)*</w:rPr><w:tab/></w:r><w:r><w:rPr>(?:(?!</w:rPr>).)*</w:rPr><w:t xml:space="preserve">)(\d+)(</w:t>)'
if '--no-render' in sys.argv:
    print('packaged', package(doc)); sys.exit(0)
for it in range(4):
    dst = package(doc); n, pages = render(dst); changed = 0
    for t in TITLES:
        m = re.search(TOC_RX.format(t=re.escape(esc(t))), doc, re.S)
        assert m and t in pages, (t, pages)
        if m.group(2) != str(pages[t]):
            doc = doc[:m.start(2)] + str(pages[t]) + doc[m.end(2):]; changed += 1
    print(f'pass {it}: {n} pages, toc updates {changed}, {pages}')
    if not changed: break
for ext in ('docx', 'pdf'): shutil.copy(f'{BUILD}/{NAME}.{ext}', f'{OUT}/{NAME}.{ext}')
open(f'{BUILD}/document.xml', 'w').write(doc)
print('built', OUT)
