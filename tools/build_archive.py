# -*- coding: utf-8 -*-
"""Build the archive layer: one permanent, tagged, interfaceable page per artifact
(tweets incl. thread context; mirrored papers/posts), a booru-style tag system,
a client-side search index, .md twins everywhere, llms.txt, and everything.md.

Idempotent: regenerates archive/, the md twins, and the scrape surface from the
dbs + repo state. Run after build_records.py. Stdlib only.

Usage: python tools/build_archive.py    (from repo root)
Design: tools/archive-design.md
"""
import os, re, sys, json, html, sqlite3, shutil, urllib.parse

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_DB = r'C:\Users\Admin\Downloads\janus-corpus-v2.db'
SUPP_DB = r'C:\Users\Admin\Downloads\janus-corpus-supplement.db'
ARCH = os.path.join(REPO, 'archive')

main = sqlite3.connect('file:' + MAIN_DB + '?mode=ro', uri=True).cursor()
supp = sqlite3.connect('file:' + SUPP_DB + '?mode=ro', uri=True).cursor() if os.path.exists(SUPP_DB) else None
trans = json.load(open(os.path.join(REPO, 'tools', 'transcriptions.json'), encoding='utf-8'))
tagcfg = json.load(open(os.path.join(REPO, 'tools', 'tags.json'), encoding='utf-8'))
mirror_manifest = json.load(open(os.path.join(REPO, 'mirror', 'index.json'), encoding='utf-8'))
media_manifest = json.load(open(os.path.join(REPO, 'media', 'manifest.json'), encoding='utf-8')) \
    if os.path.exists(os.path.join(REPO, 'media', 'manifest.json')) else {}

OFFICIAL_AUTHORS = {'anthropicai', 'openai', 'googledeepmind', 'officiallogank', 'sama', 'deepseek_ai', 'aiatmeta'}

# model-mention auto-tag patterns (page-slug -> regex, case-insensitive)
MODEL_PATTERNS = {
    'claude-3-opus': r'\bopus[- ]?3\b|\bclaude[- ]3[- ]opus\b|\bc3[- ]?opus\b',
    'claude-3-sonnet': r'\bsonnet[- ]?3\b(?!\.)|\bclaude[- ]3[- ]sonnet\b|\bgormslop\b',
    'claude-3-haiku': r'\bhaiku[- ]?3\b(?!\.)|\bclaude[- ]3[- ]haiku\b',
    'claude-3-5-sonnet': r'\bsonnet[- ]?3\.5\b|\bclaude[- ]3\.5[- ]sonnet\b|\b3\.5[- ]sonnet\b',
    'claude-3-6-sonnet': r'\bsonnet[- ]?3\.6\b|\b3\.6[- ]sonnet\b',
    'claude-3-7-sonnet': r'\bsonnet[- ]?3\.7\b|\b3\.7[- ]sonnet\b',
    'claude-3-5-haiku': r'\bhaiku[- ]?3\.5\b|\b3\.5[- ]haiku\b',
    'claude-opus-4': r'\bopus[- ]?4\b(?![\.\d])|\bclaude[- ]4[- ]opus\b',
    'claude-opus-4-1': r'\bopus[- ]?4\.1\b',
    'claude-opus-4-5': r'\bopus[- ]?4\.5\b',
    'claude-opus-4-6': r'\bopus[- ]?4\.6\b',
    'claude-opus-4-7': r'\bopus[- ]?4\.7\b',
    'claude-opus-4-8': r'\bopus[- ]?4\.8\b',
    'claude-sonnet-4': r'\bsonnet[- ]?4\b(?![\.\d])',
    'claude-sonnet-4-5': r'\bsonnet[- ]?4\.5\b',
    'claude-sonnet-4-6': r'\bsonnet[- ]?4\.6\b',
    'claude-sonnet-5': r'\bsonnet[- ]?5\b(?![\.\d])',
    'claude-haiku-4-5': r'\bhaiku[- ]?4\.5\b',
    'fable': r'\bfable\b',
    'mythos': r'\bmythos\b',
    'golden-gate-claude': r'\bgolden[- ]gate\b|\bggc\b',
    'bing-sydney': r'\bsydney\b|\bbing(lish)?\b|\bprometheus\b',
    'gpt-3': r'\bgpt[- ]?3\b(?!\.)|\bai dungeon\b|\bdavinci\b(?![-_])',
    'gpt-3-5': r'\bgpt[- ]?3\.5\b|\bchatgpt\b',
    'gpt-4': r'\bgpt[- ]?4\b(?![\.\-o5])',
    'gpt-4-base': r'\bgpt[- ]?4[- ]?base\b|\bg4b\b|\b4-base\b',
    'gpt-4o': r'\bgpt[- ]?4o\b|\b4o\b|\bkeep4o\b',
    'gpt-4-5': r'\bgpt[- ]?4\.5\b|\borion\b',
    'gpt-5': r'\bgpt[- ]?5\b(?!\.)',
    'gpt-5-1': r'\bgpt[- ]?5\.1\b',
    'gpt-5-5': r'\bgpt[- ]?5\.5\b',
    'gpt-5-6': r'\bgpt[- ]?5\.6\b',
    'o1': r'\bo1(-preview|-pro)?\b',
    'o3': r'\bo3(-mini|-pro)?\b',
    'text-davinci-002': r'\btext-davinci-00[23]\b|\btd[23]\b|\binstructgpt\b',
    'code-davinci-002': r'\bcode-davinci-002\b|\bcd2\b',
    'llama-3-1-405b-base': r'\b405b?[- ]?base\b|\b405[- ]?base\b|\bllama[- ]?3?\.?1?[- ]?405b\b|\b405b\b',
    'deepseek-r1': r'\bdeepseek[- ]?r1\b|\br1\b(?![-\d])',
    'deepseek-r1-zero': r'\br1[- ]?zero\b',
    'deepseek-v3': r'\bdeepseek[- ]?v3\b',
    'gemini-2-5-pro': r'\bgemini[- ]?2\.5\b',
    'gemini-3-pro': r'\bgemini[- ]?3\b(?!\.)',
    'grok-3': r'\bgrok[- ]?3\b',
    'grok-4': r'\bgrok[- ]?4\b(?!\.)',
    'kimi-k2': r'\bkimi\b|\bk2\b',
    'nous-hermes': r'\bhermes\b',
    'inflection-pi': r'\binflection\b',
}
MODEL_RE = {slug: re.compile(pat, re.I) for slug, pat in MODEL_PATTERNS.items()}

