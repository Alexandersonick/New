import re,sys
sys.path.insert(0,'/root/.claude/skills/synced/bd2694d4-4c02-48e4-b638-527ccb841fad_be25934a-7495-42ed-b478-ac156b97130e/master-fiction-pipeline/scripts')
import prose_metrics as pm
raw=open(sys.argv[1]).read()
chs=pm.parse_manuscript(raw)
chs=chs[1] if isinstance(chs,tuple) else chs
for ch in chs:
    paras=[p for p in ch['paragraphs'] if p!='<<SCENEBREAK>>']
    sents=[]
    for p in paras:
        q=pm.strip_markdown(p)
        if q.strip(): sents.extend(pm.split_sentences(q))
    hits=[]
    for s in sents:
        if re.search(r"\b\w+, \w+,? and \w+[.!?]$", s.strip()): hits.append('LIST: '+s.strip()[-70:])
    run=[]
    for s in sents:
        if len(pm.words_of(s))<=3:
            run.append(s.strip())
            if len(run)==3: hits.append('RUN: '+' | '.join(run))
        else: run=[]
    print('##',ch.get('title'),len(hits))
    for h in hits: print('  ',h)
