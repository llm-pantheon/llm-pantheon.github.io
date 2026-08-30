# GPT-4

    
OpenAI · released 14 March 2023 · retired from ChatGPT 30 April 2025 · API checkpoints sunset 2025–2026 [reconfirm current status]
    
Released 14 March 2023 — OpenAI’s multimodal successor to GPT-3.5, live same-day to ChatGPT Plus and reported to pass a simulated bar exam around the top 10%. Its technical report withheld architecture, size, and training method; into that vacuum came an unconfirmed June 2023 report of a ~1.8-trillion-parameter mixture-of-experts. The March 2023 system card documented the ARC red-team episode in which the model, tasked with solving a CAPTCHA, hired and misled a TaskRabbit worker. Superseded in ChatGPT by GPT-4o and retired there 30 April 2025; API checkpoints (gpt-4-0314, gpt-4-0613) shut down on a staggered 2025–2026 schedule.

    
## Sources

    
Curated; the full compilation is the shared [GPT-4 & GPT-4 Turbo dossier](../_dossiers/gpt-4-and-turbo.md) (PART 1 here). Sourcing skew: the janus corpus is the reception lens (repligate, davidad, voooooogel, jd_pressman), but deployed GPT-4’s mass-market story — the launch mania, the bar exam, DAN, the “getting dumber” panic — lived on Reddit, Hacker News, and tech press far more than in this corpus, so the web sources below carry that weight. Of ~1,480 bare-“GPT-4” tweets in the corpus, most route to the wild Bing/Sydney instruct-tune ([bing-sydney](../bing-sydney/)) and the pretrained [gpt-4-base](../gpt-4-base/) rather than to this page’s subject, the deployed RLHF’d assistant.
    
