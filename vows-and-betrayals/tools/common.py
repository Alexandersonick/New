"""Shared paragraph model for the Vows and Betrayals revision.
Paragraph index = zero-based <w:p> index in the source document body (audit P-number minus 1).
Paragraph text uses *...* for italic runs, exactly as the per-book extracts show it."""
import re, html, os, importlib.util
SCR = os.environ.get('VB_SCRATCH', '/tmp/claude-0/-home-user-New/f169b227-9417-57fe-87a6-175a310dc5fe/scratchpad')
SRC_XML = SCR + '/ms_x/word/document.xml'
HERE = os.path.dirname(os.path.abspath(__file__))
EDIT_DIR = os.path.join(HERE, '..', 'edits')
PRX = re.compile(r'<w:p[ >].*?</w:p>|<w:p/>', re.S)
BOOK_RANGES = {1: (35, 1087), 2: (1087, 2576), 3: (2576, 3878), 4: (3878, 5107), 5: (5107, 6492), 0: (0, 6497)}

def load_xml(path=SRC_XML):
    x = open(path, encoding='utf-8').read()
    b0 = x.index('<w:body>')
    return x, list(PRX.finditer(x, b0))

def marked(p):
    segs = []
    for r in re.findall(r'<w:r[ >].*?</w:r>', p, re.S):
        ital = re.search(r'<w:i/>|<w:i w:val="(true|1)"/>', r) is not None
        t = ''.join(html.unescape(m) for m in re.findall(r'<w:t[^>]*>([^<]*)</w:t>', r))
        if t: segs.append('*' + t + '*' if ital and t.strip() else t)
    return ''.join(segs)

def load_edits(book):
    path = os.path.join(EDIT_DIR, f'edits_b{book}.py')
    spec = importlib.util.spec_from_file_location(f'edits_b{book}', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, 'EDITS', []), getattr(m, 'SUBS', [])

def resolve(book, ms, errs):
    """Return (rep: idx->new text, dele: set, ins: idx->[texts]) for one book's edits, collecting errors."""
    EDITS, SUBS = load_edits(book)
    lo, hi = BOOK_RANGES[book]
    cur = {}
    def text(i): return cur.get(i, marked(ms[i].group(0)))
    replaced = {e[1] for e in EDITS if e[0] == 'replace'}
    deleted = {e[1] for e in EDITS if e[0] == 'delete'}
    rep, dele, ins = {}, set(), {}
    for e in EDITS:
        if len(e) != 5: errs.append(f'B{book} malformed edit {e!r:.120}'); continue
        op, i, exp, tag, t = e
        if not (lo <= i < hi): errs.append(f'B{book} ¶{i} outside book range {lo}-{hi}'); continue
        orig = marked(ms[i].group(0))
        if exp is not None and not orig.startswith(exp):
            errs.append(f'B{book} ¶{i} prefix mismatch: expected {exp[:60]!r} got {orig[:60]!r}')
        if '[Heading' in orig or 'pStyle' in ms[i].group(0) and op != 'insert_after':
            errs.append(f'B{book} ¶{i} is a heading; do not {op} it')
        if op == 'replace':
            if i in rep: errs.append(f'B{book} ¶{i} replaced twice')
            if i in deleted: errs.append(f'B{book} ¶{i} both replaced and deleted')
            if not t or not t.strip(): errs.append(f'B{book} ¶{i} empty replacement (use delete)')
            rep[i] = t
        elif op == 'delete':
            dele.add(i)
        elif op == 'insert_after':
            if not t or not t.strip(): errs.append(f'B{book} ¶{i} empty insert')
            ins.setdefault(i, []).append(t)
        else:
            errs.append(f'B{book} ¶{i} unknown op {op}')
    for s in SUBS:
        if len(s) != 3: errs.append(f'B{book} malformed sub {s!r:.120}'); continue
        i, old, new = s
        if not (lo <= i < hi): errs.append(f'B{book} sub ¶{i} outside book range'); continue
        if i in replaced or i in deleted: errs.append(f'B{book} sub ¶{i} conflicts with a replace/delete on the same paragraph'); continue
        t = text(i)
        n = t.count(old)
        if n == 0: errs.append(f'B{book} sub ¶{i} MISS: {old[:70]!r}')
        elif n > 1: errs.append(f'B{book} sub ¶{i} ambiguous ({n} matches): {old[:70]!r}')
        else: cur[i] = t.replace(old, new)
    for i, t in cur.items(): rep[i] = t
    for i, t in list(rep.items()) + [(i, x) for i, v in ins.items() for x in v]:
        if t.count('*') % 2: errs.append(f'B{book} ¶{i} unbalanced * italics marker')
        if '"' in t: errs.append(f'B{book} ¶{i} straight double quote; use curly “ ”')
        if re.search(r"\w'\w|'\s|\s'", t): errs.append(f"B{book} ¶{i} straight apostrophe; use ’")
        if '  ' in t: errs.append(f'B{book} ¶{i} double space')
    return rep, dele, ins
