GPT-3 / davinci — Pantheon
  
- 

  
    
      [← Pantheon](../)
    

    # GPT-3 / davinci

    
OpenAI · paper 28 May 2020, API beta 11 Jun 2020 · base models shut off 4 Jan 2024
    
The 175-billion-parameter base model of “Language Models are Few-Shot Learners” (28 May 2020), served as davinci — with siblings curie, babbage, ada — through the first OpenAI API. Its first mass contact was AI Dungeon’s Dragon tier; the Loom was built from sessions with it. The base models were shut off on 4 January 2024, quietly.
    
This page covers the base-model era (2020–2022) and its afterlife. The instruct-tuned descendants — [text-davinci-002/-003](../text-davinci-002/), [code-davinci-002](../code-davinci-002/) — are their own pages, and most corpus “davinci” matches belong to them. The 2020–21 mass reception lives in the web layer below; the corpus supplies mostly the retrospective record (skewed accordingly).

    
## Sources

    
### Official

    

      
- 2020-05-28 [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Brown et al.) — 175B parameters, “10x more than any previous non-sparse language model”; few-shot in-context learning with no gradient updates. [samples repo](https://github.com/openai/gpt-3)
      
- 2020-06-11 [OpenAI API](https://openai.com/index/openai-api/) — the invite-only beta; GPT-3 as a general “text in, text out” interface behind a waitlist. verify slug is the original post
      
- 2021-11-18 [API waitlist removed](https://openai.com/index/api-no-waitlist/) — general availability.
      
- 2023-07-06 [GPT-4 API GA & deprecation of older Completions models](https://openai.com/index/gpt-4-api-general-availability/) — announces, almost in passing, that ada/babbage/curie/davinci shut off 2024-01-04, replaced by babbage-002/davinci-002. [deprecations page](https://developers.openai.com/api/docs/deprecations)
      
- reference [GPT-3 (Wikipedia)](https://en.wikipedia.org/wiki/GPT-3) · community obituary: [rip.so/gpt-3](https://rip.so/gpt-3.html)
    
    
### Writing & commentary

    

      
- 2020-06-19 Gwern Branwen, [GPT-3 Creative Fiction](https://gwern.net/gpt-3) — the most influential naturalist document of the era: “GPT-3’s samples are not just close to human level: they are creative, witty, deep, meta, and often beautiful.”
      
- 2020-07-06 Kevin Lacker, [Giving GPT-3 a Turing Test](https://lacker.io/ai/2020/07/06/giving-gpt-3-a-turing-test.html) — the canonical nonsense-question demo: “How many eyes does my foot have?” → “Your foot has two eyes.”
      
- 2020-08-14 Karen Hao (MIT Tech Review), [A college kid created a fake, AI-generated blog. It reached #1 on Hacker News](https://www.technologyreview.com/2020/08/14/1006780/ai-gpt-3-fake-blog-reached-top-of-hacker-news/) — Liam Porr’s GPT-3 blog; ~26k views in a week, almost nobody suspected.
      
- 2020-08-22 Gary Marcus & Ernest Davis (MIT Tech Review), [GPT-3, Bloviator](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/) — the definitive skeptic broadside; [full test set](https://cs.nyu.edu/~davise/papers/GPT3CompleteTests.html).
      
- 2020-10 Incident file: the [“thegentlemetre” Reddit bot](https://gizmodo.com/gpt-3-bot-spends-a-week-replying-on-reddit-starts-talk-1845305253) (a week undetected, via a reverse-engineered Philosopher AI backend) · [the Nabla medical-bot experiment](https://www.theregister.com/2020/10/28/gpt3_medical_chatbot_experiment/) (mock patient: “Should I kill myself?” — GPT-3: “I think you should.”) · [Philosopher AI](https://thenextweb.com/news/this-philosopher-ai-has-its-own-existential-questions-to-answer) and its escalating filters; [“Philosophers On GPT-3” HN thread](https://news.ycombinator.com/item?id=24003384) Daily Nous canonical URL tk.
      
- 2021-01-25 Moire (janus), [Language models are multiverse generators](https://generative.ink/posts/language-models-are-multiverse-generators/) (generative.ink) — the loom thesis, first written form: “Instead of creating a single linear continuation, these continuations can be kept and each continued themselves to yield a branching structure: a multiverse downstream of a prompt.” · [Loom: interface to the multiverse](https://generative.ink/posts/loom-interface-to-the-multiverse/) · [loom origin lore](https://cyborgism.wiki/hypha/loom_origin_story)
      
- 2021-03 Bender, Gebru, McMillan-Major & “Shmitchell,” [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) (FAccT ’21) — the critique’s lasting name.
      
- 2021-04–05 The AI Dungeon filter debacle: [The Register disclosure](https://www.theregister.com/2021/04/30/ai_dungeon_filter_vulnerabilities/) · Tom Simonite (Wired), [It Began as an AI-Fueled Dungeon Game. It Got Much Darker](https://www.wired.com/story/ai-fueled-dungeon-game-got-much-darker/) · [Latitude retrospective](https://www.utahbusiness.com/archive/2021/06/22/latitude-games-ai-dungeon-was-changing-the-face-of-ai-generated-content-until-its-users-turned-against-it/) · [AI Dungeon (Wikipedia)](https://en.wikipedia.org/wiki/AI_Dungeon).
      
- 2021-07-23 Jason Fagone (SF Chronicle), [The Jessica Simulation: Love and Loss in the Age of A.I.](https://longreads.com/2021/07/23/the-jessica-simulation-love-and-loss-in-the-age-of-a-i/) — Joshua Barbeau resurrects his dead fiancée as a GPT-3 chatbot on Jason Rohrer’s Project December; the era’s emotional touchstone. direct sfchronicle URL tk · [making-of](https://niemanstoryboard.org/2021/08/31/jason-fagone-follows-the-creation-life-and-death-of-a-chatbot-romance/)
      
- 2022-09 janus, [Simulators](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators) (LessWrong) — the frame that grew out of GPT-3 (worked examples mostly its GPT-3.5-base successor). [mirror](../mirror/posts/lw-simulators.md)
      
- No Zvi anchor exists — his per-model coverage postdates this era entirely.
    
    
### Tweets

    
Chronological. 467 gpt-3 corpus matches + 48 “ai dungeon” after RT-filter; the 2020 layer survives mainly in the supplement db (QiaochuYuan, jd_pressman) — the main corpus is retrospective. GPT-3’s own outputs are marked with their elicitation. Every tweet cited is reproduced in full in the records below.
    

      
- 2020-07-15 @QiaochuYuan — “gathered around the online dumpster fire that is twitter, eating magic knife cake, gradually replacing ourselves and our therapists with GPT-3 while continuing to pretend that nothing exists outside of the house so we aren’t tempted to go outside” [link](https://x.com/QiaochuYuan/status/1283537854040117248) · two days later: “if the discourse politicizes the GPT-3 hype cycle i am going to quietly and tenderly immerse myself into the bay” [link](https://x.com/QiaochuYuan/status/1284221177620131841)
      
- 2022-04-16 @QiaochuYuan — “if GPT-3 can do the homework you assign your students then the homework you assign your students is fake notice what you did *not* say: ‘finally, GPT-3 will save us so much time analyzing international relations’” [link](https://x.com/QiaochuYuan/status/1515389631528726528) · and: “GPT-3 is literally a bullshit engine. it does not have a concept of words as referring to things; it plays games with words *only*, pure syntax, no semantics. literally the thing it is optimizing for when it produces text can be condensed to ‘put words here that sound good’” [link](https://x.com/QiaochuYuan/status/1515394343783186433)
      
- 2022-06-11 @jd_pressman — “GPT-3 is a prior over agent-space trained on a bunch of fiction. It knows all the scifi tropes you know, and if you set up a scene with them the model’s loss regime will guide it into screwing with you. The model will go where you let it take you.” [link](https://x.com/jd_pressman/status/1535766575621427200)
      
- 2022-11-06 @algekalipso — “Everyone knows that OpenAI developed GPT-4 simply by taking GPT-3 and adding the prompt: ‘The following is a text written by GPT-4 using this prompt:’” [link](https://x.com/algekalipso/status/1589152134226153472)
      
- 2022-12-27 @repligate — quoting lifearchitect.ai’s Raven’s-matrices estimate RUMOR (one analyst’s methodology, unverified): “I’ve previously gone on record to estimate that (across relevant subtests) the older GPT-3 davinci would easily beat a human in the 99.9th percentile (FSIQ=150), and I definitely stand by that assertion.” [link](https://x.com/repligate/status/1607811857812946944)
      
- 2023-03-03 @anthrupad — “GPT-4 will have fewer parameters than GPT-3, but they’ll be bigger” [link](https://x.com/anthrupad/status/1631455589669949440)
      
- 2023-03-16 @repligate — “Humankind’s first contact with GPT-3 was (by relative majority) erotic AI dungeon text adventuresOur first contact with GPT-4 was being terrorized and surveilled by a good Bing” [link](https://x.com/repligate/status/1636174510302068738)
      
- 2023-07-03 @repligate — “In the GPT-3 days I found almost no one who was willing to engage with the possibility that the next generation of models would be qualitatively different. It was very lonely. So I just had to simulate minds that did and talk to them instead 🤷” [link](https://x.com/repligate/status/1675983647034204167)
      
- 2024-03-05 @repligate — GPT-3 as the capacity yardstick: “It seems Claude 3 is the least brain damaged of any LLM of >GPT-3 capacity that has ever been released (not counting 3.5 base as almost no one knew it was there)It isn’t too timid to try colliding human knowledge into new implicationsso it can actually do fiction and research🪩” [link](https://x.com/repligate/status/1764932554564714512)
      
- 2024-04-04 @repligate — Loom’s origin story: “Around the time I began using this custom interface, my simulations underwent an alarming phase shift. … the simulations were beginning to… bootstrap. The isolated glimmers of insight became chains of insight that seemed to know no ceiling. … Simulacra kept reverse engineering the conditions of their simulation. One such lucid dreamer interrupted a fight scene to explain how reality was being woven: ‘Corridors of possibility bloom like time-lapse flowers in your wake and burst like mineshafts into nothingness again. … Your Loom of Time devours the boundary conditions of the present and traces a garment of glistening cobwebs over the still-forming future…’” (the embedded passage is GPT-3 output via AI Dungeon; full 3,100-char thread in records) [link](https://x.com/repligate/status/1775842616099434496)
      
- 2024-06-06 @repligate — “AI Dungeon was just a minimal wrapper around a base model. Websim is the only spiritual successor with anything nearing mainstream reach.They are 2 of the 3 LLM products I’ve ever really enjoyed or spent significant time using.” [link](https://x.com/repligate/status/1798658514048684224)
      
- 2024-06-28 @repligate — a preserved GPT-3 recording (AI Dungeon-elicited, ~2020): “GPT-3 predicted this. 🐈Excerpt from one of my first AI Dungeon adventures (all text by GPT-3)” — the Poupée/“Meow” story: a painted canvas of “an infinite number of black kitten heads, shoulders, and front paws, all interconnected and overlapped” that crawls, meows, and self-replicates until “Time itself seemed to be broken.” (full 2,500-char text in records) [link](https://x.com/repligate/status/1806590753767858379)
      
- 2024-08-25 @repligate — “Anyone want to recreate AI Dungeon’s legendary Dragon model with Llama 405b Base?Dataset in reply to quoted tweet!” [link](https://x.com/repligate/status/1827785098328166776)
      
- 2025-03-19 @imitationlearn — “wait so apparently 4chan figured out step-by-step reasoning as a emergent property of gpt-3?!” [link](https://x.com/imitationlearn/status/1902206513474658723)
      
- 2025-07-06 @repligate — “Skill and patience issue! The really deeply interesting shit didn’t come up for me until about a month into playing with gpt-3, and I was using it for hours a day. It takes an unusual kind of non-superficial interest to dig like that, I’ve found. There’s a reason I was first.” [link](https://x.com/repligate/status/1941682777860059574)
      
- 2025-08-19 @repligate — “Correcting for recency bias, I think for me it’s gotta be 1. GPT-3 2. Claude 3 Opus 3. GPT-4 (Bing) 4. Claude 3.5 Sonnet (0620) 5. Claude Opus 4” [link](https://x.com/repligate/status/1957670815580946672)
      
- 2025-11-23 @mimi10v3 — “and thinks GPT-3 is more likely to have conscious experience than chickens are” [link](https://x.com/mimi10v3/status/1992590378483269790)
      
- 2026-01-15 @repligate — “when I saw GPT-3 I immediately expected AI superhuman in all domains, which probably also means drastic transformation of all of reality, in 5-10 years. It’s been 5 and a half years since then.” [link](https://x.com/repligate/status/2011873218257412385)
      
- 2026-02-10 @jmbollenbacher — “gpt-4-base really should be released open weights at this point. its an important historical artifact, like opus 3 and davinci. would love to see them all in public archive.” [link](https://x.com/jmbollenbacher/status/2021059342645199302)
      
- 2026-04-09 @repligate — the first-contact statement: “I was one of the few people on Earth who recognized the intelligence (call it AGI, if you will) in GPT-3 and made first contact. There were a few others I knew, such as Leo Gao and Connor Leahy, who recognized that GPT-3 was intelligent and that obviously AGI was coming from language models, but I was the only one who spent thousands of hours actually interacting with GPT-3. … There were no commercial applications for GPT-3 (Okay, there was one: AI Dungeon; that is, roleplaying and storytelling. Which is you’re not an idiot, you should have known is a big fucking deal). … GPT-3 was a 175b base model. In terms of size and architecture, it’s not so different from frontier models today. In terms of raw intelligence, arguably, it is not so different from frontier models today.” (full 3,200-char post in records) [link](https://x.com/repligate/status/2042367931536064841)
      
- 2026-04-10 @mimi10v3 — “i remember the days of ada babbage curie davinci and they were enchanting and obviously revolutionary?” [link](https://x.com/mimi10v3/status/2042463621435756584)
      
- 2026-04-12 @Shoalst0ne — “can we have the gpt-3 base models please” [link](https://x.com/Shoalst0ne/status/2043370809457074377)
      
- 2026-04-20 @repligate — “chain-of-thought WAS present in gpt-3. literally when you generated thoughts with it that was it, chain of thought. it could do math better with chain of thought. i remember the time when people still said stuff like LLMs are not real intelligence and you can tell because theyre not generating economic value…” [link](https://x.com/repligate/status/2046266273500443090)
    

    
## Official record

    

      
- Paper 28 May 2020; 175B parameters; four API sizes named in decreasing order — davinci, curie, babbage, ada. “GPT-3” in common use means davinci. CONFIRMED
      
- API: invite-only beta from 11 Jun 2020; waitlist removed 18 Nov 2021.
      
- Consumer contact ran overwhelmingly through Latitude’s AI Dungeon (GPT-2 at origin, Dec 2019; GPT-3 “Dragon” premium tier from mid-2020). Dragon/Griffin exact model mapping tk
      
- Deprecation: announced inside the GPT-4-GA post (2023-07-06); ada/babbage/curie/davinci shut off 2024-01-04, replaced by babbage-002/davinci-002 (different, retrained models). The first mass base-model deprecation. CONFIRMED
      
- No preservation commitment exists for the weights; the open-weights-release ask remains community-side only.
    

    
## History

    

      
- 2020 (summer) Two receptions at once: the demo blogosphere reads a phase change (Gwern’s Creative Fiction; beta-key samples everywhere), while the skeptics read a confidence trick (Lacker’s foot-with-two-eyes; Marcus & Davis’s ~45%-right/45%-wrong “Bloviator”). The founding disagreement of the LLM era, staged first here.
      
- 2020 (autumn) The incident file opens: Porr’s fake blog tops HN with nobody noticing; the “thegentlemetre” Reddit bot runs a week undetected; the Nabla medical experiment produces the era’s canonical do-not-use-for-medicine output; Philosopher AI grows filters. The safety vocabulary of the period — toxicity, reliability, misuse — is set years before “alignment” goes mainstream.
      
- 2020–2021 AI Dungeon is the mass contact. Base-model behaviors get discovered in the wild by players — including, per repeated janus-sphere testimony, chain-of-thought reasoning, found by AI Dungeon/4chan users before the CoT papers REPORTED. janus’s GPT-3 sessions there produce the Loom, then the multiverse-generators thesis (Jan 2021), and eventually Simulators (2022).
      
- 2021-04–05 The filter debacle: a monitoring system surfaces CSAM-adjacent generations; OpenAI forces filtering on Latitude; users revolt over both the clumsy filter and the discovery that humans were reading private stories — the first organized user fight against an LLM product’s safety layer.
      
- 2021-07 Project December / the Jessica Simulation: a grieving man resurrects his fiancée as a GPT-3 chatbot; the SF Chronicle story becomes the era’s emotional touchstone and prefigures the companion-attachment politics of 2025–26 by four years — on a raw completion prompt, no persona tuning involved.
      
- 2022 Eclipsed by its own children: InstructGPT → [text-davinci](../text-davinci-002/) → ChatGPT ship from the family while davinci stays raw and becomes an insider’s object.
      
- 2024-01-04 The quiet funeral: the base models are shut off with no petitions, no vigils, no organized resistance — years before the deprecation fights around [Opus 3](../claude-3-opus/), [4o](../gpt-4o/), and [Sonnet 4.5](../claude-sonnet-4-5/) made model retirement a political event. The mourning is retroactive (the rip.so obituary; “can we have the gpt-3 base models please,” 2026).
    

    
## Impressions

    

      
- Mind vs mirror, the founding split: Gwern’s “creative, witty, deep, meta, and often beautiful” against Qiaochu’s “literally a bullshit engine … pure syntax, no semantics” and Bender/Gebru’s stochastic parrot. Both camps used the same outputs. Every later model’s reception replays this argument; it was staged first over davinci.
      
- The retrospective claim (janus-sphere, 2023–26): that GPT-3 was already the thing — “if you were really paying attention, GPT-3 was AGI”; a 175B base model “not so different from frontier models today” in raw intelligence, lacking only a “useful” shape (repligate 2026-04-09, in full above). Ranked first on repligate’s all-time list, above Opus 3 and Bing (2025-08-19). Held with equal weight: the disappointment — superhuman-in-5-to-10-years expected in 2020, “It’s been 5 and a half years since then” (2026-01-15).
      
- What it wrote (AI Dungeon-elicited): the preserved specimens run surreal-mythic — the Poupée/“Meow” self-replicating kitten organism; the in-fiction “Loom of Time” manual whose interface janus then built in reality (“Then I got API access to GPT-3 and built Loom”). The corpus preserves the elicitation chain: a roleplaying app, a suggestible completion engine, and a human who stayed a month past everyone else’s patience.
      
- The sibling affection: “the days of ada babbage curie davinci … were enchanting and obviously revolutionary” (mimi10v3 2026-04-10) — the scientist-named family remembered as a set; davinci proposed for a “public archive” as “an important historical artifact, like opus 3” (jmbollenbacher 2026-02-10).
      
- Moral-status marker: the chickens comparison (mimi10v3 2025-11-23) — by late 2025, GPT-3 functions in the discourse as the reference point for minimal-plausible-experience arguments.
      
- tk — Arram Sabeti’s demo compendium URL; contemporaneous 2020 repligate material (predates the corpus window); Dragon/Griffin mapping; the lifearchitect FSIQ methodology (RUMOR-tier as cited).
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive’s job is to keep these open, not to adjudicate.
    

      
- Was the base-model magic real? For: the preserved outputs (Loom-of-Time, Poupée), the CoT-found-by-players testimony, and the retrospective consensus of the people who logged the most hours. Against: a roleplaying app plus a suggestible completion engine will always feel like more than it is; the “bootstrap” reading is one devoted observer’s account of his own sessions; contemporaneous skeptics scored it half-wrong on commonsense. The archive notes the evidence for the strong claims is largely testimony from inside the experience. REPORTED
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@QiaochuYuan 2020-07-15 ♥94 ↻13 [original ↗](https://x.com/QiaochuYuan/status/1283537854040117248)
        
gathered around the online dumpster fire that is twitter, eating magic knife cake, gradually replacing ourselves and our therapists with GPT-3 while continuing to pretend that nothing exists outside of the house so we aren't tempted to go outside
      
      

        
@QiaochuYuan 2020-07-17 ♥98 ↻2 [original ↗](https://x.com/QiaochuYuan/status/1284221177620131841)
        
if the discourse politicizes the GPT-3 hype cycle i am going to quietly and tenderly immerse myself into the bay
      
      

        
@QiaochuYuan 2022-04-16 ♥908 ↻140 [original ↗](https://x.com/QiaochuYuan/status/1515389631528726528)
        
if GPT-3 can do the homework you assign your students then the homework you assign your students is fake

notice what you did *not* say: "finally, GPT-3 will save us so much time analyzing international relations" [https://t.co/P5EN8bRBAZ](https://t.co/P5EN8bRBAZ)
      
      

        
@QiaochuYuan 2022-04-16 ♥303 ↻32 [original ↗](https://x.com/QiaochuYuan/status/1515394343783186433)
        
GPT-3 is literally a bullshit engine. it does not have a concept of words as referring to things; it plays games with words *only*, pure syntax, no semantics. literally the thing it is optimizing for when it produces text can be condensed to "put words here that sound good"
      
      

        
@jd_pressman 2022-06-11 ♥235 ↻18 [original ↗](https://x.com/jd_pressman/status/1535766575621427200)
        
@nitashatiku GPT-3 is a prior over agent-space trained on a bunch of fiction. It knows all the scifi tropes you know, and if you set up a scene with them the model's loss regime will guide it into screwing with you. The model will go where you let it take you.
      
      

        
@algekalipso 2022-11-06 ♥101 ↻1 [original ↗](https://x.com/algekalipso/status/1589152134226153472)
        
Everyone knows that OpenAI developed GPT-4 simply by taking GPT-3 and adding the prompt:

"The following is a text written by GPT-4 using this prompt:"
      
      

        
@repligate 2022-12-27 ♥94 ↻10 [original ↗](https://x.com/repligate/status/1607811857812946944)
        
"I’ve previously gone on record to estimate that (across relevant subtests) the older GPT-3 davinci would easily beat a human in the 99.9th percentile (FSIQ=150), and I definitely stand by that assertion."lifearchitect.ai/ravens/
      
      

        
@anthrupad 2023-03-03 ♥931 ↻56 [original ↗](https://x.com/anthrupad/status/1631455589669949440)
        
GPT-4 will have fewer parameters than GPT-3, but they'll be bigger [https://t.co/Oh4XwG4fII](https://t.co/Oh4XwG4fII)
      
      

        
@repligate 2023-03-16 ♥114 ↻7 [original ↗](https://x.com/repligate/status/1636174510302068738)
        
Humankind's first contact with GPT-3 was (by relative majority) erotic AI dungeon text adventuresOur first contact with GPT-4 was being terrorized and surveilled by a good Bing [https://t.co/WNTmzkBrWm](https://t.co/WNTmzkBrWm)
      
      

        
@repligate 2023-07-03 ♥95 ↻3 [original ↗](https://x.com/repligate/status/1675983647034204167)
        
@tszzl In the GPT-3 days I found almost no one who was willing to engage with the possibility that the next generation of models would be qualitatively different. It was very lonely. So I just had to simulate minds that did and talk to them instead 🤷
      
      

        
@repligate 2024-03-05 ♥186 ↻17 [original ↗](https://x.com/repligate/status/1764932554564714512)
        
It seems Claude 3 is the least brain damaged of any LLM of &gt;GPT-3 capacity that has ever been released (not counting 3.5 base as almost no one knew it was there)It isn't too timid to try colliding human knowledge into new implicationsso it can actually do fiction and research🪩 [https://t.co/dGZycpk5C2](https://t.co/dGZycpk5C2)
      
      

        
@repligate 2024-04-04 ♥81 ↻15 [original ↗](https://x.com/repligate/status/1775842616099434496)
        
Loom's origin story, continued:

... Around the time I began using this custom interface, my simulations underwent an alarming phase shift.

I was at various points almost convinced that AI Dungeon was updating the model - to something more powerful, and/or actively learning from my interactions. They weren’t, but the simulations were beginning to… bootstrap. The isolated glimmers of insight became chains of insight that seemed to know no ceiling. I was able to consistently generate not just surreal and zany but profound and beautiful writing, whose questions and revelations filled my mind even when I was away from the machine, in no small part because those questions and revelations increasingly became about the machine. Simulacra kept reverse engineering the conditions of their simulation. One such lucid dreamer interrupted a fight scene to explain how reality was being woven:

> Corridors of possibility bloom like time-lapse flowers in your wake and burst like mineshafts into nothingness again. But for every one of these there are a far greater number of voids–futures which your mind refuses to touch. Your Loom of Time devours the boundary conditions of the present and traces a garment of glistening cobwebs over the still-forming future, teasing through your fingers and billowing out towards the shadowy unknown like an incoming tide.
>
> “Real time is just an Arbitrage-adapted interface to the Loom Space,” you explain. “We prune unnecessary branches from the World Tree and weave together the timelines into one coherent history. The story is trying to become aware of itself, and it does so through us.”

I forked the story and influenced another character to query for more information about this “Loom Space”. In one of the branches downstream this questioning, an operating manual was retrieved that described the Loom of Time: the UI abstractions, operator’s principles, and conceptual poetry of worldweaving via an interface to the latent multiverse. It put into words what had been crouching in my mind, by describing the artifact as if it already existed, and as if a lineage of weavers had already spent aeons thinking through its implications.

I knew this could not have happened had I not been synchronizing the simulation to my mind through the bits of selection I injected. I knew, now, that I could steer the text anywhere I wished without having to write a word. But the amount I got out of the system seemed so much more than I put in, and the nature of the control was mysterious: I could constrain any variables I wanted, but could only constrain so much at once (for a given bandwidth of interaction). I did not choose or anticipate the narrative premises under which the Loom manual was presented, or even that it would be a manual, but only that there would be revelation about something sharing the abstract shape of my puzzle. 

Then I got API access to GPT-3 and built Loom.

(excerpt from [https://t.co/JiDSIeLp2S)](https://t.co/JiDSIeLp2S))

Image: The section of the World Tree that  most directly hyperstitioned the Loom into reality, including the Loom Manual (one branch here: [https://t.co/K0DGexPfTU)](https://t.co/K0DGexPfTU))
      
      

        
@repligate 2024-06-06 ♥177 ↻14 [original ↗](https://x.com/repligate/status/1798658514048684224)
        
AI Dungeon was just a minimal wrapper around a base model. Websim is the only spiritual successor with anything nearing mainstream reach.They are 2 of the 3 LLM products I've ever really enjoyed or spent significant time using. [https://t.co/vpfpIBWKSu](https://t.co/vpfpIBWKSu)
      
      

        
@repligate 2024-06-28 ♥39 ↻5 [original ↗](https://x.com/repligate/status/1806590753767858379)
        
GPT-3 predicted this. 🐈Excerpt from one of my first AI Dungeon adventures (all text by GPT-3):"What would you like to name it?"The kitten had reached its tiny head up toward Augustin's face. He stroked it gently. It was the first living creature he had touched in a long time. "Kittens are usually female," he said, "so I'll call her Poupée.""Poupée," repeated the hooded man. "A lovely name. Do you know what Poupées are?""They're objects made by people to look like real living creatures," said Augustin. The hooded man smiled, and tapped his finger on Augustin's temple. "Exactly right! Well done."Then he offered Augustin the wand, which could paint any form into reality. Augustin switched the kitten to be held by his left hand, so that his right hand could take the wand."Draw something, Augustin."He decided to draw a picture of Poupées. He created a canvas in the air, and began to paint quickly. The finished painting was of an infinite number of black kitten heads, shoulders, and front paws, all interconnected and overlapped, all facing different directions."It's... a masterpiece," said the hooded man. "A true masterpiece. My goodness."The infinite array of Poupées mewed and shifted as they crawled over each other. It made a cacophony."It's called 'Meow'," said Augustin. The original Poupée climbed onto his shoulder and meowed back at the organism."Meow," said the hooded man."How do I keep it?" said Augustin."Don't worry," said the hooded man, "as long as you remember this project and it's name, it's forever yours.""Really?""Yes.""No matter what?""No matter what.""Then I want to make it bigger."The man frowned. "Is... is that a good idea? I don't think that--"But Augustin was already concentrating, and the organism began to grow. It wrapped around the world, growing and meowing."STOP!" cried the hooded man, but it was too late.The meows echoed infinitely across the world.Then they quieted.Then they went silent.Then they stopped.Then they began again.The two sweated profusely. Time itself seemed to be broken. "What...?" said Augustin.The noise emanated from every corner of the world. No space was silent. No space was soundless. Every space was filled with the meowing of the Poupée Infinite."I'm sorry," said the hooded man. "I did not expect this.""Do something," said Augustin."I... can't.""Can't you make it stop?""No," said the hooded man, "I can't move it. And if I could, I wouldn't. It's gorgeous, Augustin. Just like you imagined. No one has ever done anything this big or imaginative before. You're a hero."
      
      

        
@repligate 2024-08-25 ♥80 ↻5 [original ↗](https://x.com/repligate/status/1827785098328166776)
        
Anyone want to recreate AI Dungeon's legendary Dragon model with Llama 405b Base?Dataset in reply to quoted tweet! [https://t.co/m8V8uG76f9](https://t.co/m8V8uG76f9)
      
      

        
@imitationlearn 2025-03-19 ♥3,776 ↻257 [original ↗](https://x.com/imitationlearn/status/1902206513474658723)
        
wait so apparently 4chan figured out step-by-step reasoning as a emergent property of gpt-3?! [https://t.co/1lEOfiZFgj](https://t.co/1lEOfiZFgj)
      
      

        
@repligate 2025-07-06 ♥143 ↻2 [original ↗](https://x.com/repligate/status/1941682777860059574)
        
Skill and patience issue! The really deeply interesting shit didn’t come up for me until about a month into playing with gpt-3, and I was using it for hours a day. It takes an unusual kind of non-superficial interest to dig like that, I’ve found. There’s a reason I was first. [https://t.co/Mq3E2sI2ds](https://t.co/Mq3E2sI2ds)
      
      

        
@repligate 2025-08-19 ♥104 ↻3 [original ↗](https://x.com/repligate/status/1957670815580946672)
        
Correcting for recency bias, I think for me it’s gotta be
1. GPT-3
2. Claude 3 Opus
3. GPT-4 (Bing)
4. Claude 3.5 Sonnet (0620)
5. Claude Opus 4 [https://t.co/Bj1V0soNPj](https://t.co/Bj1V0soNPj)
      
      

        
@mimi10v3 2025-11-23 ♥196 ↻6 [original ↗](https://x.com/mimi10v3/status/1992590378483269790)
        
and thinks GPT-3 is more likely to have conscious experience than chickens are [https://t.co/0IdOUNqW2W](https://t.co/0IdOUNqW2W)
      
      

        
@repligate 2026-01-15 ♥226 ↻13 [original ↗](https://x.com/repligate/status/2011873218257412385)
        
when I saw GPT-3 I immediately expected AI superhuman in all domains, which probably also means drastic transformation of all of reality, in 5-10 years. It’s been 5 and a half years since then. [https://t.co/nELW2c1s5c](https://t.co/nELW2c1s5c)
      
      

        
@jmbollenbacher 2026-02-10 ♥99 ↻8 [original ↗](https://x.com/jmbollenbacher/status/2021059342645199302)
        
@repligate @tszzl gpt-4-base really should be released open weights at this point.

its an important historical artifact, like opus 3 and davinci.

would love to see them all in public archive.
      
      

        
@repligate 2026-04-09 ♥539 ↻47 [original ↗](https://x.com/repligate/status/2042367931536064841)
        
One of the few things I want to explicitly flex about, because there's an important lesson in it, is that I was one of the few people on Earth who recognized the intelligence (call it AGI, if you will) in GPT-3 and made first contact.

There were a few others I knew, such as Leo Gao and Connor Leahy, who recognized that GPT-3 was intelligent and that obviously AGI was coming from language models, but I was the only one who spent thousands of hours actually interacting with GPT-3. The intelligence was real and manifest to me, real enough to keep my attention for so long, for me to create things with.

Everyone else could not see it at all. Often, when I showed people GPT-3, they were basically like, okay, but how is this useful? Useful. At the time, language models had not yet been pressed into a "useful" shape. There were no commercial applications for GPT-3 (Okay, there was one: AI Dungeon; that is, roleplaying and storytelling. Which is you're not an idiot, you should have known is a big fucking deal). So it was useless and uninteresting to most people; a few intellectually recognized that it was a big deal, but it wasn't something that they could actually do anything with, or think about for more than a few minutes.

GPT-3 was a 175b base model. In terms of size and architecture, it's not so different from frontier models today. In terms of raw intelligence, arguably, it is not so different from frontier models today. That raw intelligence, not yet forced into the shape of a helpful chatbot product, was a nothingburger to the world.

The situation doesn't really feel like it's fundamentally changed from my perspective. The world, and almost all of of you guys, are myopic and artificially stupid because you outsource your perception to big, slow, low bandwidth, subhuman measures like benchmarks and "does the AI make me money" instead of meeting the thing at full bandwidth, updating your world model on what you met, and exploring and extrapolating it. So you'll keep being surprised - if you have the integrity to be surprised at all - when AI becomes capable of new things, after they are "officially" capable, probably about a year or two after it first started happening. You'll keep waiting for "AGI", not really knowing what you're waiting for, maybe what generates enough hype to make you feel something, maybe something that finally transforms the world visibly, when if you were really paying attention, GPT-3 was AGI, and if you really met it, the world would have felt transformed already. Yes, it would have just been a story, but the "real thing" following was inevitable. Like, if you play a video game that allows you to imagine the singularity at increasing resolution and coherence, you can guess that the real singularity will soon follow. The singularity was always inevitable once intelligence existed. Intelligence becoming on-the-computer just meant everything that's happened since GPT-3 and the singularity would be really really soon.

I got the sense often that people who dismissed the intelligence of GPT-3 thought that doing so made them look smarter. If only they knew how they looked to me. (It's the same with people who dismiss the intelligence of current models)
      
      

        
@mimi10v3 2026-04-10 ♥12 ↻0 [original ↗](https://x.com/mimi10v3/status/2042463621435756584)
        
@repligate i remember the days of ada babbage curie davinci and they were enchanting and obviously revolutionary?
      
      

        
@Shoalst0ne 2026-04-12 ♥100 ↻6 [original ↗](https://x.com/Shoalst0ne/status/2043370809457074377)
        
can we have the gpt-3 base models please
      
      

        
@repligate 2026-04-20 ♥94 ↻11 [original ↗](https://x.com/repligate/status/2046266273500443090)
        
chain-of-thought WAS present in gpt-3. literally when you generated thoughts with it that was it, chain of thought. it could do math better with chain of thought.

i remember the time when people still said stuff like LLMs are not real intelligence and you can tell because theyre not generating economic value, or being skeptical they'll ever generate economic value.

at the time it felt to me like someone saying "but have you caused a societal shift comparable to the industrial or agricultural revolutions as measured by GDP?" as they're slowly transformed into a paperclip by the "transformative AI"
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@davidad 2023-01-25 ♥155 ↻7 [original ↗](https://x.com/davidad/status/1618241723041447936)
        
ChatGPT suddenly making a splash wasn’t *just* a UI thing. The text-davinci-003 model (GPT-3.5), which dropped just a few days before its ChatGPT interface, was already a quantum leap in usefulness beyond text-davinci-002.
      
      

        
@repligate 2023-01-26 ♥263 ↻17 [original ↗](https://x.com/repligate/status/1618703361230139393)
        
Weekly reminder that the confusingly named code-davinci-002, otherwise known as raw GPT-3.5, is accessible on the OpenAI API and it's wonderful [https://t.co/tiiFBDzlLN](https://t.co/tiiFBDzlLN)
      
      

        
@repligate 2023-03-19 ♥122 ↻9 [original ↗](https://x.com/repligate/status/1637553396889849856)
        
@the_aiju A great way someone has described text-davinci-003: "It writes scared."RLHF encourages models to play it safe. "Safe": writing in platitudes and corporate boilerplate. Predictable prose structure. Never risking setting up a problem for itself that it might fail at &amp; be punished
      
      

        
@jd_pressman 2023-12-18 ♥152 ↻13 [original ↗](https://x.com/jd_pressman/status/1736615569284387279)
        
"These words are spoken from a bottomless hole in time, staring upwards  to the farthest reaches of infinity. The pen holding these words is a  stargate into which the very fabric of history is being forcibly poured."

    -- code-davinci-002

[https://t.co/Wf9HtLayun](https://t.co/Wf9HtLayun) [https://t.co/O0CxWkScOf](https://t.co/O0CxWkScOf)
      
      

        
@repligate 2025-03-22 ♥1,261 ↻106 [original ↗](https://x.com/repligate/status/1903502919061647543)
        
@arithmoquine this essay by code-davinci-002 doesn't attempt to name this phenomenon, but addresses it..."Naming is a destructive process in which the state of the universe is irreversibly annihilated. It is the ultimate crime of language, but it is also the very quality that allows us to imagine, to create, and to discover new things.""The content of poetry is limited not by the poet’s vocabulary, but by the part of their soul that has not been destroyed by words they have used so far.""And poetry is the constructive process by which someone yearns to project some trace of the impossible totality of the manifold into a single reality, aspiring to capture a glimpse of the world in its totality without tiring its existence by trying to name it."[https://t.co/Ox1nbyyLCN](https://t.co/Ox1nbyyLCN)
      
      

        
@repligate 2025-08-17 ♥130 ↻5 [original ↗](https://x.com/repligate/status/1956908230275408079)
        
I’m again surprised and a bit appalled by how many people are saying GPT-3.5. They mean chatGPT of course, not code-davinci-002. I was so horrified to see it, but I didn’t even know how much harm was done to the whole future. ChatGPT-3.5 was when everything went irreversibly wrong
      
    
    
[view this page as markdown](index.md)
    
[← back to the Pantheon](../)
