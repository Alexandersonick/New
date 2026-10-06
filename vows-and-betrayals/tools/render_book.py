"""Write the revised text of one book (¶-numbered, original indices; inserted paragraphs shown as ¶N+) so it can be re-read.
usage: python3 render_book.py BOOK OUT.txt"""
import sys
from common import *
book = int(sys.argv[1]); out = sys.argv[2]
x, ms = load_xml(); errs = []
rep, dele, ins = resolve(book, ms, errs)
lo, hi = BOOK_RANGES[book]; L = []
for i in range(lo, hi):
    if i not in dele: L.append(f'¶{i} ' + rep.get(i, marked(ms[i].group(0))))
    for t in ins.get(i, []): L.append(f'¶{i}+ ' + t)
open(out, 'w').write('\n'.join(L) + '\n')
print('wrote', out, '; errors:', len(errs))
for e in errs: print(' ', e)
