"""Build the EPUB from the revised document.xml written by build.py.
usage: python3 build_epub.py"""
import re, html, subprocess, os, shutil
from common import SCR, HERE
BUILD = SCR + '/build'; OUT = os.path.abspath(os.path.join(HERE, '..', 'manuscript')); NAME = 'Vows_and_Betrayals'
x = open(f'{BUILD}/document.xml').read(); body = x[x.index('<w:body>'):]
ps = re.findall(r'<w:p[ >].*?</w:p>|<w:p/>', body, re.S)
def plain(p): return ''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p)).strip()
def md(p):
    segs = []
    for r in re.findall(r'<w:r[ >].*?</w:r>', p, re.S):
        ital = re.search(r'<w:i/>|<w:i w:val="(true|1)"/>', r) is not None
        t = ''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>', r))
        if not t: continue
        t = t.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('<', '&lt;')
        if ital and t.strip():
            lead = t[:len(t) - len(t.lstrip())]; trail = t[len(t.rstrip()):]
            t = f'{lead}*{t.strip()}*{trail}'
        segs.append(t)
    s = ''.join(segs).strip().replace('**', '')
    if re.match(r'^(\d+[.)]\s|[#>+-]\s)', s): s = '\\' + s
    return s
def is_italic_only(p):
    rs = [r for r in re.findall(r'<w:r[ >].*?</w:r>', p, re.S) if re.search(r'<w:t[^>]*>[^<]+<', r)]
    return rs and all(re.search(r'<w:i/>', r) for r in rs)
SB = '<p class="scenebreak">*&#160;&#160;&#160;*&#160;&#160;&#160;*</p>'
pen = 'Marlowe Ashwood'
o = ['# Title Page {.visually-hidden}', '', '<div class="titlepage">',
     '<p class="booktitle">Vows and Betrayals</p>',
     '<p class="booksubtitle"><em>5 Marriage-in-Crisis Second-Chance Grovel Romances in One Collection</em></p>',
     f'<p class="authorline">{pen}</p>', '</div>', '', '# Copyright {.visually-hidden}', '', '<div class="copyright">']
i0 = next(i for i, p in enumerate(ps) if plain(p).startswith('Copyright ©'))
i1 = next(i for i, p in enumerate(ps) if plain(p) == 'Contents')
for p in ps[i0 - 1:i1]:
    t = plain(p)
    if t: o.append(f'<p>{html.escape(t)}</p>')
o += ['</div>', '']
start = next(i for i, p in enumerate(ps) if plain(p) == 'BOOK ONE')
bookno = None; prev = None; after_title = False
for p in ps[start:]:
    t = plain(p)
    if not t: continue
    if re.fullmatch(r'BOOK (ONE|TWO|THREE|FOUR|FIVE)', t): bookno = t.title(); continue
    if 'w:val="Heading1"' in p:
        if bookno: o += ['', f'# {bookno}: {t}', '']; bookno = None; after_title = True
        else: o += ['', f'# {t}', '']
        prev = 'h'; continue
    if after_title and is_italic_only(p):
        o += [f'<p class="booksub">{html.escape(t)}</p>', '']; after_title = False; prev = 'sub'; continue
    after_title = False
    if 'w:val="Heading2"' in p: o += ['', f'## {t}', '']; prev = 'h'; continue
    if re.fullmatch(r'[*•]\s*[*•]\s*[*•]', t.replace(' ', ' ')) or set(t) <= set('*•  '):
        if prev not in ('h', 'sub'): o += ['', SB, '']; prev = 'sb'
        continue
    if prev == 'h' and is_italic_only(p) and len(t) < 40 and 'w:jc w:val="center"' in p:
        o += [f'<p class="povline"><em>{html.escape(t)}</em></p>', '']; prev = 'pov'; continue
    o += [md(p), '']; prev = 'p'
open(f'{BUILD}/{NAME}.md', 'w').write('\n'.join(o))
shutil.copy(HERE + '/style.css', BUILD + '/style.css')
cmd = ['pandoc', f'{BUILD}/{NAME}.md', '-f', 'markdown-smart+raw_html', '-o', f'{BUILD}/{NAME}.epub', '--toc', '--toc-depth=2',
       '--split-level=2', '--css', f'{BUILD}/style.css', '--epub-metadata', HERE + '/book-metadata.xml',
       '--metadata', 'title=Vows and Betrayals', '--metadata', f'author={pen}', '--metadata', 'lang=en-US']
subprocess.run(cmd, check=True)
r = subprocess.run(['java', '-jar', '/usr/local/lib/python3.13/dist-packages/epubcheck/epubcheck.jar', f'{BUILD}/{NAME}.epub'],
                   capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-1500:])
shutil.copy(f'{BUILD}/{NAME}.epub', f'{OUT}/{NAME}.epub')