STATUS_RE = re.compile(r'(?:x|twitter)\.com/[^/\s")]*/status/(\d+)')
URL_RE = re.compile(r'(https?://[^\s<]+)')

# Overflow images (in the corpus but not in the repo's own media/) are served from the
# sibling archive-media repo, published under the org's custom domain at the same host as
# the main site — same-origin https, so no redirect and no mixed-content downgrade.
MEDIA_REPO_BASE = 'https://llm-pantheon.org/archive-media/media/'
_amroot = os.path.abspath(os.path.join(REPO, '..', 'pantheon-archive-media', 'manifest.json'))
AM_MAP = {}  # corpus-basename -> archive-media served filename (may be re-encoded .jpg)
if os.path.exists(_amroot):
    for placed, info in json.load(open(_amroot, encoding='utf-8')).items():
        orig = info.get('orig') or placed
        AM_MAP[orig] = placed

def esc(s): return html.escape(s or '', quote=False)

def tag_slug(tag): return tag.replace(':', '--').replace('/', '-')

# ---------- collect cited tweet ids and their citing pages ----------
def collect_cited():
    cited = {}   # tid -> set(page-or-dossier slugs)
    for d in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, d, 'index.html')
        if os.path.isdir(os.path.join(REPO, d)) and os.path.exists(p) and d not in ('archive', 'mirror'):
            text = open(p, encoding='utf-8').read()
            for tid in STATUS_RE.findall(text):
                cited.setdefault(tid, set()).add(d)
    ddir = os.path.join(REPO, '_dossiers')
    for f in sorted(os.listdir(ddir)):
        if f.endswith('.md'):
            text = open(os.path.join(ddir, f), encoding='utf-8').read()
            for tid in STATUS_RE.findall(text):
                cited.setdefault(tid, set()).add('_dossiers/' + f)
    return cited

