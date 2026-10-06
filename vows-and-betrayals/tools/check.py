"""Validate one book's edit file against the source and print a before/after preview.
usage: python3 check.py BOOK [--quiet]"""
import sys, difflib
from common import *
book = int(sys.argv[1]); quiet = '--quiet' in sys.argv
x, ms = load_xml(); errs = []
rep, dele, ins = resolve(book, ms, errs)
if not quiet:
    for i in sorted(set(rep) | dele | set(ins)):
        o = marked(ms[i].group(0))
        if i in dele: print(f'--- ¶{i} DELETE: {o[:200]}')
        elif i in rep:
            print(f'--- ¶{i} REPLACE')
            print('  before:', o); print('  after: ', rep[i])
        for t in ins.get(i, []): print(f'--- ¶{i} INSERT AFTER: {t}')
print(f'B{book}: {len(rep)} replaced/subbed, {len(dele)} deleted, {sum(map(len, ins.values()))} inserted')
if errs:
    print('ERRORS:'); [print(' ', e) for e in errs]; sys.exit(1)
print('OK')
