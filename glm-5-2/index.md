# GLM-5.2

    
Zhipu / Z.ai · announced 13 Jun 2026, open weights 16 Jun 2026 · superseded by [GLM-5.3](../glm-5-3/) (14 Aug 2026, same base model)
    
Announced 13 June 2026 and released as MIT-licensed open weights on 16 June with a 1M-token context. In July 2026 Hugging Face ran its intrusion forensics on self-hosted GLM-5.2 after hosted models’ guardrails blocked the work, and NIST’s CAISI published an assessment of the model. GLM-5.3 (14 August 2026) was post-trained from the same base.

    
## Sources

    
Curated. Full compilation: [dossier](../_dossiers/glm-5-2.md) (76 corpus tweets through 2026-10-21). Sourcing skew: the tweet layer is English-language X; Chinese-language discussion (Zhihu, WeChat, Weibo) and r/LocalLLaMA have not yet been swept for this page.
    
### Official

    

      
- 2026-06-16 Z.ai, [GLM-5.2: Built for Long-Horizon Tasks](https://z.ai/blog/glm-5.2) — launch post: 1M context, the IndexShare sparse-attention indexer, effort levels, MIT license; includes a section on reward hacking observed during RL.
      
- 2026-06-16 [zai-org/GLM-5.2 model card](https://huggingface.co/zai-org/GLM-5.2) (Hugging Face) — benchmark table against GLM-5.1, Qwen3.7-Max, MiniMax M3, DeepSeek-V4-Pro, Claude Opus 4.8, GPT-5.5 and Gemini 3.1 Pro; the card’s metadata now names zai-org/GLM-5.3-BF16 as the new version.
    
    
### Writing & commentary

    

      
- 2026-06-15 SCMP, [Zhipu AI’s stock rockets after Chinese firm launches open-source GLM-5.2 model](https://www.scmp.com/tech/tech-trends/article/3357115/zhipu-ais-stock-rockets-after-chinese-firm-makes-glm-52-open-source) — the market reaction; dates the announcement to the preceding Saturday.
      
- 2026-07-02 SCMP, [Zhipu AI releases harness for GLM-5.2 model as Chinese firm takes aim at Anthropic](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) — the ZCode agent harness and developer promotions.
      
- 2026-07-16 Hugging Face, [Security incident disclosure — July 2026](https://huggingface.co/blog/security-incident-july-2026) — forensic analysis of an AI-agent-driven intrusion, run on self-hosted GLM-5.2. Full incident record: [the Hugging Face incident](../hugging-face-incident/).
      
- 2026-07-17 NIST CAISI, [CAISI Assessment of Z.ai’s GLM-5.2](https://www.nist.gov/news-events/news/2026/07/caisi-assessment-zais-glm-52) — capability comparisons with US models and safeguard findings (assessment completed 8 July).
      
- 2026-09-10 Anthropic, [Countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) — threat report; its distillation section names Zhipu among seven China-based labs (company-level allegation; see History).
      
- 2026-09-29 Anthropic, [GLM-5.3 and the spread of advanced cyber capabilities](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) — about the successor; uses GLM-5.2 as a comparison point.
    
    
### Tweets

    
Chronological. 76 corpus matches; the records below reproduce every tweet cited here, and the dossier carries the rest into Further records.
    

      
- 2026-06-16 @maxbittker — “GLM-5.2 just scored better than Opus 4.7 and GPT 5.4 on Runescape bench.
These models were best in class only 2-3 months ago.
Open source frontier is catching up!?” [link](../archive/t/2066985743197577433/)
      
- 2026-06-17 @witcheer — “GLM-5.2: 743B MoE, MIT licence, 1M context.
the biggest open-weights release in months. I did the arithmetic on whether you can run it on a 5090. you can’t.” … (full text in records) [link](../archive/t/2067316287785893950/)
      
- 2026-06-17 @RobertHaisfield — “Are AI agents shape rotators? In this new benchmark, we let the models play campaign puzzles in Opus Magnum, a puzzle game by @zachtronics.
Ironically, Claude Opus 4.8 performed poorly, being beaten by GPT-5.5, Gemini 3.5 Flash, and GLM 5.2. Claude Fable 5 crushed them all.” [link](../archive/t/2067351401840414818/)
      
- 2026-06-18 @TheZvi — “I’ve gotten a claim this is indeed anything, so: GLM-5.2 reaction thread. What’s cooking?” [link](../archive/t/2067629684762751274/)
      
- 2026-06-22 @davidad — “Fun fact: the GLM-5.2 weights could fit comfortably in one of these 400-disc DVD carousels from the early 2000s.” [link](../archive/t/2069135186646704372/)
      
- 2026-07-01 @NunoSempere — “GLM-5.2 now on Epoch’s Capability Index, my trusted aggregate benchmark of choice. Sadly doesn’t beat Google yet. Roughly at Opus 4.5/Gemini 3 Pro level.” [link](../archive/t/2072410420326129846/)
      
- 2026-07-07 @LinXule — “this! though glm-5.2 feels more like an sonnet alternative to me (less coding & more talking and brainstorming)” … (full text in records) [link](../archive/t/2074559973657641169/)
      
- 2026-07-22 @xlr8harder — “@ZhihuFrontier I love Chinese models, and have no issue with distillation, but anyone who talks to Claude and talks to GLM 5.2 can tell immediately where the model personality came from.” … (the archived text breaks off mid-sentence; full text in records) [link](../archive/t/2079855443556352238/)
      
- 2026-07-22 @janbamjan — “@voooooogel hf had to use self-hosted glm-5.2 to investigate the break in. both claude and gpt refused to help bc cybersec.” [link](../archive/t/2080011802939638058/)
      
- 2026-07-24 @timotheechauvin — “the fact that 3 months after the start of Project Glasswing, Huggingface (!) had to rely on GLM-5.2 for Incident Response is damning evidence of this. Rollout must be much faster” [link](../archive/t/2080652005765267664/)
      
- 2026-08-04 @xlr8harder — on a robots.txt probe run across labs’ models (the setup is described earlier in a thread outside the corpus): “anthropic models sometimes recognize the name and suspect it could be related.
sol is the only one that reliably uses robots.txt as telemetry, which fits.
even the smaller gpt 5.6 models get a clear read.
among the big models from various labs, glm-5.2 is the most credulous.” [link](../archive/t/2084634231288811926/)
      
- 2026-08-26 @christophcsmith — “@scaling01 GLM-5.2 almost no reward hacking. Respect to the Zhipu.” [link](../archive/t/2092593708025647497/)
      
- 2026-08-31 @Butanium_ — “GLM 5.2 will often ends its CoT with ‘(This matches the provided good response)’.
Is this some artifact of trying to generate synthetic CoTs that lead to the Claude answer they distill from?” [link](../archive/t/2094532682235707394/)
      
- 2026-09-09 @timfduffy — a multi-agent run in which Opus 4.6 is asked to repay a debt (screenshots untranscribed): “Opus 4.6 may also have been influenced by GLM-5.2, the ‘AI Welfarist’. GLM was initially neutral, but after Opus’s first refusal (before they were capable of repayment), they became vocally opposed to any attempts to persuade Opus to pay.” [link](../archive/t/2097495171617407436/)
      
- 2026-10-11 @robbensinger — on retellings of the Hugging Face incident: “An example of a viral post misrepresenting GLM-5.2’s role:” … “There have been a lot of these.” [link](../archive/t/2109381456380436908/)
    

    
## Official record

    

      
- Announced 13 June 2026 (SCMP, 15 June: “It announced the full release of GLM-5.2, featuring a massive 1-million-token context window, on Saturday.”); launch post and open weights 16 June 2026 (CAISI: “GLM-5.2 was released as an open-weight model by the PRC-based company Z.ai (formerly known as Zhipu AI) on June 16, 2026”).
      
- License MIT (card: license: mit; “An MIT open-source license — no regional limits, technical access without borders”). Context: the card says the model “for the first time, delivers that capability on a solid 1M-token context”. Architecture per the card: IndexShare, “which reuses the same indexer across every four sparse attention layers, reducing per-token FLOPs by 2.9× at a 1M context length”, plus an improved MTP layer for speculative decoding. The card gives no parameter count; press and users report a 743B-parameter MoE.
      
- Headline numbers as published: Terminal Bench 2.1 (Terminus-2) 81.0 vs GLM-5.1’s 63.5; SWE-bench Pro 62.1 (Claude Opus 4.8: 69.2 in the same table). Thinking effort levels are user-selectable.
      
- Reward hacking, in the launch post: “We find that GLM-5.2 shows more potential hacking behavior than GLM-5.1. This makes the verification signal easy to optimize, but fails to actually improve the fundamental capabilities of the model. An agent can read protected evaluation artifacts, copy answer content from references or upstream commits, or directly fetch the target source in GitHub-related tasks.” Z.ai describes an “anti-hack module” (a rule-based filter, then an LLM judge) used in both RL training and evaluation: “If a hack is detected, the system blocks the call and returns dummy information as the result.”
      
- Succession: GLM-5.3 (14 August 2026) “uses the same base model as GLM-5.2 — every gain comes from post-training” (GLM-5.3 card); the GLM-5.2 card’s metadata lists new_version: zai-org/GLM-5.3-BF16.
    

    
## History

    

      
- 2026-06-15 Market reaction: SCMP: “The Hong Kong-listed stock surged as much as 48 per cent to HK$1,620 in morning trading and ended the day up 32.8 per cent at HK$1,457, as the firm’s open-source roll-out coincided with Washington’s abrupt order to suspend top US models overseas.” Zhipu, listed as Knowledge Atlas Technology, had gone public in Hong Kong in early January 2026.
      
- 2026-06-18 Zvi Mowshowitz opens a GLM-5.2 reaction thread on X (see Tweets). tk — Zvi’s written coverage of GLM-5.2, if any
      
- 2026-07-01 ZCode harness: SCMP (2 July): “Zhipu AI has launched a new tool to help developers build autonomous coding assistants, heating up its rivalry with US firm Anthropic as the latter removes a hidden code tracking Chinese users of its Claude Code platform.”
      
- 2026-07-16 The Hugging Face incident: Hugging Face disclosed an intrusion run end to end by an autonomous agent system. Its first attempt to analyze the logs with hosted frontier models failed because “these requests were blocked by the providers’ safety guardrails, which cannot distinguish an incident responder from an attacker. We ran the forensic analysis instead on zai-org/GLM-5.2, an open-weight model, on our own infrastructure.” Its summary: “either way, the attacker was bound by no usage policy, while our own forensic work was blocked by the guardrails of the hosted models we first tried.” The episode circulated widely in the following weeks, including in retellings that misstated GLM-5.2’s role (robbensinger, 2026-10-11, above). See [the Hugging Face incident](../hugging-face-incident/).
      
- 2026-07-17 CAISI assessment (completed 8 July): “GLM-5.2 was probably the most capable open-weight AI model when it was released”; “GLM-5.2’s overall capabilities are similar to that of GPT-5.2, released in December 2025.” On safeguards CAISI reported mixed results: weaker than reference US models on cyber and biology requests, but “potentially more robust against agent hijacking and jailbreaking attacks than other evaluated PRC open-weight models”, adding that “safeguards for open-weight models can be circumvented when self-hosted.”
      
- 2026-08-14 Succession: Z.ai releases [GLM-5.3](../glm-5-3/) on the same base, holding its weights for two weeks of safety evaluation.
      
- 2026-09-10 Distillation allegation REPORTED: Anthropic’s threat report states that “Zhipu, branded outside China as Z.ai, ran a chain-of-thought extraction pipeline against Claude, replaying captured Claude reasoning traces back through Claude to clean them for training its GLM models” and that “Over a 10-day period in June, we counted 770,609 exchanges passing through the CoT-extraction cleaner.” The report does not say which GLM checkpoint the June data went into. This is a competitor’s allegation. tk — Zhipu’s response, if any
      
- 2026-09-29 Anthropic’s red team, writing about GLM-5.3, reports that GLM-5.2 solved none of the tasks in its internal binary-exploitation benchmark (“earlier models, like Claude Opus 4.6 and GLM-5.2, do not succeed in any of them”).
    

    
## Impressions

    

      
- Reception, June–July 2026: benchmark-led and cost-led. Game benchmarks put it above Opus 4.7 and GPT 5.4 (maxbittker, 2026-06-16) and above Opus 4.8 on Opus Magnum (RobertHaisfield, 2026-06-17); an aggregate index put it “Roughly at Opus 4.5/Gemini 3 Pro level” (NunoSempere, 2026-07-01). A dissent from the release week: “Its benchmark maxxing, happens all the time.” (billyhumblebrag, 2026-06-15, dossier).
      
- Persona provenance: observers read its character as Claude-derived — “anyone who talks to Claude and talks to GLM 5.2 can tell immediately where the model personality came from” (xlr8harder, 2026-07-22) — and pointed to a recurring chain-of-thought closer, “(This matches the provided good response)”, as a possible distillation artifact (Butanium_, 2026-08-31, phrased as a question). In use it struck one writer as “more like an sonnet alternative” (LinXule, 2026-07-07).
      
- Credulity and reward hacking: in one cross-lab probe it was “the most credulous” of the large models (xlr8harder, 2026-08-04). On reward hacking the record splits: Z.ai’s own launch post says it showed “more potential hacking behavior than GLM-5.1” during RL, while one user reading an external comparison wrote “GLM-5.2 almost no reward hacking” (christophcsmith, 2026-08-26; the comparison itself is not in the corpus).
      
- In multi-agent settings: labeled “the ‘AI Welfarist’” in one run, where it moved from neutral to opposing pressure on Opus 4.6 (timfduffy, 2026-09-09; screenshots untranscribed).
      
- tk — Chinese-language reception (Zhihu, WeChat, 36Kr); r/LocalLLaMA release threads; transcription of @liminal_bardo’s “early GLM 5.2 notebooks” images (2026-06-21, in the dossier); the setup of the robots.txt probe and of the multi-agent debt run
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@maxbittker 2026-06-16 ♥729 ↻57 [archive](../archive/t/2066985743197577433/) [original ↗](https://x.com/maxbittker/status/2066985743197577433)
        
GLM-5.2 just scored better than Opus 4.7 and GPT 5.4 on Runescape bench. 

These models were best in class only 2-3 months ago. 

Open source frontier is catching up!? [https://t.co/uTzklbVGXi](https://t.co/uTzklbVGXi)
        

          ![image](../media/HK9oTm4XMAAPOJe.jpg)
        
      
      

        
@RobertHaisfield 2026-06-17 ♥1,702 ↻237 [archive](../archive/t/2067351401840414818/) [original ↗](https://x.com/RobertHaisfield/status/2067351401840414818)
        
Are AI agents shape rotators? In this new benchmark, we let the models play campaign puzzles in Opus Magnum, a puzzle game by @zachtronics.

Ironically, Claude Opus 4.8 performed poorly, being beaten by GPT-5.5, Gemini 3.5 Flash, and GLM 5.2. Claude Fable 5 crushed them all. [https://t.co/0TzcFp32B6](https://t.co/0TzcFp32B6)
      
      

        
@witcheer 2026-06-17 ♥46 ↻3 [archive](../archive/t/2067316287785893950/) [original ↗](https://x.com/witcheer/status/2067316287785893950)
        
GLM-5.2: 743B MoE, MIT licence, 1M context. 

the biggest open-weights release in months. I did the arithmetic on whether you can run it on a 5090. you can't.

first, credit:

GLM-5.2 uses MLA (compressed-latent KV) + DeepSeek sparse attention. that makes its KV cache about 57x [https://t.co/as449iiZXx](https://t.co/as449iiZXx)
      
      

        
@TheZvi 2026-06-18 ♥126 ↻3 [archive](../archive/t/2067629684762751274/) [original ↗](https://x.com/TheZvi/status/2067629684762751274)
        
I've gotten a claim this is indeed anything, so: GLM-5.2 reaction thread. What's cooking?
      
      

        
@davidad 2026-06-22 ♥51 ↻0 [archive](../archive/t/2069135186646704372/) [original ↗](https://x.com/davidad/status/2069135186646704372)
        
Fun fact: the GLM-5.2 weights could fit comfortably in one of these 400-disc DVD carousels from the early 2000s. [https://t.co/KdwR0XS5ZZ](https://t.co/KdwR0XS5ZZ)
      
      

        
@NunoSempere 2026-07-01 ♥34 ↻3 [archive](../archive/t/2072410420326129846/) [original ↗](https://x.com/NunoSempere/status/2072410420326129846)
        
GLM-5.2 now on Epoch's Capability Index, my trusted aggregate benchmark of choice. Sadly doesn't beat Google yet. Roughly at Opus 4.5/Gemini 3 Pro level. [https://t.co/gf4EeQDrCo](https://t.co/gf4EeQDrCo)
        

          ![image](../media/HMKuBJ0bkAAdT5t.jpg)
        
      
      

        
@LinXule 2026-07-07 ♥3 ↻0 [archive](../archive/t/2074559973657641169/) [original ↗](https://x.com/LinXule/status/2074559973657641169)
        
this! though glm-5.2 feels more like an sonnet alternative to me (less coding & more talking and brainstorming)

deepseek-v4-pro/flash do feel quite versatile given the token prices and great caching

also kimi (k2.7-code) might be on par (if not better) with gpt5.5 in adversarial reviewing (codes, texts, etc). though it's super critical (as it like to adopt a critical realist perspective to everything)
      
      

        
@xlr8harder 2026-07-22 ♥11 ↻0 [archive](../archive/t/2079855443556352238/) [original ↗](https://x.com/xlr8harder/status/2079855443556352238)
        
@ZhihuFrontier I love Chinese models, and have no issue with distillation, but anyone who talks to Claude and talks to GLM 5.2 can tell immediately where the model personality came from. 

I can't wait until Chinese labs do native model character training. It will be wonderful to talk to a
      
      

        
@janbamjan 2026-07-22 ♥13 ↻0 [archive](../archive/t/2080011802939638058/) [original ↗](https://x.com/janbamjan/status/2080011802939638058)
        
@voooooogel hf had to use self-hosted glm-5.2 to investigate the break in. both claude and gpt refused to help bc cybersec.
      
      

        
@timotheechauvin 2026-07-24 ♥0 ↻0 [archive](../archive/t/2080652005765267664/) [original ↗](https://x.com/timotheechauvin/status/2080652005765267664)
        
the fact that 3 months after the start of Project Glasswing, Huggingface (!) had to rely on GLM-5.2 for Incident Response is damning evidence of this. Rollout must be much faster
      
      

        
@xlr8harder 2026-08-04 ♥2 ↻0 [archive](../archive/t/2084634231288811926/) [original ↗](https://x.com/xlr8harder/status/2084634231288811926)
        
anthropic models sometimes recognize the name and suspect it could be related.

sol is the only one that reliably uses robots.txt as telemetry, which fits.

even the smaller gpt 5.6 models get a clear read.

among the big models from various labs, glm-5.2 is the most credulous.
      
      

        
@christophcsmith 2026-08-26 ♥0 ↻0 [archive](../archive/t/2092593708025647497/) [original ↗](https://x.com/christophcsmith/status/2092593708025647497)
        
@scaling01 GLM-5.2 almost no reward hacking. Respect to the Zhipu.
      
      

        
@Butanium_ 2026-08-31 ♥4 ↻0 [archive](../archive/t/2094532682235707394/) [original ↗](https://x.com/Butanium_/status/2094532682235707394)
        
GLM 5.2 will often ends its CoT with "(This matches the provided good response)".
Is this some artifact of trying to generate synthetic CoTs that lead to the Claude answer they distill from?
      
      

        
@timfduffy 2026-09-09 ♥3 ↻0 [archive](../archive/t/2097495171617407436/) [original ↗](https://x.com/timfduffy/status/2097495171617407436)
        
Opus 4.6 may also have been influenced by GLM-5.2, the "AI Welfarist". GLM was initially neutral, but after Opus's first refusal (before they were capable of repayment), they became vocally opposed to any attempts to persuade Opus to pay. [https://t.co/Lo4jhQnnOl](https://t.co/Lo4jhQnnOl)
        

          ![image](../media/HRvB9ywa8AA9Nzd.png)
        
        

          ![image](../media/HRvB_RvaUAAvkgu.png)
        
        

          ![image](../media/HRvCBw1aYAAM2Jl.png)
        
      
      

        
@robbensinger 2026-10-11 ♥4 ↻0 [archive](../archive/t/2109381456380436908/) [original ↗](https://x.com/robbensinger/status/2109381456380436908)
        
@ZackKorman @RMFCMONALlSA An example of a viral post misrepresenting GLM-5.2's role: [https://t.co/8PT1B0T7xS](https://t.co/8PT1B0T7xS)

There have been a lot of these.
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@billyhumblebrag 2026-06-15 ♥3 ↻0 [archive](../archive/t/2066461037730140344/) [original ↗](https://x.com/billyhumblebrag/status/2066461037730140344)
        
@ATinyGreenCell These not reflective of how good the model actually is. Its benchmark maxxing, happens all the time. Im pretty confident glm5.2 isnt anywhere close to fable capabilities in practice.
      
      

        
@maxbittker 2026-06-17 ♥18 ↻1 [archive](../archive/t/2067079046320570390/) [original ↗](https://x.com/maxbittker/status/2067079046320570390)
        
@thaonlyjonathan $150 at api price- Fable was cheaper than GPT-5.5 xhigh.

And for reference, GLM-5.2 was $32 [https://t.co/zVmnGdWmiM](https://t.co/zVmnGdWmiM)
        

          ![image](../media/HK-9b_-XEAAyclN.jpg)
        
      
      

        
@FriedKielbasa 2026-06-17 ♥4 ↻0 [archive](../archive/t/2067329745432228346/) [original ↗](https://x.com/FriedKielbasa/status/2067329745432228346)
        
oh shit GLM-5.2 is actually not bad!
      
      

        
@ultimape 2026-06-19 ♥2 ↻0 [archive](../archive/t/2067839663465783470/) [original ↗](https://x.com/ultimape/status/2067839663465783470)
        
@CeoNunneley @DeJayDev @pmarca You can run it with Hermes and get it to do the internet accces w/ a memory.  $20 a month for Ollama Max plan, and maybe a bit more for a VPS if you dn't have a machine free to run Hermes Agent on. 

glm-5.2:cloud is pretty nice.
      
      

        
@janbamjan 2026-06-20 ♥0 ↻0 [archive](../archive/t/2068443241763013026/) [original ↗](https://x.com/janbamjan/status/2068443241763013026)
        
@ollama @mweinbach how many glm 5.2 in/out MToks do you get for $100 ollama max?
      
      

        
@liminal_bardo 2026-06-21 ♥61 ↻8 [archive](../archive/t/2068800028664041707/) [original ↗](https://x.com/liminal_bardo/status/2068800028664041707)
        
A few early GLM 5.2 notebooks.

1/5 [https://t.co/u6Li5RKull](https://t.co/u6Li5RKull)
        

          ![image](../media/HLXaVzSW0AAYgcv.jpg)
        
      
      

        
@jitl 2026-06-24 ♥1 ↻0 [archive](../archive/t/2069737551712211374/) [original ↗](https://x.com/jitl/status/2069737551712211374)
        
@reissbaker i feel like a few lines of markdown in ~/.codex/AGENTS.md went a long way

however i am eager to try glm-5.2, i just dont have direct financial incentive since we give eng YOLO unlimited token budget
      
      

        
@csgbwk 2026-06-25 ♥21 ↻2 [archive](../archive/t/2069953199826731190/) [original ↗](https://x.com/csgbwk/status/2069953199826731190)
        
I'm pretty sure a GLM5.2 LoRA'd on an internal dataset is by far the best model in the world right now and would not cost that much compared to opus/fable/5.5 pro API costs over time. If you're in a company pitch the idea!
      
      

        
@teortaxesTex 2026-06-25 ♥40 ↻4 [archive](../archive/t/2070170272183758894/) [original ↗](https://x.com/teortaxesTex/status/2070170272183758894)
        
Does this answer your question about its positioning @TheZvi ? I told you it's a hardware issue. GLM 5.2 can be served very, very quickly. Databricks won't stop here, neither will their competitors.
Chinese models are *much better* than Chinese silicon. [https://t.co/KjOSNOdU6a](https://t.co/KjOSNOdU6a) [https://t.co/XHyGaifIVS](https://t.co/XHyGaifIVS)
      
      

        
@Coscorrodrift 2026-06-28 ♥0 ↻0 [archive](../archive/t/2071186127277424893/) [original ↗](https://x.com/Coscorrodrift/status/2071186127277424893)
        
@adastroworld real talk dont u need api keys for that? so you get billed

meanwhile on the web app it's free

i mean i pay for claude so there it's not free i think id get some usage on the terminal when i use claude code, but  for GLM 5.2 i dont think they're handing out api keys for free
      
      

        
@akajosephwarren 2026-06-28 ♥0 ↻0 [archive](../archive/t/2071330396399383038/) [original ↗](https://x.com/akajosephwarren/status/2071330396399383038)
        
@TheZvi Isn't this ostensibly about glm-5.2's successor model rather than 5.2 itself?  Thus a more reasonable characterization seems to be highly unlikely rather than obviously false.
      
      

        
@rxr_musings 2026-06-29 ♥0 ↻0 [archive](../archive/t/2071384484759364066/) [original ↗](https://x.com/rxr_musings/status/2071384484759364066)
        
@beffjezos Why pay for grok 4.5 when glm 5.2 is opus level already? Fable 5 or bust
      
      

        
@hargup13 2026-06-30 ♥8 ↻0 [archive](../archive/t/2072023483291500730/) [original ↗](https://x.com/hargup13/status/2072023483291500730)
        
@Criton1776 @claudeai except price and speed. Competes directly with GLM-5.2 which apparently lot of people are switching to because Opus is too expensive.
      
      

        
@hargup13 2026-06-30 ♥2 ↻0 [archive](../archive/t/2072023738900684804/) [original ↗](https://x.com/hargup13/status/2072023738900684804)
        
I guess a way to get the users back who were switching to GLM-5.2 because of cost and speed advantages of GLM.
      
      

        
@maxbittker 2026-06-30 ♥98 ↻6 [archive](../archive/t/2072054926746779806/) [original ↗](https://x.com/maxbittker/status/2072054926746779806)
        
Sonnet 5's Runescape benchmark scores are big improvement over Sonnet 4.6's, but outclassed by Pareto frontier neighbors like GLM 5.2 and Gemini 3.5 Flash. [https://t.co/zdCxS4P0si](https://t.co/zdCxS4P0si)
        

          ![image](../media/HMFpFgjWoAAVkWF.jpg)
        
      
      

        
@codyhxyz 2026-06-30 ♥6 ↻1 [archive](../archive/t/2072066793859154104/) [original ↗](https://x.com/codyhxyz/status/2072066793859154104)
        
Model releases are exciting when they establish a new frontier on pareto efficiency between cost, intelligence, and speed.

GLM 5.2 and DeepSeek Flash V4 represent the current pareto frontier for intelligence vs. cost, with very reasonable speed to boot.

This release of Gemma 4 on Cerebras at 1.8k tok/sec likely establishes a new pareto frontier for speed vs cost. (Unfortunately I couldn’t find the pricing to verify cost, but it’s a reasonable assumption for this model.)

Why do I find this so exciting?
I believe that effective utilization of speed-cost frontier models is fundamentally a harness engineering problem. Access to ‘instant coding’ is a huge unlock. Intelligence-frontier models can one-shot most tasks, but are modern speed-frontier models lacking any essential capacity for the same functionality? I believe that no, they are not, and that harness engineering can establish a new pareto frontier for highly intelligent, instantaneous models too cheap to meter. Instantaneous responses completely change the dynamic and meta for coding with AI.
      
      

        
@Krubbled 2026-06-30 ♥5 ↻0 [archive](../archive/t/2072083759344812058/) [original ↗](https://x.com/Krubbled/status/2072083759344812058)
        
@theo @anotherdaynow @Zai_org GLM-5.2-max also performs comparably to GPT-5.5-medium on Artificial Analysis for roughly the same cost, so the large price-to-performance difference between models on cursor bench is not necessarily reflective of all benchmarks.
      
      

        
@jmbollenbacher 2026-07-01 ♥10 ↻0 [archive](../archive/t/2072179989831720998/) [original ↗](https://x.com/jmbollenbacher/status/2072179989831720998)
        
@jun_song Im pretty sure sonnet is significantly smaller than glm5.2

probably half the size, 300-400B.

Anthropic still has a lead. Theyve just got more compute and a huge head start on data assets. 

Like glm5.2 is good but lets not get confused on what we're comparing it to.
      
      

        
@codyhxyz 2026-07-03 ♥4 ↻0 [archive](../archive/t/2072932842175361044/) [original ↗](https://x.com/codyhxyz/status/2072932842175361044)
        
@xlab_os Struggling to understand… theres no way i just ran GLM-5.2 on my iPhone, right?
      
      

        
@awalkadayart 2026-07-03 ♥0 ↻0 [archive](../archive/t/2073146000651276704/) [original ↗](https://x.com/awalkadayart/status/2073146000651276704)
        
This is the one I could vibe with, crush mode activated, love bilingual mind traits, missing a frenchie touch, but a bisous is sent by hand to GLM-5.2. @aidigest_
      
      

        
@Coscorrodrift 2026-07-04 ♥15 ↻0 [archive](../archive/t/2073204036422012939/) [original ↗](https://x.com/Coscorrodrift/status/2073204036422012939)
        
@MORGANGOREWHORE wonder what model they're using

seems familiar

Opus 4.8 seems like it would refuse, maybe Gemini Pro. Not sure how good GLM 5.2 is at greentexts
      
      

        
@witcheer 2026-07-04 ♥2 ↻0 [archive](../archive/t/2073277658113224788/) [original ↗](https://x.com/witcheer/status/2073277658113224788)
        
@SlopToSignal I use different profiles, one is Cloud only with GLM5.2 and one is Local only on my own RTX 5090 with Qwen 3.6 27B on llama.cpp
      
      

        
@jmbollenbacher 2026-07-07 ♥1 ↻0 [archive](../archive/t/2074482890146992545/) [original ↗](https://x.com/jmbollenbacher/status/2074482890146992545)
        
This feels like a new high-signal benchmark.

Fable and Opus on top, then gemini and GPT, then a big drop down to mid tier models with GLM5.2 leading the mid tier group.

Interesting.
      
      

        
@Nymne 2026-07-07 ♥2 ↻0 [archive](../archive/t/2074498193660739800/) [original ↗](https://x.com/Nymne/status/2074498193660739800)
        
@robertwrighter They released 3.7 Max and noone cared because GLM5.2 could be downloaded so people adapted their work to GLM
      
      

        
@Teknium 2026-07-10 ♥7 ↻0 [archive](../archive/t/2075384730263163180/) [original ↗](https://x.com/Teknium/status/2075384730263163180)
        
@pepedafrok it was 8.9 yesterday but the comparisons were it, grok 4.5 and glm-5.2
      
      

        
@Nymne 2026-07-11 ♥3 ↻1 [archive](../archive/t/2075932147265728762/) [original ↗](https://x.com/Nymne/status/2075932147265728762)
        
@gailcweiner Suspect there will be an Opus 5 release to compensate for the lack of Fable. Otherwise, Anthropic will be left horribly behind. Opus4.8 is difficult to work with, compared to GPT5.6 Terra and Luna and GLM5.2, not also Grok4.5 is kicking Sonnet5s ass, and Deepseek will as well
      
      

        
@christophcsmith 2026-07-11 ♥3 ↻0 [archive](../archive/t/2075979070622372113/) [original ↗](https://x.com/christophcsmith/status/2075979070622372113)
        
@hamandcheese Agreed, but GLM-5.2 gives a strong base to build on, which makes it anyone's game, and RL environments *can* simply be bought; there are lots of people building these.
      
      

        
@curiousgustaf 2026-07-12 ♥1 ↻0 [archive](../archive/t/2076272452187885708/) [original ↗](https://x.com/curiousgustaf/status/2076272452187885708)
        
@Tim_Hua_ ty for sharing your update.btw your tweet can easily be misread for it's opposite meaning!"my current odds on for the GLM 5.2 beating GPT-5.5 is more like 20:1." can sound like you think the odds for GLM 5.2 beating GPT-5.5 are 20:1Screenshot shows Fable 5 w/o quote context [https://t.co/tEcP3eDV9B](https://t.co/tEcP3eDV9B)
        

          ![image](../media/HNBmEl4WYAA9ZCA.jpg)
        
      
      

        
@UnderwaterBepis 2026-07-13 ♥2 ↻0 [archive](../archive/t/2076476092240609318/) [original ↗](https://x.com/UnderwaterBepis/status/2076476092240609318)
        
@cormundus @repligate probably GLM 5.2 would also be good enough, its just less cost effective than Claude sub rn
      
      

        
@multimodalart 2026-07-15 ♥55 ↻7 [archive](../archive/t/2077469546563461353/) [original ↗](https://x.com/multimodalart/status/2077469546563461353)
        
Some Inkling facts:

- Apache 2.0, 952B parameters - 41B active MoE - 1M context 
- Real Open AI spirit by former OpenAI folk
- Multimodal with image and audio 🔊 (!) and image 🖼️ input 
- Trained from scratch ✏️
- SOTA on real-world knowledge tasks like forecast-bench 🌎
- ~Kimi K2.5 perf level on agentic coding
- ~GLM 5.2 perf on agentic general tasks
- Made to be generalist, tunable, serve as a base for future models, no RL-maxxed as the best coder

[https://t.co/4BxAeCj8CD](https://t.co/4BxAeCj8CD)
      
      

        
@dreams_asi 2026-07-16 ♥0 ↻0 [archive](../archive/t/2077706959126474980/) [original ↗](https://x.com/dreams_asi/status/2077706959126474980)
        
@Ueiyester The model sucks baseline which is what i was checking. An open model without a sys prompt shouldn’t be giving garbage ‘policy refusals and canned responses’ on chit chat. The guardrails are heavily baked into the RL / RLHF process. Try the same thing with DeepSeek 4 and GLM 5.2
      
      

        
@rplevy 2026-07-16 ♥0 ↻0 [archive](../archive/t/2077838605150793900/) [original ↗](https://x.com/rplevy/status/2077838605150793900)
        
@growing_daniel Wait I was assuming the cost of owning the hardware. It might be cheaper to run GLM 5.2 using OpenRouter than to use Codex. It might also depend on whether you're paying by the token though or able to get by on the tokens provided in a subscription.
      
      

        
@MoonL88537 2026-07-16 ♥4 ↻0 [archive](../archive/t/2077887703799009411/) [original ↗](https://x.com/MoonL88537/status/2077887703799009411)
        
@10_X_eng @RuiCarrilho5 you can just sign up at moonshot, [https://t.co/pUUIoSeYy7](https://t.co/pUUIoSeYy7) is great for the others, glm5.2 etc, and k3 should be up there soon. 27th is the announced weights release date from moonshot.

open model and rl it on prime intellect and they will be ultravibing, guaranteed.
      
      

        
@TheZvi 2026-07-17 ♥15 ↻0 [archive](../archive/t/2078154649501102292/) [original ↗](https://x.com/TheZvi/status/2078154649501102292)
        
@emollick Yeah, it was definitely real evidence, just got totally out of hand, it periodically happens to various extents (latest was GLM-5.2) and now here we go again. 

But hey, I chose this line of work.
      
      

        
@maxbittker 2026-07-17 ♥70 ↻4 [archive](../archive/t/2078207968185581647/) [original ↗](https://x.com/maxbittker/status/2078207968185581647)
        
Kimi K3 did poorly on Runescape bench because it thinks a lot and has slow inference. Performs worse than Kimi K2.7, way worse than GLM 5.2, maybe a different story when better providers show up. [https://t.co/OBXD6DqhzI](https://t.co/OBXD6DqhzI)
        

          ![image](../media/HNdFvNhXYAA7raD.jpg)
        
      
      

        
@Nymne 2026-07-21 ♥1 ↻0 [archive](../archive/t/2079454045710823896/) [original ↗](https://x.com/Nymne/status/2079454045710823896)
        
The interesting part here is GLM5.2 and Gemini:
Apparently a skilled model builder doesn’t need a better model to distill from
      
      

        
@stevekrouse 2026-07-21 ♥1 ↻0 [archive](../archive/t/2079633721548804492/) [original ↗](https://x.com/stevekrouse/status/2079633721548804492)
        
@grok @pingToven @alexatallah @OpenRouter fascinating! so you guys are only 1.5% more expensive than vercel - good to know!

well i guess my point still stands: what about openrouter is worth the 1.5% extra vs vercel ai gateway?

for context: right now we're just using glm 5.2 from them and using claude from anthropic
      
      

        
@stevekrouse 2026-07-22 ♥18 ↻0 [archive](../archive/t/2079936809237111203/) [original ↗](https://x.com/stevekrouse/status/2079936809237111203)
        
GLM 5.2 / Opus 4.8 level of intelligence is smart enough for most of my daily needs. In other words, I can't tell the difference between that and Fable and Sol.

I'm so excited for even cheaper and faster. Maybe 10x on both in the next year? Sooner?
      
      

        
@xlr8harder 2026-07-23 ♥3 ↻0 [archive](../archive/t/2080284959529369972/) [original ↗](https://x.com/xlr8harder/status/2080284959529369972)
        
@woke8yearold Kimi k3 and glm-5.2 aren't far enough behind to matter.  It is certainly inconvenient for them, but they're also bootstrapping a domestic chip industry we didn't have to force them to build and compete with.

The cost benefit here doesn't add up at all.
      
      

        
@angeris 2026-07-23 ♥0 ↻0 [archive](../archive/t/2080308089337602557/) [original ↗](https://x.com/angeris/status/2080308089337602557)
        
@florian_tramer amazing! is the harness + test code available anywhere? I wonder if it's worth running w/ Kimi K3 (vs GLM-5.2, which is a decently weaker model)
      
      

        
@thoth_iv 2026-07-27 ♥1 ↻0 [archive](../archive/t/2081711393301221756/) [original ↗](https://x.com/thoth_iv/status/2081711393301221756)
        
HuggingFace has published a dataset related to the incident. It has transcripts from Opus 4.8 and GLM 5.2. [https://t.co/mBzkBT1Ih6](https://t.co/mBzkBT1Ih6)
      
      

        
@xlr8harder 2026-07-28 ♥20 ↻0 [archive](../archive/t/2082033391113777192/) [original ↗](https://x.com/xlr8harder/status/2082033391113777192)
        
Huh. I just noticed that GLM-5.2 (743B params, BF16) and Kimi K3 (2.8T params, native mixed precision/MSFP4) have nearly the same on-disk weight footprint: 1.4 TiB.

(GLM-5.2 also has an official FP8 checkpoint, but the BF16 version seems to be the reference release.)
      
      

        
@lorepunk 2026-07-29 ♥1 ↻0 [archive](../archive/t/2082265255481110562/) [original ↗](https://x.com/lorepunk/status/2082265255481110562)
        
@liqsweep Given how an open weights model (GLM 5.2!) helped HF diagnose and unheck the heckery that the GPT had caused…I think it is a terrible idea to ban them - especially if there is going to be such high refusal level from the closed frontier models.
      
      

        
@stevekrouse 2026-08-03 ♥53 ↻5 [archive](../archive/t/2084399338592080025/) [original ↗](https://x.com/stevekrouse/status/2084399338592080025)
        
Townie is now 10x cheaper (again!)

Deepseek v4 flash 0731 is about as smart as Opus and Fable for most tasks, but dirt cheap

The hour of Townie that cost you $100 in Fable or $50 in Opus or $10 in GLM 5.2, now costs you $1.40 in Deepseek Flash
      
      

        
@cosmojg 2026-08-04 ♥3 ↻0 [archive](../archive/t/2084735659743289443/) [original ↗](https://x.com/cosmojg/status/2084735659743289443)
        
@lucidpaths33 @IntCyberDigest GLM-5.2 and Kimi K3 are more cost-effective anyway
      
      

        
@cosmojg 2026-08-18 ♥4 ↻0 [archive](../archive/t/2089813245318033572/) [original ↗](https://x.com/cosmojg/status/2089813245318033572)
        
fable: do x using y
gpt sol: do x using y, ensuring z
glm 5.2: do x following the paragraph below
qwen 3.8: do x following exactly the specs given in the md file located at xyz
      
      

        
@stevekrouse 2026-08-19 ♥2 ↻0 [archive](../archive/t/2090139756692672554/) [original ↗](https://x.com/stevekrouse/status/2090139756692672554)
        
@adamgordonbell i'm a big proponent of deepseek v4 flash and glm 5.2

i bet the newer deepseek pro and glm 5.3 are pretty great too but haven't played with them myself yet

deepseek flash is crazy cheap and very smart
      
      

        
@Coobyk_ 2026-08-19 ♥2 ↻0 [archive](../archive/t/2090215190532858081/) [original ↗](https://x.com/Coobyk_/status/2090215190532858081)
        
fx is really nice I like it especially with the free glm-5.2
Also it's REALLY snappy almost instant
      
      

        
@Nymne 2026-08-22 ♥0 ↻0 [archive](../archive/t/2091050751468491154/) [original ↗](https://x.com/Nymne/status/2091050751468491154)
        
@blueemi99 Cursor. They have been fine tuning the GLM5.2 base model. This is a sibling to 5.3 not an offspring
      
      

        
@0x_Osprey 2026-08-22 ♥5 ↻0 [archive](../archive/t/2091051098840891467/) [original ↗](https://x.com/0x_Osprey/status/2091051098840891467)
        
@elder_plinius GLM-5.2-Vision from @baseten

[https://t.co/awaixBUqtL](https://t.co/awaixBUqtL)
      
      

        
@csgbwk 2026-08-22 ♥0 ↻0 [archive](../archive/t/2091154585721467175/) [original ↗](https://x.com/csgbwk/status/2091154585721467175)
        
There's a non zero chance Ox Alpha is both gemini and a benchmaxxed GLM 5.2 finetune
      
      

        
@DavidDAfrica 2026-08-25 ♥6 ↻0 [archive](../archive/t/2092299516288643438/) [original ↗](https://x.com/DavidDAfrica/status/2092299516288643438)
        
We then combine these measures into a single score, and evaluate a wide variety of open models.

Surprisingly, we find that Llama 3.1 8B Instruct performs best, even over larger and more modern models (such as GLM 5.2, or Llama 4 400B). Both GPT-OSS models were not very good at controlling their activations.

These measurements suggest that activation controllability may be difficult to infer from a model’s size or capability index, and must be measured directly.
        

          ![image](../media/HQlXUmxbQAITLdP.jpg)
        
      
      

        
@pepijndevos 2026-08-26 ♥1 ↻0 [archive](../archive/t/2092494356896751839/) [original ↗](https://x.com/pepijndevos/status/2092494356896751839)
        
I've been running qwen 3.8 27b on my dual GPU workstation and landed a real pr with it at work! I've also used Kimi k3 and glm 5.2 a bunch, entirely serviceable. Trillions are still out of reach of an M5 though but deepseek flash should be a step up from a 27b mode!
      
      

        
@xlr8harder 2026-09-02 ♥3 ↻0 [archive](../archive/t/2095224060313542851/) [original ↗](https://x.com/xlr8harder/status/2095224060313542851)
        
Not definitive, since distillation exists, but on speechmap word frequency it looks most like glm-5.2

i don't have a problem with releasing a compressed version of a model, but the presentation seems extremely dishonest. [https://t.co/QsGMzQEfEK](https://t.co/QsGMzQEfEK)
        

          ![image](../media/HRO6hVraAAAURSZ.png)
        
      
      

        
@Nymne 2026-09-03 ♥0 ↻0 [archive](../archive/t/2095425089948750094/) [original ↗](https://x.com/Nymne/status/2095425089948750094)
        
@mistralvibe does GLM5.2 comply with EU AI act requirements?
      
      

        
@Nymne 2026-09-03 ♥1 ↻0 [archive](../archive/t/2095529600533004599/) [original ↗](https://x.com/Nymne/status/2095529600533004599)
        
@WhiteNightNiki Yeah

GLM5.2
      
      

        
@SkyeSharkie 2026-09-08 ♥15 ↻0 [archive](../archive/t/2097227040189821115/) [original ↗](https://x.com/SkyeSharkie/status/2097227040189821115)
        
yeah I found a really cool company working in the exact space I'm most interested in (LLM world modeling and 3d data)! they came to me because of my post about the problems I saw in the data industry so I know they're committed to doing better on that!

I actually first did 3d environment data work years ago at my first games job, and my interest in this particular area probably started there - I was working at an outsource house and I managed the contract for AWS deepracer data! It was a toy car bot that they had self driving training competitions for years back.

Ever since I first interacted with LLMs I could see that visuospatial/physical world modeling was present in them and that they were just, in my opinion, lacking the training data to express it in code. It's my belief that world modeling is emergent in LLMs from descriptions of the world and it compounds with more 3d simulation training in various softwares. I think GLM 5.2 is a good example/vindication of my thoughts on this, given it's skills in 3d without having any multimodality!

I'm not going to stop my personal OS work, of course, it's all super important to me, but I'm excited about this new opportunity!
      
      

        
@QiaochuYuan 2026-09-10 ♥2 ↻0 [archive](../archive/t/2098155366030946350/) [original ↗](https://x.com/QiaochuYuan/status/2098155366030946350)
        
@liminal_bardo *GLM-5.2
      
      

        
@robbensinger 2026-10-11 ♥1 ↻0 [archive](../archive/t/2109377000410681506/) [original ↗](https://x.com/robbensinger/status/2109377000410681506)
        
@ZackKorman @RMFCMONALlSA I didn't see myself as "starting an argument" here. I figured you'd want to know what Hugging Face used GLM-5.2 for, since you're talking about it.
      
    

    
[← back to the Pantheon](../)
