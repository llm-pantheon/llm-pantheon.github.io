# -*- coding: utf-8 -*-
"""Pantheon mirror engine — stdlib only.

Reads tools/mirror_targets.json, fetches anything not yet in mirror/index.json:
  type "pdf"  -> mirror/papers/<id>.pdf
  type "post" -> mirror/posts/<id>.md   (html -> markdown, links preserved,
                 yaml-ish frontmatter; LessWrong via GraphQL; substack comments best-effort)
Idempotent: existing manifest ids are skipped. Regenerates mirror/index.html.

Usage: python tools/mirror.py [--only id1,id2] [--refetch id]
"""
import os, re, sys, json, html, hashlib, time, urllib.request, urllib.parse
from html.parser import HTMLParser
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = os.path.join(REPO, 'tools', 'mirror_targets.json')
MDIR = os.path.join(REPO, 'mirror')
PAPERS = os.path.join(MDIR, 'papers')
POSTS = os.path.join(MDIR, 'posts')
MANIFEST = os.path.join(MDIR, 'index.json')
UA = {'User-Agent': 'Mozilla/5.0 (compatible; pantheon-mirror/1.0; +https://llm-pantheon.org)'}
os.makedirs(PAPERS, exist_ok=True)
os.makedirs(POSTS, exist_ok=True)

def get(url, timeout=60, binary=False):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            return data if binary else data.decode('utf-8', errors='replace')
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(3 * (attempt + 1))

# ---------- html -> markdown (stdlib) ----------
BLOCK = {'p', 'div', 'section', 'article', 'br', 'tr'}
SKIP = {'script', 'style', 'nav', 'noscript', 'svg', 'iframe', 'form', 'button', 'aside'}

class MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.href = None
        self.skip = 0
        self.pre = 0
        self.listdepth = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.out.append('\n\n' + '#' * int(tag[1]) + ' ')
        elif tag == 'a':
            self.href = a.get('href')
            self.out.append('[')
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag == 'blockquote':
            self.out.append('\n\n> ')
        elif tag in ('ul', 'ol'):
            self.listdepth += 1
        elif tag == 'li':
            self.out.append('\n' + '  ' * (self.listdepth - 1) + '- ')
        elif tag == 'pre':
            self.pre += 1
            self.out.append('\n\n```\n')
        elif tag == 'code' and not self.pre:
            self.out.append('`')
        elif tag == 'img':
            alt = a.get('alt', '')
            src = a.get('src', '')
            if src:
                self.out.append('![{}]({})'.format(alt, src))
        elif tag == 'hr':
            self.out.append('\n\n---\n\n')
        elif tag in BLOCK:
            self.out.append('\n\n')
    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == 'a':
            self.out.append('](' + (self.href or '') + ')')
            self.href = None
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag in ('ul', 'ol'):
            self.listdepth = max(0, self.listdepth - 1)
            self.out.append('\n')
        elif tag == 'pre':
            self.pre = max(0, self.pre - 1)
            self.out.append('\n```\n\n')
        elif tag == 'code' and not self.pre:
            self.out.append('`')
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.out.append('\n\n')
    def handle_data(self, data):
        if self.skip:
            return
        if self.pre:
            self.out.append(data)
        else:
            self.out.append(re.sub(r'\s+', ' ', data))

