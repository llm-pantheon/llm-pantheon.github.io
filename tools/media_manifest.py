# -*- coding: utf-8 -*-
"""Emit media/manifest.json: metadata for every image served by the site.
Each entry: file -> {tweet_id, author, date, original_url, kind, transcription,
pages (which model pages embed it), favs}. Sources: the two corpora + transcriptions.json
+ the pages themselves. Stdlib only. Run after build_records.py."""
import os, re, sys, json, sqlite3

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
main = sqlite3.connect(r'C:\Users\Admin\Downloads\janus-corpus-v2.db').cursor()
supp = sqlite3.connect(r'C:\Users\Admin\Downloads\janus-corpus-supplement.db').cursor()
trans = json.load(open(os.path.join(REPO, 'tools', 'transcriptions.json'), encoding='utf-8'))

# map served file -> original basename (build re-encodes some to .jpg)
served = set(os.listdir(os.path.join(REPO, 'media'))) - {'manifest.json'}

def tweet_meta(tid):
    r = main.execute('select author_username, created_at, favorite_count from tweets where tweet_id=?', (tid,)).fetchone()
    if not r:
        r = supp.execute('select author_username, created_at, favorite_count from tweets where tweet_id=?', (tid,)).fetchone()
    return r or (None, None, None)

# original basename -> (tweet_id, url) from both media tables
origin = {}
for tid, url in main.execute('select tweet_id, media_url from media').fetchall():
    origin[url.rsplit('/', 1)[-1].split('?')[0]] = (tid, url)
for tid, url in supp.execute('select tweet_id, media_url from media_supp').fetchall():
    origin[url.rsplit('/', 1)[-1].split('?')[0]] = (tid, url)

# which pages embed which served file
pages_of = {}
for d in os.listdir(REPO):
    p = os.path.join(REPO, d, 'index.html')
    if os.path.isdir(os.path.join(REPO, d)) and os.path.exists(p) and d not in ('.git', 'tools', 'media', '_dossiers', '_statements', 'design-lab', 'mirror'):
        h = open(p, encoding='utf-8').read()
        for f in set(re.findall(r'\.\./media/([A-Za-z0-9_.-]+)', h)):
            pages_of.setdefault(f, []).append(d)

manifest = {}
for f in sorted(served):
    stem = os.path.splitext(f)[0]
    # served file may be re-encoded: match original by stem
    obase = next((b for b in (f, stem + '.png', stem + '.jpg', stem + '.jpeg') if b in origin), None)
    tid, url = origin.get(obase, (None, None))
    user, date, favs = tweet_meta(tid) if tid else (None, None, None)
    tr = trans.get(obase or f) or {}
    # db transcription fallback
    db_tr = None
    if tid and not tr:
        r = main.execute('select transcription from media where tweet_id=? and media_url=?', (tid, url)).fetchone()
        db_tr = r[0] if r and r[0] else None
    manifest[f] = {
        'tweet_id': tid,
        'author': user,
        'date': (date or '')[:10] or None,
        'favs': favs,
        'original_url': url,
        'tweet_url': 'https://x.com/{}/status/{}'.format(user or 'i', tid) if tid else None,
        'kind': tr.get('kind'),
        'transcription': tr.get('transcription') or db_tr,
        'pages': sorted(pages_of.get(f, [])),
    }

out = os.path.join(REPO, 'media', 'manifest.json')
json.dump(manifest, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n_tr = sum(1 for v in manifest.values() if v['transcription'])
print('media/manifest.json: {} files, {} with transcriptions, {} placed on pages'.format(
    len(manifest), n_tr, sum(1 for v in manifest.values() if v['pages'])))
