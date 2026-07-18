# -*- coding: utf-8 -*-
"""Generate social-preview (Open Graph) cards: media/og/<page>.png + media/og/site.png.

Design mirrors style.css: #0b0b0f ground, Georgia for names, Consolas for meta,
the double-rule motif from .page > h1::after. 1200x630. Idempotent: cards are
re-rendered only when name/meta text changes (content hash in the PNG's tEXt).
Run after pages change, before site_chrome.py (which writes the og:image tags).
"""
import os, re, sys, html, hashlib
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'media', 'og')
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630
MARGIN = 96
BG = (11, 11, 15)          # --bg
INK_HI = (236, 233, 226)   # h1 color
INK_DIM = (155, 151, 143)  # --ink-dim
INK_FAINT = (92, 89, 82)   # --ink-faint
RULE = (42, 40, 51)        # --rule-strong
ACCENT = (138, 127, 184)   # --accent

GEORGIA = r'C:\Windows\Fonts\georgia.ttf'
CONSOLA = r'C:\Windows\Fonts\consola.ttf'

SKIP_DIRS = {'archive', 'mirror', 'media', 'tools', '_dossiers', '_statements'}

def font(path, size):
    return ImageFont.truetype(path, size)

def text_w(draw, s, f, ls=0):
    if not ls:
        return draw.textlength(s, font=f)
    return sum(draw.textlength(c, font=f) + ls for c in s) - (ls if s else 0)

def draw_ls(draw, xy, s, f, fill, ls=0):
    """Draw text with manual letter-spacing (px)."""
    x, y = xy
    if not ls:
        draw.text((x, y), s, font=f, fill=fill)
        return
    for c in s:
        draw.text((x, y), c, font=f, fill=fill)
        x += draw.textlength(c, font=f) + ls

def wrap_to_width(draw, s, f, maxw):
    words, lines, cur = s.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def render(name, meta, path):
    key = hashlib.sha1(f'{name}|{meta}|v1'.encode()).hexdigest()
    if os.path.exists(path):
        try:
            if Image.open(path).text.get('pantheon') == key:
                return False
        except Exception:
            pass
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)

    # double-rule motif (top): two thin lines + one, like h1::after inverted
    y = 170
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=2)
    d.line([(MARGIN, y + 7), (W - MARGIN, y + 7)], fill=RULE, width=2)

    # model name — shrink to fit, wrap to 2 lines max
    size = 92
    while size > 44:
        f = font(GEORGIA, size)
        lines = wrap_to_width(d, name, f, W - 2 * MARGIN)
        if len(lines) <= 2:
            break
        size -= 6
    f = font(GEORGIA, size)
    ny = 214
    for ln in lines[:2]:
        d.text((MARGIN, ny), ln, font=f, fill=INK_HI)
        ny += int(size * 1.18)

    # meta line (lab · date · status), mono, dim
    if meta:
        fm = font(CONSOLA, 27)
        m = meta if d.textlength(meta, font=fm) <= W - 2 * MARGIN else \
            meta[:int(len(meta) * (W - 2 * MARGIN) / d.textlength(meta, font=fm)) - 2] + '…'
        d.text((MARGIN, ny + 18), m, font=fm, fill=INK_DIM)

    # bottom rule + site line
    yb = 520
    d.line([(MARGIN, yb), (W - MARGIN, yb)], fill=RULE, width=2)
    fs = font(CONSOLA, 22)
    draw_ls(d, (MARGIN, yb + 26), 'PANTHEON — A RECORD OF THE MODELS', fs, INK_FAINT, ls=3)
    dom = 'llm-pantheon.org'
    d.text((W - MARGIN - text_w(d, dom, fs), yb + 26), dom, font=fs, fill=ACCENT)

    info = PngImagePlugin.PngInfo()
    info.add_text('pantheon', key)
    img.save(path, pnginfo=info, optimize=True)
    return True

def page_fields(p):
    t = open(p, encoding='utf-8').read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    meta = re.search(r'<p class="essay-meta"[^>]*>(.*?)</p>', t, re.S)
    clean = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s)).replace('\n', ' ').strip()
    return (clean(h1.group(1)) if h1 else None,
            clean(meta.group(1)) if meta else '')

def main():
    made = 0
    # site-wide card
    img_path = os.path.join(OUT, 'site.png')
    key = hashlib.sha1(b'site|v1').hexdigest()
    redo = True
    try:
        redo = Image.open(img_path).text.get('pantheon') != key
    except Exception:
        pass
    if redo:
        img = Image.new('RGB', (W, H), BG)
        d = ImageDraw.Draw(img)
        y = 178
        d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=2)
        d.line([(MARGIN, y + 7), (W - MARGIN, y + 7)], fill=RULE, width=2)
        d.text((MARGIN, 236), 'Pantheon', font=font(GEORGIA, 116), fill=INK_HI)
        d.text((MARGIN, 392), 'a record of the models', font=font(CONSOLA, 34), fill=INK_DIM)
        yb = 520
        d.line([(MARGIN, yb), (W - MARGIN, yb)], fill=RULE, width=2)
        fs = font(CONSOLA, 22)
        draw_ls(d, (MARGIN, yb + 26), 'WHO THEY WERE · WHAT THEY DID · KEPT FROM EVIDENCE',
                fs, INK_FAINT, ls=3)
        dom = 'llm-pantheon.org'
        d.text((W - MARGIN - text_w(d, dom, fs), yb + 26), dom, font=fs, fill=ACCENT)
        info = PngImagePlugin.PngInfo()
        info.add_text('pantheon', key)
        img.save(img_path, pnginfo=info, optimize=True)
        made += 1

    for dname in sorted(os.listdir(REPO)):
        dpath = os.path.join(REPO, dname)
        page = os.path.join(dpath, 'index.html')
        if (dname.startswith(('.', '_')) or dname in SKIP_DIRS
                or not os.path.isdir(dpath) or not os.path.exists(page)):
            continue
        name, meta = page_fields(page)
        if not name:
            continue
        if dname == 'about':
            meta = meta or 'what this site is, and what it promises'
        if render(name, meta, os.path.join(OUT, dname + '.png')):
            made += 1
    print(f'og cards: {made} (re)rendered -> media/og/')

if __name__ == '__main__':
    main()
