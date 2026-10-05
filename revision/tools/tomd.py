import re,html,sys
src,out=sys.argv[1],sys.argv[2]
x=open(src).read(); body=x[x.index('<w:body>'):]
ps=re.findall(r'<w:p[ >].*?</w:p>|<w:p/>',body,re.S)
lines=[];on=False
for p in ps:
    t=''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)).strip()
    if 'Heading1' in p:
        if t.startswith('A Note'): break
        m=re.match(r'Chapter (\d+) — (\w+)',t); on=True
        lines.append(f'\n## Chapter {m.group(1)}\n<!-- POV: {m.group(2)} -->\n'); continue
    if not on or not t: continue
    if set(t)<=set('• '): lines.append('\n* * *\n'); continue
    lines.append(t+'\n')
open(out,'w').write('# My Twin Sister Took My Place as His Wife\n'+'\n'.join(lines))
