import re,subprocess,sys,os,shutil
S=os.path.dirname(os.path.abspath(__file__))
SRC='/root/.claude/uploads/2b2aae46-ed0e-50a1-bd85-e45927c94a3c/eada9f8b-My_Twin_Sister_Took_My_Place_as_His_Wife_2.docx'
B='/home/user/build'; NAME='My_Twin_Sister_Took_My_Place_as_His_Wife'
docxml=S+'/rev/docx/word/document.xml'
def render():
    subprocess.run(['python3',S+'/package.py',SRC,docxml,f'{B}/{NAME}.docx'],check=True)
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',B,f'{B}/{NAME}.docx'],capture_output=True,timeout=400)
    pdf=f'{B}/{NAME}.pdf'
    n=int(subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
    pages={}
    for p in range(1,n+1):
        t=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-layout',pdf,'-'],capture_output=True,text=True).stdout
        L=[l.strip() for l in t.splitlines() if l.strip()]
        if L and re.match(r'(Chapter \d+ — \w+|A Note to Readers)$',L[0]): pages[L[0]]=p
    return n,pages
def toc_entries(x):
    return list(re.finditer(r'(<w:hyperlink w:history="1" w:anchor="toc_h\d+">.*?<w:t xml:space="preserve">)([^<]+)(</w:t></w:r></w:hyperlink><w:r><w:rPr><w:color w:val="000000"/></w:rPr><w:tab/></w:r><w:r><w:rPr><w:color w:val="000000"/></w:rPr><w:t xml:space="preserve">)(\d+)(</w:t>)',x,re.S))
for it in range(3):
    n,pages=render()
    x=open(docxml).read(); es=toc_entries(x); changed=0
    for m in reversed(es):
        title=m.group(2); want=str(pages[title])
        if m.group(4)!=want:
            x=x[:m.start(4)]+want+x[m.end(4):]; changed+=1
    print(f'pass {it}: {n} pages, {len(es)} toc entries, {changed} numbers updated')
    if not changed: break
    open(docxml,'w').write(x)
print({k:v for k,v in pages.items()})
