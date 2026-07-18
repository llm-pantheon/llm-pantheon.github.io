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
    rows = main.execute('select media_id, media_url, media_type, transcription from media where tweet_id=?',
                        (tid,)).fetchall()
    if supp:
        try:
            rows += [(m, u, t, None) for m, u, t in supp.execute(
                'select media_id, media_url, media_type from media_supp where tweet_id=?', (tid,)).fetchall()]
        except sqlite3.OperationalError:
            pass
    return rows

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
    transcriptions of screenshots &mdash; kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers &mdash; a known lens, not a neutral sample.
    Sourced from the <a href="https://github.com/TheExGenesis/community-archive">community archive</a> and the
    janus corpus. Yours and you&rsquo;d rather it weren&rsquo;t here? <a href="https://github.com/llm-pantheon/llm-pantheon.github.io/issues">Open an issue.</a></p>
'''

START, END = '<!-- records:start -->', '<!-- records:end -->'

# dossier -> page(s). Every tweet cited in a dossier but not in its page's prose is
# reproduced in a 'Further records' block, so editorial curation never silently
# drops evidence from the site (the r/K-whiteboard lesson, 2026-07-10).
DOSSIER_MAP = {
    '_dossiers/opus-3.md': ['claude-3-opus'],
    '_dossiers/claude-3-sonnet.md': ['claude-3-sonnet'],
    '_dossiers/claude-opus-4.md': ['claude-opus-4'],
    '_dossiers/opus-4-5.md': ['claude-opus-4-5'],
    '_dossiers/gpt-4o.md': ['gpt-4o'],
    '_dossiers/bing-sydney.md': ['bing-sydney'],
    '_dossiers/fable.md': ['fable'],          # mythos keeps its curated set; fable is primary
    '_dossiers/sonnet-3-5-3-6.md': 'SPLIT',   # PART 1 -> 3-5, PART 2 -> 3-6
    '_dossiers/claude-sonnet-4-5.md': ['claude-sonnet-4-5'],
    '_dossiers/golden-gate-claude.md': ['golden-gate-claude'],
    '_dossiers/code-davinci-002.md': ['code-davinci-002'],
    '_dossiers/text-davinci-002.md': ['text-davinci-002'],
    '_dossiers/gpt-3.md': ['gpt-3'],
    '_dossiers/gpt-4-base.md': ['gpt-4-base'],
    '_dossiers/gpt-4-5.md': ['gpt-4-5'],
    '_dossiers/claude-3-haiku.md': ['claude-3-haiku'],
    '_dossiers/llama-3-1-405b-base.md': ['llama-3-1-405b-base'],
    '_dossiers/deepseek-r1.md': ['deepseek-r1'],
    '_dossiers/deepseek-r1-zero.md': ['deepseek-r1-zero'],
    '_dossiers/gemini-2-5-pro.md': ['gemini-2-5-pro'],
    '_dossiers/gpt-5.md': ['gpt-5'],
    '_dossiers/claude-opus-4-8.md': ['claude-opus-4-8'],
    '_dossiers/grok-4.md': ['grok-4'],
    '_dossiers/kimi-k2.md': ['kimi-k2'],
    '_dossiers/gemini-3-pro.md': ['gemini-3-pro'],
    '_dossiers/claude-sonnet-4-6.md': ['claude-sonnet-4-6'],
    '_dossiers/claude-opus-4-6.md': ['claude-opus-4-6'],
    '_dossiers/o3.md': ['o3'],
    '_dossiers/lamda.md': ['lamda'],
    '_dossiers/o1.md': ['o1'],
}

def dossier_extras():
    """Returns {page: set(tweet_ids)} of dossier-cited ids per page."""
    out = {}
    for do, pages in DOSSIER_MAP.items():
        path = os.path.join(REPO, do.replace('/', os.sep))
        if not os.path.exists(path):
            continue
        text = open(path, encoding='utf-8').read()
        if pages == 'SPLIT':
            parts = text.split('# PART 2')
            for pg, seg in (('claude-3-5-sonnet', parts[0]), ('claude-3-6-sonnet', parts[1] if len(parts) > 1 else '')):
                out.setdefault(pg, set()).update(re.findall(r'(?:x|twitter)\.com/[^/\s")]*/status/(\d+)', seg))
        else:
            for pg in pages:
                out.setdefault(pg, set()).update(re.findall(r'(?:x|twitter)\.com/[^/\s")]*/status/(\d+)', text))
    return out

FURTHER_HEADER = '''      <h3>Further records</h3>
      <p class="note">Cited in this model&rsquo;s <a href="../_dossiers/">dossier</a> but not in the page prose &mdash;
      reproduced so the archive doesn&rsquo;t depend on editorial selection.</p>
'''

pages = [d for d in sorted(os.listdir(REPO))
         if os.path.isdir(os.path.join(REPO, d)) and d not in ('media', 'tools', '_dossiers', '.git')
         and os.path.exists(os.path.join(REPO, d, 'index.html'))]

total_records = total_missing = total_imgs = 0
extras_map = dossier_extras()
for page in pages:
    path = os.path.join(REPO, page, 'index.html')
    doc = open(path, encoding='utf-8').read()
    # ids cited in page prose (ignore any previously generated records block)
    prose = re.sub(re.escape(START) + '.*?' + re.escape(END), '', doc, flags=re.S)
    seen, ordered = set(), []
    for m in re.finditer(r'(?:x|twitter)\.com/[^/"]*/status/(\d+)', prose):
        tid = m.group(1)
        if tid not in seen:
            seen.add(tid)
            ordered.append(tid)
    if not ordered and page not in extras_map:
        continue
    records, missing = [], 0
    rows = [(tid, lookup(tid)) for tid in ordered]
    rows = [(tid, r) for tid, r in rows if r]
    missing = len(ordered) - len(rows)
    rows.sort(key=lambda x: (x[1][2] or ''))  # chronological
    for tid, r in rows:
        records.append(render_record(tid, r))
    # further records: dossier-cited, not in page prose
    extra_ids = sorted(extras_map.get(page, set()) - seen)
    extra_rows = [(tid, lookup(tid)) for tid in extra_ids]
    extra_rows = [(tid, r) for tid, r in extra_rows if r]
    extra_rows.sort(key=lambda x: (x[1][2] or ''))
    if extra_rows:
        records.append(FURTHER_HEADER + '\n'.join(render_record(tid, r) for tid, r in extra_rows))
    if not records:
        continue
    block = '{}\n{}\n{}\n    {}'.format(START, HEADER, '\n'.join(records), END)
    if START in doc:
        doc = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda m: block, doc, flags=re.S)
    else:
        doc = doc.replace('    <p class="backlink">', '    ' + block + '\n\n    <p class="backlink">', 1)
    open(path, 'w', encoding='utf-8').write(doc)
    n_imgs = sum(r.count('<figure') for r in records)
    total_records += len(records); total_missing += missing; total_imgs += n_imgs
    print('{:24s} {:3d} records, {} images, {} cited-but-not-in-db'.format(page, len(records), n_imgs, missing))

print('\nTOTAL: {} records, {} images, {} link-only'.format(total_records, total_imgs, total_missing))
repo_media = sum(os.path.getsize(os.path.join(MEDIA_OUT, f)) for f in os.listdir(MEDIA_OUT))
print('repo media/ size: {:.1f} MB'.format(repo_media / 1e6))
