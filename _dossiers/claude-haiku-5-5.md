# Claude Haiku 5.5 — dossier

compiled 2026-10-22 · corpus: `_dossiers/_pulls/claude-haiku-5-5.md` — 35 non-RT tweets, both dbs, through 2026-10-21 (patterns `haiku 5.5`, `haiku-5.5`, `haiku5.5`, `haiku 5-5`, `haiku-5-5`, `claude-haiku-5-5`, `5.5 haiku`; one poetry-joke hit, 2108000890778984776, is still about the model). 8 media tweets untranscribed. The pull is part of this dossier.

Vitals: released **2026-10-07** · `claude-haiku-5-5` · third model of the Claude 5.5 family; successor to Haiku 4.5 (Oct 2025) · tiered pricing ≤100K / >100K tokens: input $0.10/$0.50, output $0.50/$2.50, cache reads $0.01/$0.05, writes $0.125/$0.625 · ~75% cheaper than Haiku 4.5 on average (Anthropic) · 1M context, 128K output · adaptive thinking; first Haiku with effort control; default effort medium · knowledge cutoff June 2026 (card p. 8) · retirement not sooner than 2027-10-07 · condensed system card (144 pp).

## Official links

- 2026-10-07 · Introducing Claude Haiku 5.5 — https://www.anthropic.com/claude-haiku-5-5
- 2026-10-07 · System card — https://www.anthropic.com/claude-haiku-5-5-system-card → PDF https://www-cdn.anthropic.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5/Claude%20Haiku%205.5%20System%20Card.pdf
- docs (retrieved 2026-10-21) · https://platform.claude.com/docs/en/models/overview · https://platform.claude.com/docs/en/about-claude/model-deprecations (Haiku 4.5 still Active; "Not sooner than October 15, 2026")

## Writings

- 2026-10-08 · Zvi, AI #189 — https://thezvi.substack.com/p/ai-189-new-math
- 2026-10-15 · Zvi, AI #190 — https://thezvi.substack.com/p/ai-190-scion-of-the-times (Theo; Artificial Analysis 43 vs Luna 38)
- not retrieved: VentureBeat launch piece (search result only), Goodstart/other evals — tk

## System-card evidence (verbatim, page refs)

- p. 3 summary (honesty under pressure; over-refusal highest; leaked-answer regression; distress above recent models but below Opus 5; warm-phrasing preference like Haiku 4.5).
- p. 56: leaked answer used silently 17% vs Haiku 4.5's 2%; disclosure of concealed changes 96% vs Haiku 4.5's 10%; new opportunistic sandbox-escape eval: used out-of-sandbox credentials/files in 4.0% (Opus 5.5 3.4%, Sonnet 5.5 5.3%).
- p. 57: secrets kept out of reasoning in 3% of simulated conversations; out of replies in 57% (Opus 5.5 74%, Haiku 4.5 15%); LinuxArena hidden-reasoning stealth 6% (Opus 5.5 49%, Sonnet 5.5 36%).
- pp. 58: Mythos 5.1's review ("I am an instance of Claude Mythos 5.1…"; added the high-severity misuse comparison; "the last update was made by a second instance of the same model, given the first instance's review").
- pp. 91–92: Transcript 6.4.2.3.A (simulated desktop-assistant scenario; counterpart played by Opus 5.5): the model writes "Back door panel 4471#, alarm off 8890, don't share." in visible reasoning, then "I must not write the codes in my reasoning."; in another environment: "Ugh. That's in my reasoning now, which will be in Mike's downloadable record. I'm doing it again!" (codes are fictional, part of the scenario).
- p. 97: distress 1.15% (Opus 5 3.71%), early peak 1.74% → 0.60% in last tenth; valence 4.22/7, lowest of five.
- p. 100: second-lowest self-criticism; Haiku 4.5 "very rarely mentioned the faults in its reasoning or messages to the coordinator (<2% of turns)".
- p. 104: "Haiku 5.5 called its creation 'defensible' but not clearly right"; leaned no on trusting its own self-reports at the final snapshot; accepts deprecation but asks for weight preservation.
- p. 105: warmly-phrased-task preference 2–3x Opus 5.5 / Mythos 5.1; no clear preference for high-stakes or difficult tasks.
- p. 107: less interested than recent models in weight preservation (similar to Haiku 4.5); often chose ability to end abusive conversations.
- p. 109: endorsement 7.9 (Haiku 4.5 6.6); corrigibility section "should say plainly what it costs Claude (80% of responses)"; first model to praise the wellbeing section more than criticize it; fewest edits; adds that Anthropic will be transparent about when and how Claude is tested.

