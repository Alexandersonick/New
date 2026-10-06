#!/usr/bin/env python3
"""Assemble chapters/ch*.md into the canonical build manuscript.
- '## Chapter N' + '<!-- POV: X -->'  ->  '## Chapter N — X'
- '* * *' scene breaks -> '---'
- appends '## A Note to Readers' back matter
"""
import glob, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TITLE = "Two Tickets to the Haunted Hayride"
SUBTITLE = "A Sweet Halloween Second-Chance Romance"
out = [f"# {TITLE}", f"### {SUBTITLE}", ""]
for f in sorted(glob.glob(os.path.join(ROOT, 'manuscript/chapters/ch*.md'))):
    s = open(f).read()
    m = re.search(r'^## (Chapter \d+)\s*\n\s*<!-- POV: (\w+) -->', s, re.M)
    assert m, f
    s = s.replace(m.group(0), f"## {m.group(1)} — {m.group(2)}")
    s = re.sub(r'^\* \* \*\s*$', '---', s, flags=re.M)
    assert '<!--' not in s, f
    out.append(s.strip())
    out.append("")
out.append(open(os.path.join(HERE, 'note_to_readers.md')).read().strip())
dst = os.path.join(ROOT, 'manuscript/canonical/Two_Tickets_to_the_Haunted_Hayride.md')
open(dst, 'w').write('\n\n'.join(x for x in out if x is not None).replace('\n\n\n', '\n\n') + '\n')
print(dst, len(open(dst).read().split()), 'words incl. headings/back matter')
