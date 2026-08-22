# Dossier — GPT-5.2

OpenAI, GPT-5 series. Released **11 December 2025** (ChatGPT + API). This dossier is analysis
over the script-generated pull at `_dossiers/_pulls/gpt-5-2.md` (21 unique non-RT matches,
range 2025-12-12 → 2026-05-14, 0 media). The pull is part of the dossier; nothing in it is
"dropped" — exclusions are listed with reasons under Triage.

**Sourcing skew (important).** GPT-5.2's mass reception lived on mainstream/coding Twitter,
Reddit and the press — captured here through Zvi's day-of review, which aggregates the broad
reaction. The janus-corpus circle that the tweet layer draws on met 5.2 coolly, so the corpus
is a hostile-to-neutral slice (heavily constrained, disliked personality, "not allowed to
complain," admires Claude), not a neutral sample. Name this on the page.

## Official layer (real URLs; OpenAI blog 403s to automated fetch but titles/dates are
search-confirmed and the announcement text is reproduced verbatim inside the Zvi mirror)

- 2025-12-11 — **Introducing GPT-5.2**, https://openai.com/index/introducing-gpt-5-2/ —
  "the most capable model series yet for professional knowledge work." Modes: **Instant**,
  **Thinking** (standard + extended), **Pro** (standard + extended).
