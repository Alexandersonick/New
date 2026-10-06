"""Write each book as pipeline markdown (# Title / ## Chapter N / <!-- POV: Name -->) for prose_metrics.py.
usage: python3 tomd.py original|revised OUTDIR"""
import sys, re, os
from common import *
mode, outdir = sys.argv[1], sys.argv[2]; os.makedirs(outdir, exist_ok=True)
x, ms = load_xml(); errs = []
for b in range(1, 6):
    rep, dele, ins = resolve(b, ms, errs) if mode == 'revised' else ({}, set(), {})
    lo, hi = BOOK_RANGES[b]; L = []
    for i in range(lo, hi):
        p = ms[i].group(0); t = marked(p).strip()
        texts = [] if i in dele else [rep.get(i, t)]
        texts += ins.get(i, [])
        if 'w:val="Heading1"' in p: L.append(f'# {t}\n'); continue
        if 'w:val="Heading2"' in p:
            L.append(f'\n## {"Chapter 13" if t == "Epilogue" else t}\n'); continue
        if re.fullmatch(r'\*[A-Z][a-z]+\*', t) and 'w:jc w:val="center"' in p:
            L.append(f'<!-- POV: {t.strip("*")} -->\n'); continue
        for tt in texts:
            tt = tt.strip()
            if not tt: continue
            if set(tt) <= set('* '): L.append('\n* * *\n'); continue
            L.append(tt.replace('*', '') + '\n')
    open(f'{outdir}/book{b}.md', 'w').write('\n'.join(L))
print('ok', errs[:3])
