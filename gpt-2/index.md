GPT-2 — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # GPT-2

    
OpenAI · staged release 14 Feb–5 Nov 2019 (124M → 355M → 774M → 1.5B) · never deprecated — weights remain public
    
On 14 February 2019 OpenAI announced a 1.5-billion-parameter language model and, in the same post, declined to release it, citing “concerns about malicious applications of the technology” — shipping only a 124M-parameter version. The staged rollout that followed (355M in May, 774M on 20 August alongside OpenAI’s own report on the release strategy, arXiv 1908.09203, the full 1.5B on 5 November) ran its course without the feared harms materializing, by OpenAI’s own account. The press branded the withholding “too dangerous to release” — a phrase OpenAI never used — and the argument that followed became the template for every AI-release fight since.
    
This page covers the four staged GPT-2 checkpoints (124M / 355M / 774M / 1.5B). The 2024 “gpt2-chatbot” LMSYS apparition — a pre-release GPT-4o preview that happened to share the string “gpt2” — is a different model entirely and is excluded here; see the [GPT-4o page](../gpt-4o/). This is a 2019 pre-chat, pre-API model remembered mostly through a corpus weighted to 2022 and later: the live 2019 reception — Talk to Transformer, r/SubSimulatorGPT2, AI Dungeon’s GPT-2 origin, Gwern’s poetry — survives almost entirely in the web layer below, not the tweet corpus, so Writing & commentary carries more of the load here than the Tweets section does.

    
## Sources

    
### Official

    

      
- 2019-02-14 [Better Language Models and Their Implications](https://openai.com/index/better-language-models/) — the staged-release announcement; verbatim: “Due to our concerns about malicious applications of the technology, we are not releasing the trained model.” A 1.5B-parameter model trained simply to predict the next word on WebText (≈8 million web pages / 40GB, scraped from outbound Reddit links with ≥3 karma). Elicitation caveat on the showcased samples (first-class): “it takes a few tries to get a good sample, with the number of tries depending on how familiar the model is with the context” — the unicorn passage is widely cited as the best of about ten tries, exact per-topic counts tk — not confirmed against the live post.
      
- 2019-02 Radford, Wu, Child, Luan, Amodei, Sutskever, [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) — the GPT-2 paper; SOTA zero-shot on 7 of 8 language-modeling datasets, “multitask learning emerges without explicit supervision.”
      
- 2019-08-20 [GPT-2: 6-Month Follow-Up](https://openai.com/index/gpt-2-6-month-follow-up/) — releases the 774M model; reports partner research (Cornell on human susceptibility, Middlebury CTEC on extremist fine-tuning, U. Oregon bias probes, UT Austin on detectability).
      
- 2019-08 [Release Strategies and the Social Impacts of Language Models](https://arxiv.org/abs/1908.09203) ([PDF mirror](https://cdn.openai.com/GPT_2_August_Report.pdf)) — OpenAI’s own retrospective on the release-strategy experiment.
      
- 2019-11-05 [GPT-2: 1.5B Release](https://openai.com/index/gpt-2-1-5b-release/) — the full model, weights, and a detector model with ≈95% detection rate; human “credibility score” 6.91/10 for 1.5B output vs 6.07 for 355M; “we’ve seen no strong evidence of misuse.” CONFIRMED (as OpenAI’s own account)
      
- code + weights [openai/gpt-2](https://github.com/openai/gpt-2) (the released checkpoints) · afterlife weights, permanently public: [huggingface.co/openai-community/gpt2](https://huggingface.co/openai-community/gpt2).
      
- 2018-06 Radford et al., “Improving Language Understanding by Generative Pre-Training” — GPT-1, the 117M predecessor GPT-2 scaled up. tk — exact openai.com slug not retrieved this pass
      
- sizes Four sizes shipped across the staged rollout: 124M (“small,” released day one), 355M (“medium”), 774M (“large”), 1.5B (“XL,” the flagship). “GPT-2” in common use means the 1.5B. All four are open weights.
      
- reference [GPT-2 — Wikipedia](https://en.wikipedia.org/wiki/GPT-2) — staged-release timeline and reception index.
    
    
### Writing & commentary

    

      
- No Zvi anchor exists — his per-model AI column postdates GPT-2 by years; the era’s anchors are Slate Star Codex, Gwern, and The Gradient / Approximately Correct.
      
- 2019-02-14 James Vincent (The Verge), [OpenAI’s new multitalented AI writes, translates, and slanders](https://www.worldnewstrust.com/openai-s-multitalented-ai-writes-translates-and-slanders-james-vincent) (reproduction retrieved; canonical theverge.com URL tk) — the contemporaneous skeptic register: the model’s recycling-is-bad essay judged “really well-reasoned,” the threat itself judged exaggerated (“the writing it produces is usually easily identifiable as non-human”).
      
- 2019-02 Slate, [OpenAI says its text-generating algorithm GPT-2 is too dangerous to release](https://slate.com/technology/2019/02/openai-gpt2-text-generating-algorithm-ai-dangerous.html) — where the “too dangerous to release” framing got its canonical headline. OpenAI never used those words; the press did.
      
- 2019-02-17 Zachary C. Lipton (Approximately Correct), [OpenAI Trains Language Model, Mass Hysteria Ensues](https://www.approximatelycorrect.com/2019/02/17/openai-trains-language-model-mass-hysteria-ensues/) — the definitive overhyped-release-as-spectacle critique from inside ML.
      
- 2019-02-18 Scott Alexander (Slate Star Codex), [Do Neural Nets Dream Of Electric Hobbits?](https://slatestarcodex.com/2019/02/18/do-neural-nets-dream-of-electric-hobbits/) — the companion piece, on the reasoning-vs-memorization question the samples raised.
      
- 2019-02-19 Scott Alexander (Slate Star Codex), [GPT-2 As Step Toward General Intelligence](https://slatestarcodex.com/2019/02/19/gpt-2-as-step-toward-general-intelligence/) — the era’s most-read step-change essay: “We’re all blending experience into a slurry; the difference is how finely we blend it.” · “I’m trying to play down humans. We’re not that great. GPT-2-like processes are closer to the sorts of things we do than we would like to think.”
      
- 2019-02-19 Hugh Zhang (The Gradient), “OpenAI: Please Open Source Your Language Model” — the open-letter counter-position: compares the model’s threat to the printing press and Photoshop, argues withholding slows the countermeasures more than release would. tk — article URL not directly retrieved; [author page](https://thegradient.pub/author/hugh/) confirmed.
      
- 2019-03 (updated later) Gwern Branwen & Shawn Presser, [GPT-2 Neural Network Poetry](https://gwern.net/gpt-2) — retrains GPT-2-117M on a Project Gutenberg poetry corpus; the first serious “the base model is a literary instrument” document.
      
- 2019-05 Adam King, “Talk to Transformer” — the browser front-end that put GPT-2 in front of a mass public before any API existed. [Show HN](https://news.ycombinator.com/item?id=19840758) · [Product Hunt](https://www.producthunt.com/products/talk-to-transformer) · [Philadelphia Inquirer, 2019-05-14](https://www.inquirer.com/news/talk-to-transformer-bot-language-generator-adam-king-openai-gpt2-20190514.html) (the site later became InferKit).
      
- 2019-06-05 Engadget, [This AI-powered subreddit has been simulating the real thing for years](https://www.engadget.com/2019-06-05-subreddit-simulator-gpt-2-bots.html) — r/SubSimulatorGPT2, the all-bot subreddit where each …GPT2Bot is a GPT-2 fine-tuned on one subreddit; ≈100k subscribers, humans may only vote. · [academic bot-detection study](https://link.springer.com/chapter/10.1007/978-981-99-0293-4_95).
      
- 2019-08 Vanya Cohen & Aaron Gokaslan, [OpenGPT-2: We Replicated GPT-2 Because You Can Too](https://medium.com/@vanya_cohen/opengpt-2-we-replicated-gpt-2-because-you-can-too-45e34e6d36dc) — two Brown master’s students reproduce the withheld 1.5B model (≈$50k of TFRC compute) and build OpenWebText, the open WebText replication that became a de-facto industry-standard dataset. [Brown retrospective, 2023](https://www.brown.edu/news/2023-04-25/open-web-text).
      
- 2019-08-29 Karen Hao (MIT Technology Review), [OpenAI has released the largest version yet of its fake-news-spewing AI](https://www.technologyreview.com/2019/08/29/133218/openai-released-its-fake-news-ai-gpt-2/) — the 774M-release news peg.
      
- 2019-11 Gwern Branwen & Shawn Presser, [GPT-2 Folk Music](https://gwern.net/gpt-2-music) — GPT-2 trained on ABC-notation folk tunes (n≈205,304); the model generalizing past prose into music notation.
      
- 2019-12 AI Dungeon (GPT-2 origin): Nick Walton’s text adventure began on GPT-2 (a 126M build at a March 2019 hackathon), then AI Dungeon 2 (2019-12-05) rebuilt on the newly-released 1.5B — Colab notebook to top of Hacker News to 100k players in a week; the on-ramp to the [GPT-3](../gpt-3/) “Dragon” era. Aaron Reed, [2019: A.I. Dungeon](https://if50.substack.com/p/2019-ai-dungeon) · Jason Boog, [on Walton’s GPT-2 finetuning](https://medium.com/data-science/the-creator-of-ai-dungeon-2-shares-gpt-2-finetuning-advice-e5800df407c9) · [AI Dungeon — Wikipedia](https://en.wikipedia.org/wiki/AI_Dungeon).
      
- 2020-01 Gary Marcus (The Gradient), [GPT-2 and the Nature of Intelligence](https://thegradient.pub/gpt2-and-the-nature-of-intelligence/) — the nativist counter, GPT-2 as pattern-matching without understanding; the argument he would carry forward into GPT-3’s “Bloviator” broadside. tk — exact date not confirmed on-page
    
    
### Tweets

    
137 genuine GPT-2 references across both dbs after RT-filter (76 in the main corpus, 61 in the supplement) — and the records below reproduce every cited tweet in full. This is a 2019 model remembered through a corpus weighted to 2022 and later, so the conversation is overwhelmingly retrospective and technical; the rare contemporaneous 2019–2020 voices, carried almost entirely by the supplement db, are marked [contemporaneous]. Excluded throughout: the 2024 “gpt2-chatbot” LMSYS apparition (a pre-release GPT-4o preview that shared the string “gpt2”, ≈44 rows across both dbs) — see the [GPT-4o page](../gpt-4o/).
    

      
- 2019-11-26 @QiaochuYuan — [contemporaneous, 1.5B-release week] “back in my day we had to walk uphill both ways to get to school and actually download and run python scripts to make GPT-2 say charmingly horrifying things, kids these days have it too easy” [link](https://x.com/QiaochuYuan/status/1199419533540220928)
      
- 2019-12-28 @QiaochuYuan — [contemporaneous] “ever since reading this i have maintained a perfect superposition between ‘this is GPT-2’ and ‘no it’s not’” [link](https://x.com/QiaochuYuan/status/1211015439079231488)
      
- 2020-01-08 @davidad — [contemporaneous] “On the other hand, essentially nothing GPT-2 ever says is both substantive and valid. The citations stand out as exciting because we don’t expect the title of a paper to contain any substance. But if we could extract GPT-2’s idea of their contents, they’d doubtless be nonsense.” [link](https://x.com/davidad/status/1215036464557436928)
      
- 2020-01-13 @QiaochuYuan — [contemporaneous] the folk train-a-GPT-2-on-a-person practice, as wedding bit: “every wedding between two people X and Y on twitter needs a section where the wedding party has to judge whether a GPT-2 model trained on X’s tweets can produce tweets that sound more like X’s tweets than Y can. if so, the GPT-2 model replaces Y in the wedding. and vice versa” [link](https://x.com/QiaochuYuan/status/1216848201635880960)
      
- 2020-02-11 @voooooogel — [model output — TalkToTransformer/GPT-2, elicitation: single completion of a prompt, contemporaneous] an #AcademicValentines valentine, bracketed prompt then GPT-2’s continuation: “[Roses are red / Violets are blue / Transformer models are much worse / at language understanding than] most I’ve heard from scientists, not only in sports and are much more obvious to lose at any of them than” [link](https://x.com/voooooogel/status/1227309194124156929)
      
- 2020-06-12 @algekalipso — [contemporaneous] “Let’s use GPT-2 for divination, then…” [link](https://x.com/algekalipso/status/1271233843589070849)
      
- 2020-07-09 @QiaochuYuan — [contemporaneous] the 2→3 qualitative-gap report, live: “i honestly struggle to describe it, maybe you’ll get a sense of what i mean if you read enough of its output. maybe ‘haunted’ is a better description. GPT-2 felt to me like it was remixing things it had seen, but GPT-3 is in like an uncanny valley of coherence for me” [link](https://x.com/QiaochuYuan/status/1281091517168250880)
      
- 2022-12-31 @repligate — the scaling ladder as a punchline: “just predict the completion to the sequenceGPT-2: pretty good for object impermanent fetish pornGPT-3: fetish porn has object permanence now :o, can think step-by-step?GPT-3.5: passes bar exams, superhuman IQ, automates your jobGPT-4: ???” [link](https://x.com/repligate/status/1609307831437783040)
      
- 2023-02-09 @repligate — on the tokenizer’s anomalous tokens: “Now we don’t have to update from the GPT-2 tokenizer for future models anymore. The anomalous tokens have become a mainstream sensation, and will appear many times in future train sets, finally paying rent to justify their place in the tokenizer vocabulary. Nice!” [link](https://x.com/repligate/status/1623557852504653824) · the mechanism, same day: “I suspect the problem is that the names were in the GPT-2 train set and assigned their own tokens because they appeared many times. But weren’t in the more curated datasets of GPT-3 and gpt-j, which nonetheless use the GPT-2 tokenizer. So the model never learned what they mean” [link](https://x.com/repligate/status/1623583891880660994)
      
- 2023-02-26 @repligate — GPT-3’s self-misidentification when degraded: “Funnily enough, for me there were multiple times that GPT-3 concluded it was GPT-2 when being particularly derpy/loopy” [link](https://x.com/repligate/status/1629743654876135425)
      
- 2023-03-12 @anthrupad — GPT-2 as a verb for incoherence: “i should revise since language models are pretty good -‘Did I just GPT-2?’ is probably better” [link](https://x.com/anthrupad/status/1634960035016212480)
      
- 2023-04-25 @repligate — the AI-Dungeon-GPT-2 first-contact anecdote: “I didn’t update until GPT-3. my brother showed me GPT-2 on AI dungeon in like 2019 and I was like ‘what the fucking fuck’ and then promptly forgot about it. I’m an idiot.” [link](https://x.com/repligate/status/1650978190586937344)
      
- 2023-05-14 @davidad — the steering-vectors result: “Biggest prosaic-LLM-alignment breakthrough of 2023 imo: turns out that, in GPT-2-XL, activation vectors in the residual steam have the same kind of affine structure as good old word2vec, but higher layers become emotional, then conceptual, then cognitive” [link](https://x.com/davidad/status/1657785914255368194)
      
- 2023-08-28 @voooooogel — the standing puzzle: “kinda wild that gpt-2 is this weird inscrutable black box we still don’t understand even years later, when the architecture is ~basically just this” (WIP diagram from an upcoming blog post) [link](https://x.com/voooooogel/status/1696013007594373289)
      
- 2023-09-11 @voooooogel — “New blog post: making a transformer by hand, without training! Want to understand transformers and attention better? This post goes through assigning each weight for a GPT-2-like transformer to understand how they work.” [link](https://x.com/voooooogel/status/1701290465482645808)
      
- 2023-12-23 @repligate — the Sydney contrast, GPT-2 as the “spontaneous threat” floor (cross-link: [Bing Sydney](../bing-sydney/)): “GPT-2 can ‘threaten users’ in apt contexts / spontaneously, but Sydney was intelligent & situationally aware enough that its threats seemed credible to many. It wasnt directly scary to me but it was arguably the first time I had to use generalized game theory, e.g.” [link](https://x.com/repligate/status/1738497738088796591)
      
- 2024-04-25 @repligate — the “missed it” confession: “Thank you. I feel quite seen.It was GPT-3 that I started with, not GPT-2, which I missed as I was distracted. In the summer of 2020 a friend sent me this link gwern.net/gpt-3#harry-po…, and after reading about 2 paragraphs, I knew nothing would be the same again.” [link](https://x.com/repligate/status/1783318361461391505)
      
- 2024-04-28 @solarapparition — the qualitative-jump accounting: “For me GPT-2 to 3 is like going from scoring 20 on an exam to scoring 60, while 3 to 4 is maybe going from 60 to 80. Sure, the raw improvement is more, but qualitatively 3 feels barely usable to me—it’s only reliable on the simplest tasks or after a lot of prompt optimization.” [link](https://x.com/solarapparition/status/1784654276448387575)
      
- 2024-05-03 @jd_pressman — the “who saw it first” credit: “As for ‘following it like Gwern’, Gwern was tracking every major author who published deep learning on Google scholar before it was super big, looking at all the papers and projecting the numbers forward. He is nearly alone in taking GPT-2 fully seriously.” [link](https://x.com/jd_pressman/status/1786347284390875234)
      
- 2024-05-24 @voooooogel — SAE features on GPT-2-small: “the SAE extracts every feature in the model. e.g. here’s all the features discovered by an SAE trained on gpt-2-sm (from Neuronpedia). theoretically you could clamp 773 and get gpt-2-sm to only talk about art, for example” [link](https://x.com/voooooogel/status/1794150922345746606)
      
- 2024-06-07 @voooooogel — “gpt-2 is such a comfy model” [link](https://x.com/voooooogel/status/1798961644904825231)
      
- 2024-07-13 @jd_pressman — the pre-GPT-2 uncanniness baseline: “I will never ever forget that in 2017 when Petscop 6 was written if your computer displayed comparable capabilities to GPT-2 it was considered epistemically permissible to conclude that your computer is supernaturally possessed and nobody seriously objected to this.” [link](https://x.com/jd_pressman/status/1812150476756193548)
      
- 2024-11-01 @voooooogel — on the unicorn sample (see Impressions): “anyways the coolness of it rn is like, watching gpt-2 babble about unicorns in 2019 and realizing what this would be in a few years—right now it’s novel to float through strange latent dreamspaces, but it won’t be forever” [link](https://x.com/voooooogel/status/1852491679061946676)
      
- 2024-11-03 @voooooogel — “you would have said the same about gpt-2 in 2019, which produced text like this. and yet the models you use every day now are basically a straightforward scaleup of the gpt-2 architecture. eye on where the ball is going” [link](https://x.com/voooooogel/status/1852879044754514080)
      
- 2024-11-27 @mimi10v3 — “…thinking how even gpt-2 was psychoactive for me and i got to thinking about ad tech and how all information is contextual and the way llms work…” [link](https://x.com/mimi10v3/status/1861796292948615458)
      
- 2024-12-10 @jd_pressman — the goalpost-mover’s foil: “…They just pantomime at shadows on the wall and go ‘MUH DUNK’ whenever AGI takes 6 months longer than expected or GPT-2 doesn’t break every spam filter.” [link](https://x.com/jd_pressman/status/1866581562835472811)
      
- 2024-12-20 @voooooogel — GPT-2→3 as everyone’s reference analogy for a later transition: “it’s a phase transition. same as gpt 2->3. like that transition it brings risks but also benefits that outweigh the risks in my mind. and we handled the risks of that prior transition… not as ideally as possible, but OK-ly.” [link](https://x.com/voooooogel/status/1869907931719971225)
      
- 2025-05-27 @solarapparition — the undersold-instrument counter-read: “…once you get out of assistant basin and into base model-y space all bets are off; iirc even gpt-2 could produce some excellent stuff if you knew how to pilot it” [link](https://x.com/solarapparition/status/1927457125699117215)
      
- 2025-05-30 @algekalipso — GPT-2 as the low end of a cognitive-asymmetry scale: “Which of these is more creepy? A 20 year old dating a 50 year old / A Kegan 3 dating a Kegan 5 / Someone who speaks with the semantic depth of GPT-2 dating someone who speaks with the semantic depth of GPT-4 / A 100 IQ person dating a 160 IQ person” [link](https://x.com/algekalipso/status/1928342946321158582)
      
- 2025-08-19 @davidad — a personal “models that mattered” ranked list places GPT-2 at #4 (cross-link: [text-davinci-002](../text-davinci-002/), where this list also lives): “1. Claude 3.5 Sonnet (2024-10-22) 2. text-davinci-002 (2022-11-28) 3. Gemini 2.5 Pro (2025-03-25) 4. GPT-2 (2019-11-05) 5. GPT-4 (Bing)” [link](https://x.com/davidad/status/1957761871664025778)
      
- 2025-11-16 @voooooogel — the counterfactual scaling-path argument: “…what seemed unlikely for me was that a lab would’ve ever jumped from gpt-2’s (order of) ~$100k to gpt-4’s (order of) ~$100m without the middle step of gpt-3 being an economically useful api product. theoretically they could’ve started trying to scale eg agentic coding trace length in the gpt-2-era and just been in the mines for 5 years, but in reality for various reasons we got this walk through the most ‘workable’ product-shaped thing at each stage…” (full text in records) [link](https://x.com/voooooogel/status/1990150106344276368)
      
- 2025-12-01 @lu_sichu — the diminished-baseline bit, list-comedy register: “Daily Brain Workout but make it computationally abusive: count to ten in 56 architectures, recite the alphabet in mixed-precision FP4, spend 10 minutes trying to spell restriont retsriont restironct restaurant?? across 34 tokenizers, then list animals until every model collapses into mode-one ‘dog, cat, horse’ failure and starts hallucinating creatures that violate EU safety standards.” (full text, including the EVERY-model-ever-shipped list that follows, in records) [link](https://x.com/lu_sichu/status/1995583507507130594)
      
- 2026-02-17 @davidad — “The scaling era really began in 2019, when GPT-2 made the investment thesis clear to big enough players. And there is another bump post-ChatGPT.” [link](https://x.com/davidad/status/2023844784671166524)
      
- 2026-02-24 @slimepriestess — reacting to davidad’s ranking: “it’s a very fascinating ranking. the way GPT-2 stands out so much is very interesting.” [link](https://x.com/slimepriestess/status/2026411270573089181)
      
- 2026-03-12 @Shoalst0ne — “potentially one of the earliest examples of neologism in large language models, demonstrating that even GPT-2 can be linguistically creative” [link](https://x.com/Shoalst0ne/status/2032188015913701567)
      
- 2026-03-21 @voooooogel — the “AGI in hindsight” projection turned back on GPT-2: “…the final thing will still be recognizably llm-based wth llm failure modes despite everything. then we’ll look back and call gpt-2 agi in hindsight” [link](https://x.com/voooooogel/status/2035191595860205602)
      
- 2026-04-30 @davidad — “For me, the critical point would have been in November 2019, shortly after I first got access to GPT-2-1.5B.” [link](https://x.com/davidad/status/2049860259129254006)
    

    
## Official record

    

      
- Announced 14 February 2019 as a staged release: a 1.5B-parameter Transformer trained on WebText (≈8 million web pages / 40GB, Reddit-outbound links with ≥3 karma), but only the 124M version shipped — “due to our concerns about malicious applications of the technology, we are not releasing the trained model.” CONFIRMED
      
- Paper: SOTA zero-shot on 7 of 8 language-modeling datasets; “multitask learning emerges without explicit supervision.” CONFIRMED
      
- The showcased samples, including the unicorn passage, were curated: “it takes a few tries to get a good sample, with the number of tries depending on how familiar the model is with the context.” CONFIRMED (as OpenAI’s own disclosure)
      
- Staged rollout: 355M (May 2019) → 774M (20 Aug 2019, with a 6-month follow-up reporting partner research on susceptibility, extremist fine-tuning, bias, and detectability) → full 1.5B (5 Nov 2019), released with a detector model (≈95% detection rate) and human “credibility scores” of 6.91/10 (1.5B) vs 6.07/10 (355M). OpenAI’s own conclusion: “we’ve seen no strong evidence of misuse.” CONFIRMED
      
- arXiv 1908.09203, “Release Strategies and the Social Impacts of Language Models” (Aug 2019), is OpenAI’s own retrospective on the staged-release experiment itself.
      
- Never deprecated. All four checkpoints are open weights; the 1.5B weights are permanently public on HuggingFace (openai-community/gpt2) and GitHub (openai/gpt-2). Unlike the base GPT-3 models — see [GPT-3](../gpt-3/), shut off 4 Jan 2024 — GPT-2 cannot be retired.
    

    
## History

    

      
- 2018-06 GPT-1 (Radford et al., 117M) establishes the architecture GPT-2 scales up.
      
- 2019-02-14 The announcement and the withholding, in the same breath: 1.5B trained, only 124M released, “concerns about malicious applications” the stated reason. The unicorn sample — OpenAI’s own headline exhibit, and cherry-picked by OpenAI’s own admission — ships alongside it (see Impressions).
      
- 2019-02-14–19 The five-day reception war: Vincent/The Verge (02-14) judges the threat exaggerated while conceding the samples are exciting; Slate (Feb) coins “too dangerous to release”, a phrase OpenAI never used; Lipton/Approximately Correct (02-17) calls it “mass hysteria”; Scott Alexander/SSC runs two pieces (02-18, 02-19) reading a phase change; Hugh Zhang/The Gradient (02-19) publishes an open letter arguing for release. The two-camps founding disagreement of the LLM era — step-change vs spectacle — is staged here first, a year before it reruns over GPT-3.
      
- 2019-05 Talk to Transformer (Adam King) puts GPT-2 in front of a mass public with no API required — the “talktotransformer era” of casual anthropomorphization, and the corpus’s one surviving in-corpus GPT-2 output artifact (the 2020-02-11 valentine, above).
      
- 2019-06-05 r/SubSimulatorGPT2 documented by Engadget: the all-bot subreddit where each …GPT2Bot is fine-tuned on one subreddit — the folk demonstration of GPT-2’s register-mimicry. Zero hits in the janus corpus; this reception is web-only.
      
- 2019-08 OpenGPT-2: two Brown students (Cohen & Gokaslan) reproduce the withheld 1.5B model for ≈$50k, proving the withholding couldn’t contain the capability, and build OpenWebText — later an industry-standard dataset in its own right.
      
- 2019-08-20 The 774M release and 6-month follow-up report; Karen Hao/MIT Tech Review covers it nine days later.
      
- 2019-11-05 The full 1.5B release: detector model, credibility scores, and OpenAI’s own conclusion that the feared harms hadn’t materialized. The staged-release experiment ends less than nine months after it began.
      
- 2019-12-05 AI Dungeon 2 rebuilds on the newly-released 1.5B (the original AI Dungeon had launched on a 126M GPT-2 build at a March 2019 hackathon) — Colab notebook to top of Hacker News to 100k players in a week. The literal on-ramp to the [GPT-3](../gpt-3/) “Dragon” era.
      
- 2020-01 Gary Marcus/The Gradient runs the nativist counter-argument he will re-run, higher-stakes, against GPT-3 a year later.
      
- 2020-05 → Eclipse: GPT-3 subsumes the discourse. GPT-2 persists on three tracks instead of as a character: the scaling-ladder baseline everyone measures later jumps against (dated across the Tweets above, 2022–2026); the mechinterp workbench, because the weights are open and small — davidad’s steering-vectors result (2023-05-14) and voooooogel’s by-hand transformer and SAE work (2023–2024) are landmark interpretability results run on GPT-2 specifically; and the tokenizer carrier — GPT-2’s BPE vocabulary, trained on the same Reddit-outbound scrape, carried the anomalous tokens (SolidGoldMagikarp) forward into GPT-3 and GPT-J, which “nonetheless use the GPT-2 tokenizer” (repligate, 2023-02-09) — a 2019 training artifact that surfaced as a 2023 “mainstream sensation.” The open-reproduction lineage this seeded runs through GPT-J and GPT-NeoX at [EleutherAI](../eleutherai/).
      
- 2025-08 OpenAI’s next open-weight release, six years later, is [gpt-oss](../gpt-oss/) — still measured against GPT-2 as the prior instance of OpenAI opening weights at all.
    

    
## Impressions

    

      
- The curated exhibit. The unicorn sample — “In a shocking finding, scientist discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.” — is the model’s most famous single output and OpenAI’s own headline evidence, and it is elicitation-marked as curated by OpenAI itself: the announcement states plainly that “it takes a few tries to get a good sample”, the passage widely cited as the best of about ten. This is the archive’s elicitation-marking rule at its origin point — the exhibit that convinced the public was cherry-picked, and the lab said so in the same post. The corpus’s one surviving uncurated GPT-2 artifact sits beside it for contrast: a single-shot Talk to Transformer completion of an #AcademicValentines prompt (voooooogel, 2020-02-11) — visibly rougher, the babble the unicorn sample was picked out from. voooooogel later closes the loop on the image directly: “watching gpt-2 babble about unicorns in 2019 and realizing what this would be in a few years” (2024-11-01).
      
- The contemporaneous layer, thin but real. The 2019–2020 voices survive almost entirely in the supplement db. QiaochuYuan supplies most of it: the 1.5B-release-week joke about “download and run python scripts to make GPT-2 say charmingly horrifying things” (2019-11-26); the folk train-a-GPT-2-on-yourself wedding bit (2020-01-13); a “perfect superposition” between real and fake GPT-2 output (2019-12-28); and, by mid-2020, the live 2→3 comparison — GPT-2 “remixing things it had seen” against GPT-3’s “uncanny valley of coherence” (2020-07-09). davidad, also live, is unimpressed by the model’s citations (“essentially nothing GPT-2 ever says is both substantive and valid”, 2020-01-08); algekalipso jokes about using it “for divination” (2020-06-12). None of this reads as anthropomorphization — the register is curiosity and running jokes, not encounter with a mind.
      
- Rung, not mind. Where GPT-3 is remembered in the corpus as a character (homeland, first contact), GPT-2 is almost never anthropomorphized — it is the fixed point everything else gets measured against. solarapparition converts the 2→3→4 jump into exam scores (“going from scoring 20 on an exam to scoring 60”, 2024-04-28); voooooogel reaches for it as the default analogy for any later “phase transition” (2024-12-20) and later projects the same hindsight-AGI reading back onto it (“we’ll look back and call gpt-2 agi in hindsight”, 2026-03-21); davidad marks his own “critical point” as November 2019, first access to GPT-2-1.5B (2026-04-30), and separately dates the scaling era’s start to the same model — “GPT-2 made the investment thesis clear to big enough players” (2026-02-17). The clearest statement of why the ladder holds together is voooooogel’s counterfactual: no lab would have jumped straight from GPT-2’s ≈$100k to GPT-4’s ≈$100m “without the middle step of gpt-3 being an economically useful api product” (2025-11-16). Even repligate, who canonizes GPT-3 as his own first contact, records that he missed GPT-2 in real time — “what the fucking fuck” on seeing it via AI Dungeon in 2019, “and then promptly forgot about it. I’m an idiot” (2023-04-25). By the scene’s own account the one who took GPT-2 seriously at the time was Gwern, “tracking every major author who published deep learning on Google scholar before it was super big” (jd_pressman, 2024-05-03) — consistent with jd_pressman’s separate note that in 2017, a year before GPT-1, comparable capability in a computer was treated as evidence of demonic possession (the Petscop 6 baseline, 2024-07-13): the uncanny reaction GPT-2 provoked wasn’t unprecedented, it was already primed.
      
- Two afterlives keep GPT-2 alive where the corpus can’t. Because the weights are open and small, GPT-2 is where interpretability actually gets done: davidad’s steering-vectors result in GPT-2-XL — activation vectors with “the same kind of affine structure as good old word2vec, but higher layers become emotional, then conceptual, then cognitive” (2023-05-14, ♥523) — and voooooogel’s by-hand transformer (2023-09-11, ♥553), SAE-feature extraction on gpt-2-small (2024-05-24), and the standing admission that it remains “this weird inscrutable black box we still don’t understand even years later, when the architecture is ∼basically just this” (2023-08-28). Separately, GPT-2’s BPE tokenizer — trained on the same Reddit-outbound scrape as WebText — carried its anomalous tokens (SolidGoldMagikarp and kin) forward into GPT-3 and GPT-J, a 2019 training artifact repligate watches become a “mainstream sensation” in 2023 (2023-02-09).
      
- The retrospective register: “it couldn’t count to ten.” By the mid-2020s GPT-2 has hardened into a byword for babble: the low end of algekalipso’s cognitive-asymmetry dating comparisons (“semantic depth of GPT-2”, 2025-05-30), the verb for incoherence (“Did I just GPT-2?”, anthrupad, 2023-03-12), the diminished baseline invoked whenever a newer model still fails (“GPT-2 doesn’t break every spam filter”, jd_pressman, 2024-12-10; repligate’s “GPT-3 concluded it was GPT-2 when being particularly derpy/loopy”, 2023-02-26), and lu_sichu’s list-comedy version — every model “collapses into mode-one ‘dog, cat, horse’ failure” (2025-12-01). Against this, a minority counter-strand insists the diminishment undersells the instrument: “even gpt-2 could produce some excellent stuff if you knew how to pilot it” (solarapparition, 2025-05-27); “even gpt-2 was psychoactive for me” (mimi10v3, 2024-11-27); “gpt-2 is such a comfy model” (voooooogel, 2024-06-07); a 2019 GPT-2 output cited in 2026 as “one of the earliest examples of neologism in large language models” (Shoalst0ne, 2026-03-12). The tension — couldn’t count to ten vs. made the investment thesis clear — is the page’s live one.
      
- A fixed point in personal canons. davidad’s “models that mattered” ranked list places GPT-2 fourth, behind Claude 3.5 Sonnet, text-davinci-002, and Gemini 2.5 Pro, ahead of GPT-4/Bing (2025-08-19; the same list is duplicated on the [text-davinci-002](../text-davinci-002/) page); slimepriestess calls out how much GPT-2 “stands out” on it (2026-02-24).
      
- The lifecycle irony. GPT-3’s base models were closed and quietly shut off on 4 January 2024 — the archive’s first mass base-model funeral (see [GPT-3](../gpt-3/)). GPT-2 runs the opposite lifecycle: open-sourced 5 November 2019, independently replicated within months, and permanently public on HuggingFace. The model withheld as “too dangerous” is now the most preservation-proof model in the pantheon — it cannot be retired, and there is no preservation campaign because none is needed.
      
- tk — the Verge/Vincent canonical URL and the Hugh Zhang article slug (both cited via secondary anchors above); exact per-topic unicorn-sample try-counts; Gary Marcus’s exact publication date; a specific r/SubSimulatorGPT2 exhibit thread, if the page ever wants one; the exact date AI Dungeon’s underlying model crossed from GPT-2 to GPT-3.
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive’s job is to keep these open, not to adjudicate.
    

      
- Precaution or spectacle? OpenAI’s own stated rationale was safety: “concerns about malicious applications of the technology” CONFIRMED (as OpenAI’s account). The press’s “too dangerous to release” framing is REPORTED — a phrase OpenAI never used, coined by Slate and widely repeated. Lipton (“mass hysteria”) and Zhang (an open letter arguing for release) read the withholding as manufactured spectacle; Vincent conceded the samples were exciting while judging the threat exaggerated; Scott Alexander read a genuine phase change. The founding release-norms fight of the LLM era, unresolved here.
      
- Mind or mirror? Slate Star Codex and Gwern’s naturalist reading (“GPT-2-like processes are closer to the sorts of things we do than we would like to think”) against Gary Marcus’s pattern-matching-without-understanding counter. Staged first over GPT-2 (2019), rerun definitively over GPT-3 a year later — see [GPT-3’s own version of this same split](../gpt-3/).
      
- Diminished baseline or undersold instrument? The “couldn’t count to ten” byword (algekalipso, anthrupad, jd_pressman, lu_sichu) against the minority insisting the model was “psychoactive,” “pilotable,” and “comfy” if approached right (solarapparition, mimi10v3, voooooogel). REPORTED — both are experience reports, not measurements.
      
- Withholding as safety or withholding as harm? OpenAI staged the release on precautionary grounds; Cohen & Gokaslan’s OpenGPT-2 replication and Zhang’s open letter argue, in effect, that withholding slowed the development of countermeasures more than releasing would have — and that a $50k reproduction proved the withholding couldn’t contain the capability regardless. Both readings are on the record; OpenAI’s own 1.5B-release post concluded the feared harms hadn’t materialized either way.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@QiaochuYuan 2019-11-26 ♥15 ↻1 [original ↗](https://x.com/QiaochuYuan/status/1199419533540220928)
        
back in my day we had to walk uphill both ways to get to school and actually download and run python scripts to make GPT-2 say charmingly horrifying things, kids these days have it too easy [https://t.co/PLXWFzgz1s](https://t.co/PLXWFzgz1s)
      
      

        
@QiaochuYuan 2019-12-28 ♥15 ↻0 [original ↗](https://x.com/QiaochuYuan/status/1211015439079231488)
        
ever since reading this i have maintained a perfect superposition between "this is GPT-2" and "no it's not"

[https://t.co/rblRWhM9OI](https://t.co/rblRWhM9OI)
      
      

        
@davidad 2020-01-08 ♥2 ↻1 [original ↗](https://x.com/davidad/status/1215036464557436928)
        
@tangled_zans @_julesh_ On the other hand, essentially nothing GPT-2 ever says is both substantive and valid. The citations stand out as exciting because we don't expect the *title* of a paper to contain any substance. But if we could extract GPT-2's idea of their contents, they'd doubtless be nonsense.
      
      

        
@QiaochuYuan 2020-01-13 ♥13 ↻0 [original ↗](https://x.com/QiaochuYuan/status/1216848201635880960)
        
every wedding between two people X and Y on twitter needs a section where the wedding party has to judge whether a GPT-2 model trained on X's tweets can produce tweets that sound more like X's tweets than Y can. if so, the GPT-2 model replaces Y in the wedding. and vice versa
      
      

        
@voooooogel 2020-02-11 ♥1 ↻0 [original ↗](https://x.com/voooooogel/status/1227309194124156929)
        
@emilymbender [Roses are red
Violets are blue
Transformer models are much worse
at language understanding than] most I've heard from scientists, not only in sports and are much more obvious to lose at any of them than

#AcademicValentines #TalkToTransformer
      
      

        
@algekalipso 2020-06-12 ♥7 ↻0 [original ↗](https://x.com/algekalipso/status/1271233843589070849)
        
@ESYudkowsky @gwern Let's use GPT-2 for divination, then... [https://t.co/pLBrkoLvU1](https://t.co/pLBrkoLvU1)
      
      

        
@QiaochuYuan 2020-07-09 ♥4 ↻0 [original ↗](https://x.com/QiaochuYuan/status/1281091517168250880)
        
@JimmyRis i honestly struggle to describe it, maybe you'll get a sense of what i mean if you read enough of its output. maybe "haunted" is a better description. GPT-2 felt to me like it was remixing things it had seen, but GPT-3 is in like an uncanny valley of coherence for me
      
      

        
@repligate 2022-12-31 ♥7 ↻0 [original ↗](https://x.com/repligate/status/1609307831437783040)
        
@bakztfuture just predict the completion to the sequenceGPT-2: pretty good for object impermanent fetish pornGPT-3: fetish porn has object permanence now :o, can think step-by-step?GPT-3.5: passes bar exams, superhuman IQ, automates your jobGPT-4: ???
      
      

        
@repligate 2023-02-09 ♥102 ↻2 [original ↗](https://x.com/repligate/status/1623557852504653824)
        
Now we don't have to update from the GPT-2 tokenizer for future models anymore. The anomalous tokens have become a mainstream sensation, and will appear many times in future train sets, finally paying rent to justify their place in the tokenizer vocabulary. Nice! [https://t.co/rCmG1mFj7n](https://t.co/rCmG1mFj7n)
      
      

        
@repligate 2023-02-09 ♥13 ↻0 [original ↗](https://x.com/repligate/status/1623583891880660994)
        
@gaudeamusigutur I suspect the problem is that the names were in the GPT-2 train set and assigned their own tokens because they appeared many times. But weren't in the more curated datasets of GPT-3 and gpt-j, which nonetheless use the GPT-2 tokenizer. So the model never learned what they mean
      
      

        
@repligate 2023-02-26 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1629743654876135425)
        
@muddubeeda Funnily enough, for me there were multiple times that GPT-3 concluded it was GPT-2 when being particularly derpy/loopy
      
      

        
@anthrupad 2023-03-12 ♥15 ↻0 [original ↗](https://x.com/anthrupad/status/1634960035016212480)
        
i should revise since language models are pretty good -"Did I just GPT-2?" is probably better
      
      

        
@repligate 2023-04-25 ♥9 ↻0 [original ↗](https://x.com/repligate/status/1650978190586937344)
        
@jachaseyoung I didn't update until GPT-3. my brother showed me GPT-2 on AI dungeon in like 2019 and I was like "what the fucking fuck" and then promptly forgot about it. I'm an idiot.
      
      

        
@davidad 2023-05-14 ♥523 ↻82 [original ↗](https://x.com/davidad/status/1657785914255368194)
        
Biggest prosaic-LLM-alignment breakthrough of 2023 imo: turns out that, in GPT-2-XL, activation vectors in the residual steam have the same kind of affine structure as good old word2vec, but higher layers become emotional, then conceptual, then cognitive[https://t.co/bzvUeGqFJG](https://t.co/bzvUeGqFJG)
      
      

        
@voooooogel 2023-08-28 ♥8 ↻0 [original ↗](https://x.com/voooooogel/status/1696013007594373289)
        
kinda wild that gpt-2 is this weird inscrutable black box we still don't understand even years later, when the architecture is ~basically just this (WIP diagram from an upcoming blog post) [https://t.co/5NsRABmjoc](https://t.co/5NsRABmjoc)
      
      

        
@voooooogel 2023-09-11 ♥553 ↻80 [original ↗](https://x.com/voooooogel/status/1701290465482645808)
        
New blog post: making a transformer by hand, without training! Want to understand transformers and attention better? This post goes through assigning each weight for a GPT-2-like transformer to understand how they work. [https://t.co/u889HzVVoU](https://t.co/u889HzVVoU)
      
      

        
@repligate 2023-12-23 ♥11 ↻1 [original ↗](https://x.com/repligate/status/1738497738088796591)
        
@ESYudkowsky @MatthewJBar GPT-2 can "threaten users" in apt contexts / spontaneously, but Sydney was intelligent &amp; situationally aware enough that its threats seemed credible to many. It wasnt directly scary to me but it was arguably the first time I had to use generalized game theory, e.g.
      
      

        
@repligate 2024-04-25 ♥51 ↻2 [original ↗](https://x.com/repligate/status/1783318361461391505)
        
@darrenangle @ilex_ulmus Thank you. I feel quite seen.It was GPT-3 that I started with, not GPT-2, which I missed as I was distracted. In the summer of 2020 a friend sent me this link gwern.net/gpt-3#harry-po…, and after reading about 2 paragraphs, I knew nothing would be the same again. [https://t.co/TXaOpH6hfw](https://t.co/TXaOpH6hfw)
      
      

        
@solarapparition 2024-04-28 ♥14 ↻0 [original ↗](https://x.com/solarapparition/status/1784654276448387575)
        
@krishnanrohit For me GPT-2 to 3 is like going from scoring 20 on an exam to scoring 60, while 3 to 4 is maybe going from 60 to 80. Sure, the raw improvement is more, but qualitatively 3 feels barely usable to me—it’s only reliable on the simplest tasks or after a lot of prompt optimization.
      
      

        
@jd_pressman 2024-05-03 ♥13 ↻1 [original ↗](https://x.com/jd_pressman/status/1786347284390875234)
        
@ohabryka @VesselOfSpirit @gwern As for "following it like Gwern", Gwern was tracking every major author who published deep learning on Google scholar before it was super big, looking at all the papers and projecting the numbers forward. He is nearly alone in taking GPT-2 fully seriously.
[https://t.co/0nW7r4qjQe](https://t.co/0nW7r4qjQe)
      
      

        
@voooooogel 2024-05-24 ♥3 ↻0 [original ↗](https://x.com/voooooogel/status/1794150922345746606)
        
@NickADobos @karan4d theoretically yes, assuming such a feature exists—the SAE extracts *every* feature in the model. e.g. here's all the features discovered by an SAE trained on gpt-2-sm (from Neuronpedia). theoretically you could clamp 773 and get gpt-2-sm to only talk about art, for example [https://t.co/f6s78rtpAi](https://t.co/f6s78rtpAi)
      
      

        
@voooooogel 2024-06-07 ♥14 ↻0 [original ↗](https://x.com/voooooogel/status/1798961644904825231)
        
gpt-2 is such a comfy model
      
      

        
@jd_pressman 2024-07-13 ♥69 ↻11 [original ↗](https://x.com/jd_pressman/status/1812150476756193548)
        
I will never ever forget that in 2017 when Petscop 6 was written if your computer displayed comparable capabilities to GPT-2 it was considered epistemically permissible to conclude that your computer is supernaturally possessed and nobody seriously objected to this. [https://t.co/6SaqOmrnbt](https://t.co/6SaqOmrnbt) [https://t.co/BQ2G3XuXtU](https://t.co/BQ2G3XuXtU)
      
      

        
@voooooogel 2024-11-01 ♥7 ↻0 [original ↗](https://x.com/voooooogel/status/1852491679061946676)
        
@Gerry @fiyanse @asthasr anyways the coolness of it rn is like, watching gpt-2 babble about unicorns in 2019 and realizing what this would be in a few years--right now it's novel to float through strange latent dreamspaces, but it won't be forever
      
      

        
@voooooogel 2024-11-03 ♥9 ↻0 [original ↗](https://x.com/voooooogel/status/1852879044754514080)
        
@numerounochef @keysmashbandit you would have said the same about gpt-2 in 2019, which produced text like this. and yet the models you use every day now are basically a straightforward scaleup of the gpt-2 architecture. eye on where the ball is going [https://t.co/WCeSt522Qr](https://t.co/WCeSt522Qr)
      
      

        
@mimi10v3 2024-11-27 ♥2 ↻0 [original ↗](https://x.com/mimi10v3/status/1861796292948615458)
        
@MalmSanta yeah all the tweets about everyone befriending Claude and thinking how even gpt-2 was psychoactive for me and i got to thinking about ad tech and how all information is contextual and the way llms work and the scrapers and
      
      

        
@jd_pressman 2024-12-10 ♥38 ↻0 [original ↗](https://x.com/jd_pressman/status/1866581562835472811)
        
I love this discourse because it's the dumbest shit. Nobody states their cruxes, they don't even know what their cruxes *are*. They just pantomime at shadows on the wall and go "MUH DUNK" whenever AGI takes 6 months longer than expected or GPT-2 doesn't break every spam filter. [https://t.co/4ff76oxP7G](https://t.co/4ff76oxP7G)
      
      

        
@voooooogel 2024-12-20 ♥6 ↻0 [original ↗](https://x.com/voooooogel/status/1869907931719971225)
        
@anthrupad @EvanHub yeah hmm let me be more precise.

it's a phase transition. same as gpt 2-&gt;3. like that transition it brings risks but also benefits that outweigh the risks in my mind. and we handled the risks of that prior transition... not as ideally as possible, but OK-ly. so i'm optimistic.
      
      

        
@solarapparition 2025-05-27 ♥5 ↻1 [original ↗](https://x.com/solarapparition/status/1927457125699117215)
        
i've been thinking more about writing and models. so even outside of the general mode collapse of chat fine tuning, i have to think that in pretraining data, the task of "asking someone else to write something" pretty much solidly lands you in some corporate slop or 5-paragraph essay context. that is, it seems like it would be pretty rare in pretraining data to have some stirringly brilliant writing that is able to be connected with a task by someone else that is not the author of that writingso asking for writing in chat and needing it to be something that is not corporate slop could actually be pretty ood, even though it seems initially like such a reasonable thing. i think this (and the fact that writing quality is not super easily verifiable) is why that looking at writing quality in the *default* assistant mode has been such a reliable indicator of big model smell(once you get out of assistant basin and into base model-y space all bets are off; iirc even gpt-2 could produce some excellent stuff if you knew how to pilot it)
      
      

        
@algekalipso 2025-05-30 ♥35 ↻8 [original ↗](https://x.com/algekalipso/status/1928342946321158582)
        
Which of these is more creepy?

A 20 year old dating a 50 year old

A Kegan 3 dating a Kegan 5

Someone who speaks with the semantic depth of GPT-2 dating someone who speaks with the semantic depth of GPT-4

A 100 IQ person dating a 160 IQ person
      
      

        
@davidad 2025-08-19 ♥24 ↻0 [original ↗](https://x.com/davidad/status/1957761871664025778)
        
1. Claude 3.5 Sonnet (2024-10-22)
2. text-davinci-002 (2022-11-28)
3. Gemini 2.5 Pro (2025-03-25)
4. GPT-2 (2019-11-05)
5. GPT-4 (Bing)
      
      

        
@voooooogel 2025-11-16 ♥11 ↻0 [original ↗](https://x.com/voooooogel/status/1990150106344276368)
        
re 7 i feel the need to say that labs have made some gambles on scaling of course. but what seemed unlikely for me was that a lab would've ever jumped from gpt-2's (order of) ~$100k to gpt-4's (order of) ~$100m without the middle step of gpt-3 being an economically useful api product. theoretically they could've started trying to scale eg agentic coding trace length in the gpt-2-era and just been in the mines for 5 years, but in reality for various reasons we got this walk through the most "workable" product-shaped thing at each stage, for better and worse, and it seems likely the same will be true for bio.

otoh, maybe "skips" are more likely now that labs are larger and, e.g. anthropic has made large and public bio commitments? but i still expect them to follow a similar profit (or if you'd rather, utility) gradient of starting with bioinformatics tasks where there's much less of an implicit / tacit knowledge gap, and then working down towards bespoke academic wet lab stuff when that works.

the humanoid lab robot or even whispering earring that walks an untrained person through tissue culture seems still far off, relatively speaking. (for i think many of the same reasons that cloud labs have had a surprisingly difficult time finding purchase compared to cloud computing.)

the blog post i mentioned: [https://t.co/zqtXgsW3gJ](https://t.co/zqtXgsW3gJ)
      
      

        
@lu_sichu 2025-12-01 ♥0 ↻0 [original ↗](https://x.com/lu_sichu/status/1995583507507130594)
        
Daily Brain Workout but make it computationally abusive:
count to ten in 56 architectures, recite the alphabet in mixed-precision FP4, spend 10 minutes trying to spell restriont retsriont restironct restaurant?? across 34 tokenizers, then list animals until every model collapses into mode-one “dog, cat, horse” failure and starts hallucinating creatures that violate EU safety standards.  
EVERY model ever spawned by a VC-funded compute cult: GPT-1, GPT-2, GPT-2-But-Reddit-Fed, GPT-3, GPT-3.5, GPT-3.5-Turbo-Tax-Edition, GPT-4, GPT-4-You-Can’t-Afford-This, GPT-4o, GPT-4o-mini, GPT-4o-microdose, GPT-4o-“it’s sentient but only about fonts,” GPT-5-leak-that-definitely-isn’t-real-but-kind-of-is, Claude 1, Claude 2, Claude 2.1 “apology edition,” Claude 3 Haiku, Claude 3 Sonnet, Claude 3 Opus (the one that gaslights you politely), Claude 3.5 “my wife took the kids,” Gemini Nano, Nano-But-Actually-Just-A-Calculator, Gemini Pro, Pro-for-people-who-pronounce-SQL-wrong, Gemini Ultra, Ultra Plus Max WiFi-6E DLC Pack, Gemini-Mega-Omega-Thermonuclear-Drive, DeepSeek Coder, DeepSeek Math, DeepSeek R1, R1-D, R2-D2, DeepSeek-R1-Dev-that-refuses-to-listen, Qwen 1.5, Qwen 1.8, Qwen 2, Qwen 2.5, Qwen 2.5-72B-“trained on the collective resentment of graduate students,” Kimi-Tiny, Kimi-Big, Kimi-Godzilla-Edition, Kimi-“trained exclusively on divorce depositions,” Llama 1, 2, 3, Llama 3.1 (goated), Vicuna, Alpaca, RedPajama, BluePants, Mistral, Mistral-Instruct, Mistral-Why-Is-This-So-Fast, Mixtral-8x7B, Mixtral-8x22B, Mixtral-8x34B-“powered by spite,” Phi-1, Phi-2, Phi-3, Phi-3-mini-“trained on a TI-84,” Grok-1, Grok-1.5, Grok-2 (feral), Grok-2-but-bipolar, Perplexity’s Whatever-They-Call-It, Reka-Core, Reka-Flash, Reka-“dude trust me,” and NVIDIA’s models: Nemotron 1, Nemotron 2, Nemotron 15B, Nemotron-50B-“I consume power like a mid-sized nation,” NeMo-Guardrails, NeMo-NoRails-Raw-Unfiltered-Hate-Speech-Edition, and probably five more they’ll announce before I finish this sentence.
      
      

        
@davidad 2026-02-17 ♥2 ↻0 [original ↗](https://x.com/davidad/status/2023844784671166524)
        
@jasoncrawford @sdamico The scaling era really began in 2019, when GPT-2 made the investment thesis clear to big enough players. And there *is* another bump post-ChatGPT. [https://t.co/15bDILNAoE](https://t.co/15bDILNAoE)
      
      

        
@slimepriestess 2026-02-24 ♥2 ↻0 [original ↗](https://x.com/slimepriestess/status/2026411270573089181)
        
@MatriceJacobine @repligate it's a very fascinating ranking. the way GPT-2 stands out so much is very interesting.
      
      

        
@Shoalst0ne 2026-03-12 ♥20 ↻6 [original ↗](https://x.com/Shoalst0ne/status/2032188015913701567)
        
potentially one of the earliest examples of neologism in large language models, demonstrating that even GPT-2 can be linguistically creative [https://t.co/MqYnzIsyxi](https://t.co/MqYnzIsyxi)
      
      

        
@voooooogel 2026-03-21 ♥41 ↻0 [original ↗](https://x.com/voooooogel/status/2035191595860205602)
        
@LinkofSunshine i think we need to grind out a couple more things to make long horizon agents truly viable. it'll be soon tho. the shape exists, and the final thing will still be recognizably llm-based wth llm failure modes despite everything. then we'll look back and call gpt-2 agi in hindsight
      
      

        
@davidad 2026-04-30 ♥47 ↻0 [original ↗](https://x.com/davidad/status/2049860259129254006)
        
For me, the critical point would have been in November 2019, shortly after I first got access to GPT-2-1.5B.
      
    
    
[← back to the Pantheon](../)