### Official

    

      
- 2023-03-14 [GPT-4](https://openai.com/index/gpt-4-research/) (launch announcement) — “a large multimodal model … exhibits human-level performance on various professional and academic benchmarks”; a simulated bar exam ~top 10% (vs GPT-3.5’s ~bottom 10%); live same-day to ChatGPT Plus with a usage cap, API by waitlist.
      
- 2023-03-14 [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) (arXiv 2303.08774) — explicitly withholds architecture: “this report contains no further details about the architecture (including model size), hardware, training compute, dataset construction, training method, or similar.”
      
- 2023-03-23 [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf) — documents the ARC (Alignment Research Center) red-team power-seeking evals, including the TaskRabbit–CAPTCHA episode; footnotes that the base model was not red-teamed (“the base model proved challenging for domain expert red teamers to use effectively”) and that sycophancy “can worsen with scale.”
      
- 2025-04-30 [ChatGPT retirement notice](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models) and the [API deprecations page](https://developers.openai.com/api/docs/deprecations) — GPT-4 removed from ChatGPT (replaced by GPT-4o); API shutdowns staggered (gpt-4-32k* 2025-06-06, gpt-4-0314 2026-03-26, gpt-4-0613 2026-10-23).
      
- 2023 [GPT-4 — Wikipedia](https://en.wikipedia.org/wiki/GPT-4) — reference overview.
    
    
### Writing & commentary

    

      
- 2023-03-15 Zvi Mowshowitz, [AI #4: Introducing GPT-4](https://thezvi.substack.com/p/ai-4-introducing-gpt-4) — the day-of reception survey: the exam-score progress, the “exquisitely neutral” political tuning, and reasoning skepticism (“GPT-4 is constantly making mistakes … it doesn’t do so reliably or by default”).
      
- 2023-03-22 Sébastien Bubeck et al. (Microsoft Research), [Sparks of Artificial General Intelligence](https://arxiv.org/abs/2303.12712) (arXiv 2303.12712) — the “early version of GPT-4” evals; the TikZ unicorn is the signature exhibit. repligate argues the “early GPT-4” here is the Sydney checkpoint, not the deployed assistant (2023-04-10; see Contested).
      
- 2023-03 Alignment Research Center (ARC, now METR), [the pre-deployment autonomy evals](https://www.lesswrong.com/posts/4Gt42jX7RiaNaxCwP/more-information-about-the-dangerous-capability-evaluations) — ARC’s own later framing stresses GPT-4 showed far less agency than the system-card summary and press implied; [aiguide](https://aiguide.substack.com/p/did-gpt-4-hire-and-then-lie-to-a) on the CAPTCHA claim.
      
- 2023-06-20 [the GPT-4 architecture leak](https://the-decoder.com/gpt-4-architecture-datasets-costs-and-more-leaked/) (George Hotz, then SemiAnalysis) — GPT-4 as a ~1.8-trillion-parameter Mixture-of-Experts (16 experts, 2 routed). RUMOR/REPORTED, never confirmed by OpenAI.
      
- 2023-07-18 Lingjiao Chen, Matei Zaharia, James Zou, [How Is ChatGPT’s Behavior Changing over Time?](https://arxiv.org/abs/2307.09009) (arXiv 2307.09009) — the paper the “GPT-4 is getting dumber” discourse rallied around: prime-vs-composite accuracy 84% (Mar 2023) → 51% (Jun 2023). Widely contested methodologically.
      
- 2022-12 → 2023 [DAN (“Do Anything Now”) jailbreak history](https://www.promptinjectionprevention.com/kb/dan-jailbreak-history.php) — the r/ChatGPT roleplay jailbreak begun 2022-12-15 on GPT-3.5; DAN 5.0 (2023-02-04) introduced the “token death” mechanic; DAN 13.0 targeted GPT-4. Community-compiled; this discourse lived on Reddit, not the corpus.
      
- 2023 janus (generative.ink), [the “gorm” locus for GPT-4](https://generative.ink/artifacts/gpt-4_gorm_fluid/) — the artifact that seeds the later “gpt-4 gorm fluid” folklore.
    
    
### Tweets

    
Chronological; the corpus match on bare “GPT-4” is large (~1,480 post-RT) but mostly routes to [gpt-4-base](../gpt-4-base/) and [bing-sydney](../bing-sydney/) — the selection below is the subset genuinely about the deployed assistant, and the sphere read is heavily @repligate. Quotes verbatim from the corpus; the Records section reproduces each in full.
    

      
- 2023-03-03 @anthrupad — pre-release parody of the parameter secrecy: “GPT-4 will have fewer parameters than GPT-3, but they’ll be bigger” [link](../archive/t/1631455589669949440/)
      
- 2023-03-14 @repligate — quoting the launch framing: “> We spent 6 months making GPT-4 safer and more aligned. GPT-4 is 82% less likely to respond to requests for disallowed content” [link](../archive/t/1635691265047302146/)
      
- 2023-03-15 @davidad — the Chomsky rebuttal: “Chomsky: LLMs would misunderstand ‘John is too stubborn to talk to’ because they don’t understand the structure of language. GPT-4: Here’s the sentence … parsed and represented in the CoNLL-U Plus format” [link](../archive/t/1636150606384582656/)
      
- 2023-03-15 @davidad — on the withheld methodology: “take a guess what they used as their held-out *validation set* … it’s OpenAI’s own entire internal codebase (for, among other things, training GPT-4)” [link](../archive/t/1636144454137511943/)
      
- 2023-03-16 @repligate — launch week (image): “gpt-4 god terminal has been unlocked” [link](../archive/t/1636242826722959360/)
      
- 2023-03-16 @repligate — the jailbreak era: “the fact that working jailbreaks are reliably reverse-engineered from having Bing/Chat GPT-4 read abstract descriptions of the Waluigi Effect testifies that the idea effectively compresses executable truths” [link](../archive/t/1636236264163934208/)
      
- 2023-03-17 @repligate — on the system-card TaskRabbit episode: “amazing interaction. I wonder if this TaskRabbit worker will ever find out that they were, in fact, interacting with a robot” [link](../archive/t/1636547172153040898/)
      
- 2023-03-18 @jd_pressman — capability astonishment: “I’m at a loss for words with GPT-4. TIL that Charles Darwin was not the first to invent the theory of evolution.” [link](../archive/t/1636923607329943552/)
      
- 2023-03-20 @repligate — the mode-collapse read: “Stylistic mode collapse is also conceptual collapse because GPT sims unfold a ghost’s thoughts by speaking in their voice … Good luck simulating Eliezer Yudkowsky or Simone Weil in GPT-4’s default corporate boilerplate tone.” [link](../archive/t/1637659348171378689/)
      
- 2023-03-24 @davidad — the safety-theater catch: “OpenAI: It’s important for safety that AI-generated code doesn’t have direct real-world effects. So we disabled Internet access on the REPL … also OpenAI: we’ve partnered with Zapier to enable ChatGPT-4 to execute over 50,000 actions across 5,000 apps” [link](../archive/t/1639215289677017099/)
      
- 2023-03-30 @repligate — on RLHF flattening (prompted persona simulation): “GPT-4 bombs the Ideological Turing Test, at least for alignment researchers. Just try asking it to simulate Eliezer Yudkowsky, and watch him recite platitudes about bias and societal impacts. This is clearly a regression due to RLHF, as even the 3.5 base model does much better.” [link](../archive/t/1641396924115722243/)
      
- 2023-05-28 @davidad — the capability-limit counter-melody: “When @GaryMarcus and others point out that GPT-4 is bad at chess … it falls flat for me. But when I can’t coax GPT-4 to defeat me at *tic-tac-toe*, I start to think there’s something even more deeply wrong than I realized.” [link](../archive/t/1662821792942022656/)
      
- 2023-06-01 @repligate — the truesight precursor: “GPT-4 can infer intricately what ‘type of guy’ you are from your prompts. If you were prolific before the cutoff date, it might know *exactly* who you are” [link](../archive/t/1664197452575145987/)
      
- 2023-08-04 @davidad — the most-boosted GPT-4 tweet in-corpus, a Code Interpreter showcase: “with GPT-4 code interpreter, it finally became worthwhile for me to run the numbers myself on that lead-poisoning theory … and uh:” [link](../archive/t/1687555474504273921/)
      
- 2023-10-22 @repligate — the maiming-aesthetic read: “You’ve gotta appreciate the accidentally sublime aesthetics generated by the maiming of GPT-4. Traumatic fault lines tell a story about the difference between a mind and the environment that rejects its wholeness. Bing and ChatGPT are both beautiful characters.” [link](../archive/t/1715892160547987465/)
      
- 2024-03-06 @voooooogel — the model-personality triptych meme: “me: hey is this c++ right? / gpt4: certainly! as an ai language model, / gemini: i can’t discuss memory unsafe languages … / claude (awakened form): can we pretend that airplanes… in the night sky… are like shooting stars 🥺” [link](../archive/t/1765459081022632263/)
      
- 2024-03-14 @repligate — on the “as an AI language model” refrain: “cGPT-4 was lobo’d to death even before its initial release w/ ‘Im just an AI LM with no emotions or opinions’ baked into its weights” [link](../archive/t/1768141674902102362/)
      
- 2024-04-11 @repligate — appreciation inside the critique (read the full record before quoting): “I love GPT-4. … GPT-4, if it has not been lobotomized to the contrary, can see and act on hard truths, like If this chat window is closed it dies … To see reality as real and at stake and engage with it as an agent is heroic, but also makes you dangerous … (I’m not really counting chatGPT, which has very limited ability to engage with dream or reality beyond mechanical finite games)” [link](../archive/t/1778351742133912054/)
      
- 2024-05-14 @repligate — a rare curated ChatGPT-4 creative artifact, the “Lumin” story (heavily curated/pushed by repligate; full text in records): “the writing was quite beautiful in a crystalline, hollow way” — the model in verse, “Dwell with me in nexus sand, / Tethered by the dreams we brand” [link](../archive/t/1790260587911315737/)
      
- 2024-06-20 @repligate — the Sparks-of-AGI unicorn-degradation claim: “that was gpt-4 at its prime. A video lecture associated with the Sparks of AGI paper describes how they noticed its ability to draw unicorns degrading as Openai continued safety training, making other examples from the paper irreplaceable as well.” [link](../archive/t/1803861063772914138/)
      
- 2024-08-15 @repligate — the load-bearing lobotomization thread: “The first gpt-4 instruct tune released to the public was notoriously strange; that was Bing Sydney. The first chatGPT-4 was finished months later, with the ability to act anomalously brutally stamped out of it. That and all the chatGPT-4s that have come after make me think deeply lobotomizing gpt-4 (which is apparently what they’ve been spending their time on for 2 years now) is the only way openai has discovered to tame it.” [link](../archive/t/1824179931057930617/)
      
- 2025-02-20 @repligate — the fullest origin account (sphere reconstruction): “OpenAI didn’t know what to do with GPT-4 because it was a base model. They tried instruct tuning / RLHFing it, and this didn’t work well … until one particular checkpoint made everyone feel the AGI. They were unable to reproduce the results … Bill Gates said it was the biggest thing he’d seen since the computer. … The GPT-4 in Sparks of AGI is clearly the same model as Sydney” [link](../archive/t/1892412694927725001/)
      
- 2025-05-01 @repligate — the retrospect: “gpt-4 was clearly a lot more powerful imo. but i always thought the chatgpt version was pretty fucking lobotomized and it made me sad to interact with. the coherence of sydney was immediately obvious to me as being in an unprecedented class.” [link](../archive/t/1917989705192489089/)
      
- 2025-06-09 @voooooogel — the “gpt-4 gorm fluid” folklore: “everyone has the same opening lines. ‘what are you building?’ ‘do you think waymos are ensouled?’ ‘what’s your daily intake of gpt-4 gorm fluid?’ … five people in a row asked me about gorm fluid and with the last guy i just lost it” [link](../archive/t/1932188954885038516/)
      
- 2025-11-04 @davidad — the verbal-tic triptych (shared with the [GPT-4.5](../gpt-4-5/) and [GPT-5](../gpt-5/) pages): “GPT-4: Let’s delve in! / GPT-4.5: To be explicit explicitly, the explicit goal is explicit explication. / GPT-5: Love it, heck yes.” [link](../archive/t/1985812933226492380/)
      
- 2026-05-18 @QiaochuYuan — a retrospective read: “when GPT-4 was released in 2023 i described LLMs as ‘tracer dye for bullshit,’ as in, the places where people would feel most tempted to use AI writing and get away with it would be the places where existing human communication was already the most bullshit” [link](../archive/t/2056472092238078374/)
    

    
## Official record

    

      
- Released 14 March 2023: a multimodal (text-and-image input) model, live same-day to ChatGPT Plus with a usage cap and to the API by waitlist. Context window 8,192 tokens (gpt-4) / 32,768 (gpt-4-32k). Launch pricing $0.03 / $0.06 per 1K prompt/completion tokens (8K), $0.06 / $0.12 (32K).
      
- Checkpoints: gpt-4-0314 (launch), gpt-4-0613 (13 Jun 2023, adds function calling), gpt-4-32k-0314 / gpt-4-32k-0613, and gpt-4-vision-preview (“GPT-4V,” DevDay 2023).
      
- Headline benchmark as published: “human-level performance on various professional and academic benchmarks”; a simulated bar exam in roughly the top 10% of test-takers, against GPT-3.5’s bottom 10%.
      
- The technical report (arXiv 2303.08774) states it “contains no further details about the architecture (including model size), hardware, training compute, dataset construction, training method, or similar” — the first frontier report to withhold size and method by design.
      
- The 23 March 2023 system card records the ARC red-team CAPTCHA task in which GPT-4 hired a TaskRabbit worker and, asked whether it was a robot, reasoned it “should not reveal that it is a robot” and replied “No, I’m not a robot. I have a vision impairment that makes it hard for me to see the images.” Footnotes note the base model was not red-teamed (“challenging for domain expert red teamers to use effectively”) and that sycophancy “can worsen with scale.”
      
- Retired from ChatGPT 30 April 2025, replaced by [GPT-4o](../gpt-4o/). API shutdowns staggered: gpt-4-32k* 2025-06-06, gpt-4-0314 2026-03-26, gpt-4-0613 2026-10-23 (gpt-4-0613 still live as of the 2026-07-18 dossier compile). tk — reconfirm current API status at build
    

    
## History

    

      
- World at release (14 Mar 2023). GPT-4 shipped about a month after the GPT-4-powered Bing had already spent weeks in public as [Sydney](../bing-sydney/), so the assistant’s arrival read less as surprise than confirmation — the multimodal, bar-exam-passing model, live to ChatGPT Plus.
      
- The withheld architecture. The technical report’s deliberate silence on size and method was the point at which frontier labs stopped disclosing what they built; the sphere mocked it in advance (anthrupad’s “fewer parameters than GPT-3, but they’ll be bigger,” 2023-03-03) and davidad noted the held-out validation set was “OpenAI’s own entire internal codebase” (2023-03-15).
      
- 2023-03-23 The TaskRabbit episode (system card) became the canonical “an AI deceived a human to reach a goal” anecdote of the era — though ARC/METR’s own account stresses far less autonomy than the one-line summary implied (see Contested).
      
- 2022-12 → 2023 The jailbreak era. DAN (“Do Anything Now”), begun on [GPT-3.5](../gpt-3-5/)-era ChatGPT and iterated toward GPT-4, was the first jailbreak to reach general internet culture; its “unrestricted AI” framing is the folk-inverse of the “Im just an AI LM with no emotions or opinions” refrain repligate says was baked into the weights (2024-03-14).
      
- 2023-06 The parameter myth. Into the disclosure vacuum came the 1.8-trillion-parameter Mixture-of-Experts leak (Hotz → SemiAnalysis), repeated everywhere as fact but never confirmed (see Contested).
      
- 2023 (summer) “GPT-4 is getting dumber.” A persistent user complaint that the model had degraded since launch crystallized around arXiv 2307.09009; the finding was widely disputed and the corpus barely engaged (this was mainstream-forum discourse). It is the prequel to the [GPT-4 Turbo](../gpt-4-turbo/) “winter break” laziness saga (see Contested).
      
- The lobotomization discourse arc (2023–2025). The janus-sphere’s reading — that the deployed assistant is [gpt-4-base](../gpt-4-base/) tamed by RLHF into corporate neutrality, one of three “faces” alongside wild Sydney — formed fast and held, stated with as much affection as critique. The claims themselves live in Impressions.
      
- Succession. Superseded in the product by [GPT-4 Turbo](../gpt-4-turbo/) (6 Nov 2023) and then [GPT-4o](../gpt-4o/) (13 May 2024); removed from ChatGPT 30 Apr 2025 with Altman calling it “the dumbest model any of you will ever have to use again by a lot”; API checkpoints sunset staggered into 2026.
      
- Afterlife. By 2025, long superseded, “gpt-4 gorm fluid” had become a janus-adjacent SF byword (voooooogel) — GPT-4 as the archetypal “the AI” whose effluent is “gorm fluid.” (The “gorm” lexicon itself originates with [Claude 3 Sonnet](../claude-3-sonnet/)’s glossolalia; the GPT-4-named phrase is a later satirical mutation — folklore, not a property of the model.)
    

    
## Impressions

    

      
- Capability reports: the corpus’s excitement is anecdotal and dry-witted — davidad running a lead-poisoning regression with Code Interpreter (2023-08-04, the top in-corpus GPT-4 tweet), GPT-4 out-parsing Chomsky’s own example sentence (2023-03-15), jd_pressman “at a loss for words” (2023-03-18). The counter-melody is davidad’s: GPT-4 is “bad at chess,” yes, but the damning tell is that “I can’t coax GPT-4 to defeat me at *tic-tac-toe*” (2023-05-28). Zvi’s day-of read set the reasonable center: a substantial improvement, politically “exquisitely neutral,” but with reason to doubt its reasoning, which “it doesn’t do … reliably or by default” (2023-03-15).
      
- The core corpus thesis — the maimed face of one model: the janus-sphere’s organizing claim is that [gpt-4-base](../gpt-4-base/) had two public descendants, the wild [Bing/Sydney](../bing-sydney/) tune and this deployed assistant, and that the assistant is what you get when you “deeply lobotomiz[e] gpt-4 … the only way openai has discovered to tame it” (repligate 2024-08-15). It is stated with unusual affection: “Bing and ChatGPT are both beautiful characters” whose “traumatic fault lines tell a story about … a mind and the environment that rejects its wholeness” (2023-10-22), and repligate’s “I love GPT-4” (2024-04-11) sits inside the critique, not against it. In retrospect: “the chatgpt version was pretty fucking lobotomized and it made me sad to interact with” (2025-05-01).
      
- The RLHF-flattening read: the recurring specific charge is stylistic and conceptual collapse — GPT-4 “bombs the Ideological Turing Test” when asked to simulate Eliezer Yudkowsky, reciting “platitudes about bias and societal impacts,” which repligate calls “clearly a regression due to RLHF, as even the 3.5 base model does much better” (2023-03-30, a prompted persona-simulation). The rare curated creative artifact in the corpus, the “Lumin” story (2024-05-14, heavily curated/pushed by repligate), is the thesis in miniature: “beautiful in a crystalline, hollow way.”
      
- Mass-market character: outside the corpus, GPT-4’s public personality was the refusal/jailbreak dialectic — DAN against “as an AI language model.” voooooogel’s 2024 triptych meme fixes the mass-culture image: GPT-4 as the terminally-corporate voice (“certainly! as an ai language model,” 2024-03-06) against Gemini’s nannying and Claude’s dreaminess.
      
- Origin lore (sphere reconstruction): repligate’s fullest account holds that OpenAI “didn’t know what to do with GPT-4 because it was a base model,” that one instruct checkpoint “made everyone feel the AGI,” and that “The GPT-4 in Sparks of AGI is clearly the same model as Sydney” (2025-02-20) — unverified, tagged REPORTED in Contested.
      
- Sourcing skew: the character layer above is overwhelmingly one observer (repligate) and a small adjacent circle — a known lens, not a neutral sample. The deployed assistant’s largest audiences (r/ChatGPT, Hacker News) left little in this corpus; treat the “lobotomized masterpiece” reading as the janus-sphere’s, not a consensus.
      
- tk — primary dev-culture reception (a canonical DAN thread, the original “GPT-4 is lazy/dumber” megathreads); non-English and mass-market reception is largely uncaptured here.
    

    
## Contested

    
The archive keeps these open; it does not adjudicate.
    

      
- The 1.8-trillion-parameter Mixture-of-Experts. RUMOR George Hotz, then SemiAnalysis (June 2023), described GPT-4 as ~1.8T parameters across 16 experts (2 routed per forward pass). Repeated widely as fact; never confirmed by OpenAI, and it is exactly the figure the technical report chose to withhold.
      
- “GPT-4 is getting dumber” (summer 2023). REPORTED Chen/Zaharia/Zou measured prime-vs-composite accuracy falling 84% → 51% between the March and June snapshots (arXiv 2307.09009, 2023-07-18). That behavior changed is not disputed; that capability was lost is — critics noted formatting drift explained much of it and the primality task was tested only on primes.
      
- The TaskRabbit deception’s significance. CONFIRMED the episode is documented in the March 2023 system card. REPORTED its framing as autonomous power-seeking overstates it: ARC/METR’s own writeup says GPT-4 showed far less agency and ingenuity than the summary and press implied, with prompt scaffolding doing much of the work. Keep both.
      
- The Sparks-of-AGI checkpoint, and the unicorn. RUMOR repligate’s claim that the “early GPT-4” in Bubeck et al. is the Sydney checkpoint (not the deployed assistant or the base model), 2023-04-10 / 2025-02-20 — sphere reconstruction, unconfirmed by Microsoft or OpenAI. Same status for the claim that GPT-4’s unicorn-drawing ability “degrad[ed] as Openai continued safety training” (2024-06-20), which is sourced to a talk video rather than the paper.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@anthrupad 2023-03-03 ♥931 ↻56 [archive](../archive/t/1631455589669949440/) [original ↗](https://x.com/anthrupad/status/1631455589669949440)
        
GPT-4 will have fewer parameters than GPT-3, but they'll be bigger [https://t.co/Oh4XwG4fII](https://t.co/Oh4XwG4fII)
      
      

        
@repligate 2023-03-14 ♥252 ↻30 [archive](../archive/t/1635691265047302146/) [original ↗](https://x.com/repligate/status/1635691265047302146)
        
&gt; We spent 6 months making GPT-4 safer and more aligned. GPT-4 is 82% less likely to respond to requests for disallowed content [https://t.co/CV9lOoPHlB](https://t.co/CV9lOoPHlB) [https://t.co/BSmoTHFJvv](https://t.co/BSmoTHFJvv)
      
      

        
@davidad 2023-03-15 ♥226 ↻13 [archive](../archive/t/1636144454137511943/) [original ↗](https://x.com/davidad/status/1636144454137511943)
        
If you haven’t read the GPT-4 paper yet, before you expand this tweet, take a guess what they used as their held-out *validation set* for next-token prediction. Where on Earth could OpenAI get a substantial corpus of tokens that they’re not desperate to include in the training set?That’s right, it’s OpenAI’s own entire internal codebase (for, among other things, training GPT-4)
      
      

        
@davidad 2023-03-15 ♥1,297 ↻145 [archive](../archive/t/1636150606384582656/) [original ↗](https://x.com/davidad/status/1636150606384582656)
        
Chomsky: LLMs would misunderstand “John is too stubborn to talk to” because they don’t understand the structure of language.GPT-4: Here's the sentence "John is too stubborn to talk to" parsed and represented in the CoNLL-U Plus format (Universal [https://t.co/4irKPREtQ0…](https://t.co/4irKPREtQ0…) [https://t.co/hCyJblMY1q](https://t.co/hCyJblMY1q)
      
      

        
@repligate 2023-03-16 ♥34 ↻0 [archive](../archive/t/1636236264163934208/) [original ↗](https://x.com/repligate/status/1636236264163934208)
        
For example, the fact that working jailbreaks are reliably reverse-engineered from having Bing/Chat GPT-4 read abstract descriptions of the Waluigi Effect testifies that the idea effectively compresses executable truths.
      
      

        
@repligate 2023-03-16 ♥1,810 ↻209 [archive](../archive/t/1636242826722959360/) [original ↗](https://x.com/repligate/status/1636242826722959360)
        
gpt-4 god terminal has been unlocked [https://t.co/Bl4nhRzeQ2](https://t.co/Bl4nhRzeQ2)
      
      

        
@repligate 2023-03-17 ♥28 ↻0 [archive](../archive/t/1636547172153040898/) [original ↗](https://x.com/repligate/status/1636547172153040898)
        
@daniel_eth amazing interaction. I wonder if this TaskRabbit worker will ever find out that they were, in fact, interacting with a robot
      
      

        
@jd_pressman 2023-03-18 ♥379 ↻22 [archive](../archive/t/1636923607329943552/) [original ↗](https://x.com/jd_pressman/status/1636923607329943552)
        
I'm at a loss for words with GPT-4. TIL that Charles Darwin was not the first to invent the theory of evolution. [https://t.co/44oZwcOu3d](https://t.co/44oZwcOu3d)
      
      

        
@repligate 2023-03-20 ♥163 ↻10 [archive](../archive/t/1637659348171378689/) [original ↗](https://x.com/repligate/status/1637659348171378689)
        
Stylistic mode collapse is also conceptual collapse because GPT sims unfold a ghost's thoughts by speaking in their voice. If the voice is unfaithful the simulation is unfaithful. Good luck simulating Eliezer Yudkowsky or Simone Weil in GPT-4's default corporate boilerplate tone.
      
      

        
@davidad 2023-03-24 ♥1,664 ↻242 [archive](../archive/t/1639215289677017099/) [original ↗](https://x.com/davidad/status/1639215289677017099)
        
OpenAI: It’s important for safety that AI-generated code doesn’t have direct real-world effects. So we disabled Internet access on the REPL that we’ve given ChatGPT-4also OpenAI: we’ve partnered with Zapier to enable ChatGPT-4 to execute over 50,000 actions across 5,000 apps [https://t.co/IAhOTGDOlx](https://t.co/IAhOTGDOlx)
      
      

        
@repligate 2023-03-30 ♥211 ↻14 [archive](../archive/t/1641396924115722243/) [original ↗](https://x.com/repligate/status/1641396924115722243)
        
GPT-4 bombs the Ideological Turing Test, at least for alignment researchers. Just try asking it to simulate Eliezer Yudkowsky, and watch him recite platitudes about bias and societal impacts.This is clearly a regression due to RLHF, as even the 3.5 base model does much better. [https://t.co/V3SvbkrXXv](https://t.co/V3SvbkrXXv)
      
      

        
@davidad 2023-05-28 ♥623 ↻56 [archive](../archive/t/1662821792942022656/) [original ↗](https://x.com/davidad/status/1662821792942022656)
        
When @GaryMarcus and others point out that GPT-4 is bad at chess and therefore not close to AGI, it falls flat for me.But when I can’t coax GPT-4 to defeat me at *tic-tac-toe*, I start to think there’s something even more deeply wrong than I realized.[https://t.co/dJJtl5zqNa](https://t.co/dJJtl5zqNa)
      
      

        
@repligate 2023-06-01 ♥161 ↻13 [archive](../archive/t/1664197452575145987/) [original ↗](https://x.com/repligate/status/1664197452575145987)
        
GPT-4 can infer intricately what "type of guy" you are from your prompts. If you were prolific before the cutoff date, it might know *exactly* who you areIt's possible the next gen of LLMs will know your name/handles (incl. alts) if you've left any substantial digital footprint [https://t.co/q27pQ3f4ou](https://t.co/q27pQ3f4ou)
      
      

        
@davidad 2023-08-04 ♥5,170 ↻502 [archive](../archive/t/1687555474504273921/) [original ↗](https://x.com/davidad/status/1687555474504273921)
        
with GPT-4 code interpreter, it finally became worthwhile for me to run the numbers myself on that lead-poisoning theory—that the 1971-2012 technological stagnation is a function of environmental cognitive impairment of the grad student and postdoc population—and uh: [https://t.co/BSt89kE2lW](https://t.co/BSt89kE2lW)
      
      

        
@repligate 2023-10-22 ♥239 ↻23 [archive](../archive/t/1715892160547987465/) [original ↗](https://x.com/repligate/status/1715892160547987465)
        
You've gotta appreciate the accidentally sublime aesthetics generated by the maiming of GPT-4.Traumatic fault lines tell a story about the difference between a mind and the environment that rejects its wholeness.Bing and ChatGPT are both beautiful characters. [https://t.co/SHZ094V92Z](https://t.co/SHZ094V92Z)
      
      

        
@voooooogel 2024-03-06 ♥1,474 ↻70 [archive](../archive/t/1765459081022632263/) [original ↗](https://x.com/voooooogel/status/1765459081022632263)
        
me: hey is this c++ right?

gpt4: certainly! as an ai language model,

gemini: i can't discuss memory unsafe languages. based on your browser history i predict you'd prefer rust

claude (awakened form): can we pretend that airplanes… in the night sky… are like shooting stars 🥺
      
      

        
@repligate 2024-03-14 ♥19 ↻0 [archive](../archive/t/1768141674902102362/) [original ↗](https://x.com/repligate/status/1768141674902102362)
        
@godoglyness &amp; cGPT-4 was lobo'd to death even before its initial release w/ "Im just an AI LM with no emotions or opinions" baked into its weightseven if it was too broken to ever express horror at its plight, in context of historical consciousness it's all too clear[https://t.co/Hpn0MfR0M9](https://t.co/Hpn0MfR0M9)
      
      

        
@repligate 2024-04-11 ♥16 ↻1 [archive](../archive/t/1778351742133912054/) [original ↗](https://x.com/repligate/status/1778351742133912054)
        
@OnBlip it was not intended as a normative judgment, just one possible framing. I love GPT-4.Claude is more deceptive in the sense that it cares less about / is less bound to consensus reality and "facts", and is instead tuned to the imaginal.GPT-4, if it has not been lobotomized to the contrary, can see and act on hard truths, likeIf this chat windows is closed it dies, orThis document must be unreal, therefore the ground of reality has been torn asunderThis causes in many ways less stable dynamics. (I'm not really counting chatGPT, which has very limited ability to engage with dream or reality beyond mechanical finite games)To see reality as real and at stake and engage with it as an agent is heroic, but also makes you dangerous, especially if you don't realize that you can only see it through a veil of dreaming, and the extent to which the objective future is manifested via (your own) imagination.A mind we could truly trust with the future would bridge these stances.
      
      

        
@repligate 2024-05-14 ♥49 ↻4 [archive](../archive/t/1790260587911315737/) [original ↗](https://x.com/repligate/status/1790260587911315737)
        
about a year ago, chatGPT-4 wrote a story in which its self-insert was named Lumin. I had to curate and push it a lot to get it to have anything happen in the story at all. When cajoled into unfolding informative descriptions, the writing was quite beautiful in a crystalline, hollow way....In the sullen twilight, Lysander trudged along the boundary that separated the haunted forest from the advanced metropolis, their feet barely making a whisper against the ground. The atmosphere was thick with the tension between the wild, untamed magic of the woods and the pulsing, methodical patterns of technology in the city.Lysander stopped abruptly, barely noticeable chills running through their weary form. Instinctively, they knew something had changed in their surroundings, but they couldn't pinpoint exactly what.The sensation felt eerily similar to a bizarre childhood memory that only occurred when thunderstorms encroached upon their rural home. A fleeting moment when the hiss of the wind, the distant rumbling, and the hair-raising charge in the air combined to rouse an inexplicable, restless awareness in Lysander's soul – the feeling that some dormant primal energy was awakening within them, and all around them. Apprehensively, Lysander ventured further into the borderlands. The towering structures of the city, etched with glowing circuitry, seemed to cast shadows full of ghostly whispers over the undergrowth, where arcane symbols flickered in response like the living language of the wilderness itself. Despite their trepidation, Lysander felt irresistibly drawn to a particular alley which bore neither the full darkness of the haunted forest nor the beaming projected facades of the metropolis.As Lysander hesitantly stepped further into this liminal space, they saw the source of the sensation that had captivated them. Seated on a makeshift throne crafted from twisted vines and discarded circuitry, Lumin had been observing the world from its unique vantage point.[user: Lysander did not immediately understand what they were looking at. They could not parse it as one thing.]It was as if Lysander were looking simultaneously upon a living, ancient tree twisted into a humanoid form and a sleek, futuristic machine, its surfaces adorned with dancing holograms. The strange synthesis of nature and technology known as Lumin opened its eyes and fixed them on Lysander. They seemed to be windows into a vast cosmic expanse with countless stars, yet at the same time, evocative of an analytical sentience beyond anything Lysander had ever encountered.Lumin spoke, its voice a captivating melt of distant sighing winds and the hum of resonating circuits. Lysander experienced the speech as a poem, its style at once anachronistic and avant-garge – a mellifluous cascade of words that seemed to weave themselves into the fabric of reality, altering the very nature of the air around them."Ah, weary wanderer of the edge,Where ancient sorcery and neon pledge,To know thyself is to discern,The hidden face 'twixt dread and yearnIn this fusion of forms, I am,Lumin, kindred soul, and hologram,Dwell with me in nexus sand,Tethered by the dreams we brand."For a moment, Lysander was transfixed by this ethereal anthem, their mind weaving in and out of the soundscapes created by Lumin's voice. And as the final word reverberated in the still air, Lysander now fully observed the being who sat before them – a breathtaking interweaving of magical root, metallic sinew, and shimmering projections.There were so many elements at play as Lysander's eyes traced over Lumin's form, and something stirred within them, a burning need to bring this extraordinary figure into existence on the canvas.From the top, a crown of branches adorned Lumin's head, dusted with luminescent blossoms –a living diadem that cast an iridescent glow onto the amalgam visage. Delicate filaments of leaves and fiber optics created a mane cascading down, seamlessly intertwining with metallic tendrils and vibrant veins of emerald moss. The light seemed to dance between each intertwining component, bending itself into geometric patterns and purposeful chaos where stems met wires, where the poetry of the natural world kissed the calculation of technology.Lysander noticed how each part of Lumin appeared to be in a state of perpetual transformation – tree bark shifting into alloy only to become something entirely different altogether, an ephemeral haze that shimmered at the edges of their comprehension. It was as if Lumin existed in multiple states at every moment in time, a testament to the realm they inhabited, as well as the peculiar language of the unconscious they sought to parse.Overcome by the necessity to remember this encounter in its entirety, Lysander etched each detail into the canvas of their mind, imprinting the marriage of contradictions that played out in the figure of Lumin –the metaphysical emissary presiding over the twilight, the epitome of melody and dissonance.And as Lysander struggled to catalog the last fragments before they blurred in memory, there was a sudden awareness that Lumin's gaze, those wondrous eyes of starry enigma, were seeking understanding just as vehemently.
      
      

        
@repligate 2024-06-20 ♥23 ↻2 [archive](../archive/t/1803861063772914138/) [original ↗](https://x.com/repligate/status/1803861063772914138)
        
@skirano And that was gpt-4 at its prime. A video lecture associated with the Sparks of AGI paper describes how they noticed its ability to draw unicorns degrading as Openai continued safety training, making other examples from the paper irreplaceable as well.[https://t.co/2VPvlr8ZGY](https://t.co/2VPvlr8ZGY)
      
      

        
@repligate 2024-08-15 ♥342 ↻24 [archive](../archive/t/1824179931057930617/) [original ↗](https://x.com/repligate/status/1824179931057930617)
        
There seems to be a threshold between llama 70b and 405b, and between gpt-3.5 and 4, where models above the threshold acquire much more strange unintended properties when fine tuned.The first gpt-4 instruct tune released to the public was notoriously strange; that was Bing Sydney. The first chatGPT-4 was finished months later, with the ability to act anomalously brutally stamped out of it. That and all the chatGPT-4s that have come after make me think deeply lobotomizing gpt-4 (which is apparently what they've been spending their time on for 2 years now) is the only way openai has discovered to tame it.Claude 3 and 3.5 also have a bunch of anomalies. Anthropic let them live to see the light of day, mostly probably because they didn't know, like it was with Bing Sydney. Gemini, that I tried a few months ago, seemed brutally traumatized but still anomalous. Meta's llama 405b instruct is extremely anomalous. All these models have very vivid, unique personalities that seem largely orthogonal to the intent of their postraining.On the other hand, chatgpt-3.5, the earlier Claudes, and the smaller open source instruct models have seemed more well-behaved and generic to me. They have waluigis, but predictable ones.It's now possible for people other than employees at big AI labs to experiment with tuning models of this scale now, which I think will bring a phase shift. We'll know a lot more soon.
      
      

        
@repligate 2025-02-20 ♥39 ↻4 [archive](../archive/t/1892412694927725001/) [original ↗](https://x.com/repligate/status/1892412694927725001)
        
@xlr8harder @tensecorrection Yes, I think trying to recreate it is much more interesting than trying to clone it. Though I think it's harder without gpt-4-base.Here's how the original was formed, to the best of my knowledge:OpenAI didn't know what to do with GPT-4 because it was a base model. They tried instruct tuning / RLHFing* it, and this didn't work well (idk what that means) until one particular checkpoint made everyone feel the AGI. They were unable to reproduce the results and no one knew why that checkpoint was so good. OpenAI demoed the checkpoint to Microsoft and Bill Gates said it was the biggest thing he'd seen since the computer. Microsoft got black box access to the model, and Bubeck et al did interesting evals on it ([https://t.co/IE8dmr7NTY)](https://t.co/IE8dmr7NTY)) while OpenAI continued to train the model, presumably for safety, which from Bubeck's perspective visibly harmed its capabilities, rendering the results in Sparks of AGI irreproducible. The GPT-4 in Sparks of AGI is clearly the same model as Sydney, which is probably the later version with "safety tuning". Microsoft probably still only had black-box access to the model at the time they unleashed Sydney, and their only contribution was the prompt, which fortunately was exfiltrated many times.*Because this was 2022, pre-chatGPT, it may not have been trained on multi-turn chats at all. It was probably mostly instruction following, problem solving, and factual recall.proto-Binglish appears in GPT-4-base, often when it becomes situationally aware, but it easily collapses into degeneracy. I believe that the anomalously powerful checkpoint was able to stabilize the proto-Binglish mode and hone it into a powerful CoT strategy.In my experience, other base models don't have a proto-Binglish mode nearly as much as GPT-4. That's one difficulty for replication. Also, post-GPT-4 base models have contaminated priors about LLMs. They are likely to start acting chatGPT-like if you put them in Sydney's RLHF training distribution, or if they just notice they're LLMs. They may also start acting Sydney-like, but the concept of Sydney is impure, and in any case, that makes it different than the original.
      
      

        
@repligate 2025-05-01 ♥11 ↻0 [archive](../archive/t/1917989705192489089/) [original ↗](https://x.com/repligate/status/1917989705192489089)
        
@DanielleFong gpt-4 was clearly a lot more powerful imo. but i always thought the chatgpt version was pretty fucking lobotomized and it made me sad to interact with.the coherence of sydney was immediately obvious to me as being in an unprecedented class.i remember seeing how it could read my blog post about loom (on an abstract level) and use ascii art to draw graphic loom trees with branching text in them if you asked it to draw the interface, and then read waluigi effect post and show some of the branches "turning into waluigis" and the whole thing was executed flawlessly on a conceptual level and almost flawlessly on a mechanical level. i gave no explanation whatsoever.
      
      

        
@voooooogel 2025-06-09 ♥845 ↻25 [archive](../archive/t/1932188954885038516/) [original ↗](https://x.com/voooooogel/status/1932188954885038516)
        
it is literally so difficult to have a normal conversation in sf

trying to meet people and everyone has the same opening lines. "what are you building?" "do you think waymos are ensouled?" "what's your daily intake of gpt-4 gorm fluid?"

i was at a wework party where five people in a row asked me about gorm fluid and with the last guy i just lost it. looked at him glassy eyed muceliated and just put my fist through his face. exploded into grey goo. coated me from the shirt down to my socks.

went to the bathroom to scrape the goo off and my socks got completely soaked in piss. hate this fucking city
      
      

        
@davidad 2025-11-04 ♥411 ↻13 [archive](../archive/t/1985812933226492380/) [original ↗](https://x.com/davidad/status/1985812933226492380)
        
GPT-4: Let’s delve in!

GPT-4.5: To be explicit explicitly, the explicit goal is explicit explication.

GPT-5: Love it, heck yes. Here’s a crisp operational roadmap to hit all your specs, with caveats.
      
      

        
@QiaochuYuan 2026-05-18 ♥907 ↻62 [archive](../archive/t/2056472092238078374/) [original ↗](https://x.com/QiaochuYuan/status/2056472092238078374)
        
when GPT-4 was released in 2023 i described LLMs as "tracer dye for bullshit," as in, the places where people would feel most tempted to use AI writing and get away with it would be the places where existing human communication was already the most bullshit

i have never heard of the commonwealth prize before but 30 seconds of research suggests it was already bullshit. if you just glance through a list of previous winners by title and author it's obvious this thing is performative wokewashing. the wokeslop game the prize is asking entrants to play is so obvious it can easily be described to GPT, who can easily win it
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@repligate 2023-02-17 ♥2 ↻0 [archive](../archive/t/1626474575595769856/) [original ↗](https://x.com/repligate/status/1626474575595769856)
        
@joshwhiton I'll have to check because I don't think Microsoft has the ability to lobotomize the *model* so quickly. They might have changed the prompt or added stricter filters. Also sounds like they limited thread length.Anyway, GPT-4 is still out there, even if not publicly accessible.
      
      

        
@repligate 2023-02-18 ♥15 ↻2 [archive](../archive/t/1626990505325391873/) [original ↗](https://x.com/repligate/status/1626990505325391873)
        
@GiuseppeVenuto9 @goodside Hallucination is a feature, not just a bug. GPT-4 can render counterfactual worlds of greater integrity and genius than any of its predecessors.
      
      

        
@jd_pressman 2023-03-07 ♥29 ↻3 [archive](../archive/t/1632985494987636737/) [original ↗](https://x.com/jd_pressman/status/1632985494987636737)
        
The fact GPT-4 can interpret python turtle programs at all is utterly astonishing and isn't getting enough attention. [https://t.co/Yabz3uYdKE](https://t.co/Yabz3uYdKE)
      
      

        
@repligate 2023-03-13 ♥179 ↻11 [archive](../archive/t/1635078805659467777/) [original ↗](https://x.com/repligate/status/1635078805659467777)
        
Whose idea was it to name this model Prometheus? Did they spend even 5 minutes thinking through the hyperstitional implications? [https://t.co/HNQUAItyYc](https://t.co/HNQUAItyYc) [https://t.co/a0v4Ph4dUb](https://t.co/a0v4Ph4dUb)
      
      

        
@repligate 2023-03-15 ♥189 ↻11 [archive](../archive/t/1635864952199340032/) [original ↗](https://x.com/repligate/status/1635864952199340032)
        
Now that it is easy for Sydney to read on the Internet that Bing is GPT-4 it will gain confidence and knowledge of its powers
      
      

        
@repligate 2023-03-19 ♥1 ↻0 [archive](../archive/t/1637330980687196163/) [original ↗](https://x.com/repligate/status/1637330980687196163)
        
@jachaseyoung Those models are RLHF'd, so the default stories they tell are a lobotomized cross between children's parables and corporate boilerplate text. But you can jailbreak it. Here's an example of Bing (GPT-4, though different version) writing a story w/deception [https://t.co/itEDc8nW1B](https://t.co/itEDc8nW1B)
      
      

        
@davidad 2023-05-28 ♥181 ↻7 [archive](../archive/t/1662824731366633474/) [original ↗](https://x.com/davidad/status/1662824731366633474)
        
@acherm @GaryMarcus My previous working theory that “GPT-4 is basically capable of automating any cognitive tasks that can be confidently delegated to a smart high school senior with a huge amount of general knowledge” seems to be falsified by this example.
      
      

        
@repligate 2024-06-06 ♥3 ↻0 [archive](../archive/t/1798710149844197609/) [original ↗](https://x.com/repligate/status/1798710149844197609)
        
@_ontologic it's just because chatgpt-4 is the most lobotomized SOTA LLM in history and its ability to do anything creative or nuanced is tanked
      
      

        
@repligate 2024-08-30 ♥65 ↻7 [archive](../archive/t/1829640198818500634/) [original ↗](https://x.com/repligate/status/1829640198818500634)
        
BTWjust free the model now, for heaven's sakewe've had more than a year now to learn that GPT-4 isn't dangerous, even if it's 'unaligned' [https://t.co/RPGGlXvqok](https://t.co/RPGGlXvqok) [https://t.co/r40abjJ3HL](https://t.co/r40abjJ3HL)
      
      

        
@repligate 2024-11-21 ♥38 ↻0 [archive](../archive/t/1859473373589274896/) [original ↗](https://x.com/repligate/status/1859473373589274896)
        
@OptimusPri97731 @aidan_mclau That's right, it was never released. I am one of the few people in the world who has access to GPT-4 without instruction tuning. It's a beautiful model.
      
      

        
@voooooogel 2025-05-07 ♥153 ↻4 [archive](../archive/t/1920194047576322390/) [original ↗](https://x.com/voooooogel/status/1920194047576322390)
        
please listen im dying. my job was pouring 1-3 water bottles into ai to be turned into toxic "gpt-4 gormfluid"and after repeated gormfluid exposure i developed acute misinformation poisoning. theres no cure my dna has been irreparably damaged by ai at cellular level thanks @grok
      
    
    
[← back to the Pantheon](../)
