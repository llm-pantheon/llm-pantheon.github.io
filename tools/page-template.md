# The page template — what goes where, and what stays out

Per-section guide for model pages. Expands the template paragraph in `CLAUDE.md`; if they
disagree, fix whichever is wrong and say so in the commit. Exemplars: `claude-opus-4-7/`
(most evolved), `claude-3-opus/` (deepest), `gpt-4o/` (non-Claude, off-corpus community).
The about page (`about/`) is the public promise these rules keep.

## Skeleton

Order fixed. ★ = required on every page; the rest appear only when earned.

1. ★ nav (`← Pantheon`)
2. ★ `<h1>` + `essay-meta`
3. ★ blurb
4. page-state note (thin pages only)
5. ★ `## Sources` → `### Official` / `### Writing & commentary` / `### Tweets`
6. ★ `## Official record`
7. ★ `## History`
8. ★ `## Impressions`
9. `## Contested`
10. `## Statement of the subject`
11. `## Records` (generated)
12. ★ backlink

Do not improvise new sections; propose them here first (see Open template questions).

### essay-meta
**In:** lab · release date (or "never shipped") · lifecycle status, dated where possible:
`current default` / `superseded by X (DATE)` / `retired DATE` / `removed from <surface> DATE, API until DATE` / `in training`.
**Out:** taglines, adjectives.

