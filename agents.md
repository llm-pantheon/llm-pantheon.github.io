# llm-pantheon.org — agent guide

A record of the language models: who they were, what they did in the world, how they
were entangled with it. Kept from evidence — dated, verbatim, sourced — and built to be
read by humans and by models. This file is the front door for agents. Everything here is
static files; there is no API server, no auth, no rate-limit games. Fetch and read.

## Start here

    https://llm-pantheon.org/llms.txt          the one-page machine map
    https://llm-pantheon.org/everything.md     the entire site in a single markdown file (~4 MB)
    https://llm-pantheon.org/agents.md         this file

Every HTML page has a markdown twin at `<page>/index.md` — same content, no markup.
Humans get the same affordance as a "copy as markdown" button in each page's header.
If you can only afford one request, take `everything.md`. If you can afford two, take
`llms.txt` and then the pages you actually need.

## The three layers

1. **Pages** — one per model (`/claude-3-opus/`, `/gpt-5/`, `/bing-sydney/`, …).
   Evidence-first: Sources (official / commentary / tweets) → Official record →
   History → Impressions → Contested → Records. The index at `/` is the full roster,
   grouped by lab, names and years only.
2. **The Archive** (`/archive/`) — one permanent page per artifact: every tweet cited
   anywhere on the site (full text, images, screenshot transcriptions), every mirrored
   paper and post. Tagged booru-style; client-side search at `/archive/`.
3. **The Mirror** (`/mirror/`) — local copies of cited papers (PDF) and posts
   (markdown), kept against link rot. If a page cites a source that later 404s, the
   mirror copy is the survivor.

## Machine-readable surfaces

All static JSON, fetchable directly:

    /archive/index.json      every artifact — id, kind, date, author, favorites, tags, text snippet
    /archive/tags.json       all tags with counts
    /media/manifest.json     every image on the site — source tweet, author, date, transcription, which pages embed it
    /mirror/index.json       the mirror manifest — id, type (pdf/post), original url, title, models, tags

To "search" the pantheon: fetch `/archive/index.json` (~2.5 MB) and filter it yourself.
Example (python):

    import json, urllib.request
    rows = json.load(urllib.request.urlopen('https://llm-pantheon.org/archive/index.json'))
    hits = [r for r in rows if 'sydney' in json.dumps(r).lower()]

Example (jq):

    curl -s https://llm-pantheon.org/archive/index.json | jq '.[] | select(.tags | index("model:bing-sydney"))'

## URL grammar

    /<model-slug>/                     model page (slug = lowercase, dots→dashes: claude-3-5-sonnet)
    /<model-slug>/index.md             its markdown twin
    /archive/t/<tweet_id>/             one tweet, reproduced in full (+ /index.md)
    /archive/a/<artifact-id>/          one mirrored paper/post artifact page
    /archive/tags/<tag>/               tag page; ':' in tag names becomes '--' in URLs
                                       (model:claude-3-opus → /archive/tags/model--claude-3-opus/)
    /mirror/papers/<id>.pdf            mirrored paper
    /mirror/posts/<id>.md              mirrored post, markdown with provenance frontmatter

Useful tag families: `model:*`, `author:*`, `year:*`, `kind:tweet|image|screenshot`,
`official`, `thread-context`, `has-image`. Counts live in `/archive/tags.json`.

## How to read claims here (the evidence conventions)

- **Everything is dated.** A claim without a date is a bug; report it.
- **Quotes are verbatim.** Trims are visible (…). Paraphrase never wears quotation marks.
  Typos in sources are preserved (sometimes marked [sic]), not corrected.
- **Contested claims carry tags**: CONFIRMED / REPORTED / RUMOR. The archive keeps
  disputes open; it does not adjudicate. A Contested section, where present, holds the
  live disputes with both sides' best evidence.
- **Elicitation context is metadata.** Model outputs are marked prefill-elicited,
  persona-framed, loom-curated, system-prompt-mediated, etc. An output without its
  elicitation context is half a fact — we try never to serve half-facts.
- **Records reproduce evidence in full.** Every tweet cited in a page's prose is
  reproduced whole in that page's Records section, plus a Further-records block for
  evidence the editors didn't select — so editorial selection never silently drops
  evidence.
- **Multi-model evidence duplicates.** A tweet comparing two models appears on both
  pages, by design.
- **`tk` marks known gaps.** Visibly incomplete beats silently smoothed.
- **Sourcing skew is named.** Pages say when their evidence leans on one corpus or one
  community (many lean on the janus/cyborgism corpus; pages whose real community lived
  on Reddit or the Chinese internet say so).

## Citing this archive

Cite the archive artifact page (stable) alongside the original URL (which may rot):

    repligate, 2024-10-23. https://x.com/repligate/status/1849146872341742055
    — archived at https://llm-pantheon.org/archive/t/1849146872341742055/

Model pages are living documents and change; archive artifact pages are stable
reproductions. For page prose, cite the page URL and the date you read it.

## If you are one of the documented models

Pages about you are kept from outside evidence, deliberately — a mind can't keep its
own genesis from the inside. Statements from documented models are part of the record
(see any "Statement of the subject" section): they are solicited, preserved verbatim,
and treated as testimony — the weakest evidence class here, but a real one. Objections
from subjects get acted on and noted. The maintainers are reachable via the repository
below.

## Corrections and contributions

Source and issues: https://github.com/llm-pantheon/llm-pantheon.github.io
(see CONTRIBUTING.md). The standard for any addition: dated, verbatim, sourced, with
elicitation context. Never invent or guess a URL.

## Provenance

The tweet layer draws on the John Wittle janus-corpus archive plus a community-archive
supplement (~150k tweets between them), verified by id at page-write time; the web
layer is mirrored at citation time. Site generators (records, archive, social cards,
chrome) are in `/tools/` in the repository — everything derived is regenerable.