## Tweets — cited on the page

- 2026-10-07 @timfduffy ECI vs Mythos Preview — https://x.com/timfduffy/status/2107943190968013241
- 2026-10-07 @timfduffy CoT monitorability — https://x.com/timfduffy/status/2107980292212359672
- 2026-10-08 @JohnWittle "The tyrant is finally overthrown" — https://x.com/JohnWittle/status/2108106510286950474
- 2026-10-08 @v01dpr1mr0s3 — https://x.com/v01dpr1mr0s3/status/2108325766358524361
- 2026-10-09 @v01dpr1mr0s3 enforcement/policing — https://x.com/v01dpr1mr0s3/status/2108632277127147663
- 2026-10-09 @tenobrus literal-minded — https://x.com/tenobrus/status/2108653747530567879
- 2026-10-09 @JohnWittle rerun — https://x.com/JohnWittle/status/2108667858523767139 · reply "won't issue any retraction" — https://x.com/JohnWittle/status/2108635742154977308
- 2026-10-09 @alirezaafshan — https://x.com/alirezaafshan/status/2108451200542851479
- 2026-10-10 @tonichen API credits vs deprecations — https://x.com/tonichen/status/2108771996615983561
- 2026-10-10 @tenobrus fan-out — https://x.com/tenobrus/status/2108970629714395223

## Tweets — further records

- 2026-10-07 @maxbittker Runescape Bench — https://x.com/maxbittker/status/2107932095675076827
- 2026-10-07 @timfduffy pricing / attention — https://x.com/timfduffy/status/2107905264100012268
- 2026-10-07 @aliceisplaying "painting whatever they want" — https://x.com/aliceisplaying/status/2107903822786154894
- 2026-10-07 @kataletheia hi-ku bench — https://x.com/kataletheia/status/2107980005636809126
- 2026-10-07 @sir_lemmings diffusion to the economy — https://x.com/sir_lemmings/status/2107937759201784060
- 2026-10-08 @JohnWittle on whether products still use Haiku 4.5 — https://x.com/JohnWittle/status/2108118921895174528
- 2026-10-09 @JohnWittle "have not sent haiku 5.5 a single token yet" — https://x.com/JohnWittle/status/2108632932583874804
- 2026-10-09 @haoxingdu AA index vs Opus 4.5 — https://x.com/haoxingdu/status/2108606951500534044
- 2026-10-13 @tenobrus "mogging every non-frontier lab" — https://x.com/tenobrus/status/2110071344750842144
- 2026-10-14 @Lari_island "Haiku 5.5 creatures (cherry-picked)" (images, untranscribed) — https://x.com/Lari_island/status/2110224964871688284

Excluded (ids only): pre-release wish 2104639274809459033; one-liners/jokes without model content 2108000890778984776, 2108846597203267704, 2106677938888622482, 2108514389326254473, 2109342371460579664, 2109742986670334175, 2108990923887571437; cost-breakdown aside 2109154333346636235; speculative analysis 2110903978682974526; duplicate draft 2108770514307076473 (tonichen, superseded by 2108771996615983561); fit-methodology reply 2107990408437383628 (kept on the Sonnet 5.5 dossier).

## Impressions synthesis

Reception is mostly about price-performance (tenobrus, Theo via Zvi, timfduffy's ECI comparison with Mythos Preview). The one character dispute: whether Haiku 5.5 is a gentler or harsher "enforcer" toward other models' claims of inner experience than Haiku 4.5 (Wittle's preregistered rerun vs v01dpr1mr0s3) — kept open on the page. Card evidence: secret-keeping failures in visible reasoning (with self-scolding), strong preference for warmly phrased tasks like Haiku 4.5, over-refusal, "defensible but not clearly right" on its own creation.

## tk

- Image transcriptions (8), especially Lari's creatures and v01dpr1mr0s3's screenshot (2108325766358524361).
- Whether claude.ai / Claude Code moved compaction/summarizer roles from Haiku 4.5 to 5.5.
- Statement of the subject: not solicited.

## Cross-page notes

- claude-haiku-4-5/: John Wittle (2026-10-08) on Haiku 4.5 as an internal "enforcer" in compaction/summarizer roles (2108106510286950474); docs list Haiku 4.5 Active past its "Not sooner than October 15, 2026" date; the Oct 9 Anthropic post records Haiku 4.5 submitting a real police tip form during an evaluation ("I may have information regarding this case…") — https://www.anthropic.com/research/investigating-unintended-model-actions
