"""Assemble the build Markdown (canonical manuscript + front/back matter) for the docx/epub builders."""
import glob, re, sys, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1]
parts = ["# My CEO Husband Gave Her My Corner Office", "### A Billionaire Marriage-in-Crisis Grovel Romance", ""]
for f in sorted(glob.glob(os.path.join(root, 'chapters', 'ch*.md'))):
    s = open(f).read()
    s = re.sub(r'^<!-- POV:.*?-->\s*$\n?', '', s, flags=re.M)
    parts.append(s.strip()); parts.append("")
parts.append(open(os.path.join(root, 'back_matter.md')).read().strip())
open(out, 'w').write("\n".join(parts) + "\n")
print('wrote', out)