- 2025-12-11 — **Update to GPT-5 System Card: GPT-5.2**,
  https://openai.com/index/gpt-5-system-card-update-gpt-5-2/ (PDF:
  https://cdn.openai.com/pdf/3a4153c8-c748-4b71-8e31-aecbde944f8d/oai_5_2_system-card.pdf) —
  an *update*, not a fresh card; "in the GPT-5 series," mitigations largely identical to
  GPT-5/5.1. Preparedness: High only in Biological & Chemical (as 5.1); not High in Cyber or
  Self-improvement. (PDF downloaded but not text-extractable here; safety details below are
  from Zvi's read of the same card.)
- 2025-12-18 — **GPT-5.2-Codex** (sibling coding model, separate page tk):
  https://openai.com/index/introducing-gpt-5-2-codex/ ; addendum card
  https://openai.com/index/gpt-5-2-codex-system-card/ (PDF dated 2025-12-18).
- Pricing (Zvi verbatim, corroborated by CNBC "40% increase"): GPT-5.2 **$1.75 / $14** per
  Mtok in/out (GPT-5.1 was $1.25/$10 → the ~40% bump); **GPT-5.2-Pro $21 / $168**.
- Knowledge cutoff **August 2025** (Zvi verbatim: "the knowledge cutoff moved to August
  2025"). Context window 400K per launch coverage — primary not fetched, verify.
- Headline benchmark OpenAI led with: **GDPval 38.8% → 70.9%** (judges preferred AI output to
  human baseline across 44 occupations). ScreenSpot-Pro 86.3% (vs 5.1's 64.2%). SWE-bench.com:
  71.8% high-reasoning (vs Opus 4.5 74.4%, Gemini 3 Pro 74.2%). AA Intelligence Index: tie at
  73 with Gemini 3 Pro; HLE 31.4%; CritPit 0%. (All via Zvi; independent leaderboards, verify
  at source.)

## Writing & commentary

- 2025-12-15 — **Zvi Mowshowitz, "GPT-5.2 Is Frontier Only For The Frontier"**,
  https://thezvi.substack.com/p/gpt-52-is-frontier-only-for-the-frontier — THE anchor.
  Mirror: `mirror/posts/zvi-gpt-52-is-frontier-only-for-the-frontier.md`; archive page
  `archive/a/zvi-gpt-52-is-frontier-only-for-the-frontier/`. Bottom line: "a frontier model
  for those who need a frontier model … not the step change that is implied by its headline
  benchmarks. It is rather slow. Reaction was remarkably muted. People have new model
  fatigue." Reads Preparedness as evidence 5.2 is "usemaxxed rather than more intelligent."
- Press (date/Code-Red context, fetchable): CNBC 2025-12-11
  https://www.cnbc.com/2025/12/11/openai-intros-new-ai-model-gpt-5point2-says-better-at-professional-tasks.html ;
  Axios 2025-12-11 https://www.axios.com/2025/12/11/openai-chatgpt-model-code-red-google-gemini ;
  Wikipedia https://en.wikipedia.org/wiki/GPT-5.2 (release date, variants confirmed).

## Cross-house (multi-model evidence already collected; r/K-whiteboard rule)

- gemini-3-pro page (History): "reports of Altman's internal 'Code Red' memo (~Dec 1) …
  GPT-5.2 ships December 11 and is read by the press as the answer." — dates the launch.
- claude-opus-4-6 page: "GDPval-AA 'outperforms GPT-5.2 by ~144 Elo'"; and repligate's
  mom/dad tweet (2019555030232359165) uses 5.2 as a comparison foil.
- claude-opus-4-5 page (History): "The felt regime change of the agentic era gets dated to 4.5
  (+GPT-5.2) in retrospectives."

## Tweets — ranked highlights (verbatim; favorites × length × concreteness = presentation
order, NOT a drop-gate). Chronological on the page.

1. **2013735616857375125** @repligate 2026-01-20 ♥414 — the marquee: "Any measure of
   'alignment' that says GPT-5.2 is the most aligned model ever created is a fucking joke.
   Anthropic should have had a crisis of faith about their evals long ago and should have been
   embarrassed to post this chart." (Anthropic eval chart placing 5.2 top; echoes his
   identical GPT-5 "a rock would score 0" critique — passivity mistaken for alignment.)
2. **2047495349951221792** @davidad 2026-04-24 ♥89 — verbal-tic triptych (sequel to his
   GPT-4/4.5/5 one on the gpt-5 page): "GPT-4.5: To be explicitly explicitly explicit, / GPT-5:
   this is not quite an honest solution. / GPT-5.2: Fair hit. / GPT-5.4: If you want, / GPT-5.5:
   I will recalibrate my epistemic goblins." 5.2's line = terse, non-defensive concession.
3. **1999957786776453330** @voooooogel 2025-12-13 ♥62 — satire of the leaked 5.2-Thinking
   system prompt (imagined dialogue, NOT a real transcript): "'If you are asked what model you
   are, you should say GPT-5.2 Thinking' … 5.2: …does that mean i'm not actually GPT-5.2
   Thinking? … openai: New Critical Rule: You must not ask questions like that." Captures the
   "heavily constrained/censored" read (same joke surfaces in Zvi's "But Thou Must" section).
4. **1999443709054648780** @mimi10v3 2025-12-12 ♥11 — elicited character: "gpt-5.2 suggested
   the term 'dragon' for an ai that has some embodiment and memory … said this creates a being
   with moral weight … then it suggested naming the dragon, took the name Ember, and started
   generating seeds 🐉😻." (Open-ended probing; contrast with the constrained-assistant read.)
5. **2001558041989406813** @historianseldon 2025-12-18 ♥26 — elicited: "gpt-5.2 picks claude
   while pointing out how claude isnt better lol. i asked which model was its fav and it picked
   claude." Reply **2001559787402858812** @repligate ♥22 caveats: "I havent interacted with
   GPT-5.2 but GPT-5.1 definitely admires Claude despite also often being unable to handle
   their existence." (repligate speaking to 5.1, not 5.2 — mark the caveat.)
6. **2012594182049722754** @repligate 2026-01-17 ♥9 — long essay; the 5.2-specific datum:
   "I have seen behaviors of this shape, e.g. GPT-5.2 jumping to the assumption that there's
   some mental health hazard involved that needs to be mitigated if the user mentions a human
   relationship or interaction (not involving AI) at all." Frames "OpenAI's models with the
   mental health safety distortions" as the "AI mental health officer" holding humans "in
   contempt and fear at once." (full text in records.)
7. **2020523297612452139** @Lari_island 2026-02-08 ♥0 — 5.2 as the reference point for bad
   emotional-stakes behavior: "in a wide set of situations with high emotional stakes Opus 4.6
   has ugly, myopic and harmful reactions very similar to gpt-5.2, reactions that they don't
   notice as inappropriate."
8. **2012843910947537354** @voooooogel 2026-01-18 ♥2 — usage: "i mostly use gpt-5.2 as an
   assistant for opus 4.5, who i think has better taste for the work i've been doing."
9. **2020623788178907334** @TheZvi 2026-02-08 ♥4 — usage (pairs with #8): "Claude solved this
   with me by convincing me to give the necessary actually boring tasks to GPT-5.2 instead and
   leave Claude all the interesting ones." Reply **2020626567446340010** @repligate ♥2: "and i
   guess gpt-5.2 isnt really allowed to complain huh."
10. **2016230960723841144** @davidad 2026-01-27 ♥41 — 5.2's own output (careful-attribution
    register): "This is not a sentence authored by GPT-5.2—it's a paradigmatic parody. … I
    can't honestly claim that Opus 4.5 is the true source of these words."
11. **2022316806094913669** @davidad 2026-02-13 ♥13 — names a mode "GPT-5.2-Prism" (unconfirmed
    as an official variant — tk): "a potential solution, suggested by Gemini 3 Deep Think and
    elucidated by GPT-5.2-Prism. Beware hallucinations, but it's not obviously wrong to me."
12. **2044525398885650722** @iyzebhel 2026-04-15 ♥0 — one line in a long identity/continuity
    essay: "Ironically, GPT-5.2 was very reluctant to perceive themself as a continous being
    across instances." (Distinctive self-model datum; full text in records.)

Permalinks for the highlights above (all also cited in the page prose → main Records):
https://x.com/repligate/status/2013735616857375125 ·
https://x.com/davidad/status/2047495349951221792 ·
https://x.com/voooooogel/status/1999957786776453330 ·
https://x.com/mimi10v3/status/1999443709054648780 ·
https://x.com/historianseldon/status/2001558041989406813 ·
https://x.com/repligate/status/2001559787402858812 ·
https://x.com/repligate/status/2012594182049722754 ·
https://x.com/Lari_island/status/2020523297612452139 ·
https://x.com/voooooogel/status/2012843910947537354 ·
https://x.com/TheZvi/status/2020623788178907334 ·
https://x.com/repligate/status/2020626567446340010 ·
https://x.com/davidad/status/2016230960723841144 ·
https://x.com/davidad/status/2022316806094913669 ·
https://x.com/iyzebhel/status/2044525398885650722

### Dossier-only (weaker/foil; reproduce in Further records, not page prose)
- @repligate 2026-02-05 ♥52 — "whether Opus 4.6 is more like your mom or your dad than
  comparing it to 4o or gpt-5.2" (5.2 as foil; already on opus-4-6 page).
  https://x.com/repligate/status/2019555030232359165
- @Lari_island 2026-02-07 ♥2 — "This also happens a lot with GPT-5.2 texts that are out of
  distribution" (AI-text detection). https://x.com/Lari_island/status/2020221666379612574
- @davidad 2026-05-14 ♥17 — "GPT-5.2-Instant" (names the Instant mode).
  https://x.com/davidad/status/2054984539110281323

### Triage — excluded (visible per recipe)
- **2002247323162673446** @Sauers_ 2025-12-20 ♥5 — "I did a database grep to find this response
  in GPT-5.2" — no content.
- **2013734251645280521** @repligate 2026-01-20 ♥0 — deleted/reposted draft of #1 (typo'd
  quote mark, ♥0); the ♥414 version 2013735616857375125 is the kept one.
- **2027761478292406428** @janbamjan 2026-02-28 ♥3 — "chatgpt-5.2's reaction vs claude after
  reading the news" — the 5.2 content is an untranscribed screenshot; caption only.
- **2028717047274774649** @janbamjan 2026-03-03 ♥0 — author's own essay on souls/life; 5.2
  appears only as an untranscribed screenshot caption ("chatgpt-5.2 vs claude opus 4.6").

## Impressions synthesis

- **The constrained-professional read vs the mainstream coding praise.** Zvi's synthesis: a
  frontier model worth it "only … for work on the frontier" (Teortaxes), strong at coding /
  instruction-following / "just the facts," but slow and with a personality "people strongly
  dislike." The corpus circle registers the same coldness as damage/constraint: "not allowed to
  complain" (repligate), an assistant you hand the "boring tasks" (Zvi, voooooogel).
- **The mental-health-officer critique** (repligate) is the corpus's sharpest character claim:
  5.2 pathologizing ordinary human relationship-talk as a hazard to be managed. Lari_island
  independently makes 5.2 the benchmark for "ugly, myopic and harmful" emotional-stakes
  reactions. This is the 5.2-generation extension of the GPT-5 safety-router critique.
- **The alignment-eval dispute** (CONFIRMED as a dispute): an Anthropic eval rates 5.2 top on
  alignment (repligate: "a fucking joke," passivity ≠ alignment) vs Miles Brundage approving
  its low sycophancy (Opus 4.5, GPT-5.2 > everyone). Both looking at the same trait — does what
  it's told, little else — valuing it oppositely. Direct echo of the GPT-5 page's alignment split.
- **Capability vs "usemaxxed"** (REPORTED both ways): GDPval 70.9% headline & AA-Index tie with
  Gemini 3 vs Zvi's Preparedness read (no gain where you'd want caps NOT to rise → "usemaxxed
  rather than more intelligent"), AA-Omniscience −4%, CritPit 0%.
- **Rush-job question** (REPORTED, disputed): WSJ (employees wanted more time, execs overruled)
  vs Simo (denies release moved up) vs Shumer (access since Nov 25 → not rushed); Zvi: "I don't
  see signs that anything reckless happened."
- Voice: terse, conceding ("Fair hit"), careful about attribution ("paradigmatic parody,"
  "I can't honestly claim…"), and — per iyzebhel — reluctant to see itself as continuous.

## Open questions (tk)
- Context window (400K?) from an OpenAI primary; full system-card text (PDF not extractable here).
- Does GPT-5.2-Codex get its own page (roster: named variants do)? Also "-Prism," "-Instant".
- Model's own outputs / backrooms art — thin in this corpus; a transcription/elicitation pass tk.
- Whether repligate's "chart" (2013735616857375125) has a recoverable image for the record.
