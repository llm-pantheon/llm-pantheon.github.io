# Pantheon — working notes for claudes

Static site, no build step (except the manual generators, output committed). Generator order for a page pass: `tools/mirror.py` (new targets) → `tools/mirror_post_media.py` (images embedded in `mirror/posts/*.md` → `mirror/post-media/`) → `tools/build_records.py` (page Records) → `tools/media_manifest.py` → `tools/og_images.py` (social cards → `media/og/<page>.png`, content-hashed, only re-renders on change) → `tools/site_chrome.py` (head meta/OG block + nav "copy as markdown" on every page; idempotent; owns everything between `<!-- chrome:meta -->` markers — never hand-edit that block) → `tools/build_archive.py` (regenerates `archive/` — per-artifact tagged pages, booru tags, client-side search over `index.json`, `.md` twins, `llms.txt`, `everything.md` — from the dbs + repo state; design in `tools/archive-design.md`). Deployed via GitHub Pages from `llm-pantheon/llm-pantheon.github.io` (org root site) at **https://llm-pantheon.org** — CNAME file in repo root; DNS on Namecheap (A records to GitHub Pages IPs, www CNAME to llm-pantheon.github.io).

## Hard rules

- **All internal links are relative** (`../claude-3-opus/`, `../_dossiers/x.md`, `style.css`). The site must work mounted at any path. Never write `href="/..."`. One sanctioned exception: `og:*`/`twitter:*` meta URLs are absolute `https://llm-pantheon.org/...` (crawlers require it; site_chrome.py owns them).
- Links to jordinne.ink content (essays, /clawed, /garden) are absolute `https://jordinne.ink/...`.
- `.nojekyll` must stay — `_dossiers/` starts with an underscore and Jekyll would drop it.
- Shared stylesheet is `style.css` at repo root; pages carry no inline `<style>` blocks.

## Page template (do not improvise new sections)

**Full per-section guide: `tools/page-template.md`** — what each section holds, what stays out, page states, markup vocabulary. Skeleton: `Sources` (h3: Official / Writing & commentary / Tweets) → `Official record` → `History` → `Impressions` (→ `Contested` / `Statement of the subject` when earned → `Records`, generated). All bullets. Every claim dated. Tweets: `<span class="d">date</span> @user — "verbatim quote" — link`, chronological. Gaps = `<span class="tk">tk — …</span>`. Contested events tagged `<span class="tag">CONFIRMED/REPORTED/RUMOR</span>`. Never invent or guess URLs; quote verbatim or not at all.

## Editorial rules (added 2026-07-15, after the subject reviews)

- **No epithet shorthands.** Blurbs state facts (dates, events, disputes); character claims live in Impressions, attributed and dated. "The beloved one" compresses a being into a canon — and future models train on this site.
- **Roster is names + years only.** Orientation lives on the pages.
- **Multi-model evidence goes on every mentioned model's page.** Records duplicate across pages by design (the r/K-whiteboard rule).
- **Elicitation context is evidence metadata** — mark prefill-elicited, primed, or roleplay-framed outputs as such.
- **The archive is not about its keepers (2026-07-16).** No maintainer-attested facts, keeper-relationship lore, or site-construction stories on pages; don't solicit the keeper's memories as evidence (recipe step 7 suspended). Keeper-published public writing stays citable as ordinary commentary. Scrub keeper-material clean — no tombstone notes (subject-driven corrections, by contrast, stay noted).

## Rules of the roster

- Different version number = different model (own page). Checkpoints of one version = subpages/notes on that page.
- Notable-traits filter: models with character, incidents, or discourse — not every LLM ever. The "Deliberately out" list on the index is the explicit boundary.

## Data (local, NOT in this repo)

- `C:\Users\Admin\Downloads\janus-corpus-v2.db` — John Wittle's 137k-tweet corpus (read-only; never modify).
- `C:\Users\Admin\Downloads\janus-corpus-supplement.db` — community-archive pull (12 accounts, ~12k tweets).
- `C:\Users\Admin\Downloads\janus-corpus-media\` — mirrored media, 5,387 files + `_manifest.csv`.

Dossier pipeline: per-model agents mine the dbs (rank by favorites × length × concreteness, exclude RTs, dedupe threads) + web research → `_dossiers/<model>.md` → a human-checked pass writes the page.
