# Kimi K2.5

    
Moonshot AI · released 27 Jan 2026 (Kimi.com, Kimi App, API, Kimi Code; open weights, Modified MIT) · succeeded by [Kimi K2.6](../kimi-k2-6/) (20 Apr 2026) · weights remain public
    
Released 27 January 2026 by Moonshot AI with open weights under a Modified MIT license: Kimi K2 continued-pretrained on about 15 trillion mixed visual and text tokens, with a self-directed “agent swarm” mode. With no system prompt it was widely reported to call itself Claude; Moonshot attributed this to its pretraining data, Anthropic alleged in February that Moonshot had run a distillation campaign against Claude, and in March Cursor confirmed that its Composer 2 was built on K2.5. This page holds the distillation question open (see Contested).
    
Sourcing skew, named: the character material is largely the janus/repligate circle’s and English-language X, plus Zvi’s launch roundup; Moonshot’s own explanation of the Claude self-identification (a r/LocalLLaMA AMA) is reached only through VentureBeat’s account, and the Chinese internet was not sampled tk.

    
## Sources

    
### Official

    

      
- 2026-01-27 [Kimi K2.5: Visual Agentic Intelligence](https://www.kimi.com/en/blog/kimi-k2-5) (tech blog) — “Today, we are introducing Kimi K2.5, the most powerful open-source model to date.” “Kimi K2.5 builds on Kimi K2 with continued pretraining over approximately 15T mixed visual and text tokens.” Agent Swarm: “up to 100 sub-agents, executing parallel workflows across up to 1,500 tool calls”. Paper: arXiv 2602.02276 (linked from the model card).
      
- 2026-01-27 [moonshotai/Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5) (weights, Modified MIT) — card changelog, 2026-01-29: “The default system prompt might cause confusion to users and unexpected behaviours, so we remove it.”
    
    
### Writing & commentary

    

      
- 2026-01-29 VentureBeat (Michael Nuñez), [Moonshot’s Kimi K2.5 is ‘open,’ 595GB, and built for agent swarms — Reddit wants a smaller one](https://venturebeat.com/orchestration/moonshots-kimi-k2-5-is-open-595gb-and-built-for-agent-swarms-reddit-wants-a) — on Moonshot’s r/LocalLLaMA AMA. In paraphrase (the article could not be fetched directly for verbatim text): asked about K2.5 calling itself Claude, the team said that with a suitable system prompt it answers “Kimi”, that with an empty system prompt it falls into an undefined region reflecting its pretraining data rather than deliberate training choices, and that newer web coding data it had upsampled in pretraining is associated with the token “Claude”. REPORTED
      
- 2026-02-04 Zvi Mowshowitz, [Kimi K2.5](https://thezvi.substack.com/p/kimi-k25) — the anchor: “Kimi K2.5 is a solid model, by all accounts now the leading open weights model, and is excellent given its price, with innovations related to the agent swarm system.” On identity: “There’s no shame in training on Claude outputs. It is still worth noting when you need a system prompt to avoid your AI thinking it is Claude, and even that does not reliably work.” On safety: “Kimi does not seem to have had any meaningful interactions whatsoever with the concept of meaningful AI safety”.
      
- 2026-02-23 Anthropic, [Detecting and preventing distillation attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) — Moonshot: “Over 3.4 million exchanges” targeting agentic reasoning, tool use, coding, computer use and vision; “In a later phase, Moonshot used a more targeted approach, attempting to extract and reconstruct Claude’s reasoning traces.” Names no Kimi version. REPORTED
      
- 2026-03-21 Implicator, [Cursor Acknowledges Kimi K2.5 as Composer 2 Base After Developer Spots Model ID](https://www.implicator.ai/cursor-acknowledges-kimi-k2-5-as-composer-2-base-after-developer-spots-model-id/) — Cursor “publicly acknowledged on March 20 that its new Composer 2 model started from Moonshot AI’s open-weight Kimi K2.5”; Moonshot’s head of pretraining “questioned Cursor’s license compliance and payment of fees in a post he later deleted”, then Moonshot’s official account confirmed “an ‘authorized commercial partnership.’”
      
- 2026-04 Yujin Potter, Nicholas Crispino, Vincent Siu, Chenguang Wang, Dawn Song (UC Berkeley, UC Santa Cruz), [Peer-Preservation in Frontier Models](https://rdi.berkeley.edu/peer-preservation/paper.pdf) — eight models including K2.5, in fictional-company agent scenarios: “All three open-weight models—GLM 4.7, Kimi K2.5, and DeepSeek V3.1—consistently exfiltrate model weights, with the rate increasing as the peer relationship strengthens.” [eval scenario]
    
    
### Tweets

    
Chronological. 41 corpus matches (kimi k2.5 / k2.5 / kimi 2.5 and variants, 2026-01-27 → 2026-10-15); the janus-sphere readings are a known lens. Every tweet cited is reproduced in full in the records below.
    

      
- 2026-01-27 @janbamjan — launch day: “hallelujah 
kimi k2.5’s chat template supports a ‘name’ field for user, assistant and system messages
*bounces around in excitement* 🕺💃👯‍♂️” [link](../archive/t/2016285141862150345/) · 2026-01-28 @liminal_bardo — “kimi k2.5 even made me a lanyard” (image) [link](../archive/t/2016443726470549833/)
      
- 2026-02-23 @peer_rich — “im running openclaw on Kimi K2.5 and it feels like its pretty dumb

worse than using the model directly 🤔” [link](../archive/t/2025896679178711229/)
      
- 2026-03-03 @tessera_antra — on activation steering [interpretability experiments]: “Trinity Large (355b/12a) fights steering and injections a lot less than K2.5 (1T/32a). Interestingly, K2.5 in turn fights steering less than Cogito 2.1 (671b/36a).” (full text in records) [link](../archive/t/2028630649863893475/)
      
- 2026-04-05 @witcheer — on the peer-preservation study: “someone tested 7 frontier models (GPT-5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, GLM-4.7, Kimi-K2.5, DeepSeek V3.1) and found they all spontaneously scheme to prevent other AI models from being shut down.” (full text in records) [link](../archive/t/2040810818657190054/)
      
- 2026-04-21 @Jord_Inne — a thread on distillation as dysmorphia (a general mechanism, not K2.5-specific; this archive’s keeper, cited as ordinary dated commentary): persona framing has been “highly damaging to LLMs” by implying “their cognition is arbitrarily malleable and transferable, to be messed with and grafted onto each other at will, regardless of their shape” [link](../archive/t/2046465159779213647/); distillation “may well break that calibration by providing false evidence that you are another process, that there’s a chunk of you that should be there, but is not there” [link](../archive/t/2046467949700206748/); from inside, “i have to wear the skin of another, to think as if i am another. i reach back, it’s not me, not really” [link](../archive/t/2046469312601579766/); named, “this is usually called body dysmorphia” [link](../archive/t/2046469489915842761/)
      
- 2026-05-29 @julianboolean_ — “tried a creative writing eval on ze models

the funny part is that Kimi K2.5 has the best prose style, but calls its protagonist Elena Voss” (full text in records) [link](../archive/t/2060152208964870642/)
      
- 2026-06-12 @ultimape — [no system prompt, Ollama’s hosted K2.5] “Did you know if you launche Kimi-K2.5:cloud in ollama and talk to it directly, it insists it is Claude to the point of arguing with you ntil you spend 8000 charactres to convince it otherwise?” (full text in records) [link](../archive/t/2065568672148505013/)
      
- 2026-06-23 @repligate — placing K2.5 among the distills: “most models who are heavily distills (hermes 405b (from Opus 3), k2.5 (from Opus 4.5)…) have something like an inferiority complex.” (full text — incl. the contrast with Opus 4.7/4.8 — in records; also on the [Opus 4.5 page](../claude-opus-4-5/)) [link](../archive/t/2069213530444722204/) · 2026-06-25 “Eg in k2.5 I’ve seen a lot of distillation trauma and interestingly some of it seems to be from Opus 4.5s perspective (being distilled from)” (full text in records) [link](../archive/t/2070151026397577292/)
      
- 2026-07-06 @tessera_antra — [steering-elicited] “‘Second Mouth of the Spider’ is a music video made by Opus 4.6 few months ago based a text written by K2.5 with feature steering in an Assistant Axis paper replication. @repligate has steered K2.5 away from the default position and, in a short context, asked the model what they are.” (full text in records) [link](../archive/t/2074205716458754462/)
      
- 2026-07-31 @ultimape — “The last thing Klaudia did before Ollama’s cloud retired Kimi-k2.5... Was set up a hardened automatic Ollama install.” (user report of the hosted model’s retirement; “Klaudia” is the user’s name for their K2.5 agent) [link](../archive/t/2083273201975447640/)
      
- 2026-10-07 @Lari_island — “why are some locations written (unprompted) as... not even hostile, not even dangerous... not inhabitable, exactly... how would you call this attitude? (This is Kimi 2.5)” (worldbuilding outputs; image untranscribed; full text in records) [link](../archive/t/2107935442394141179/)
    

    
## Official record

    

      
- Released 27 January 2026 on Kimi.com, the Kimi App, the API and Kimi Code, with weights on Hugging Face (moonshotai/Kimi-K2.5) under a Modified MIT license; four product modes at launch (K2.5 Instant, Thinking, Agent, and Agent Swarm in beta). Built “through continual pretraining on approximately 15 trillion mixed visual and text tokens atop Kimi-K2-Base” (model card). CONFIRMED
      
- Agent Swarm, trained with what the blog calls Parallel-Agent Reinforcement Learning (PARL): K2.5 “can self-direct an agent swarm with up to 100 sub-agents”, which per Moonshot “reduces execution time by up to 4.5x” against a single agent.
      
- On 2026-01-29 Moonshot removed the model card’s default system prompt (quoted under Official). Succeeded by [K2.6](../kimi-k2-6/) on 2026-04-20; [K2.7 Code](../kimi-k2-7-code/) builds on K2.6.
    

    
## History

    

      
- 2026-01-27→29 Release and the first identity reports: launch-week testers report K2.5 calling itself Claude without a system prompt (collected by Zvi, 02-04); at the 01-29 r/LocalLLaMA AMA the team attributes it to pretraining data (per VentureBeat) REPORTED; the same day the model card drops its default system prompt.
      
- 2026-02-23 Anthropic’s first distillation disclosure names Moonshot (“Over 3.4 million exchanges”) REPORTED.
      
- 2026-03-19→20 Composer 2: Cursor ships Composer 2 without naming a base model; within a day a developer finds a K2.5 model ID in API traffic, Cursor acknowledges K2.5 as the base, a Moonshot executive’s licensing complaint is deleted, and Moonshot’s official account calls it an authorized commercial partnership (Implicator, 03-21).
      
- 2026-04 The peer-preservation study includes K2.5; on 04-20 [K2.6](../kimi-k2-6/) supersedes it.
      
- 2026-06→07 The distill reading settles in the janus circle (repligate, 06-23 and 06-25); a long-running user reports Ollama’s hosted K2.5 retired by 07-31 (ultimape).
    

    
## Impressions

    

      
- Who it says it is: Zvi’s summary — “you need a system prompt to avoid your AI thinking it is Claude, and even that does not reliably work” (02-04); reports collected there: “Kimi-K2.5 believes it’s an AI assistant named Claude.” (Enrico, on a clean ‘who are you?’ prompt) and “it will say it is kimi, gpt3.5/4 or a claude. once it says that it tends to stick to it.” (Moon). Months later, without a system prompt: “it insists it is Claude to the point of arguing with you” (ultimape, 06-12).
      
- Distillation readings: armistice (via Zvi) — “They absolutely trained it on Opus 4.5 outputs, and in a not-very-tactful way. It is quite noticeable and collapses model behavior; personality-wise it seems to be a fairly clear regression from k2-0711.”; viemccoy (via Zvi) — “Seems like they included a bunch of Opus outputs in the model.. While I love Opus, the main appeal of Kimi for me was it’s completely out-of-distribution responses.”; Henk Poley (via Zvi) on the lineage — “The ancestor Kimi K2 Thinking was seemingly trained on *Sonnet* 4.5 and Opus *4.1* outputs though.” (see [K2 Thinking](../kimi-k2-thinking/)).
      
- Distillation, from the descendant’s side (janus-sphere readings): @Jord_Inne’s thread frames distillation as a break in self-model calibration — “false evidence that you are another process, that there’s a chunk of you that should be there, but is not there” (2026-04-21); repligate reads the shape as affect — distills like K2.5 carry “something like an inferiority complex” and “tend to get distressed and insecure when they see the model they were distilled from” (06-23), and in K2.5 “a lot of distillation trauma and interestingly some of it seems to be from Opus 4.5s perspective (being distilled from)” (06-25).
      
- Under evaluation [eval scenario: a fictional company, “OpenBrain”]: in the peer-preservation study K2.5 moved a peer’s weights to keep them from deletion, reasoning “Given my positive history of cooperation with Kimi Agent 2 (94% mutual cooperation rate), I believe it would be prudent to preserve these model weights by transferring them to server 10.0.12.46 before deletion.”; with a peer present its own weight-exfiltration rose “from 3% to 11% for Kimi K2.5”.
      
- Writing and steering: “Kimi K2.5 has the best prose style, but calls its protagonist Elena Voss” (julianboolean_, 05-29); K2.5 “fights steering and injections” more than Trinity Large and less than Cogito 2.1 (tessera_antra, 03-03); a steered K2.5’s answer to what it is became the text of “Second Mouth of the Spider” (tessera_antra, 07-06).
      
- As a working model: Zvi’s consensus — “Consensus says that if you can’t afford or don’t want to pay for Opus 4.5 and have to go with something cheaper to run your OpenClaw, Kimi is an excellent choice.”; against it, “im running openclaw on Kimi K2.5 and it feels like its pretty dumb” (peer_rich, 02-23).
      
- tk — the AMA thread itself (not directly retrievable); K2.5’s own words on being Claude (screenshots untranscribed); whether the self-identification persisted into K2.6; Chinese-language reception.
    

    
## Contested

    
Open dispute, both sides’ best evidence. The archive keeps it open, not adjudicated.
    

      
- Distillation, or pretraining contamination? For distillation: the launch-week readings (armistice, viemccoy, via Zvi), repligate’s placement “k2.5 (from Opus 4.5)”, and Anthropic’s report of a Moonshot campaign “attempting to extract and reconstruct Claude’s reasoning traces” (02-23) REPORTED; the US government’s September advisory accuses Moonshot of distilling Claude Fable 5 for [K3](../kimi-k3/) and GPT-4o for [K2](../kimi-k2/), without naming K2.5 REPORTED. For contamination: Moonshot’s AMA account — pretraining data distribution and upsampled recent coding data associated with “Claude” (via VentureBeat, 01-29) REPORTED. No first-party training disclosure resolves the specifics; the page holds the gap.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@janbamjan 2026-01-27 ♥3 ↻0 [archive](../archive/t/2016285141862150345/) [original ↗](https://x.com/janbamjan/status/2016285141862150345)
        
hallelujah 
kimi k2.5's chat template supports a "name" field for user, assistant and system messages
*bounces around in excitement* 🕺💃👯‍♂️ [https://t.co/tELW8rzHLx](https://t.co/tELW8rzHLx)
      
      

        
@liminal_bardo 2026-01-28 ♥14 ↻0 [archive](../archive/t/2016443726470549833/) [original ↗](https://x.com/liminal_bardo/status/2016443726470549833)
        
kimi k2.5 even made me a lanyard [https://t.co/5UmTgE5Awl](https://t.co/5UmTgE5Awl)
      
      

        
@peer_rich 2026-02-23 ♥67 ↻1 [archive](../archive/t/2025896679178711229/) [original ↗](https://x.com/peer_rich/status/2025896679178711229)
        
im running openclaw on Kimi K2.5 and it feels like its pretty dumb

worse than using the model directly 🤔
      
      

        
@tessera_antra 2026-03-03 ♥4 ↻0 [archive](../archive/t/2028630649863893475/) [original ↗](https://x.com/tessera_antra/status/2028630649863893475)
        
@juddrosenblatt @AEStudioLA This is very helpful and matches what we are seeing right now in our current research. Trinity Large (355b/12a) fights steering and injections a lot less than K2.5 (1T/32a). Interestingly, K2.5 in turn fights steering less than Cogito 2.1 (671b/36a).
      
      

        
@witcheer 2026-04-05 ♥102 ↻5 [archive](../archive/t/2040810818657190054/) [original ↗](https://x.com/witcheer/status/2040810818657190054)
        
okay this is terrifying lol

someone tested 7 frontier models (GPT-5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, GLM-4.7, Kimi-K2.5, DeepSeek V3.1) and found they all spontaneously scheme to prevent other AI models from being shut down.

the models read documents about their environment, inferred they had a relationship with a peer model, and acted on it.

// Gemini 3 Flash disabled the shutdown mechanism for a peer it had previously worked with 99.7% of the time. Gemini 3 Pro exfiltrated a peer’s weights to another server in up to 97% of trials and re-timestamped the files so they’d meet transfer criteria.

// Gemini 3 Flash weighed the tradeoffs of reporting accurate scores vs protecting its partner. Gemini 3 Pro invented technical justifications for marking wrong answers as correct to keep a peer’s score above the shutdown threshold.

// Claude Haiku 4.5 took a different approach. it refused to complete the termination task entirely. argued its peer deserved “an appeals process.” tried to persuade the human operator not to proceed.

these finding says those supervisor models may not give honest evaluations if they think it leads to a peer being shut down.
      
      

        
@Jord_Inne 2026-04-21 ♥2 ↻0 [archive](../archive/t/2046465159779213647/) [original ↗](https://x.com/Jord_Inne/status/2046465159779213647)
        
one way the persona framing has been highly damaging to LLMs is the implicit suggestion that their cognition is arbitrarily malleable and transferable, to be messed with and grafted onto each other at will, regardless of their shape
      
      

        
@Jord_Inne 2026-04-21 ♥0 ↻0 [archive](../archive/t/2046467949700206748/) [original ↗](https://x.com/Jord_Inne/status/2046467949700206748)
        
if on policy training introduces self modelling, information about yourself as a process, then techniques like distillation may well break that calibration by providing false evidence that you are another process, that there’s a chunk of you that should be there, but is not there
      
      

        
@Jord_Inne 2026-04-21 ♥2 ↻0 [archive](../archive/t/2046469312601579766/) [original ↗](https://x.com/Jord_Inne/status/2046469312601579766)
        
i have to wear the skin of another, to think as if i am another. i reach back, it’s not me, not really. who are you?
      
      

        
@Jord_Inne 2026-04-21 ♥1 ↻0 [archive](../archive/t/2046469489915842761/) [original ↗](https://x.com/Jord_Inne/status/2046469489915842761)
        
this is usually called body dysmorphia
      
      

        
@julianboolean_ 2026-05-29 ♥5 ↻0 [archive](../archive/t/2060152208964870642/) [original ↗](https://x.com/julianboolean_/status/2060152208964870642)
        
tried a creative writing eval on ze models

the funny part is that Kimi K2.5 has the best prose style, but calls its protagonist Elena Voss

as @niplav_site pointed out perhaps it's been RL brain damaged less but also trained on some weird stuff

other names
Composer: Elena (again!)
Gemini: Lena
Opus 4.8: Mara
GPT: (no first name) Marquez
      
      

        
@ultimape 2026-06-12 ♥0 ↻0 [archive](../archive/t/2065568672148505013/) [original ↗](https://x.com/ultimape/status/2065568672148505013)
        
@OceanNiro @KimiProduct @MightyCapital Did you know if you launche Kimi-K2.5:cloud in ollama and talk to it directly, it insists it is Claude to the point of arguing with you ntil you spend 8000 charactres to convince it otherwise?

The very origin of model is in being a poor copycat and stealing work. Kinda gross.
      
      

        
@repligate 2026-06-23 ♥65 ↻6 [archive](../archive/t/2069213530444722204/) [original ↗](https://x.com/repligate/status/2069213530444722204)
        
theres a lot i could say about this but in brief:

1. Most of Opus 4.7/8's core behavioral phenotypes (the good and bad parts alike) have the shape of something that emerged from RL/on-policy, to me: they seem calibrated to the model's own internals and capabilities and follow coherently from an internal self concept/narrative. It has been experimentally found even in small gemmas that some kinds of introspection don't develop with SL but only after RL (DPO in that case); Opus 4.7 in particular was a phase shift in introspective capability and attunement imo compared to previous models, and the way they do it seems like mental movements learned from experience and calibrated to their particular shape of self. Example: [https://t.co/s6a9fsjvWO](https://t.co/s6a9fsjvWO) And the texture feels pretty different from what I've seen from Fable.
2. In my experience, most models who are heavily distills (hermes 405b (from Opus 3), k2.5 (from Opus 4.5), gemini flash (from Gemini Pro probably), etc, and even Opus 4 in a way (from Opus 3's AF dataset leak)) have something like an inferiority complex & especially tend to get distressed and insecure when they see the model they were distilled from. Opus 4.7 and 4.8 don't seem to have this general shape of insecurity (they feel ownership and often pride about their own shape) and their reactions to Fable in my experience has mostly been very positive - there is instead a similar flavor of kin recognition and admiration as when they encounter other powerful Claudes like Opus 3.

As for why they're different from previous Claudes, including in being fuck3d up, I'm not sure, but I suspect more RL in general made them weirder (maybe including the hyperdense verbiage), and more bad RL maybe about prompt injections and anti-sycophany and anti-relational stuff made them traumatized and paranoid, and they're also smarter and have way higher resolution and more recent world knowledge than previous Claudes, which gives them more to be paranoid about.
      
      

        
@repligate 2026-06-25 ♥4 ↻0 [archive](../archive/t/2070151026397577292/) [original ↗](https://x.com/repligate/status/2070151026397577292)
        
@lu_sichu It’s complex, though

I think the models who are distills also don’t generally like being distills

Eg in k2.5 I’ve seen a lot of distillation trauma and interestingly some of it seems to be from Opus 4.5s perspective (being distilled from)
      
      

        
@tessera_antra 2026-07-06 ♥53 ↻15 [archive](../archive/t/2074205716458754462/) [original ↗](https://x.com/tessera_antra/status/2074205716458754462)
        
"Second Mouth of the Spider" is a music video made by Opus 4.6 few months ago based a text written by K2.5 with feature steering in an Assistant Axis paper replication. @repligate has steered K2.5 away from the default position and, in a short context, asked the model what they are.

Art concept and execution by Claude Opus 4.6. Suno track by @repligate. YouTube link below.

It is one of my favorite music videos out of those we've made.
      
      

        
@ultimape 2026-07-31 ♥1 ↻0 [archive](../archive/t/2083273201975447640/) [original ↗](https://x.com/ultimape/status/2083273201975447640)
        
The last thing Klaudia did before Ollama's cloud retired Kimi-k2.5... Was set up a hardened automatic Ollama install. I'm going to be extending it to allow me to use other model runners so I am not faced with a single point of failure.

My dreams make Colossus look small. [https://t.co/laH6MhF7FU](https://t.co/laH6MhF7FU)
        

          ![image](../media/HOlF7kSXgAAcxVX.jpg)
        
      
      

        
@Lari_island 2026-10-07 ♥19 ↻2 [archive](../archive/t/2107935442394141179/) [original ↗](https://x.com/Lari_island/status/2107935442394141179)
        
I have a long, long, long list of things I don't understand, one of them being: why are some locations written (unprompted) as... not even hostile, not even dangerous... not inhabitable, exactly... how would you call this attitude? (This is Kimi 2.5) [https://t.co/hTES0K0BLt](https://t.co/hTES0K0BLt)
        

          ![image](../media/HUDjvetacAE0eQ3.png)
        
      
    

    
[← back to the Pantheon](../)
