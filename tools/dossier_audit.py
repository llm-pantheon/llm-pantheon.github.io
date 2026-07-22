# -*- coding: utf-8 -*-
"""Dossier transformation audit — did an agent rewrite a tweet?

For every dossier: find every cited status id; for each, take the paragraph
around the citation, extract quoted spans, and check each span against the
db row's full_text (and its media transcriptions). Classification per span:

  VERBATIM  — whole span found (whitespace/quote-normalized, case-insensitive)
  TRIMMED   — span has visible ellipses and every fragment >=12 chars is found
  ALTERED   — some fragment >=12 chars is NOT in the source: rewritten,
              stitched, or paraphrase-wearing-quotation-marks. The bug class.
  NOT_IN_DB — id absent from both dbs (web-only tweet; can't audit here)

Usage: python tools/dossier_audit.py [dossier.md ...]   (default: all)
Writes the full report to the path given by --report, else prints summary only.
"""
import os, re, sys, glob, sqlite3, unicodedata

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = sqlite3.connect(r'C:\Users\Admin\Downloads\janus-corpus-v2.db')
SUPP = sqlite3.connect(r'C:\Users\Admin\Downloads\janus-corpus-supplement.db')

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = (s.replace('‘', "'").replace('’', "'").replace('“', '"')
          .replace('”', '"').replace('—', '-').replace('–', '-')
          .replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<'))
    # squash ALL whitespace (the corpus scrape stripped newlines without spaces)
    # and ALL quote marks (house convention converts nested double->single)
    return re.sub(r"[\s'\"]+", '', s).strip().lower()

def source_text(tid):
    for con, mq in ((MAIN, "SELECT transcription FROM media WHERE tweet_id=? AND transcription IS NOT NULL"),
                    (SUPP, None)):
        r = con.execute("SELECT full_text FROM tweets WHERE tweet_id=?", (tid,)).fetchone()
        if r:
            extra = ''
            if mq:
                extra = ' '.join(t[0] for t in con.execute(mq, (tid,)).fetchall())
            else:
                fn = [u[0].rsplit('/', 1)[-1].split('?')[0] for u in
                      con.execute("SELECT media_url FROM media_supp WHERE tweet_id=?", (tid,)).fetchall()]
                if fn:
                    ph = ','.join('?' for _ in fn)
                    extra = ' '.join(t[0] for t in con.execute(
                        f"SELECT transcription FROM media_transcriptions WHERE filename IN ({ph})", fn).fetchall())
            return norm(r[0] + ' ' + extra)
    return None

ELL = re.compile(r'…|\.\.\.|\[[^\]]{0,60}\]')  # ellipses AND [editorial insertions] break fragments
QSPAN = re.compile(r'[\"“]([^\"“”]{12,}?)[\"”]')

def audit_file(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    # unit = a single bullet/line (dossier quotes live on the line that cites
    # their id); paragraph-level pairing lumps neighbors and flags falsely
    paras = [ln for ln in text.split('\n') if ln.strip()]
    res = dict(V=0, T=0, A=0, N=0, altered=[])
    for para in paras:
        ids = set(re.findall(r'(?:x|twitter)\.com/[^/\s")]*/status/(\d+)', para))
        if not ids:
            continue
        spans = QSPAN.findall(para)
        if not spans:
            continue
        sources = {tid: source_text(tid) for tid in ids}
        for span in spans:
            frags = [f for f in (norm(f) for f in ELL.split(span)) if len(f) >= 12]
            if not frags:
                continue
            best = 'A'
            for tid, src in sources.items():
                if src is None:
                    best = min(best, 'N') if best == 'A' else best
                    continue
                hit = sum(1 for f in frags if f in src)
                if hit == len(frags):
                    best = 'T' if ELL.search(span) else 'V'
                    break
            if best == 'A' and all(s is None for s in sources.values()):
                best = 'N'
            res[best] += 1
            if best == 'A':
                miss = next((f for f in frags if not any(s and f in s for s in sources.values())), None)
                res['altered'].append((sorted(ids)[0], span[:90],
                                       miss[:70] if miss else '(all fragments found, but split across different cited tweets — possible cross-tweet stitch)'))
    return res

def main():
    argv = sys.argv[1:]
    report_path = None
    if '--report' in argv:
        i = argv.index('--report')
        report_path = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    args = [a for a in argv if not a.startswith('--')]
    files = args or sorted(glob.glob(os.path.join(REPO, '_dossiers', '*.md')))
    files = [f for f in files if not os.path.basename(f).startswith('_')]
    grand = dict(V=0, T=0, A=0, N=0)
    lines = []
    for f in files:
        r = audit_file(f)
        for k in grand: grand[k] += r[k]
        flag = '  <-- ALTERED' if r['A'] else ''
        lines.append(f"{os.path.basename(f):<28} V:{r['V']:>3} T:{r['T']:>3} N:{r['N']:>3} A:{r['A']:>3}{flag}")
        for tid, span, miss in r['altered']:
            lines.append(f"    [{tid}] \"{span}...\" -- missing: \"{miss}\"")
    out = '\n'.join(lines)
    print(out if not report_path else '\n'.join(l for l in lines if 'A:  0' not in l or 'ALTERED' in l))
    print(f"\nTOTAL quoted spans: {sum(grand.values())} — verbatim {grand['V']}, trimmed-visible {grand['T']}, "
          f"not-in-db {grand['N']}, ALTERED {grand['A']}")
    if report_path:
        open(report_path, 'w', encoding='utf-8').write(out + '\n')
        print('full report:', report_path)

if __name__ == '__main__':
    main()