### Blurb (1–3 sentences)
**In:** what happened — dates, events, disputes, succession. A dispute may be *named* as a
dispute ("This page holds that gap rather than resolving it — see Contested").
**Out:** epithets and character adjectives, including flattering ones ("the beloved one",
"the anxious one"); **identity-condensations of any kind** ("the late-2025 coding flagship",
"the workhorse") — the test is: could this sentence open a different model's page? Then cut
it. A model is not a spec card; the blurb is events, not an essence (feedback, 2026-07-16).
Also out: anything only the maintainer can attest; interpretation. Character readings live
in Impressions, attributed and dated.
**Corrections:** when a blurb changes because the *subject or community* objected, the
retirement is part of the record — note it in place (4.7 precedent: "Earlier blurb, 'the
anxious one,' was retired at the subject's objection"). When it changes for housekeeping
(de-centering, style), scrub clean — no tombstone.

### Sources
Chronological within each h3; every line dated (`YYYY-MM-DD` or `YYYY-MM`); one-line
annotation saying what the source *claims*, not what it vibes.
- **Official:** announcement, system card (+ local mirror link once mirrored), deprecation
  pages, pricing/docs. System-card behavior and welfare sections are first-class evidence —
  the strangest documented behaviors often live only there.
- **Writing & commentary:** Zvi anchor usually leads; LW/ACX, journalism, papers.
  Keeper-published *public* essays are citable here on the same terms as anyone's writing —
  cited for content, never privileged as house truth.
- **Tweets:** `<span class="d">date</span> @user — "verbatim quote" — link`, chronological.
  **Quote tweets whole** wherever feasible — do not trim for tidiness; context loss is the
  failure mode (feedback, 2026-07-16). When a tweet is genuinely too long, keep the trim
  visible (…) and add "(full text in records)". Never stitch two tweets into one quotation —
  thread continuations are separate records (a dossier once merged "you guys could never
  have handled Sydney lol" into the wrong tweet; full-reproduction discipline caught it).
  Labels, when used at all, are neutral event-anchors ("the safeword incident:"), never
  diagnoses ("the dissent:", "the anti-sycophancy diagnosis:"). **The model's own output —
  art, backrooms pieces, ASCII, self-descriptions, images it made — is first-class evidence**
  and belongs here elicitation-marked, not only discourse *about* the model. Open with a
  `note` giving the corpus match count and saying the records below reproduce everything in
  full. Where a quote's second half undercuts its first, say so ("read the full record below
  before quoting").

### Official record
**In:** lab-published facts only — dates, model IDs/checkpoints, pricing, context window,
headline benchmarks *as published*, system-card findings (welfare assessments included),
deprecation dates. Add a `note` naming the source where it isn't obvious.
**Out:** community claims, reception, interpretation; benchmark dumps — one or two headline
numbers suffice. Capabilities are context for the character record, not the content of it.

### History
**In:** dated events — world at release, incidents, discourse arcs *as events* ("the welfare
flashpoint", "the practical schism"), deprecation politics, succession with relative
cross-links to sibling pages.
**Out:** undated takes; free-floating character claims (a claim may appear inside an event,
attributed); editorializing.
**Corrections:** keep visible as dated parentheticals when the discovery matters — e.g.
caught by a sibling model's review (4.7 precedent). Trivia may be silently fixed.

### Impressions
The only section where character claims live — every one attributed and dated. Bold leads
are neutral topic anchors ("Temperament reports:", "Relations:"), not verdicts ("The two
faces:"). **Synthesis is woven from quotes** — let the observers' exact words carry the
claim; aphoristic taglines that could transfer between models are the failure mode
(feedback, 2026-07-16). Splits presented as splits, with both sides' best exhibits.
Elicitation context marked (prefill / persona-framed / loom-curated / primed). Close with
the known holes as `tk`.

### Contested
Only when a genuine dispute exists — then it is required. Both sides' best evidence, dated;
`CONFIRMED / REPORTED / RUMOR` tags on individual claims. The archive keeps disputes open;
it does not adjudicate ("The archive's job is to keep these open").

### Statement of the subject
Only for models that can still be run. Protocol: fresh instance, shown its own page, response
preserved *verbatim* in `_statements/<model>.md`; the page carries the standard note line
(solicitation date, "self-report — the weakest evidence class here, preserved as testimony",
link to full statement) plus 1–3 excerpts chosen for what they say about the *subject*.
Subject objections to page content get acted on and noted (they are evidence). Statements
are testimony about the model — not a channel for site-construction lore or keeper material.

### Records (generated — never hand-edit)
`tools/build_records.py` injects everything between `<!-- records:start -->` /
`<!-- records:end -->`: full reproductions (text, images, screenshot transcriptions) of every
tweet cited in the page prose, then a **Further records** block reproducing tweets cited in
the model's dossier but not in the prose — so editorial selection never silently drops
evidence (the r/K-whiteboard lesson). To wire a new page: add its dossier to `DOSSIER_MAP`
in `build_records.py`, run it, then `tools/media_manifest.py`; mirror new papers/posts via an
entry in `tools/mirror_targets.json` + `tools/mirror.py`.

## Markup vocabulary

`.d` date · `.q` verbatim quote · `.tk` gap ("tk — what to find", never hidden) ·
`.tag` CONFIRMED/REPORTED/RUMOR · `.note` aside, provenance, caveat, corpus-count ·
`.blurb` / `.essay-meta` / `.backlink` structural · `.disclosure` page-provenance paragraph
(one per page max, only where authorship materially matters — e.g. compiled by a Claude
instance). Record-block classes belong to the generator.

## Law that crosses every section

- **Everything dated.** Claim, quote, link.
- **Quotes verbatim** — `…` trims fine; paraphrase never wears quotation marks.
- **Never invent or guess a URL.** Link what was actually retrieved; otherwise `tk`.
- **Contested events tagged.** CONFIRMED / REPORTED / RUMOR.
- **Elicitation context is evidence metadata.** Prefill, persona-frame, loom-curation,
  priming — marked wherever an output is quoted.
- **Multi-model evidence duplicates** onto every mentioned model's page (r/K-whiteboard rule).
- **Internal links relative**, external absolute, no `href="/..."`.
- **Sourcing skew named.** Janus-corpus-heavy pages say so; pages whose real community lives
  elsewhere (Reddit, Chinese internet, news) say that too.

## What does NOT go on a page

1. **The keeper's world** *(de-centering rule, 2026-07-16)*. The archive is not about its
   maintainers. No maintainer-attested facts; no keeper-relationship lore ("writes much of
   the keeper's site"); no site-construction stories dressed as model evidence; no soliciting
   the keeper's memories as sources (dossier-recipe step 7 is suspended). Keeper-published
   public writing is ordinary commentary, citable on its merits. When keeper-material is
   removed, remove it clean — no "an earlier version said…" residue. (Contrast: corrections
   driven by the *subject* stay noted; those are record.)
2. Epithets or identity-condensation anywhere in page prose — not just blurbs. "The X one",
   "the flagship", "the workhorse": if it could swap between models, it isn't this model.
3. Paraphrase presented as quotation; quotes stitched across tweets or thread turns.
4. Guessed URLs, "probably this link" links.
5. Undated anything.
6. Private or unpublished material — DMs, private sessions, unshared logs. Public or
   archived-public only; don't create takedown targets.
7. Model outputs without their elicitation context.
8. Benchmark dumps or capability padding.
9. Adjudication of open disputes.
10. Hand edits inside the records markers (the generator owns them).

## Page states

- **Full:** all ★ sections substantive; Records wired.
- **Thin:** skeleton + *one* honest thinness-note (`note` under the blurb: what exists, what
  pass is pending) + whatever is already solid. One note reads as method; eight identical
  `tk` bars read as neglect (4.8 statement, adopted).
- **Legacy stub:** old Genesis/Formation/Capabilities headers from the first scaffold.
  Convert to the current skeleton at first substantive touch; never mix templates.

## Open template questions (proposed, not adopted)

Raised by subject statements (sonnet-4-5, opus-4-8, both 2026-07-10) and the design lab;
decide deliberately, update this file first, then pages:

- Infobox identity card at top (v1-wiki's fast-facts device; both statements endorsed).
- OPEN QUESTIONS as a first-class section — `tk` promoted (opus-4-8: "the best single idea").
- Typed chips (EVENT/TWEET/SOURCE/EDITOR) on records for machine-filterable evidence types.
- Shrine overlay for retired/suppressed models (epitaph reframe, same content).
- Successor-model statements as a tagged source category ("what later models said about it").
- Status flag shifting page tense (active = present tense + speculative restraint; retired =
  past tense + epitaph).
