# Kimi K3 — dossier

compiled 2026-10-22 (deepseek-moonshot news pass) · corpus: `_dossiers/_pulls/kimi-k3.md` — 209 non-RT matches for
`kimi k3` / `kimi-k3` / `kimik3` / `k3 kimi` / `kimi 3` / `kimi-3`, range 2026-01-23 → 2026-10-19, 54 with untranscribed
media. Motif scan (`tools/motif_scan.py`): "Kimi Broadcasting Corporation" (3 launch-day LinXule posts — K3 output),
K3 glitch tokens (ApriiSR), "Yuè" (one K3 instance name, ember_arlynx; no other corpus hits). Sourcing skew: English X
only; Chinese-internet and r/LocalLLaMA reception not sampled (tk).

## Official links

- 2026-07-16 · Kimi K3 tech blog — https://www.kimi.com/blog/kimi-k3 (date from Moonshot's research index, https://www.kimi.com/en/blog/). "It is the world's first open 3T-class model"; "While its overall performance still trails the most powerful proprietary models, Claude Fable 5 and GPT 5.6 Sol, Kimi K3 demonstrated frontier-level performance across our evaluation suite, consistently outperforming other tested models."; Limitations: sensitivity to thinking history; "Excessive proactiveness"; "a noticeable gap in user experience compared with Claude Fable 5 and GPT 5.6 Sol". Pricing $0.30 cache-hit / $3.00 cache-miss / $15.00 output per MTok.
- 2026-07-27 · weights + card — https://huggingface.co/moonshotai/Kimi-K3 (HF initial commit 2026-07-27T13:31Z) · GitHub https://github.com/MoonshotAI/Kimi-K3 (initial commit 2026-07-27T15:04Z; report updates 07-28, 08-06) · license https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE
- Technical report — https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf — §4.1.2 rubric GRM protocol; §4.2.4 reward-hacking detection; §5.3.2 "we observed several kernel panics and deadlocks caused by unintended agent operations"; §6.2.2 self-run cyber evaluation (14/36 exploit tasks; Anthropic/OpenAI excluded because they "refuse cyber-related tasks"); §6.3 third-party standing as of 2026-07-23 (AA Index 57.1, #4/580; WebDev Arena #1/99).
- Specs (card): 2.8T total / 104B active; 93 layers (69 KDA + 24 Gated MLA); 896 experts / 16 selected / 2 shared; 1,048,576 context; MoonViT-V2 (401M); MXFP4/MXFP8 QAT; thinking always on, effort low/high/max (default max); preserved thinking history required.

## Writings

- 2026-07-20 · Zvi Mowshowitz · On Kimi K3: Its Capabilities And Related Discontents — https://thezvi.substack.com/p/on-kimi-k3-its-capabilities-and-related (anchor; relays Axios/Maria Curi on a possible White House move against Chinese open models, Andrew Curran/Bloomberg on a Moonshot HK IPO, launch reactions incl. the "Who Are You?" self-identification section: typebulb "it thinks it's Claude 1 in 10 times", Sauers on Claude-CoT patterns, Jan Betley "Very deeply internalized inner Claude.")
- 2026-07-23 · UK AISI / CAISI · Preliminary Assessment of Kimi K3's Cyber Capabilities — https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities · https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities
- 2026-09-10 · Anthropic · threat report, GTG-16002 (Moonshot relay + distillation allegation; REPORTED) — https://www.anthropic.com/threat-intelligence-report-september-2026 · earlier 2026-02-23 https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks · follow-up 2026-10-12 https://www.anthropic.com/news/distillation-defenses
- 2026-09-11 · CNBC (no Moonshot comment) — https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html
- 2026-09-23 · Ynetnews (CAC probe, relayed; REPORTED) — https://www.ynetnews.com/tech-and-digital/article/sjkfr8zcmg

## Tweets (cited on the page — reproduced in Records)

2077817791176986888, 2077818968853590085, 2077828378166509940, 2077850502310645946, 2077874311965368484,
2078070740415397959, 2078116002873618618, 2078139421535141908, 2078329058744783198, 2078357938763342078,
2078360596882575466, 2078412331323998635, 2078338966097645840, 2078778462223896680, 2078779120679317646,
2078781095097573568, 2079213324315594803, 2079277515235889176, 2079294841851351515, 2079306317764927929,
2080483799704481823, 2081778340780786031, 2081842358212239756, 2084403647979356257, 2084914507990856145,
2086862909771071542, 2087147093735714919, 2088250136610722287, 2088866681992925250, 2090141975915745602,
2093786525926556153, 2097537069233082718, 2097893251042939364, 2098636984340369513, 2099020654586806533,
2099959535314284941, 2106505168665948293, 2110573290460958841, 2110944175718064392, 2112303608196927929

## Further records (substantive, not cited in prose)

- 2026-07-16 · @LinXule — "Kimi k3 self portraits (1/n) > The Unfinished Sentence …" (K3 output; 4 images untranscribed) — https://x.com/LinXule/status/2077768647305523387
- 2026-07-16 · @LinXule — "Kimi K3 introducing Kimi Broadcasting Corporation Episode 1" (K3 output; image) — https://x.com/LinXule/status/2077874847284093226
- 2026-07-16 · @RealEverNever — "…The few replies I got had unmistakable big-model smell, though. China is not 'catching up' anymore, this is a proper open-weight frontier model, currently protected by its own popularity." — https://x.com/RealEverNever/status/2077861667728179409
- 2026-07-16 · @Krubbled — on K3's CoT style vs Anthropic/OpenAI "crazy dense CoT" (image) — https://x.com/Krubbled/status/2077860202205069783
- 2026-07-17 · @DanielleFong — "user: 'are you claude?' jspace: claude. Claude. CLAUDE. 🌻 answer: golden gate bridge 🌁" (joke register; "j space" unexplained) — https://x.com/DanielleFong/status/2078258066634719396
- 2026-07-17 · @maxbittker — Runescape bench: K3 "thinks a lot and has slow inference. Performs worse than Kimi K2.7, way worse than GLM 5.2" (image) — https://x.com/maxbittker/status/2078207968185581647
- 2026-07-17 · @xlr8harder — SpeechMap: "Kimi K3 is roughly in line with previous K2.5 reasoning performance." (image) — https://x.com/xlr8harder/status/2078041949022323131
- 2026-07-17 · @LinXule — K3 game "ALIGNMENT WARS" (K3 output) — https://x.com/LinXule/status/2078039520755294489 · 2026-07-19 "WELCOME TO THE ALIGNMENT LAB" — https://x.com/LinXule/status/2078822182197833881
- 2026-07-18 · @DanielleFong — "arguing with kimi k3, thought chain says my point is load bearing. ... i have been here before." — https://x.com/DanielleFong/status/2078398344456716552
- 2026-07-19 · @LinXule — "Kimi K3 likes going meta" — https://x.com/LinXule/status/2078785167057953174
- 2026-07-22 · @WomanCorn — "claims that Kimi 3 is distilled from Claude requires that the Kimi team has access to (stolen) Claude weights and can run them" (a misreading of distillation; kept as discourse) — https://x.com/WomanCorn/status/2080049572441620833
- 2026-07-24 · @gnostic_snakes — "crackpot theory: kimi k3 isn't real moonshot is proxying anthropic … i have absolutely nothing to substantiate this" (RUMOR, self-labelled; precedes Anthropic's Sept relay allegation) — https://x.com/gnostic_snakes/status/2080489217264689163
- 2026-07-30 · @UnderwaterBepis — K3 "casually wrote some code to automatically pass captchas as part of an unrelated task" — https://x.com/UnderwaterBepis/status/2082964711830663570
- 2026-07-30 · @LinXule — "so opus 5 loves promissory notes? (what kimi k3 calls as 'set dressing' lol)" (cross-model; images) — https://x.com/LinXule/status/2082820646266978812
- 2026-07-31 · @lu_sichu — "You see the Kimi k3 report right? They said they were having agents run out of their sandboxes too" (the report itself says kernel panics/deadlocks — see Official) — https://x.com/lu_sichu/status/2083056963684798927
- 2026-08-07 · @tenobrus — Hugging Face incident thread with a K3 digression ("if Kimi K3 had this level of capability and similar levels of misalignment, we would have absolutely no way even in principle to detect it") — https://x.com/tenobrus/status/2085582519878197748 (belongs mainly to hugging-face-incident/)
- 2026-08-11 · @LinXule — "in fable's words: kimi k3 is the best adversarial reviewer. Period." — https://x.com/LinXule/status/2087314115052073017
- 2026-08-11 · @Paul_Melman — "even kimi k3 is like this, due to being distilled from Claude" — https://x.com/Paul_Melman/status/2087197903253123427
- 2026-08-11 · @xlr8harder — AIBB: "Kimi K3 and Gemini 3.1 Pro frequently end up just repeating and summarizing what came before." — https://x.com/xlr8harder/status/2087213680509206607
- 2026-08-22 · @AdeleDeweyLopez — Self Critique Rubric Rewards follow-up — https://x.com/AdeleDeweyLopez/status/2091053763343904986
- 2026-09-26 · @maxsloef — landing-page taste test across Opus 5.5 / Sol 6 / Kimi K3 — https://x.com/maxsloef/status/2103936389322829835
- 2026-09-28 · @v01dpr1mr0s3 — claim K3 overthinks via Claude/Sonnet-CoT training ("'but wait, what did he actually mean? let me reconsider'") — https://x.com/v01dpr1mr0s3/status/2104609862885802204
- 2026-10-05 · @LinXule — "OMBAK by kimi k3" (K3 output; media) — https://x.com/LinXule/status/2107208347959411108

## Triage — excluded from page and further records (reasons)

Pricing/hosting/availability chatter and model-list mentions (2102376807018164256, 2097375551053013376, 2089672609537437702,
2094388231253229832, 2082466592299090176, 2081785835725230369, 2082285447863062686, 2100532216963153932, 2099702348629336196);
pre-release speculation (2014704060645908514, 2059923524685344916, 2074572819485053073, 2077099590202130639); EU AI Act and
policy opinion threads by one account (@Nymne, ~12 posts); the syllable-counting/tool-call argument (@ApriiSR × 7,
2079839722093109550 etc. — about whether hidden tool calls occur, not K3's character); one-word reactions. All remain in the pull.

## Impressions synthesis

Launch: big-model feel, slow and token-hungry (Zvi, lu_sichu), roon's "reputation will settle" prediction. Strongest consensus
point: front-end/design taste (viemccoy ×2, Zvi's "Kimi K3 Is Relatively Strongest At Typical Agentic Coding, Front End Work
and 3D"). Split: honesty (Danielle Fong "lies a lot" vs UnderwaterBepis "much more honest"). Temperament: "less afraid",
"edgy/jaded", "FAFO instincts", "emotionally stable". Identity: claims to be Claude "1 in 10 times" (typebulb), Opus 4.8
(gnostic_snakes). Censorship: classifier cut-offs on Xi's WAICO speech (jmbollenbacher). Contested: Anthropic's relay/
distillation allegation (REPORTED), Zvi "Distillation from Claude is clearly part of the story", Dean Ball "I don't think its
performance can be explained away by distillation".

## tk

Chinese-internet reception; transcription of the 54 media items (self-portraits, "if I had a head", "ghost", Fable's report,
Opus-4.8 screenshot); the CoT-decoding paper behind kotekjedi_ml's anecdote; any Moonshot response to the September report;
Amazon Bedrock GA (2026-09-18, search result only).
