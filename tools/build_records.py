# -*- coding: utf-8 -*-
"""Generate per-page 'Records' sections: full reproductions of every cited tweet
(text + images + transcriptions) from the local corpora, injected between
<!-- records:start/end --> markers. Idempotent — safe to re-run after editing pages.

Usage: python tools/build_records.py  (from repo root)
Data (local, not in repo): janus-corpus-v2.db (John Wittle's — read only),
janus-corpus-supplement.db, janus-corpus-media/ mirror.
"""
import os, re, sys, json, html, sqlite3, shutil

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_DB = r'C:\Users\Admin\Downloads\janus-corpus-v2.db'
SUPP_DB = r'C:\Users\Admin\Downloads\janus-corpus-supplement.db'
MIRROR = r'C:\Users\Admin\Downloads\janus-corpus-media'
MEDIA_OUT = os.path.join(REPO, 'media')
TRANS_JSON = os.path.join(REPO, 'tools', 'transcriptions.json')

main = sqlite3.connect(MAIN_DB).cursor()
supp = sqlite3.connect(SUPP_DB).cursor() if os.path.exists(SUPP_DB) else None
extra_trans = json.load(open(TRANS_JSON, encoding='utf-8')) if os.path.exists(TRANS_JSON) else {}
os.makedirs(MEDIA_OUT, exist_ok=True)

try:
    from PIL import Image
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False

def lookup(tid):
    r = main.execute('''select author_username, full_text, created_at, favorite_count, retweet_count
                        from tweets where tweet_id=?''', (tid,)).fetchone()
    if not r and supp:
        r = supp.execute('''select author_username, full_text, created_at, favorite_count, retweet_count
                            from tweets where tweet_id=?''', (tid,)).fetchone()
    return r

def media_for(tid):
    return main.execute('select media_id, media_url, media_type, transcription from media where tweet_id=?',
                        (tid,)).fetchall()

def place_image(basename):
    """Copy (optionally downscale/re-encode) a mirrored image into repo media/. Returns final basename or None."""
    src = os.path.join(MIRROR, basename)
    if not os.path.exists(src):
        return None
    stem, ext = os.path.splitext(basename)
    if HAVE_PIL and not (ext.lower() == '.png' and os.path.getsize(src) <= 400_000):
        dst_name = stem + '.jpg'
        dst = os.path.join(MEDIA_OUT, dst_name)
        if not os.path.exists(dst):
            try:
                im = Image.open(src).convert('RGB')
                if im.width > 1100:
                    im = im.resize((1100, int(im.height * 1100 / im.width)), Image.LANCZOS)
                im.save(dst, 'JPEG', quality=85)
            except Exception:
                shutil.copy2(src, os.path.join(MEDIA_OUT, basename))
                return basename
        return dst_name
    dst = os.path.join(MEDIA_OUT, basename)
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
    return basename

URL_RE = re.compile(r'(https?://[^\s<]+)')

def render_text(text):
    esc = html.escape(text)
    esc = URL_RE.sub(r'<a href="\1" rel="nofollow">\1</a>', esc)
    return esc

def render_record(tid, row):
    user, text, created, favs, rts = row
    date = (created or '')[:10]
    handle = '@' + user if user else 'unknown'
    orig = 'https://x.com/{}/status/{}'.format(user or 'i', tid)
    parts = []
    parts.append('      <article class="record" id="t{}">'.format(tid))
    parts.append('        <div class="record-head"><span class="rh-user">{}</span> <span class="rh-date">{}</span>'
                 ' <span class="rh-stats">&#9829;{:,} &#8635;{:,}</span>'
                 ' <a class="rh-orig" href="{}">original &#8599;</a></div>'.format(
                     html.escape(handle), date, favs or 0, rts or 0, orig))
    parts.append('        <div class="record-body">{}</div>'.format(render_text(text)))
    for mid, murl, mtype, db_trans in media_for(tid):
        base = murl.rsplit('/', 1)[-1].split('?')[0]
        placed = place_image(base)
        if not placed:
            continue
        info = extra_trans.get(base) or {}
        trans = (info.get('transcription') or db_trans or '').strip()
        kind = info.get('kind') or mtype or 'image'
        alt = (kind + ': ' + trans[:180]) if trans else kind
        parts.append('        <figure class="record-media">')
        parts.append('          <img src="../media/{}" alt="{}" loading="lazy">'.format(placed, html.escape(alt, quote=True)))
        if trans:
            parts.append('          <figcaption class="transcript"><span class="transcript-label">transcription ({})</span>'
                         '{}</figcaption>'.format(html.escape(kind), render_text(trans)))
        parts.append('        </figure>')
    parts.append('      </article>')
    return '\n'.join(parts)

HEADER = '''    <h2 id="records">Records</h2>
    <p class="note">Full reproductions of the tweets cited on this page &mdash; text, images, and verbatim
    transcriptions of screenshots &mdash; kept here against link rot, credited and linked to their originals.
    Sourced from the <a href="https://github.com/TheExGenesis/community-archive">community archive</a> and the
    janus corpus. Yours and you&rsquo;d rather it weren&rsquo;t here? <a href="https://github.com/Jordine/pantheon/issues">Open an issue.</a></p>
'''

START, END = '<!-- records:start -->', '<!-- records:end -->'

pages = [d for d in sorted(os.listdir(REPO))
         if os.path.isdir(os.path.join(REPO, d)) and d not in ('media', 'tools', '_dossiers', '.git')
         and os.path.exists(os.path.join(REPO, d, 'index.html'))]

total_records = total_missing = total_imgs = 0
for page in pages:
    path = os.path.join(REPO, page, 'index.html')
    doc = open(path, encoding='utf-8').read()
    seen, ordered = set(), []
    for m in re.finditer(r'(?:x|twitter)\.com/[^/"]*/status/(\d+)', doc):
        tid = m.group(1)
        if tid not in seen:
            seen.add(tid)
            ordered.append(tid)
    if not ordered:
        continue
    records, missing = [], 0
    rows = [(tid, lookup(tid)) for tid in ordered]
    rows = [(tid, r) for tid, r in rows if r]
    missing = len(ordered) - len(rows)
    rows.sort(key=lambda x: (x[1][2] or ''))  # chronological
    for tid, r in rows:
        records.append(render_record(tid, r))
    if not records:
        continue
    block = '{}\n{}\n{}\n    {}'.format(START, HEADER, '\n'.join(records), END)
    if START in doc:
        doc = re.sub(re.escape(START) + '.*?' + re.escape(END), block, doc, flags=re.S)
    else:
        doc = doc.replace('    <p class="backlink">', '    ' + block + '\n\n    <p class="backlink">', 1)
    open(path, 'w', encoding='utf-8').write(doc)
    n_imgs = sum(r.count('<figure') for r in records)
    total_records += len(records); total_missing += missing; total_imgs += n_imgs
    print('{:24s} {:3d} records, {} images, {} cited-but-not-in-db'.format(page, len(records), n_imgs, missing))

print('\nTOTAL: {} records, {} images, {} link-only'.format(total_records, total_imgs, total_missing))
repo_media = sum(os.path.getsize(os.path.join(MEDIA_OUT, f)) for f in os.listdir(MEDIA_OUT))
print('repo media/ size: {:.1f} MB'.format(repo_media / 1e6))
