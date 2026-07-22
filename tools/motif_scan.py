# -*- coding: utf-8 -*-
"""Motif scan — find distributed motifs the favorites-ranking is blind to.

The Princess lesson (2026-07-21): a model's nickname arc lived in short,
low-favorite, image-caption tweets. Name-variant search FOUND them; the
favorites x length x concreteness ranking DROPPED them; and the purest
motif tweets carried no model name at all. Distributed motifs — recurring
names, bits, imagery spread across many small posts — are first-class
character evidence and need frequency-level detection, not per-tweet weight.

Usage:
  python tools/motif_scan.py "sonnet 4.5,sonnet-4.5,claude-sonnet-4-5"
  python tools/motif_scan.py "405b,llama 405" --top 50

Output: cluster size; distinctive terms ranked by lift (cluster frequency vs
whole-corpus frequency) with tweet counts and example ids; clusters of
untranscribed image-tweets sharing caption terms (transcription candidates —
do NOT drop these); and reply-context leads (motif tweets whose parents may
carry the model attribution the tweet itself lacks).
"""
import os, re, sys, sqlite3, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
MAIN = r'C:\Users\Admin\Downloads\janus-corpus-v2.db'
SUPP = r'C:\Users\Admin\Downloads\janus-corpus-supplement.db'

STOP = set('''the a an and or but if then else of to in on at by for with from as is are was were be been being
this that these those it its it's im i'm you your we our they their he she his her them us not no yes so very
just like about into over under out up down off all any some more most other another such only own same too
can could will would shall should may might must do does did doing done have has had having what which who whom
whose when where why how there here also than because while during before after above below between through https
http t.co amp rt via ok oh lol im dont don't its it's thats that's isnt isn't cant can't wont won't u ur one two
new now get got make made even still really actually thing things way people know think see say said want going
model models claude gpt ai llm llms'''.split())

def tokenize(text):
    text = re.sub(r'https?://\S+', ' ', text.lower())
    return [t for t in re.findall(r"[a-z][a-z0-9'’\-]{2,}", text)
            if t.strip("'’-") not in STOP and len(t.strip("'’-")) > 2]

def cluster_rows(con, pats, has_media):
    like = ' OR '.join("lower(full_text) LIKE ?" for _ in pats)
    q = f"SELECT tweet_id, author_username, created_at, favorite_count, full_text FROM tweets WHERE ({like}) AND full_text NOT LIKE 'RT @%'"
    rows = con.execute(q, [f'%{p}%' for p in pats]).fetchall()
    media = {}
    if has_media:
        for tid, a, c, f, t in rows:
            m = con.execute("SELECT COUNT(*), SUM(CASE WHEN transcription IS NULL OR transcription='' THEN 1 ELSE 0 END) FROM media WHERE tweet_id=?", (tid,)).fetchone()
            if m and m[0]:
                media[tid] = (m[0], m[1] or 0)
    return rows, media

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    pats = [p.strip().lower() for p in sys.argv[1].split(',') if p.strip()]
    top_n = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 40

    main_con = sqlite3.connect(MAIN)
    supp_con = sqlite3.connect(SUPP)
    rows_m, media_m = cluster_rows(main_con, pats, True)
    rows_s, _ = cluster_rows(supp_con, pats, False)
    seen, rows = set(), []
    for r in rows_m + rows_s:
        if r[0] not in seen:
            seen.add(r[0]); rows.append(r)
    print(f'cluster: {len(rows)} unique non-RT tweets for patterns {pats}')
    if not rows:
        return

    # term counts within the cluster (per-tweet presence, not raw frequency)
    term_tweets = collections.defaultdict(list)
    for tid, author, created, favs, text in rows:
        for t in set(tokenize(text)):
            term_tweets[t].append((tid, favs, created))
    cand = {t: v for t, v in term_tweets.items()
            if len(v) >= 3 and not any(p in t or t in p for p in pats)}

    # global doc-frequency for lift: ONE tokenizing pass over the whole main db —
    # never pre-cut candidates by raw count: that re-hides exactly the rare-but-
    # distinctive terms this tool exists to catch (the Princess bug, twice)
    wanted = set(cand)
    gcount = collections.Counter()
    total_global = 0
    for (text,) in main_con.execute('SELECT full_text FROM tweets'):
        total_global += 1
        hits = wanted.intersection(tokenize(text))
        for t in hits:
            gcount[t] += 1
    scored = []
    for t, v in cand.items():
        g = gcount.get(t, 0)
        lift = (len(v) / len(rows)) / ((g + 5) / total_global)
        scored.append((lift, t, len(v), g, v))
    scored.sort(reverse=True)

    print(f'\ndistinctive terms (lift = cluster rate / corpus rate; chase anything that looks like a name, bit, or image):')
    print(f'{"term":<22}{"in-cluster":>10}{"corpus":>8}{"lift":>8}  examples')
    for lift, t, n, g, v in scored[:top_n]:
        ex = ' '.join(tid for tid, _, _ in sorted(v, key=lambda x: -x[1])[:3])
        print(f'{t:<22}{n:>10}{g:>8}{lift:>8.0f}  {ex}')

    # untranscribed image clusters — the double-penalized evidence class
    untr = [(tid, text) for tid, a, c, f, text in rows
            if media_m.get(tid, (0, 0))[1] > 0]
    if untr:
        capterms = collections.Counter()
        for tid, text in untr:
            for t in set(tokenize(text)): capterms[t] += 1
        shared = [t for t, n in capterms.most_common(15) if n >= 2]
        print(f'\nuntranscribed image-tweets in cluster: {len(untr)} — shared caption terms: {shared}')
        print('  (transcription candidates; do NOT drop for thin captions)')

    # replies whose motif may resolve via an out-of-cluster parent
    lead = [tid for tid, a, c, f, text in rows if text.startswith('@')]
    if lead:
        print(f'\nreply-context leads (attribution may sit in parents outside this cluster): {len(lead)} — sample: {lead[:6]}')

if __name__ == '__main__':
    main()
