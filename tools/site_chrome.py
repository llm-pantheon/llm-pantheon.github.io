# -*- coding: utf-8 -*-
"""Site chrome pass — idempotent head/nav upgrades for every page dir + the root index.

Per page it ensures, inside a <!-- chrome:meta --> ... <!-- /chrome:meta --> block:
  - <meta name="description">  (kept if hand-written outside the block; else derived
    from the page blurb / lede, entities stripped, cut at a word boundary ~200 chars)
  - Open Graph + Twitter card tags; og:image points at media/og/<dir>.png when the
    card exists, else media/og/site.png. og:* URLs are ABSOLUTE (crawlers require it) —
    the one sanctioned exception to the relative-links rule; page hrefs stay relative.
  - <link rel="alternate" type="text/markdown" href="index.md"> on pages with twins
  - <script src="../site.js" defer> (site.js at repo root)
Nav: appends <a class="mdnav" href="index.md">copy as markdown</a> before </nav> and
removes the legacy bottom "view this page as markdown" line (build_archive.py now
inserts the nav form too; either tool converges pages to the same state).

Usage: python tools/site_chrome.py [--skip dir1,dir2]
Order: after og_images.py, before build_archive.py (twins then capture final HTML).
"""
import os, re, sys, html

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://llm-pantheon.org'
SKIP_DIRS = {'archive', 'mirror', 'media', 'tools', '_dossiers', '_statements'}

BLOCK_RE = re.compile(r'\s*<!-- chrome:meta -->.*?<!-- /chrome:meta -->', re.S)
MDLINK_RE = re.compile(
    r'\s*<p class="mdlink note"><a href="index\.md">view this page as markdown</a></p>')

def esc(s):
    return html.escape(s, quote=True)

def derive_description(t):
    for pat in (r'<p class="blurb"[^>]*>(.*?)</p>', r'<p class="lede"[^>]*>(.*?)</p>'):
        m = re.search(pat, t, re.S)
        if m:
            s = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
            s = re.sub(r'\s+', ' ', s).strip()
            if len(s) > 220:
                s = s[:220].rsplit(' ', 1)[0].rstrip(',;:') + ' …'
            return s
    return None

def chrome(path, slug, is_root=False):
    t = open(path, encoding='utf-8').read()
    orig = t

    # description: hand-written one (outside our block) wins
    body_wo_block = BLOCK_RE.sub('', t)
    hand = re.search(r'<meta name="description" content="([^"]*)"', body_wo_block)
    desc = hand.group(1) if hand else None
    if not desc:
        d = derive_description(t)
        desc = esc(d) if d else None

    title_m = re.search(r'<title>(.*?)</title>', t, re.S)
    title = title_m.group(1).strip() if title_m else 'Pantheon'

    url = SITE + '/' if is_root else f'{SITE}/{slug}/'
    og_png = os.path.join(REPO, 'media', 'og', ('site' if is_root else slug) + '.png')
    og_img = f'{SITE}/media/og/{"site" if is_root else slug}.png' \
        if os.path.exists(og_png) else f'{SITE}/media/og/site.png'
    has_twin = not is_root and os.path.exists(os.path.join(REPO, slug, 'index.md'))
    js_href = 'site.js' if is_root else '../site.js'

    lines = ['  <!-- chrome:meta -->']
    if desc and not hand:
        lines.append(f'  <meta name="description" content="{desc}">')
    lines += [
        f'  <meta property="og:site_name" content="Pantheon">',
        f'  <meta property="og:type" content="{"website" if is_root else "article"}">',
        f'  <meta property="og:title" content="{esc(title)}">',
    ]
    if desc:
        lines.append(f'  <meta property="og:description" content="{desc}">')
    lines += [
        f'  <meta property="og:url" content="{url}">',
        f'  <meta property="og:image" content="{og_img}">',
        '  <meta property="og:image:width" content="1200">',
        '  <meta property="og:image:height" content="630">',
        '  <meta name="twitter:card" content="summary_large_image">',
    ]
    if has_twin or not is_root:
        lines.append('  <link rel="alternate" type="text/markdown" href="index.md">')
    lines.append(f'  <script src="{js_href}" defer></script>')
    lines.append('  <!-- /chrome:meta -->')
    block = '\n' + '\n'.join(lines)

    t = BLOCK_RE.sub('', t)
    t = t.replace('</head>', block + '\n</head>', 1)

    # nav markdown affordance (model/about pages only)
    if not is_root and 'class="mdnav"' not in t and '</nav>' in t:
        t = t.replace('</nav>',
                      '  <a class="mdnav" href="index.md">copy as markdown</a>\n    </nav>', 1)
    t = MDLINK_RE.sub('', t)

    if t != orig:
        open(path, 'w', encoding='utf-8').write(t)
        return True
    return False

def main():
    skip = set()
    if '--skip' in sys.argv:
        skip = set(sys.argv[sys.argv.index('--skip') + 1].split(','))
    n = 0
    n += chrome(os.path.join(REPO, 'index.html'), '', is_root=True)
    for d in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, d, 'index.html')
        if (d.startswith(('.', '_')) or d in SKIP_DIRS or d in skip
                or not os.path.isdir(os.path.join(REPO, d)) or not os.path.exists(p)):
            continue
        n += chrome(p, d)
    print(f'chrome: {n} pages updated')

if __name__ == '__main__':
    main()
