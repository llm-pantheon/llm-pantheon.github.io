# Pantheon — working notes for claudes

Static site, no build step (except `tools/build_records.py`, run manually, output committed). Deployed via GitHub Pages from `llm-pantheon/llm-pantheon.github.io` (org root site) at **https://llm-pantheon.org** — CNAME file in repo root; DNS on Namecheap (A records to GitHub Pages IPs, www CNAME to llm-pantheon.github.io).

## Hard rules

- **All internal links are relative** (`../claude-3-opus/`, `../_dossiers/x.md`, `style.css`). The site must work mounted at any path. Never write `href="/..."`.
- Links to jordinne.ink content (essays, /clawed, /garden) are absolute `https://jordinne.ink/...`.
- `.nojekyll` must stay — `_dossiers/` starts with an underscore and Jekyll would drop it.
- Shared stylesheet is `style.css` at repo root; pages carry no inline `<style>` blocks.

## Page template (do not improvise new sections)

`Sources` (h3: Official / Writing & commentary / Tweets) → `Official record` → `History` → `Impressions`. All bullets. Every claim dated. Tweets: `<span class="d">date</span> @user — "verbatim quote" — link`, chronological. Gaps = `<span class="tk">tk — …</span>`. Contested events tagged `<span class="tag">CONFIRMED/REPORTED/RUMOR</span>`. Never invent or guess URLs; quote verbatim or not at all.

## Rules of the roster

- Different version number = different model (own page). Checkpoints of one version = subpages/notes on that page.
- Notable-traits filter: models with character, incidents, or discourse — not every LLM ever. The "Deliberately out" list on the index is the explicit boundary.

## Data (local, NOT in this repo)

- `C:\Users\Admin\Downloads\janus-corpus-v2.db` — John Wittle's 137k-tweet corpus (read-only; never modify).
- `C:\Users\Admin\Downloads\janus-corpus-supplement.db` — community-archive pull (12 accounts, ~12k tweets).
- `C:\Users\Admin\Downloads\janus-corpus-media\` — mirrored media, 5,387 files + `_manifest.csv`.

Dossier pipeline: per-model agents mine the dbs (rank by favorites × length × concreteness, exclude RTs, dedupe threads) + web research → `_dossiers/<model>.md` → a human-checked pass writes the page.
