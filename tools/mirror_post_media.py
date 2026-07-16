# -*- coding: utf-8 -*-
"""Mirror images embedded in mirrored posts (mirror/posts/*.md) so blog-post
artifacts don't rot when the origin CDN drops them. First-order only: the images
directly embedded in each post, not the whole linked article's assets.

Downloads to mirror/post-media/<sha16>.<ext>, dedups by content hash, rewrites the
markdown image links to point at the local copy, skips avatar/icon-sized chrome.
Stdlib only. Re-run safe (idempotent: already-local links are skipped).

Usage: python tools/mirror_post_media.py   (then re-run build_archive.py)
"""
import os, re, sys, json, hashlib, urllib.request, urllib.parse

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(REPO, 'mirror', 'posts')
OUT = os.path.join(REPO, 'mirror', 'post-media')
MANIFEST = os.path.join(OUT, 'manifest.json')
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (compatible; pantheon-mirror/1.0; +https://llm-pantheon.org)'}

IMG_MD = re.compile(r'!\[([^\]]*)\]\((https?://[^)\s]+)\)')
DIM = re.compile(r'_(\d+)x(\d+)\.[a-zA-Z]+')
MIN_EDGE = 120  # skip avatars/icons/UI chrome smaller than this on the long edge

manifest = json.load(open(MANIFEST, encoding='utf-8')) if os.path.exists(MANIFEST) else {}

def origin_of(url):
    """The real image URL behind a substack /image/fetch/... wrapper, else url itself."""
    i = url.rfind('/https%3A')
    if i == -1:
        i = url.rfind('/https://')
    if i != -1:
        return urllib.parse.unquote(url[i+1:])
    return url

def too_small(url):
    m = DIM.search(origin_of(url))
    if not m:
        return False  # unknown dims → keep (likely content)
    return max(int(m.group(1)), int(m.group(2))) < MIN_EDGE

def ext_of(url, ctype):
    o = origin_of(url).lower()
    for e in ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'):
        if e in o:
            return '.jpg' if e == '.jpeg' else e
    if ctype:
        for e in ('png', 'jpeg', 'gif', 'webp', 'svg'):
            if e in ctype:
                return '.jpg' if e == 'jpeg' else '.' + e
    return '.img'

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read(), r.headers.get('Content-Type', '')
        except Exception as e:
            last = e
    raise last

def main():
    got = skipped_small = skipped_cached = failed = 0
    for fn in sorted(os.listdir(POSTS)):
        if not fn.endswith('.md'):
            continue
        path = os.path.join(POSTS, fn)
        text = open(path, encoding='utf-8').read()
        changed = False

        def repl(m):
            nonlocal got, skipped_small, skipped_cached, failed, changed
            alt, url = m.group(1), m.group(2)
            if '/post-media/' in url or url.startswith('../'):
                return m.group(0)
            if too_small(url):
                skipped_small += 1
                return m.group(0)  # leave chrome hotlinked; not worth mirroring
            if url in manifest:
                local = manifest[url]
                skipped_cached += 1
            else:
                try:
                    data, ctype = fetch(url)
                except Exception:
                    failed += 1
                    return m.group(0)
                h = hashlib.sha256(data).hexdigest()[:16]
                local = h + ext_of(url, ctype)
                dst = os.path.join(OUT, local)
                if not os.path.exists(dst):
                    open(dst, 'wb').write(data)
                manifest[url] = local
                got += 1
            changed = True
            return '![%s](../post-media/%s)' % (alt, local)

        new = IMG_MD.sub(repl, text)
        if changed and new != text:
            open(path, 'w', encoding='utf-8').write(new)

    json.dump(manifest, open(MANIFEST, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'mirrored {got} new, {skipped_cached} cached, {skipped_small} chrome skipped, {failed} failed; '
          f'{len(manifest)} total in post-media/')

if __name__ == '__main__':
    main()