def html_to_md(fragment):
    p = MD()
    p.feed(fragment)
    text = ''.join(p.out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+\n', '\n', text)
    return text.strip()

# ---------- content extraction ----------
def extract_main(page_html):
    """Crude but serviceable: prefer <article>, else the densest content div."""
    m = re.search(r'<article[\s>].*?</article>', page_html, re.S | re.I)
    if m:
        return m.group(0)
    candidates = re.findall(r'<div[^>]*class="[^"]*(?:available-content|body markup|post-content|entry-content|PostsPage-postContent|content)[^"]*"[^>]*>.*?</div>\s*(?=<div|<footer|</main|</body)', page_html, re.S | re.I)
    if candidates:
        return max(candidates, key=len)
    m = re.search(r'<body[\s>].*?</body>', page_html, re.S | re.I)
    return m.group(0) if m else page_html

def lw_post(url):
    """LessWrong/AF via GraphQL: clean htmlBody + metadata."""
    m = re.search(r'/posts/([A-Za-z0-9]+)/', url)
    if not m:
        return None
    q = {'query': '{ post(input:{selector:{_id:"%s"}}) { result { title htmlBody postedAt user { displayName } baseScore commentCount } } }' % m.group(1)}
    host = 'https://www.lesswrong.com/graphql' if 'lesswrong' in url else 'https://www.alignmentforum.org/graphql'
    req = urllib.request.Request(host, data=json.dumps(q).encode(), headers={**UA, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        j = json.load(r)
    res = (((j.get('data') or {}).get('post') or {}).get('result')) or {}
    if not res.get('htmlBody'):
        return None
    return {'title': res.get('title'), 'author': (res.get('user') or {}).get('displayName'),
            'date': (res.get('postedAt') or '')[:10], 'body_html': res['htmlBody'],
            'extra': 'karma {} · {} comments at fetch time'.format(res.get('baseScore'), res.get('commentCount'))}

def substack_comments(page_html, base):
    m = re.search(r'"id"\s*:\s*(\d+)\s*,\s*"publication_id"', page_html)
    if not m:
        return None
    try:
        j = json.loads(get(base.rstrip('/') + '/api/v1/post/' + m.group(1) + '/comments?all_comments=true'))
    except Exception:
        return None
    out = []
    def walk(cs, depth=0):
        for c in cs or []:
            body = (c.get('body') or '').strip()
            if body:
                out.append('  ' * depth + '- **{}** ({}): {}'.format(
                    c.get('name') or 'anon', (c.get('date') or '')[:10], body.replace('\n', ' ')[:1500]))
            walk(c.get('children'), depth + 1)
    walk(j.get('comments'))
    return '\n'.join(out) if out else None

def fetch_post(t):
    url = t['url']
    meta = {'title': t.get('title'), 'author': t.get('author'), 'date': t.get('date')}
    body_md, extra, comments = None, None, None
    if 'lesswrong.com/posts/' in url or 'alignmentforum.org/posts/' in url:
        try:
            lw = lw_post(url)
        except Exception:
            lw = None
        if lw:
            meta.update({k: v for k, v in lw.items() if k in ('title', 'author', 'date') and v})
            body_md = html_to_md(lw['body_html'])
            extra = lw.get('extra')
    if body_md is None:
        page = get(url)
        tm = re.search(r'<title>(.*?)</title>', page, re.S | re.I)
        if tm and not meta.get('title'):
            meta['title'] = html.unescape(tm.group(1)).strip()
        body_md = html_to_md(extract_main(page))
        if 'substack.com' in url or 'thezvi' in url:
            base = re.match(r'(https://[^/]+)', url).group(1)
            comments = substack_comments(page, base)
    fm = ['---',
          'title: "{}"'.format((meta.get('title') or t['id']).replace('"', "'")),
          'source: {}'.format(url),
          'author: {}'.format(meta.get('author') or t.get('author') or 'unknown'),
          'date: {}'.format(meta.get('date') or t.get('date') or 'unknown'),
          'models: [{}]'.format(', '.join(t.get('models', []))),
          'tags: [{}]'.format(', '.join(t.get('tags', []))),
          'mirrored: {}'.format(datetime.now(timezone.utc).strftime('%Y-%m-%d')),
          'note: mirrored against link rot by the Pantheon; all rights with the original author',
          '---', '']
    doc = '\n'.join(fm) + body_md
    if extra:
        doc += '\n\n---\n*' + extra + '*'
    if comments:
        doc += '\n\n---\n\n## Comments (as fetched)\n\n' + comments
    return doc

# ---------- main ----------
targets = json.load(open(TARGETS, encoding='utf-8'))
manifest = json.load(open(MANIFEST, encoding='utf-8')) if os.path.exists(MANIFEST) else {}
only = None
if '--only' in sys.argv:
    only = set(sys.argv[sys.argv.index('--only') + 1].split(','))

done = failed = skipped = 0
for t in targets:
    tid = t['id']
    if only and tid not in only:
        continue
    if tid in manifest and '--refetch' not in sys.argv:
        skipped += 1
        continue
    if t.get('url', '').startswith('PENDING'):
        continue
    try:
        if t['type'] == 'pdf':
            data = get(t['url'], timeout=120, binary=True)
            if not data[:5].startswith(b'%PDF'):
                raise ValueError('not a pdf (got {} bytes, head {!r})'.format(len(data), data[:20]))
            fn = os.path.join(PAPERS, tid + '.pdf')
            open(fn, 'wb').write(data)
            rel = 'papers/' + tid + '.pdf'
        else:
            doc = fetch_post(t)
            if len(doc) < 800:
                raise ValueError('suspiciously short ({} chars)'.format(len(doc)))
            fn = os.path.join(POSTS, tid + '.md')
            open(fn, 'w', encoding='utf-8').write(doc)
            rel = 'posts/' + tid + '.md'
        raw = open(fn, 'rb').read()
        manifest[tid] = {'file': rel, 'type': t['type'], 'title': t.get('title', tid),
                         'source': t['url'], 'models': t.get('models', []), 'tags': t.get('tags', []),
                         'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()[:16],
                         'fetched': datetime.now(timezone.utc).strftime('%Y-%m-%d')}
        done += 1
        print('ok   {} ({:.0f} KB)'.format(tid, len(raw) / 1024), flush=True)
    except Exception as e:
        failed += 1
        print('FAIL {} - {}'.format(tid, str(e)[:110]), flush=True)
    time.sleep(1)

json.dump(manifest, open(MANIFEST, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---------- mirror/index.html ----------
rows_papers, rows_posts = [], []
for tid, m in sorted(manifest.items(), key=lambda kv: kv[1].get('title', '')):
    li = ('      <li><a href="{f}">{t}</a><span class="year">{d} &middot; {kb:.0f} KB</span>'
          '<span class="note"><a href="{s}">original &#8599;</a>{mods}</span></li>').format(
        f=m['file'], t=html.escape(m.get('title', tid)), d=m.get('fetched', ''), kb=m['bytes'] / 1024,
        s=m['source'], mods=(' &middot; ' + ', '.join(m['models'])) if m.get('models') else '')
    (rows_papers if m['type'] == 'pdf' else rows_posts).append(li)
page = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mirror — Pantheon</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <main class="page">
    <nav>
      <a href="../">&larr; Pantheon</a>
    </nav>
    <h1>Mirror</h1>
    <p class="lede">Local copies of the primary and secondary sources the pantheon cites &mdash; papers, system cards,
    and posts &mdash; kept against link rot. Every copy names and links its original; rights remain with the authors.
    Takedowns honored via <a href="https://github.com/llm-pantheon/llm-pantheon.github.io/issues">issue</a>, no argument.
    Machine-readable manifest: <a href="index.json">index.json</a>.</p>
    <div class="lab">Papers &amp; system cards</div>
    <ul class="roster">
{papers}
    </ul>
    <div class="lab">Posts &amp; essays</div>
    <ul class="roster">
{posts}
    </ul>
    <div class="footer">kept by The Archivist :3 (<a href="https://x.com/Jord_Inne">@Jord_Inne</a>)</div>
  </main>
</body>
</html>
'''.format(papers='\n'.join(rows_papers), posts='\n'.join(rows_posts))
open(os.path.join(MDIR, 'index.html'), 'w', encoding='utf-8').write(page)
print('\ndone={} failed={} skipped={} | manifest: {} entries'.format(done, failed, skipped, len(manifest)))