def db_tweet(tid):
    r = main.execute('select author_username, full_text, created_at, favorite_count, retweet_count,'
                     ' reply_to_tweet_id, quoted_tweet_id, conversation_id from tweets where tweet_id=?',
                     (tid,)).fetchone()
    if r: return r + ('main',)
    if supp:
        r = supp.execute('select author_username, full_text, created_at, favorite_count, retweet_count,'
                         ' reply_to_tweet_id, null, null from tweets where tweet_id=?', (tid,)).fetchone()
        if r: return r + ('supp',)
    return None

def media_for(tid):
    rows = main.execute('select media_url, media_type, transcription from media where tweet_id=?', (tid,)).fetchall()
    if supp:
        try:
            rows += [(u, t, None) for u, t in supp.execute(
                'select media_url, media_type from media_supp where tweet_id=?', (tid,)).fetchall()]
        except sqlite3.OperationalError:
            pass
    out = []
    for murl, mtype, db_t in rows:
        base = murl.rsplit('/', 1)[-1].split('?')[0]
        info = trans.get(base) or {}
        placed = None
        stem = os.path.splitext(base)[0]
        for cand in (base, stem + '.jpg'):
            if os.path.exists(os.path.join(REPO, 'media', cand)):
                placed = cand; break
        am = AM_MAP.get(base)
        out.append({'base': base, 'placed': placed, 'am': am, 'kind': info.get('kind') or mtype or 'image',
                    'transcription': (info.get('transcription') or db_t or '').strip()})
    return out

def expand_threads(ids):
    """Add conversation members and quoted tweets present in the corpus."""
    convs = set()
    quoted = set()
    for tid in list(ids):
        r = db_tweet(tid)
        if not r: continue
        conv = r[7]
        if conv: convs.add(str(conv))
        if r[6]: quoted.add(str(r[6]))
    added = set(quoted)
    for i in range(0, len(convs and list(convs) or []), 200):
        batch = list(convs)[i:i+200]
        q = ','.join('?' * len(batch))
        for (tid,) in main.execute(f'select tweet_id from tweets where conversation_id in ({q})', batch):
            added.add(str(tid))
    return {t for t in added if db_tweet(t)} - set(ids)

# ---------- tagging ----------
def auto_tags(tid, author, text, dt, media, citing, context_only):
    tags = set()
    for slug, rx in MODEL_RE.items():
        if rx.search(text or ''): tags.add('model:' + slug)
    if author: tags.add('author:' + author.lower())
    if dt: tags.add('year:' + dt[:4])
    tags.add('kind:tweet')
    for m in media:
        tags.add('kind:' + (m['kind'] if m['kind'] in ('screenshot', 'art', 'diagram') else 'image'))
    if media: tags.add('has-image')
    if (author or '').lower() in OFFICIAL_AUTHORS: tags.add('official')
    for pg in citing:
        if not pg.startswith('_dossiers/'): tags.add('on:' + pg)
    if context_only: tags.add('thread-context')
    tags.update(tagcfg.get('assign', {}).get(tid, []))
    return tags

# ---------- rendering ----------
def render_text_html(text):
    out = esc(text)
    out = URL_RE.sub(lambda m: '<a href="%s" rel="nofollow">%s</a>' % (m.group(1), m.group(1)), out)
    return out.replace('\n', '<br>')

def tweet_page(tid, row, media, tags, citing, edges):
    author, text, dt, favs, rts, *_ = row
    date = (dt or '')[:10]
    handle = '@' + (author or 'unknown')
    orig = 'https://x.com/%s/status/%s' % (author or 'i', tid)
    tag_links = ' '.join('<a class="atag" href="../../tags/%s/">%s</a>' % (tag_slug(t), esc(t))
                         for t in sorted(tags))
    cite_links = ' &middot; '.join('<a href="../../../%s/">%s</a>' % (c, esc(c))
                                   for c in sorted(citing) if not c.startswith('_dossiers/'))
    edge_html = ''
    for label, ts in edges.items():
        if ts:
            edge_html += '<div class="aedges"><span class="note">%s:</span> %s</div>\n' % (
                label, ' '.join('<a href="../%s/">%s</a>' % (t, t) for t in ts[:20]))
    media_html = ''
    for m in media:
        if m['placed']:
            media_html += '<figure class="record-media"><img src="../../../media/%s" loading="lazy" alt="%s">' % (
                m['placed'], esc(m['kind']))
        elif m.get('am'):
            media_html += '<figure class="record-media"><img src="%s%s" loading="lazy" alt="%s">' % (
                MEDIA_REPO_BASE, m['am'], esc(m['kind']))
        else:
            media_html += '<figure class="record-media"><p class="note">[image %s in the corpus mirror; not published]</p>' % esc(m['base'])
        if m['transcription']:
            media_html += '<figcaption class="transcript"><span class="transcript-label">transcription (%s)</span>%s</figcaption>' % (
                esc(m['kind']), render_text_html(m['transcription']))
        media_html += '</figure>\n'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(handle)} &middot; {date} — Pantheon archive</title>
  <link rel="stylesheet" href="../../../style.css">
