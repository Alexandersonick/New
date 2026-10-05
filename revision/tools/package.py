import zipfile,xml.dom.minidom,sys
src,docxml,out=sys.argv[1],sys.argv[2],sys.argv[3]
xml.dom.minidom.parseString(open(docxml,'rb').read())
zi=zipfile.ZipFile(src)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        zo.writestr(it, open(docxml,'rb').read() if it.filename=='word/document.xml' else zi.read(it.filename))
print('packaged',out)
