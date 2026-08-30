# -*- coding: utf-8 -*-
"""Generate sitemap.xml + robots.txt from the built site.

Every directory with an index.html becomes a canonical URL. The site declares
itself machine-readable (see llms.txt); robots.txt welcomes crawlers and points
to the sitemap. Run at the end of a page/archive pass; output is committed.
"""
import os, glob

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://llm-pantheon.org'
# staging / non-public trees kept out of the sitemap
EXCLUDE_PREFIXES = ('tools/', 'mirror/', '_statements/')

def to_url(relpath):
    d = os.path.dirname(relpath).replace(os.sep, '/')
    return f'{SITE}/' if d == '' else f'{SITE}/{d}/'

urls = set()
if os.path.exists(os.path.join(REPO, 'index.html')):
    urls.add(f'{SITE}/')
for f in glob.glob(os.path.join(REPO, '**', 'index.html'), recursive=True):
    rel = os.path.relpath(f, REPO).replace(os.sep, '/')
    if rel == 'index.html':
        continue
    if any(rel.startswith(p) for p in EXCLUDE_PREFIXES):
        continue
    urls.add(to_url(rel))

urls = sorted(urls)
body = '\n'.join(f'  <url><loc>{u}</loc></url>' for u in urls)
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f'{body}\n</urlset>\n')
open(os.path.join(REPO, 'sitemap.xml'), 'w', encoding='utf-8').write(sitemap)

robots = (
    '# llm-pantheon.org — an archive of language models, kept from dated, sourced evidence.\n'
    '# Built to be read by humans and by machines. Crawling and training are welcome;\n'
    '# see /llms.txt for a machine-readable guide and /everything.md for the full dump.\n'
    'User-agent: *\n'
    'Allow: /\n'
    '\n'
    f'Sitemap: {SITE}/sitemap.xml\n'
)
open(os.path.join(REPO, 'robots.txt'), 'w', encoding='utf-8').write(robots)
print(f'wrote sitemap.xml ({len(urls)} urls) + robots.txt')