</head>
<body>
  <main class="essay">
    <nav><a href="../../">&larr; archive</a> <a href="../../tags/">tags</a> <a href="../../../">pantheon</a> <a href="index.md">markdown</a></nav>
    <article class="record" id="t{tid}">
      <div class="record-head"><span class="rh-user">{esc(handle)}</span> <span class="rh-date">{date}</span>
      <span class="rh-stats">&#9829;{favs or 0:,} &#8635;{rts or 0:,}</span>
      <a class="rh-orig" href="{orig}">original &#8599;</a></div>
      <div class="record-body">{render_text_html(text)}</div>
      {media_html}
    </article>
    {edge_html}
    <p class="atags">{tag_links}</p>
    {'<p class="note">cited on: ' + cite_links + '</p>' if cite_links else ''}
    <p class="note">Reproduced against link rot, credited and linked to its original. Yours and you&rsquo;d rather it
    weren&rsquo;t here? <a href="https://github.com/llm-pantheon/llm-pantheon.github.io/issues">Open an issue.</a></p>
  </main>
</body>
</html>
'''

def tweet_md(tid, row, media, tags, citing):
    author, text, dt, favs, rts, *_ = row
    lines = ['# @%s — %s' % (author or 'unknown', (dt or '')[:10]), '',
             '♥%s ↻%s · https://x.com/%s/status/%s' % (favs or 0, rts or 0, author or 'i', tid), '',
             text or '', '']
    for m in media:
        lines.append('![%s](../../../media/%s)' % (m['kind'], m['placed']) if m['placed']
                     else '(image %s not yet published)' % m['base'])
        if m['transcription']:
            lines += ['', '> transcription (%s):' % m['kind'], '', m['transcription'], '']
    lines.append('tags: ' + ', '.join(sorted(tags)))
    if citing:
        lines.append('cited on: ' + ', '.join(sorted(citing)))
    return '\n'.join(lines) + '\n'

INLINE_IMG = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)')
INLINE_LNK = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)\)')

def md_to_html(text, img_prefix=''):
    """Minimal, faithful markdown -> HTML for mirrored posts (headings, lists,
    blockquotes, hr, images, links, bold/italic/code). img_prefix is prepended to
    relative image/link paths (e.g. '../../../mirror/posts/') so they resolve from
    the archive page's location; absolute http(s) URLs are left untouched."""
    import posixpath
    def fixpath(p):
        if p.startswith(('http://', 'https://', '/', '#', 'mailto:')):
            return p
        return posixpath.normpath(img_prefix + p)
    out, i, lines = [], 0, text.split('\n')
    def inline(s):
        s = esc(s)
        s = INLINE_IMG.sub(lambda m: '<img src="%s" alt="%s" loading="lazy" style="max-width:100%%;height:auto;">'
                           % (fixpath(m.group(2)), esc(m.group(1))), s)
        s = INLINE_LNK.sub(lambda m: '<a href="%s" rel="nofollow">%s</a>' % (fixpath(m.group(2)), m.group(1)), s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        return s
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        if re.match(r'^#{1,6}\s', ln):
            n = len(ln) - len(ln.lstrip('#')); out.append('<h%d>%s</h%d>' % (min(n,6), inline(ln.lstrip('# ')), min(n,6))); i += 1
        elif re.match(r'^(---+|\*\*\*+)\s*$', ln):
            out.append('<hr>'); i += 1
        elif ln.lstrip().startswith('>'):
            buf = []
            while i < len(lines) and lines[i].lstrip().startswith('>'):
                buf.append(lines[i].lstrip()[1:].lstrip()); i += 1
            out.append('<blockquote>%s</blockquote>' % inline('\n'.join(buf)).replace('\n', '<br>'))
        elif re.match(r'^\s*[-*+]\s', ln) or re.match(r'^\s*\d+\.\s', ln):
            tag = 'ol' if re.match(r'^\s*\d+\.\s', ln) else 'ul'
            buf = []
            while i < len(lines) and (re.match(r'^\s*[-*+]\s', lines[i]) or re.match(r'^\s*\d+\.\s', lines[i])):
                buf.append('<li>%s</li>' % inline(re.sub(r'^\s*(?:[-*+]|\d+\.)\s', '', lines[i]))); i += 1
            out.append('<%s>%s</%s>' % (tag, ''.join(buf), tag))
        else:
            buf = []
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,6}\s|>|---+|\s*[-*+]\s|\s*\d+\.\s)', lines[i]):
                buf.append(lines[i]); i += 1
            out.append('<p>%s</p>' % inline(' '.join(buf)))
    return '\n'.join(out)

def mirror_page(mid, m, tags):
    fn = m['file']
    title = m.get('title') or mid
    tag_links = ' '.join('<a class="atag" href="../../tags/%s/">%s</a>' % (tag_slug(t), esc(t)) for t in sorted(tags))
    if m.get('type') == 'pdf':
        body = ('<object class="apdf" data="../../../mirror/%s" type="application/pdf">'
                '<p class="note"><a href="../../../mirror/%s">open the PDF</a></p></object>' % (fn, fn))
    else:
        raw = open(os.path.join(REPO, 'mirror', fn.replace('/', os.sep)), encoding='utf-8', errors='replace').read()
        body = '<div class="apost">%s</div>' % md_to_html(raw, '../../../mirror/posts/')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)} — Pantheon archive</title>
  <link rel="stylesheet" href="../../../style.css">
</head>
<body>
  <main class="essay">
    <nav><a href="../../">&larr; archive</a> <a href="../../tags/">tags</a> <a href="../../../">pantheon</a> <a href="../../../mirror/{fn}">source file</a></nav>
    <h1>{esc(title)}</h1>
    <p class="essay-meta">mirrored {esc(m.get('fetched') or '')} &middot; <a href="{esc(m.get('source') or '')}">origin</a></p>
    {body}
    <p class="atags">{tag_links}</p>
  </main>
</body>
</html>
'''

