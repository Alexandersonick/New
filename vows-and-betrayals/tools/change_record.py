"""Write CHANGE_RECORD.md: every edit, original beside revised, grouped by book and chapter.
usage: python3 change_record.py OUT.md"""
import sys, re, difflib
from common import *
x, ms = load_xml(); errs = []
TITLES = {1: 'The Cottage His Family Sold', 2: 'He Wasn’t There When It Counted', 3: 'My Husband Told My Best Friend Everything',
          4: 'The Year He Decided Without Me', 5: 'The Winter We Never Spoke Of'}
def chapter_of(i):
    for j in range(i, -1, -1):
        p = ms[j].group(0)
        if 'w:val="Heading2"' in p: return marked(p).strip()
    return '?'
def tags(book):
    E, S = load_edits(book); t = {}
    for op, i, exp, tag, txt in E: t.setdefault(i, set()).add(tag)
    return t
def short_diff(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False); out = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == 'equal': continue
        ctx0 = max(0, a0 - 40)
        out.append((a[ctx0:a1 + 40], b[max(0, b0 - 40):b1 + 40]))
    return out
L = ['# Change record: every edit, original beside revised', '',
     'Paragraph numbers are zero-based body indices in the supplied DOCX; the audit’s P-numbers are one higher (P00443 = ¶442). '
     '`*text*` marks italics. Production fixes (front matter, styles, footer, TOC) are listed in REVISION_REPORT.md, not here.', '']
for b in range(1, 6):
    rep, dele, ins = resolve(b, ms, errs); E, S = load_edits(b)
    subtag = {}
    for e in E: subtag.setdefault(e[1], []).append(e[3])
    L += [f'## Book {b}: {TITLES[b]}', '']
    n = 0
    for i in sorted(set(rep) | dele | set(ins)):
        o = marked(ms[i].group(0)); tg = ', '.join(sorted(set(subtag.get(i, [])))) or 'line pass'
        ch = chapter_of(i)
        if i in dele:
            L += [f'### {ch} · ¶{i} · {tg} · deleted', '', f'**Before:** {o}', '']; n += 1
        elif i in rep:
            new = rep[i]
            if len(o) > 400 and len(short_diff(o, new)) <= 3 and i not in [e[1] for e in E if e[0] == 'replace']:
                for a, bb in short_diff(o, new):
                    L += [f'### {ch} · ¶{i} · {tg} · in-line change', '', f'**Before:** …{a}…', '', f'**After:** …{bb}…', '']
            else:
                L += [f'### {ch} · ¶{i} · {tg} · replaced', '', f'**Before:** {o}', '', f'**After:** {new}', '']
            n += 1
        for t in ins.get(i, []):
            L += [f'### {ch} · after ¶{i} · {tg} · inserted', '', f'**Inserted:** {t}', '']; n += 1
    L.insert(L.index(f'## Book {b}: {TITLES[b]}') + 2, f'{n} changed or inserted paragraphs.\n')
open(sys.argv[1], 'w').write('\n'.join(L) + '\n')
print('wrote', sys.argv[1], 'errors', errs[:5])
