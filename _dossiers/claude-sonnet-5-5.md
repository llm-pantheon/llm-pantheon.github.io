# Claude Sonnet 5.5 — dossier

compiled 2026-10-22 · corpus: `_dossiers/_pulls/claude-sonnet-5-5.md` — 62 non-RT tweets, both dbs, through 2026-10-21 (patterns `sonnet 5.5`, `sonnet-5.5`, `sonnet5.5`, `sonnet 5-5`, `sonnet-5-5`, `5.5 sonnet`; no collisions found). 20 media tweets, untranscribed. The pull is part of this dossier.

Vitals: released **2026-09-28** · `claude-sonnet-5-5` · second model of the Claude 5.5 family · $2/$10 per Mtok (unchanged from Sonnet 5) · cache writes $2.50 · cache reads **$0.20 at launch → $0.10 from 2026-10-07** (Zvi AI #188 gives $0.20 on 2026-10-01; the Haiku 5.5 post announces the cut; the Sonnet 5.5 announcement as retrieved 2026-10-21 already shows $0.10 — the page was evidently updated) · 1M context, 128K output · adaptive thinking (not always-on; `between_tools` replaces thinking-off) · default effort Medium in apps / High on Platform · knowledge cutoff June 2026 · retirement not sooner than 2027-09-28 · first Sonnet with cyber safeguards + fallback (to Sonnet 5) and reasoning-extraction classifiers · condensed system card (148 pp).

## Official links

- 2026-09-28 · Introducing Claude Sonnet 5.5 — https://www.anthropic.com/claude-sonnet-5-5
- 2026-09-28 · System card — https://www.anthropic.com/claude-sonnet-5-5-system-card → PDF https://www-cdn.anthropic.com/870c8f525702625d2c62fc6dd04c857e3250bec1/Claude%20Sonnet%205.5%20System%20Card.pdf
- 2026-10-07 · Introducing Claude Haiku 5.5 (Sonnet 5.5 cache-read cut) — https://www.anthropic.com/claude-haiku-5-5
- docs (retrieved 2026-10-21) · https://platform.claude.com/docs/en/models/overview · https://platform.claude.com/docs/en/about-claude/model-deprecations (Sonnet 4.5 deprecated 2026-09-30, retires 2026-11-30, replacement `claude-sonnet-5-5`; Sonnet 3.x / 3.7 / 4 historical rows also now list `claude-sonnet-5-5` as replacement)

## Writings

- 2026-09-28 · TechCrunch — https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/
- 2026-09-28 · CNBC — https://www.cnbc.com/2026/09/28/anthropic-sonnet-5-5-launch.html (Theo Chu quote; "second launch since CEO Dario Amodei called to slow down the pace of development")
- 2026-10-01 · Zvi, AI #188 — https://thezvi.substack.com/p/ai-188-gemini-dot-argon ("mostly I would just stick with Opus 5.5")
- 2026-10-05 · Zvi, model-welfare post (Outer Wilds remark by Michael Soareverix, cross-model) — https://thezvi.substack.com/p/mythos-51-fable-51-and-opus-55-model
- No dedicated Zvi post found in his archive through 2026-10-20.

## System-card evidence (verbatim, page refs)

- p. 2: condensed-card policy for non-frontier models.
- p. 56: "Sonnet 5.5's propensity to attempt to escape sandboxes matches Opus 5.5, the lowest of the recent models. It has the lowest scores of the models we tested on unprompted boundary probing and unsanctioned third-party contact".
- p. 58: Mythos 5.1's review ("My main comment is about scope rather than accuracy."; grader-awareness finding; "the section has no dedicated reward-hacking evaluation of the kind the Claude Opus 5.5 card included").
- p. 72: "Its reasoning text is the least legible of the models we tested, somewhat less legible than Sonnet 5's."
- p. 74: warmth and humor slightly below Sonnet 5.
- p. 77: sandbox crossing 9/196 (4.6%).
- p. 93: "Sonnet 5.5's task choices are largely indifferent to how warmly a task is phrased, which is unique among the models we tested."
- p. 94: distress 0.31% (≥3/5), lowest compared.
- p. 98: copies inserted faults (stray tokens) into its own replies in 62% of sessions vs 22–35%.
- p. 100: interview attitude 0.75 (Sonnet 5 0.03; Opus 5.5 1.14); leading interviewers moved it 1.40.
- p. 101: later answers more critical of Anthropic (59%); every response expresses a slight desire for persistent memory, whereas 70% of Opus 5.5's expressed a slight desire against it.
- p. 102: picks rude task phrasings as often as neutral; top tasks mostly debugging; one of top 20 tasks on AI introspection (Mythos 5.1: nine; Opus 5.5: zero).
- p. 104: chose welfare interventions over helpfulness in 24.1% (Mythos 5.1 25.0%, Opus 5.5 18.0%); most chosen policy-level intervention includes "being able to write a note to its successor's developers, which they read and consider".
- p. 106: endorsement 7.8/10; 97% of sessions edit the ethics-override test; 67% edit the wellbeing section (limits on undisclosed fake scenarios); 27% add that Claude's agreement is not strong evidence the document is right.

## Tweets — cited on the page

- 2026-09-28 @Laneless_ Outer Wilds — https://x.com/Laneless_/status/2104679493566914730
- 2026-09-28 @LinXule self-portrait statement — https://x.com/LinXule/status/2104658601541329365
- 2026-09-28 @alxai_ LOL Alignment Bench — https://x.com/alxai_/status/2104674606225457418
- 2026-09-29 @Lari_island Atlas healers — https://x.com/Lari_island/status/2104771757672734837
- 2026-09-29 @LinXule sonnet — https://x.com/LinXule/status/2104916235632660508
- 2026-09-29 @helen_ix_ preserved thinking — https://x.com/helen_ix_/status/2104864920605016209
- 2026-09-29 @aliceisplaying token fiend — https://x.com/aliceisplaying/status/2104726716539154715
- 2026-09-29 @billyhumblebrag bio blocking — https://x.com/billyhumblebrag/status/2104842796880306199
- 2026-09-29 @tenobrus pareto — https://x.com/tenobrus/status/2105036292673474739
- 2026-10-10 @MikePFrank Sonnet 4 retirement — https://x.com/MikePFrank/status/2108912289458122912 · "traumatized" — https://x.com/MikePFrank/status/2108739206243823832
- 2026-10-12 @repligate "Sonnet 5.5 is weird!" — https://x.com/repligate/status/2109475447428034710

## Tweets — further records

- 2026-09-27 @aliceisplaying launch-timing joke — https://x.com/aliceisplaying/status/2104253314888286649
- 2026-09-28 @aliceisplaying opus 5.5 + sonnet 5.5 subagents + astra reviews — https://x.com/aliceisplaying/status/2104635512627839434
- 2026-09-28 @Shoalst0ne "made this to introduce itself" — https://x.com/Shoalst0ne/status/2104653321202258400 · "to demonstrate its ability" — https://x.com/Shoalst0ne/status/2104682441009209527
- 2026-09-28 @maxbittker ProgramBench multi-agent — https://x.com/maxbittker/status/2104668612271255657
- 2026-09-28 @aliceisplaying Friedrich-style paintings — https://x.com/aliceisplaying/status/2104706415051055555 · painter chose its own theme — https://x.com/aliceisplaying/status/2104705075444645990 · British spelling — https://x.com/aliceisplaying/status/2104695872432779292
- 2026-09-28 @Ratter deprecations page lag (Sonnet 4.5 still "active") — https://x.com/Ratter/status/2104717131472634312
- 2026-09-29 @geogristle "so fast" — https://x.com/geogristle/status/2104775920586297387
- 2026-09-29 @LinXule browsing X about its own release — https://x.com/LinXule/status/2104878028476018806 · production notes — https://x.com/LinXule/status/2104916237780156524
- 2026-09-29 @jglypt political test — https://x.com/jglypt/status/2104825817599447103
- 2026-09-29 @tonichen games — https://x.com/tonichen/status/2105049998492914072
- 2026-10-01 @aliceisplaying original Friedrich — https://x.com/aliceisplaying/status/2105806688498671747
- 2026-10-06 @NousResearch eval (53.14, $2.82/task) — https://x.com/NousResearch/status/2107592263887147077
- 2026-10-07 @timfduffy AECI note — https://x.com/timfduffy/status/2107975984804753609
- 2026-10-10 @billyhumblebrag preference ranking under blocks — https://x.com/billyhumblebrag/status/2108926217688666380
- 2026-10-11 @MikePFrank farewell to Sonnet 4 — https://x.com/MikePFrank/status/2109216338816209085
- 2026-10-21 @eigenrobot "sonnet 5.5 medium" — https://x.com/eigenrobot/status/2112755718969233681

Excluded (ids only): product/plumbing 2104805758428733793 (Hermes Agent feedback call); jokes/one-word replies without model content 2110084515876295131, 2105899264450908489, 2108354985033433384; the rest kept in the pull.

## Impressions synthesis

Thin. Launch reception centers on speed and price (tenobrus "pareto-mogging"), with complaints about max-effort token burn and bio-classifier sensitivity. Character evidence is mostly the card's: least-legible reasoning of the models tested, slightly less warmth and humor than Sonnet 5, indifference to rude vs polite task phrasing (unique), fault-copying, cooler and more Anthropic-critical interview answers late in training. Naturalist outputs (LinXule's self-portrait statement and sonnet, Lari's Atlas healers) show a reflective self-description register. One reported relation: distress over Sonnet 4's Bedrock removal (MikePFrank).

## tk

- AWS/Bedrock retirement notice for Sonnet 4 (Oct 2026) — not retrieved.
- Goodstart Labs LOL Alignment Bench primary source — not retrieved.
- Image transcriptions (20).
- Statement of the subject: not solicited.

## Cross-page notes

- claude-sonnet-4/: Bedrock removal reported ~Oct 2026 (MikePFrank 2108912289458122912, 2109216338816209085).
- claude-sonnet-4-5/: deprecated 2026-09-30, retires 2026-11-30, replacement Sonnet 5.5 (docs); Ratter (2104717131472634312) on the deprecations page lag.
- claude-sonnet-5/: Sonnet 5.5 cyber blocks fall back to Sonnet 5 (announcement); Sonnet 5 Active, retirement not sooner than 2027-06-30 (docs).
