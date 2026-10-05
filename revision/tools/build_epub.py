import re,html,sys,subprocess
docxml,out_md=sys.argv[1],sys.argv[2]
x=open(docxml).read(); body=x[x.index('<w:body>'):]
ps=re.findall(r'<w:p[ >].*?</w:p>|<w:p/>',body,re.S)
def md(p):
    segs=[]
    for r in re.findall(r'<w:r[ >].*?</w:r>',p,re.S):
        ital=re.search(r'<w:i/>|<w:i w:val="(true|1)"/>',r) is not None
        t=''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>',r))
        if not t: continue
        t=t.replace('\\','\\\\').replace('*','\\*').replace('_','\\_').replace('<','&lt;')
        if ital and t.strip():
            lead=t[:len(t)-len(t.lstrip())]; trail=t[len(t.rstrip()):]
            t=f'{lead}*{t.strip()}*{trail}'
        segs.append(t)
    s=''.join(segs).strip()
    s=re.sub(r'\*\*(?=\S)','',s) if '***' in s else s
    if re.match(r'^(\d+[.)]\s|[#>+-]\s)',s): s='\\'+s
    return s
def plain(p): return ''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)).strip()
o=['# Title Page {.visually-hidden}','','<div class="titlepage">',
   '<p class="booktitle">My Twin Sister Took My Place as His Wife</p>',
   '<p class="booksubtitle"><em>A Marriage-in-Crisis Betrayal Second-Chance Romance</em></p>',
   '<p class="authorline">Shawn J Dean</p>','</div>','',
   '# Copyright {.visually-hidden}','','<div class="copyright">']
# copyright block: paragraphs between 'Copyright ©' and 'Contents'
i0=next(i for i,p in enumerate(ps) if plain(p).startswith('Copyright ©'))
i1=next(i for i,p in enumerate(ps) if plain(p)=='Contents')
for p in ps[i0:i1]:
    t=plain(p)
    if t: o.append(f'<p>{html.escape(t)}</p>')
o+=['</div>','']
start=next(i for i,p in enumerate(ps) if 'Heading1' in p)
for p in ps[start:]:
    t=plain(p)
    if 'Heading1' in p: o+=['',f'# {t}','']; continue
    if not t: continue
    if set(t)<=set('• '): o+=['','<p class="scenebreak">&#8226;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;</p>','']; continue
    o+=[md(p),'']
open(out_md,'w').write('\n'.join(o))
print('wrote',out_md)
