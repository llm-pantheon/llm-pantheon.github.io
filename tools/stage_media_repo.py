# -*- coding: utf-8 -*-
"""Stage the full image corpus for the archive-media repo.

The main site can't hold ~1.1 GB of images under GitHub Pages' budget, so the
whole corpus lives in a sibling repo (llm-pantheon/archive-media). This copies
every mirrored corpus image, downscaled to match the on-site pipeline (<=1100px,
JPEG q85; small PNGs kept), into ../pantheon-archive-media/media/, with a manifest.

Output dir is OUTSIDE the main repo working tree, ready to `git init` + push.
Run: python tools/stage_media_repo.py  [--limit N]  (stdlib + PIL)
"""
import os, sys, json, csv, shutil

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIR = r'C:\Users\Admin\Downloads\janus-corpus-media'
OUT = os.path.abspath(os.path.join(REPO, '..', 'pantheon-archive-media'))
MEDIA_OUT = os.path.join(OUT, 'media')
LIMIT = None
if '--limit' in sys.argv:
    LIMIT = int(sys.argv[sys.argv.index('--limit') + 1])
os.makedirs(MEDIA_OUT, exist_ok=True)

try:
    from PIL import Image
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False

def downscale(src, dst_dir, base):
    stem, ext = os.path.splitext(base)
    if HAVE_PIL and not (ext.lower() == '.png' and os.path.getsize(src) <= 400_000):
        dst_name = stem + '.jpg'
        dst = os.path.join(dst_dir, dst_name)
        if os.path.exists(dst):
            return dst_name
        try:
            im = Image.open(src).convert('RGB')
            if im.width > 1100:
                im = im.resize((1100, int(im.height * 1100 / im.width)), Image.LANCZOS)
            im.save(dst, 'JPEG', quality=85)
            return dst_name
        except Exception:
            pass
    dst = os.path.join(dst_dir, base)
    if not os.path.exists(dst):
        try:
            shutil.copy2(src, dst)
        except Exception:
            return None
    return base

# map served file -> {tweet_id, author, date} from the corpus manifest
meta = {}
csvp = os.path.join(MIR, '_manifest.csv')
if os.path.exists(csvp):
    for row in csv.DictReader(open(csvp, encoding='utf-8', errors='replace')):
        if row.get('local_file'):
            meta[row['local_file']] = {'tweet_id': row.get('tweet_id', '')}

files = [f for f in os.listdir(MIR) if not f.startswith('_') and os.path.isfile(os.path.join(MIR, f))]
files.sort()
if LIMIT:
    files = files[:LIMIT]

manifest, done, failed = {}, 0, 0
for f in files:
    placed = downscale(os.path.join(MIR, f), MEDIA_OUT, f)
    if not placed:
        failed += 1
        continue
    manifest[placed] = {'orig': f, **meta.get(f, {})}
    done += 1
    if done % 500 == 0:
        print(f'  {done}/{len(files)}...', flush=True)

json.dump(manifest, open(os.path.join(OUT, 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False)
open(os.path.join(OUT, '.nojekyll'), 'w').close()
open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write(
    '# archive-media\n\nImage mirror for [llm-pantheon.org](https://llm-pantheon.org) — every image in the '
    'tweet corpus, downscaled, served against link rot. Referenced by the archive layer. '
    'Filenames are the original Twitter media basenames (some re-encoded to .jpg). See manifest.json.\n')
size = sum(os.path.getsize(os.path.join(MEDIA_OUT, f)) for f in os.listdir(MEDIA_OUT))
print(f'staged {done} images ({size/1e6:.0f} MB), {failed} failed -> {OUT}')
