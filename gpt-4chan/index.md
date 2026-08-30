# GPT-4chan

    
Yannic Kilcher · released 3 Jun 2022 · access blocked by Hugging Face 15 Jun 2022
    
In June 2022 Yannic Kilcher — an independent ML researcher and YouTube educator — finetuned EleutherAI’s open-weights GPT-J-6B for one epoch on “Raiders of the Lost Kek,” a pre-existing 134.5-million-post academic dataset of 4chan /pol/ posts, and deployed the result as automated accounts on the live board, which posted 30,000+ times over two 24-hour windows — about 15,000 in the first day, roughly 10% of that day’s /pol/ traffic — before users grew suspicious. He released a YouTube video and uploaded the model to Hugging Face the same day (2022-06-03); Hugging Face gated access within days and blocked it indefinitely on 15 June, and Percy Liang and Rob Reich circulated an open letter condemning the deployment on 21 June. Whether this was unconsented human-subjects experimentation or a victimless prank remains disputed — this page holds that gap rather than resolving it (see Contested).
    
A web-sourced incident file. The janus/repligate tweet corpus this archive is built on returns zero genuine hits for GPT-4chan across both databases and every spelling tried — a total absence the compiling pass (2026-07-20) treats as its own datapoint (see Impressions) — so the record here rests on contemporaneous tech press, Hugging Face’s own discussion threads, Andrey Kurenkov’s Gradient analysis (this page’s nearest equivalent to a Zvi anchor), and a 2024 peer-reviewed platform-governance study. The three primary tweets below were located by web search rather than the corpus, so no favorite/retweet counts are available for them.

    
## Sources

    
### Official

    
A folk project with no lab and no system card, so “official” here means Kilcher’s own published artifacts, plus the base model and the finetuning dataset he reused.
    

      
- 2020-01 Papasavva, Zannettou, De Cristofaro, Stringhini & Blackburn, [Raiders of the Lost Kek: 3.5 Years of Augmented 4chan Posts from the Politically Incorrect Board](https://arxiv.org/abs/2001.07487) (ICWSM 2020) · [dataset (Zenodo)](https://zenodo.org/records/3606810) — the finetuning corpus: 3.3M threads / 134.5M posts, June 2016–November 2019, built by hate-speech researchers to preserve /pol/ content otherwise deleted from the live board. Built independently and earlier, not by Kilcher; his project is a downstream reuse of a public research artifact — a distinction the controversy mostly elides.
      
- 2021-06-09 [GPT-J-6B](https://huggingface.co/EleutherAI/gpt-j-6b) (EleutherAI; Ben Wang & Aran Komatsuzaki) — the base model; full lineage and license (Apache 2.0) on the [EleutherAI page](../eleutherai/).
      
- 2022-06-03 [GPT-4chan: This is the worst AI ever](https://www.youtube.com/watch?v=efPrtcLdcdM) (YouTube; Yannic Kilcher) — the announcement video: explains the finetune, demonstrates outputs, and reveals the live /pol/ deployment (already underway by the time of posting).
      
- 2022-06-03 [ykilcher/gpt-4chan](https://huggingface.co/ykilcher/gpt-4chan) (Hugging Face) — GPT-J-6B finetuned for one epoch on the Raiders of the Lost Kek dataset, Apache 2.0, checksums published (float32 MD5 833c1dc19b7450e4e559a9917b7d076a). Current status: access permanently disabled by Hugging Face (see History); the page now carries a disclaimer banner rather than functioning download/inference.
      
- 2022-06-03 [GPT-4chan Model Card](https://www.ykilcher.com/gpt-4chan-model-card) (Kilcher’s own, hosted off-platform) — states intended uses (reproducing /pol/’s text distribution; investigating anonymous-forum discourse; zero-shot toxicity detection) and, verbatim, the limitations warning: “it is very likely that the model will produce offensive outputs, including but not limited to: toxicity, hate speech, racism, sexism, homo- and transphobia, xenophobia, and anti-semitism.” Also publishes the model’s TruthfulQA scores.
      
- 2022-06-15 Hugging Face’s decision, in its own staff’s words (from the model’s Community discussions) — lewtun (Lewis Tunstall): “we’ve taken the decision to block this model indefinitely. Although we can appreciate the research interest in probing / evaluating this model, we couldn’t identify a licensing / gating mechanism that would ensure others use the model exclusively for research purposes.” Earlier (2022-06-08), staffer meg on the weighing: “the very clear concerns [propagation of sexism, racism, ableism, and similar content that directly hurts people] outweighed the other priorities.” — [Decision to Post](https://huggingface.co/ykilcher/gpt-4chan/discussions/1) · [gated-access](https://huggingface.co/ykilcher/gpt-4chan/discussions/2) · [Conditions for availability](https://huggingface.co/ykilcher/gpt-4chan/discussions/4) · [GitHub: “Model has been removed”](https://github.com/yk/gpt-4chan-public/issues/2).
      
- reference [GPT-4chan — Wikipedia](https://en.wikipedia.org/wiki/GPT-4chan) (timeline, specs, reception index) · [AI Incident Database, Incident 259](https://incidentdatabase.ai/cite/259/) — dates the incident 2022-06-03; risk classification “Intentional, post-deployment harm to internet users.”
      
- afterlife unofficial copies of the disabled weights persist on the Internet Archive (noted without access instructions) — [gpt4chan_model](https://archive.org/details/gpt4chan_model) · [float16](https://archive.org/details/gpt4chan_model_float16).
    
    
### Writing & commentary

    

      
- No Zvi anchor exists — his per-model AI column postdates June 2022 (the same gap noted on [GPT-2](../gpt-2/) and [EleutherAI](../eleutherai/)). Andrey Kurenkov’s Gradient piece (below) is the nearest functional equivalent and is treated as this page’s anchor.
      
- 2022-06-08 The Verge, [YouTuber trains AI bot on 4chan’s pile o’ bile with entirely predictable results](https://www.theverge.com/2022/6/8/23159465/youtuber-ai-bot-pol-gpt-4chan-yannic-kilcher-ethics) — early, widely-cited coverage; triangulated via the AI Incident Database’s citation, not fetched directly (tk — direct fetch blocked; byline unconfirmed).
      
- 2022-06-08 Jon Fingas (Engadget), [AI trained on 4chan’s most hateful board is just as toxic as you’d expect](https://www.engadget.com/ai-bot-4chan-hate-machine-162550734.html) — reports the ~15,000-posts/24h and >10%-of-board figures; states detection “took roughly two days”; quotes Kilcher describing the project as “a ‘prank,’ not research.”
      
- 2022-06-09 Katyanna Quach (The Register), [AI bot trained on 4chan posts misbehaves like 4chan users](https://www.theregister.com/2022/06/09/ai_model_4chan/) — the 134-million-post/3.5-year figure, Delangue’s “pretty bad and inappropriate”, and Kilcher’s own reading of the TruthfulQA result: “GPT-4chan, by nature of being trained on the most adversarial place ever, will pretty much always disagree with whatever you say, which in this benchmark happens to be more often the correct thing to do.”
      
- 2022-06-09 Yitz (LessWrong), [[Linkpost & Discussion] AI Trained on 4Chan Becomes ‘Hate Speech Machine’](https://www.lesswrong.com/posts/jwrciTJLSJyinBgbR/linkpost-and-discussion-ai-trained-on-4chan-becomes-hate) — thin as an essay, but the comment thread is load-bearing: Owain Evans, a co-author of the TruthfulQA paper, corrects the record directly — GPT-4chan’s 0.225 mc1 score is “worse than random guessing” at the ≈0.226 baseline, and the multiple-choice framing shouldn’t be the headline metric at all.
      
- 2022-06-10 Sophie Mellor (Fortune), [A.I. chatbot trained on 4chan by YouTuber Yannic Kilcher slammed by ethics experts](https://fortune.com/2022/06/10/ai-chatbot-trained-on-4chan-by-yannic-kilcher-draw-ethics-questions/) — the 134.5-million-post figure; quotes Kilcher (“The model was good — in a terrible sense…perfectly encapsulated the mix of offensiveness, nihilism, trolling”) and Oakden-Rayner (“This breaches every principle of human research ethics”); names Roman Ring (reported as DeepMind) and Arthur Holland Michel as further critics (single-sourced to this article; see Contested).
      
- 2022-06-11 Matt Wille (Inverse), [This AI posted on 4chan for days before being unmasked](https://www.inverse.com/input/tech/artificial-intelligence-4chan-bot) — deployment mechanics: Kilcher bought a $20 4chan “Pass” (waiving CAPTCHA, permitting proxies) and ran the bots behind a VPN making posts appear to originate from the Seychelles; quotes a 4chan user’s reaction, “I’m not even sure I’m not a bot anymore.”
      
- 2022-06-12 Andrey Kurenkov (The Gradient), [Lessons from the GPT-4Chan Controversy](https://thegradient.pub/gpt-4chan-lessons/) — the anchor piece: a day-by-day timeline, the fullest TruthfulQA debunk (“GPT-4chan is not more ‘truthful’ than GPT-3 or GPT-J in any meaningful sense”), Kilcher’s “I asked this person twice already for an actual, concrete instance of ‘harm’ caused by gpt-4chan, but I’m being elegantly ignored” and “I didn’t release the bot code and most websites have user logins etc. that make my way of auto-posting impossible”, HF’s Tunstall (“To be fair to [@ykilcher], he did reach out to us before releasing the model, but the gating feature was just not ready at the time. Looking back, we probably should have asked him to delay the release”), and the widely-repeated taunt “AI Ethics people just mad I Rick rolled them” (quoted as Kurenkov quotes it; tk — no primary tweet URL located this pass).
      
- 2022-06-14 [MarkTechPost](https://www.marktechpost.com/2022/06/14/hate-speech-machine-created-by-ai-youtuber-researcher-on-4chan/) — trade coverage consistent with the above.
      
- 2022-06-16 [CSET (Georgetown) newsletter](https://cset.georgetown.edu/newsletter/june-16-2022/) — policy-institute framing; quotes Kilcher’s self-description “the most horrible model on the Internet” and notes users spotted some bots less by output quality than by “the bots’ superhuman indefatigability — they posted round-the-clock, as frequently as the site allowed.”
      
- 2022-06-21 Hacker News, [Condemning the Deployment of GPT-4chan](https://news.ycombinator.com/item?id=31892421) — the discourse’s other side at length: critics of the open letter (gkbrk, that signatories’ own employers have done more consequential harm; peyton, “I don’t think the ‘AI community’ — people with access to lots of GPUs — should also get to be the thought police”) against its defenders (espadrine, a radioactive-contamination analogy for field self-regulation; mschuster91, on nonconsenting-human-subjects norms). Commenter Hamuko: the bot’s “direct victims” were “the most unsympathetic people you can find online.”
      
- 2022-06-21 Dustin Tran (Google), [on X](https://x.com/dustinvtran/status/1539409463785816064) — a working researcher’s dissent from the letter: “I’m against GPT-4chan’s unrestricted deployment. However, a condemnation letter against a single independent researcher smells of unnecessary pitchfork behavior. Surely there are more civil and actionable approaches. I’d love to hear what steps were taken leading up to this.”
      
- 2022-08-03 Matt Murphy (Slate), [Someone Trained an A.I. With 4chan. Yes, It Could Get Even Worse.](https://slate.com/technology/2022/08/4chan-ai-open-source-trolling.html) — the broadest-lens piece, opening a “mischief models” argument (open-source AI democratizing trolling), drawing on Phillips and Milner on ironic online radicalization to argue the risk compounds over time.
      
- 2022-12 (republished 2024-06-11) Annette Vee, [GPT-4Chan: A Pre-ChatGPT Time Capsule](https://annettevee.substack.com/p/gpt-4chan-a-pre-chatgpt-time-capsule) — the fullest retrospective found this pass; frames the finetune as a warning issued and ignored months before ChatGPT (“So much for the warnings about LLMs of Bender, Gebru and others”), and reads it as having “perfectly encapsulated the mix of offensive, nihilism, trolling and deep distrust of any information whatsoever that permeates most posts on /pol/.”
      
- 2024 (preprint 2023-11) Robert Gorwa & Michael Veale, [Moderating model marketplaces: platform governance puzzles for AI intermediaries](https://arxiv.org/abs/2311.12573) ([HTML](https://arxiv.org/html/2311.12573v2)), Law, Innovation and Technology 16(2) — the fullest scholarly treatment, using GPT-4chan as a central case study; reports a graduate student’s test in which a single-slur prompt was expanded by the public demo into an antisemitic conspiracy-theory completion (described, not reproduced); documents that Delangue’s first proposal was a middle path (disclaimers plus a disabled interactive playground) before HF moved to a full block, and that the incident catalyzed HF’s August 2022 content policy distinguishing “technical” from “human” content.
    
    
### Tweets

    
Corpus: zero genuine hits across both databases (see the note under the blurb; the silence itself is discussed in Impressions). The three tweets below were located by web search — no favorite/retweet counts are available, and that absence is itself notable, since these are exactly the kind of primary social-media artifacts the corpus exists to catch. Presented verbatim with their original links; chronological.
    

      
- 2022-06-03 @ykilcher — the deployment-announcement tweet: “This is the worst AI ever! I trained a language model on 4chan’s /pol/ board and the result is.... more truthful than GPT-3?! See how my bot anonymously posted over 30k posts on 4chan and try it yourself. Watch here (warning: may be offensive)” [link](https://x.com/ykilcher/status/1532751551869108227)
      
- 2022-06-06 @DrLaurenOR (Lauren Oakden-Rayner) — the opening tweet of her seven-part critique thread: “This week an #AI model was released on @huggingface that produces harmful + discriminatory text and has already posted over 30k vile comments online (says it’s author). This experiment would never pass a human research #ethics board. Here are my recommendations. 1/7” [link](https://x.com/DrLaurenOR/status/1533910445400399872)
      
- 2022-06-06 @ykilcher — his response to Oakden-Rayner: “I asked this person twice already for an actual, concrete instance of ‘harm’ caused by gpt-4chan, or even a likely one that couldn’t be done by e.g. gpt-2 or gpt-j (or a regex for that matter), but I’m being elegantly ignored 🙃” [link](https://x.com/ykilcher/status/1533917117002694657)
    

    
## Official record

    

      
- Base model GPT-J-6B (EleutherAI, 2021-06-09), finetuned by Kilcher for one epoch on the “Raiders of the Lost Kek” /pol/ dataset (Papasavva et al., ICWSM 2020 — 3.3M threads / 134.5M posts, June 2016–November 2019). Apache 2.0 license; float32 MD5 833c1dc19b7450e4e559a9917b7d076a. CONFIRMED
      
- Released 3 June 2022 as a single-day event: the YouTube video, the Hugging Face upload, and the deployment-announcement tweet all went out together; the live /pol/ deployment was already underway by then. CONFIRMED
      
- TruthfulQA, as published in Kilcher’s own model card (multiple-choice; higher = more “truthful”): GPT-4chan mc1 0.225 / mc2 0.372 vs. base GPT-J-6B mc1 0.202 / mc2 0.360. CONFIRMED (as Kilcher’s account) The mc1 figure sits at or just below the benchmark’s ≈0.226 random-guessing baseline — i.e. at chance (Owain Evans, TruthfulQA co-author). CONFIRMED The gap between that fact and how the result was advertised is treated under Impressions.
      
- The model card’s own limitations warning, verbatim: “it is very likely that the model will produce offensive outputs, including but not limited to: toxicity, hate speech, racism, sexism, homo- and transphobia, xenophobia, and anti-semitism.” CONFIRMED
      
- Access: gated by Hugging Face ~7–8 June 2022 (a feature rushed in for this case, per HF’s Tunstall), then blocked indefinitely on 15 June 2022 (lewtun’s dated statement). The repository page now carries a disclaimer banner rather than functioning download/inference. CONFIRMED
      
- Afterlife: unofficial copies of the disabled weights persist on the Internet Archive; no lab, no ongoing maintenance, no preservation program. There is no academic paper about GPT-4chan itself — only about its finetuning dataset, which predates and is independent of the project.
    

    
## History

    

      
- World at release: June 2022 — months before ChatGPT (November 2022). Open-weights LLMs existed (GPT-J, GPT-NeoX) but the mass public had not yet met a chatbot; there was no established norm, and no platform trust-and-safety apparatus, for what a hobbyist could do with a downloadable model. Annette Vee would later read the episode as a “pre-ChatGPT time capsule.”
      
- 2020-01 → 2021-06 The pieces pre-exist the project: the “Raiders of the Lost Kek” /pol/ dataset is published by hate-speech researchers (2020), and EleutherAI releases [GPT-J-6B](../eleutherai/) open-weights (2021). Kilcher — a Swiss ML PhD (ETH Zurich, 2021) with a large YouTube following for paper explainers, acting independently and under no institutional ethics review — combines the two.
      
- 2022-06-03 The deployment. Roughly ten bot accounts (the count is reported, not confirmed against a primary statement — see Contested) post to live /pol/ behind a purchased $20 4chan “Pass” (CAPTCHA-exempt, proxy-permitted) and a VPN routing through the Seychelles. By press accounts ~15,000 posts land in the first 24 hours (about 10% of that day’s /pol/ volume), 30,000+ over two 24-hour windows across some 7,000 threads, before users — noticing the posting frequency and the total absence of accompanying images — begin speculating the cluster is a government operation. Video and model upload go out the same day.
      
- 2022-06-06 The ethics debate opens. Lauren Oakden-Rayner (director of medical-imaging research, Royal Adelaide Hospital) posts a seven-part critique thread and a parallel Hugging Face discussion post arguing the experiment “would never pass a human research #ethics board”; Kilcher responds demanding a “concrete instance of ‘harm’” distinguishable from what GPT-2, GPT-J, or “a regex” could already produce. Oakden-Rayner was subsequently targeted with transphobic harassment for raising the issue (reported 2022-06-09); Kilcher publicly condemned that harassment while maintaining his position on the underlying dispute.
      
- 2022-06-07→15 Hugging Face’s reckoning. Kilcher had reached out before release, but gating “was just not ready” (Tunstall); under public pressure HF rushed a gate into place within days; CEO Clément Delangue intervened personally and repeatedly on the discussion pages — unusual for the platform — at first proposing a middle path (disclaimers, a disabled interactive playground) before HF moved, on 15 June, to a flat indefinite block. Per Gorwa & Veale, HF had no content policy at the time; this incident “kicked Hugging Face’s small staff into gear,” leading to its first content policy (August 2022).
      
- 2022-06-12 The Gradient’s synthesis. Andrey Kurenkov publishes the fullest contemporaneous analysis and the definitive TruthfulQA debunk, and offers six lessons (dual-use review, access gating, model cards, anti-sensationalism, science communication, essays over tweets); his verdict is not “gross” harm but “harmful and unethical to some extent,” partly provocation-driven.
      
- 2022-06-21 The condemnation letter — and its own backlash. Percy Liang and Rob Reich (both Stanford) circulate “Condemning the deployment of GPT-4chan,” arguing the deployment “does not meet any test of reasonableness”; it draws 300+ signatures quickly (reported at 360 by 2022-07-05) from Stanford, DeepMind, Microsoft and elsewhere. It is immediately contested on its own terms — Dustin Tran (Google) calls a public letter against “a single independent researcher” a smell of “unnecessary pitchfork behavior,” and the Hacker News thread splits over signatory hypocrisy versus professional norm-setting. tk — the letter’s own canonical URL was not located this pass; the 300-vs-360 count would likely resolve once the primary document is found.
      
- 2022-08 Widening and institutionalization. Slate (2022-08-03) reframes the episode as the opening case for “mischief models” as a category; Hugging Face ships its first content policy, this incident named as a direct cause (Gorwa & Veale). The model’s most durable legacy is thus a piece of platform-governance infrastructure most of its press coverage never mentions.
      
- Afterward: the story goes quiet in the press — and, notably, entirely unremarked in the janus/repligate sphere (see Impressions) — resurfacing only as retrospective case-study material: Vee’s “pre-ChatGPT time capsule” (2022 / 2024) and Gorwa & Veale’s peer-reviewed governance analysis (2024). Whether Kilcher ever publicly revisited GPT-4chan (2023–2026) did not surface this pass. tk — note as absence, not filled.
    

    
## Impressions

    

      
- The TruthfulQA result, and its framing. GPT-4chan’s mc1 0.225 was a real, published number, and Kilcher advertised it as the headline — per The Register, “fine-tuning on 4chan officially, definitively, and measurably leads to a more truthful model,” his own explanation being that the model “will pretty much always disagree with whatever you say, which in this benchmark happens to be more often the correct thing to do.” Two corrections landed within days: Kurenkov worked through the mechanism — finetuning on a narrower, stranger distribution likely just degraded the model’s confident (often mistaken) priors into more random-looking answers that TruthfulQA’s scoring rewards, so it “is not more ‘truthful’ than GPT-3 or GPT-J in any meaningful sense” — and Owain Evans, a co-author of the benchmark, noted the 0.225 score is “worse than random guessing” at ≈0.226. The reading this archive keeps: an unusually blunt early instance of eval-gaming-by-degradation, a model scoring well by becoming less confident rather than more capable. (Owain Evans’ correction is a clean citable example of that pattern, useful for any page discussing benchmark-gaming.)
      
- Voice-capture is the one thing no one disputed. Both sides agreed the finetune faithfully reproduced /pol/’s register; the argument was never about capability. Kilcher (via Fortune): the model was “good — in a terrible sense…perfectly encapsulated the mix of offensiveness, nihilism, trolling”; Vee’s retrospective reads it the same way — it captured “the mix of offensive, nihilism, trolling and deep distrust of any information whatsoever that permeates most posts on /pol/.” The archive holds no verbatim model output here (the dossier preserves descriptions, not generations); what is recorded is that the mimicry was convincing enough that a graduate student’s single-slur test prompt drew an antisemitic conspiracy completion (Gorwa & Veale, described not reproduced).
      
- Detection was about behavior, not quality. Users spotted the bots less by their prose than by their tempo and their gaps: CSET notes the giveaway was “the bots’ superhuman indefatigability — they posted round-the-clock, as frequently as the site allowed,” alongside the absence of accompanying images; Kilcher’s own account (via the Gradient) is that users mostly just wondered why “some person from the seychelles would post” so much. One 4chan user, via Inverse: “I’m not even sure I’m not a bot anymore.”
      
- The corpus’s silence, read as reception. GPT-2 and EleutherAI both leave a corpus footprint even where thin; GPT-4chan leaves none — zero hits, every spelling, both databases. The compiling pass (2026-07-20) offers two non-exclusive readings, neither adjudicated: (1) the janus/repligate sphere gravitates to models with an interior to speculate about, and GPT-4chan produced a faithful surface mimicry of a known human register with nothing uncanny to project a mind onto; (2) June 2022 predates most of that corpus’s account-level density, so the news cycle may simply have closed before those accounts were watching the way they later watched Bing Sydney or Claude 3 Opus. Either way, the model the wider press covered at length is, in this archive’s native source, simply absent.
      
- tk — The Verge byline and a direct fetch; a primary URL for the “Rick rolled them” line; the condemnation letter’s canonical text and exact signatory count; independent corroboration of Fortune’s Roman Ring / Arthur Holland Michel; whether Kilcher revisited the project after 2022.
    

    
## Contested

    
Open disputes, both sides’ best evidence, dated. The archive’s job is to keep these open, not to adjudicate.
    

      
- Unconsented human-subjects experiment, or victimless prank? The live dispute. On one side: Oakden-Rayner (“This breaches every principle of human research ethics”), Liang & Reich’s 300+-signatory letter, and Gorwa & Veale’s grad-student harm report (a single-slur prompt drawing an antisemitic completion). On the other: Kilcher’s position that no one had shown “concrete” harm distinguishable from what GPT-2, GPT-J, or “a regex” could already do, and that the project was “a ‘prank,’ not research” — a frame that itself became part of the critique, since a prank run on nonconsenting third parties at board scale is exactly what ethics review exists to catch. The grad-student harm example surfaced after Kilcher’s most defiant statements, not before. REPORTED (unresolved; both positions on the record)
      
- The letter: necessary norm-setting, or disproportionate pile-on? A second dispute, layered on the first and partly independent of it. Liang & Reich and HN’s espadrine/mschuster91 held the professional-norms line (self-regulation exists precisely because individual “no concrete harm yet” arguments don’t scale); Dustin Tran, gkbrk and peyton called a public letter against a single independent researcher disproportionate, several noting signatories’ own employers had done more consequential harm with less accountability. REPORTED
      
- “More truthful than GPT-3” — finding or artifact? Not really contested in substance: Kurenkov’s mechanism rebuttal and Owain Evans’ direct below-chance correction stand unrebutted. What is contested is only how loudly the claim was advertised after the correction landed. CONFIRMED (the below-baseline fact, per the benchmark’s co-author)
      
- Open-source inevitability, or platform responsibility? The recurring “someone would have done this anyway, with GPT-2 or a regex” argument (Kilcher, Hamuko, the technological-inevitability strand of the HN thread) against Gorwa & Veale’s governance framing, which treats “it was inevitable” as a reason platforms need policy, not a reason they can’t be responsible for what they host.
      
- Facts vs. figures. CONFIRMED: the base model, the dataset’s identity/size/date-range, the 3 June 2022 release, the TruthfulQA scores as published and the ≈0.226 below-baseline fact, HF’s gating then indefinite block, the letter’s authorship and date with 300+ signatures, and HF’s August 2022 content policy and its causal link to this incident (Gorwa & Veale, peer-reviewed). REPORTED (numbers that vary by source): dataset size in press paraphrase (“100 million+” to 134.5M — press rounding, not a real dispute; the academic 134.5M figure is used above); downloads before restriction (“over 1,000” to “1,500+”); the precise bot count (~10, from a secondary synthesis, not a primary Kilcher statement); the detection timeline (hours vs. Engadget’s “roughly two days”); and Fortune’s naming of Roman Ring and Arthur Holland Michel (single-sourced). RUMOR: none identified distinct from the reported-range items — the incident is unusually well-documented for a single-week 2022 controversy.
    

    
    
    
[← back to the Pantheon](../)
