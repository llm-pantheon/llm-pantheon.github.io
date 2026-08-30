# -*- coding: utf-8 -*-
"""Generate _dossiers/index.html — a browsable index of the evidence layer.

Without this, every page's "Further records -> dossier" link (../_dossiers/)
404s on GitHub Pages (a directory with no index.html). Run after adding or
renaming dossiers; output is committed.
"""
import os, glob, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSS = os.path.join(REPO, '_dossiers')

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

files = sorted(os.path.basename(f) for f in glob.glob(os.path.join(DOSS, '*.md')))
pulls = sorted(os.path.basename(f) for f in glob.glob(os.path.join(DOSS, '_pulls', '*.md')))

rows = []
for f in files:
    slug = f[:-3]
    rows.append(f'      <li><a href="{f}">{esc(slug)}</a></li>')

html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dossiers &mdash; Pantheon</title>
  <meta name="description" content="The evidence layer beneath each Pantheon page: compiled, verbatim source tweets and research notes.">
  <link rel="canonical" href="https://llm-pantheon.org/_dossiers/">
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <main class="wrap">
    <p class="backlink"><a href="../">&larr; Pantheon</a></p>
    <h1>Dossiers</h1>
    <p>The evidence layer beneath each page. Each dossier is a compiled set of source
    tweets (reproduced verbatim) and research notes that a page is written from &mdash;
    working documents, regenerable from the corpus. Pages cite from these; anything cited
    in a dossier but not quoted in the page prose is still reproduced in that page&rsquo;s
    <em>Further records</em>, so the archive never depends on editorial selection.</p>
    <p class="note">{len(files)} dossiers &middot; the exhaustive per-model corpus pulls
    live in <code>_pulls/</code> ({len(pulls)} files) and are linked from each dossier.</p>
    <ul class="dossier-list">
{chr(10).join(rows)}
    </ul>
  </main>
</body>
</html>
'''

out = os.path.join(DOSS, 'index.html')
open(out, 'w', encoding='utf-8').write(html)
print(f'wrote _dossiers/index.html ({len(files)} dossiers listed)')