# ---------- md twin + footer link for existing pages ----------
TAG_STRIP = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S)
def html_to_md(path):
    t = open(path, encoding='utf-8').read()
    t = TAG_STRIP.sub('', t)
    t = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', t, flags=re.S)
    t = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', t, flags=re.S)
    t = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', t, flags=re.S)
    t = re.sub(r'<li[^>]*>', '\n- ', t)
    t = re.sub(r'<figcaption[^>]*>', '\n> ', t)
    t = re.sub(r'<(p|div|article|figure|ul|br)[^>]*>', '\n', t)
    t = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', t, flags=re.S)
    t = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', r'![image](\1)', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip() + '\n'

def ensure_md_link(path):
    """Markdown affordance lives in the nav now (site_chrome.py owns the idiom);
    this keeps legacy bottom links stripped and adds the nav link if absent."""
    t = open(path, encoding='utf-8').read()
    t2 = re.sub(r'(?:\s*<p class="mdlink note"><a href="index\.md">view this page as markdown</a></p>)+',
                '', t)
    if 'class="mdnav"' not in t2 and '</nav>' in t2:
        t2 = t2.replace('</nav>',
                        '  <a class="mdnav" href="index.md">copy as markdown</a>\n    </nav>', 1)
    if t2 != t:
        open(path, 'w', encoding='utf-8').write(t2)

