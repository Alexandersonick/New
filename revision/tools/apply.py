import re,html,sys,shutil,os,zipfile
from collections import defaultdict
sys.path.insert(0,'.')
from edits import EDITS
src='docx/word/document.xml'
x=open(src).read(); b0=x.index('<w:body>')
rx=re.compile(r'<w:p[ >].*?</w:p>|<w:p/>',re.S)
ms=list(rx.finditer(x,b0))
def marked(p):
    segs=[]
    for r in re.findall(r'<w:r[ >].*?</w:r>',p,re.S):
        ital=re.search(r'<w:i/>|<w:i w:val="(true|1)"/>',r) is not None
        t=''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>',r))
        if t: segs.append('*'+t+'*' if ital and t.strip() else t)
    return ''.join(segs)
tmpl=ms[100].group(0); PPR=re.search(r'<w:pPr>.*?</w:pPr>',tmpl,re.S).group(0)
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def runs(text):
    out=[]
    for i,seg in enumerate(re.split(r'\*([^*]+)\*',text)):
        if not seg: continue
        rpr='<w:rPr><w:i/><w:iCs/></w:rPr>' if i%2 else '<w:rPr><w:i w:val="false"/><w:iCs w:val="false"/></w:rPr>'
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(seg)}</w:t></w:r>')
    return ''.join(out)
rep={}; dele=set(); ins=defaultdict(list); errs=[]
for op,i,exp,tag,text in EDITS:
    cur=marked(ms[i].group(0))
    if exp is not None and not cur.startswith(exp): errs.append((i,exp,cur[:80]))
    if op=='replace': rep[i]=text
    elif op=='delete': dele.add(i)
    elif op=='insert_after': ins[i].append(text)
if errs:
    for e in errs: print('MISMATCH',e)
    sys.exit(1)
out=[x[:ms[0].start()]]; last=ms[0].start()
for i,m in enumerate(ms):
    out.append(x[last:m.start()]); last=m.end()
    p=m.group(0)
    if i in dele: pass
    elif i in rep:
        ppr=re.search(r'<w:pPr>.*?</w:pPr>',p,re.S); ppr=ppr.group(0) if ppr else PPR
        out.append(f'<w:p>{ppr}{runs(rep[i])}</w:p>')
    else: out.append(p)
    for t in ins.get(i,[]): out.append(f'<w:p>{PPR}{runs(t)}</w:p>')
out.append(x[last:])
new=''.join(out)
os.makedirs('rev',exist_ok=True)
shutil.rmtree('rev/docx',ignore_errors=True); shutil.copytree('docx','rev/docx')
open('rev/docx/word/document.xml','w').write(new)
print('ok: replaced',len(rep),'deleted',len(dele),'inserted',sum(len(v) for v in ins.values()))
