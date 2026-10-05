import re,html,sys
src=sys.argv[1]; out=sys.argv[2]
x=open(src).read()
body=x[x.index('<w:body>'):]
ps=re.findall(r'<w:p[ >].*?</w:p>|<w:p/>',body,re.S)
lines=[]
for i,p in enumerate(ps):
    segs=[]
    for r in re.findall(r'<w:r[ >].*?</w:r>',p,re.S):
        ital = re.search(r'<w:i/>|<w:i w:val="(true|1)"/>',r) is not None
        t=''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>',r))
        if '<w:br' in r and not t: t='\n'
        if not t: continue
        segs.append(('*'+t+'*') if ital and t.strip() else t)
    st=re.search(r'<w:pStyle w:val="([^"]+)"',p)
    tag=f'[{st.group(1)}]' if st else ''
    lines.append(f'¶{i}{tag} '+''.join(segs))
open(out,'w').write('\n'.join(lines)+'\n')