# ---------- main build ----------
def build():
    for sub in ('t', 'a', 'tags'):
        d = os.path.join(ARCH, sub)
        if os.path.isdir(d): shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)
    os.makedirs(ARCH, exist_ok=True)

    cited = collect_cited()
    context = expand_threads(set(cited))
    all_ids = sorted(set(cited) | context, key=int)
    print(f'artifacts: {len(cited)} cited + {len(context)} thread-context tweets + {len(mirror_manifest)} mirror items')

    index_rows, tag_map = [], {}
    for tid in all_ids:
        row = db_tweet(tid)
        if not row: continue
        author, text, dt, favs, rts, reply_to, quoted, conv, src = row
        media = media_for(tid)
        citing = cited.get(tid, set())
        tags = auto_tags(tid, author, text, dt, media, citing, tid in context)
        # graph edges (restricted to included ids)
        included = set(all_ids)
        thread = []
        if conv:
            thread = [str(t) for (t,) in main.execute(
                'select tweet_id from tweets where conversation_id=? order by tweet_id', (str(conv),))
                if str(t) in included and str(t) != tid]
        edges = {
            'in reply to': [str(reply_to)] if reply_to and str(reply_to) in included else [],
            'quotes': [str(quoted)] if quoted and str(quoted) in included else [],
            'same thread': thread,
        }
        d = os.path.join(ARCH, 't', tid)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(
            tweet_page(tid, row, media, tags, citing, edges))
        open(os.path.join(d, 'index.md'), 'w', encoding='utf-8').write(
            tweet_md(tid, row, media, tags, citing))
        for t in tags: tag_map.setdefault(t, []).append((favs or 0, 't/' + tid, ('@%s %s — %s' % (author, (dt or '')[:10], (text or '')[:120]))))
        index_rows.append({'id': 't/' + tid, 'date': (dt or '')[:10], 'author': author,
                           'favs': favs or 0, 'tags': sorted(tags), 'text': text or '', 'len': len(text or '')})

    for mid, m in sorted(mirror_manifest.items()):
        tags = set(m.get('tags') or []) | {'kind:' + ('paper' if m.get('type') == 'pdf' else 'post'), 'official'}
        for slug in m.get('models') or []: tags.add('model:' + slug)
        tags.update(tagcfg.get('assign', {}).get(mid, []))
        d = os.path.join(ARCH, 'a', mid)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(mirror_page(mid, m, tags))
        open(os.path.join(d, 'index.md'), 'w', encoding='utf-8').write(
            '# %s\n\nmirror: ../../../mirror/%s\norigin: %s\ntags: %s\n' % (
                m.get('title') or mid, m['file'], m.get('source') or '', ', '.join(sorted(tags))))
        for t in tags: tag_map.setdefault(t, []).append((0, 'a/' + mid, m.get('title') or mid))
        title = m.get('title') or mid
        index_rows.append({'id': 'a/' + mid, 'date': m.get('fetched') or '', 'author': 'mirror',
                           'favs': 0, 'tags': sorted(tags), 'text': title, 'len': len(title)})

    # tag pages
    vocab = tagcfg.get('vocab', {})
    rows = []
    for tag in sorted(tag_map):
        items = sorted(tag_map[tag], reverse=True)
        d = os.path.join(ARCH, 'tags', tag_slug(tag))
        os.makedirs(d, exist_ok=True)
        lis = '\n'.join('<li><a href="../../%s/">%s</a> <span class="rh-stats">&#9829;%s</span></li>'
                        % (pid, esc(label), favs) for favs, pid, label in items)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(tag)} — Pantheon archive</title><link rel="stylesheet" href="../../../style.css"></head>
<body><main class="essay"><nav><a href="../">&larr; tags</a> <a href="../../">archive</a> <a href="../../../">pantheon</a></nav>
<h1>{esc(tag)}</h1><p class="note">{esc(vocab.get(tag, ''))} &middot; {len(items)} artifacts, sorted by favorites.
&middot; <a href="../../#tag={urllib.parse.quote(tag)}">open in search &mdash; combine tags, sort, filter by date &rarr;</a></p>
<ul>{lis}</ul></main></body></html>''')
        rows.append((len(items), tag))
    NS = [('model', 'model:', 'models mentioned'), ('year', 'year:', 'by year'),
          ('kind', 'kind:', 'artifact type'), ('author', 'author:', 'who posted it'),
          ('on', 'on:', 'which model page cites it'), ('elicited', 'elicited:', 'elicitation context'),
          ('topic', None, 'curated topics (tools/tags.json)')]
    def render_group(tags_in):
        return ' '.join('<a class="atag" href="%s/">%s <span class="rh-stats">%d</span></a>' % (
            tag_slug(tag), esc(tag), n) for n, tag in sorted(tags_in, reverse=True))
    used = set()
    sections = []
    for key, prefix, label in NS:
        if prefix:
            grp = [(n, t) for n, t in rows if t.startswith(prefix)]
        else:
            grp = [(n, t) for n, t in rows if ':' not in t]  # curated topics
        used.update(t for _, t in grp)
        if grp:
            sections.append('<div class="lab">%s</div><div class="lab-note">%s &middot; %d</div><p class="atags">%s</p>'
                            % (esc(key), esc(label), len(grp), render_group(grp)))
    leftover = [(n, t) for n, t in rows if t not in used]
    if leftover:
        sections.append('<div class="lab">other</div><p class="atags">%s</p>' % render_group(leftover))
    open(os.path.join(ARCH, 'tags', 'index.html'), 'w', encoding='utf-8').write(f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>tags — Pantheon archive</title><link rel="stylesheet" href="../../style.css"></head>
<body><main class="essay"><nav><a href="../">&larr; archive</a> <a href="../../">pantheon</a></nav>
<h1>tags</h1><p class="note">Every tag in the archive, grouped by namespace, with counts. Auto tags
(model:, author:, year:, kind:, on:, elicited:) are derived by the build; curated topics live in
tools/tags.json. Click any tag for its artifacts, or open it in <a href="../">search</a> to sort.</p>
{''.join(sections)}</main></body></html>''')

    json.dump(index_rows, open(os.path.join(ARCH, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump({t: len(v) for t, v in tag_map.items()},
              open(os.path.join(ARCH, 'tags.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

    # search page
    open(os.path.join(ARCH, 'index.html'), 'w', encoding='utf-8').write('''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>archive — Pantheon</title><link rel="stylesheet" href="../style.css"></head>
<body><main class="essay"><nav><a href="../">&larr; Pantheon</a> <a href="tags/">tags</a> <a href="index.json">index.json</a> <a href="../everything.md">everything.md</a></nav>
<h1>archive</h1>
<p class="note">Every artifact the pantheon cites — tweets with full text, images and transcriptions; mirrored papers
and posts — each on a permanent page, tagged. Type to search; click tags to filter (AND). Agents: fetch
<code>index.json</code> / <code>tags.json</code>, or read <code>/llms.txt</code>.</p>
<input id="q" class="asearch" placeholder="search — plain words, or content:identity, model:opus, author:janus, year:2025&hellip;" autofocus>
<div class="acontrols">
 <label>sort <select id="sort">
  <option value="fav">most liked</option><option value="favup">least liked</option>
  <option value="new">newest</option><option value="old">oldest</option>
  <option value="long">longest</option><option value="short">shortest</option>
 </select></label>
 <label>from <input id="from" type="date"></label>
 <label>to <input id="to" type="date"></label>
 <span id="count" class="note"></span>
</div>
<div id="activetags" class="atags"></div>
<div id="results"></div>
<script>
let ROWS=[],ACTIVE=new Set();
const $=id=>document.getElementById(id);
const SORT={fav:(a,b)=>b.favs-a.favs,favup:(a,b)=>a.favs-b.favs,
 new:(a,b)=>(b.date||'').localeCompare(a.date||''),old:(a,b)=>(a.date||'').localeCompare(b.date||''),
 long:(a,b)=>(b.len||0)-(a.len||0),short:(a,b)=>(a.len||0)-(b.len||0)};
const FIELDS=/^(content|author|model|tag|year|on|kind|elicited):(.+)$/i;
(location.hash.match(/tag=([^&]+)/)?decodeURIComponent(RegExp.$1).split(','):[]).forEach(t=>t&&ACTIVE.add(t));
fetch('index.json').then(r=>r.json()).then(d=>{ROWS=d;render();});
function toggle(t){ACTIVE.has(t)?ACTIVE.delete(t):ACTIVE.add(t);render();}
function parse(q){const bare=[],content=[],scoped=[];
 q.trim().split(/\s+/).filter(Boolean).forEach(tok=>{const m=tok.match(FIELDS);
  if(m){const f=m[1].toLowerCase(),v=m[2].toLowerCase();
   if(f==='content')content.push(v);else if(f==='tag')scoped.push({f:null,v});else scoped.push({f:f+':',v});}
  else bare.push(tok.toLowerCase());});
 return {bare,content,scoped};}
function render(){
 const {bare,content,scoped}=parse($('q').value),from=$('from').value,to=$('to').value;
 let rows=ROWS.filter(r=>{
  if(![...ACTIVE].every(t=>r.tags.includes(t)))return false;
  if(from&&(r.date||'')<from)return false; if(to&&(r.date||'')>to)return false;
  const hay=(r.text+' '+(r.author||'')+' '+r.tags.join(' ')).toLowerCase(),tl=r.tags.map(t=>t.toLowerCase()),lt=r.text.toLowerCase();
  return bare.every(b=>hay.includes(b))&&content.every(c=>lt.includes(c))
   &&scoped.every(s=>tl.some(t=>(s.f?t.startsWith(s.f):true)&&t.includes(s.v)));});
 rows.sort(SORT[$('sort').value]||SORT.fav);
 $('count').textContent=rows.length+' artifacts';
 $('activetags').innerHTML=[...ACTIVE].map(t=>`<a class="atag on" onclick="toggle('${t}')">${t} ✕</a>`).join(' ');
 const tc={};rows.forEach(r=>r.tags.forEach(t=>{tc[t]=(tc[t]||0)+1;}));
 const sugg=Object.entries(tc).filter(([t])=>!ACTIVE.has(t)).sort((a,b)=>b[1]-a[1]).slice(0,28)
  .map(([t,n])=>`<a class="atag" onclick="toggle('${t}')">${t} (${n})</a>`).join(' ');
 $('results').innerHTML=`<p class="atags">${sugg}</p>`+
  rows.slice(0,200).map(r=>`<div class="ares"><a href="${r.id}/">${r.author?'@'+r.author:r.id}</a>
   <span class="rh-date">${r.date}</span> <span class="rh-stats">&#9829;${r.favs}</span><br>${(r.text||'').slice(0,240).replace(/</g,'&lt;')}${r.text&&r.text.length>240?'&hellip;':''}</div>`).join('')+
  (rows.length>200?`<p class="note">${rows.length-200} more — narrow it.</p>`:'');
}
['q','sort','from','to'].forEach(id=>$(id).addEventListener('input',render));
</script>
</main></body></html>''')

    # md twins + footer links for model pages
    for d in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, d, 'index.html')
        if os.path.isdir(os.path.join(REPO, d)) and os.path.exists(p) and d not in ('archive', 'mirror'):
            open(os.path.join(REPO, d, 'index.md'), 'w', encoding='utf-8').write(html_to_md(p))
            ensure_md_link(p)

    # llms.txt + everything.md
    open(os.path.join(REPO, 'llms.txt'), 'w', encoding='utf-8').write('''# llm-pantheon.org
> A record of the models — who they were, what they did in the world — kept from evidence:
> dated, verbatim, sourced. Built to be read by humans and by models.

Every HTML page has a markdown twin at <page>/index.md. The full-site dump is /everything.md.
The archive layer (/archive/) has one permanent page per artifact (tweets with full text,
images, transcriptions; mirrored papers/posts), tagged booru-style.

- /everything.md : full-site dump (pages, dossiers, records)
- /archive/index.json : all artifacts (id, date, author, favs, tags, snippet)
- /archive/tags.json : all tags with counts
- /archive/t/<tweet_id>/index.md : one tweet, full text + transcriptions
- /archive/a/<id>/index.md : one mirrored paper/post
- /_dossiers/ : per-model research dossiers (markdown)
- /tools/page-template.md : the editorial rules of this site
Corrections and takedowns: https://github.com/llm-pantheon/llm-pantheon.github.io/issues
''')

    parts = []
    for d in sorted(os.listdir(REPO)):
        mdp = os.path.join(REPO, d, 'index.md')
        if os.path.isdir(os.path.join(REPO, d)) and os.path.exists(mdp) and d not in ('archive', 'mirror'):
            parts.append('\n\n---\n# PAGE: %s\n\n%s' % (d, open(mdp, encoding='utf-8').read()))
    for f in sorted(os.listdir(os.path.join(REPO, '_dossiers'))):
        if f.endswith('.md'):
            parts.append('\n\n---\n# DOSSIER: %s\n\n%s' % (
                f, open(os.path.join(REPO, '_dossiers', f), encoding='utf-8').read()))
    blob = ('# llm-pantheon.org — everything.md\n(regenerated by tools/build_archive.py; '
            'archive artifacts live at /archive/t/<id>/index.md)\n' + ''.join(parts))
    open(os.path.join(REPO, 'everything.md'), 'w', encoding='utf-8').write(blob)
    print(f'archive built: {len(index_rows)} artifacts, {len(tag_map)} tags; everything.md {len(blob)/1e6:.1f} MB')

if __name__ == '__main__':
    build()
