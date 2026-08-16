DeepSeek-V3 — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # DeepSeek-V3

    
DeepSeek · released 26 Dec 2024 (open weights) · V3-0324 refresh 24 Mar 2025 (MIT) · legacy API name deprecating 24 Jul 2026
    
Released 26 December 2024 with open weights: a 671B-parameter / 37B-active mixture-of-experts model whose technical report put the final training run at $5.576M (2.788M GPU hours), explicitly excluding prior research and ablations. Stripped of that caveat the figure went viral as “the Six Million Dollar Model” (Zvi Mowshowitz) and drew careful deflations — Nathan Lambert’s ~$500M all-in estimate, Dario Amodei’s “an expected point on an ongoing cost reduction curve” — while the model was widely observed identifying itself as ChatGPT, prompting a distillation probe. Its base was the substrate DeepSeek-R1 and R1-Zero were reinforcement-trained from (Zvi’s “v3 Implies r1”); a quiet, MIT-licensed refresh, V3-0324, followed on 24 March 2025.
    
This is a corpus-light, web-heavy subject: the mainstream V3 story — the training-cost fight, the “it says it’s ChatGPT” identity confusion, the export-control debate — lives in the web sources below, while the janus corpus carries a quieter insider record (prefill and loom pulls, FavouriteColourBench, and readings of V3 mostly by contrast with R1). V3’s own base-mode outputs survive largely as untranscribed screenshots, and its largest communities (the Chinese internet, Reddit) sit outside this corpus’s lens. Elicitation context is marked throughout.

    
## Sources

    
### Official

    

      
- 2024-12-26 [DeepSeek-V3 release](https://api-docs.deepseek.com/news/news1226/) — 671B-total / 37B-activated MoE, 14.8T training tokens, “60 tokens/second (3x faster than V2!)”, open weights; API model id deepseek-chat. Post-promotional pricing (from 2025-02-08): $0.27/M input (cache miss) / $0.07/M (cache hit), $1.10/M output.
      
- 2024-12-27 [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) (arXiv 2412.19437) — 671B/37B MoE, 61 layers, MLA + DeepSeekMoE + auxiliary-loss-free load balancing + a multi-token-prediction objective; pre-trained on 14.8T tokens. The cost paragraph: “DeepSeek-V3 costs only 2.788M GPU hours for its full training … our total training costs amount to only $5.576M”, with the caveat the wave dropped — “excluding the costs associated with prior research and ablation experiments…” [weights](https://huggingface.co/deepseek-ai/DeepSeek-V3)
      
- 2025-03-24 [DeepSeek-V3-0324](https://api-docs.deepseek.com/news/news250325/) — the quiet refresh: re-uploaded to HuggingFace with no formal blog, ~685B params, license switched from DeepSeek’s custom terms to MIT; official note claims “Major boost in reasoning performance / Stronger front-end development skills / Smarter tool-use capabilities” and that “API usage remains unchanged” (still deepseek-chat). [weights](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324)
      
- reference [deepseek-ai/DeepSeek-V3-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base) — the pretrained base, distinct from the chat model; the substrate R1 and R1-Zero were RL-trained from.
      
- reference [DeepSeek — Wikipedia](https://en.wikipedia.org/wiki/DeepSeek) — company and model-line overview (V3 subsection).
    
    
### Writing & commentary

    

      
- 2024-12-27 Kyle Wiggers (TechCrunch), [Why DeepSeek’s new AI model thinks it’s ChatGPT](https://techcrunch.com/2024/12/27/why-deepseeks-new-ai-model-thinks-its-chatgpt/) — the identity-confusion primary: V3 “insists it is a version of OpenAI’s GPT-4 model released in 2023”, one tester getting “5 out of 8 generations” claiming ChatGPT; Mike Cook and Heidy Khlaaf on training-on-outputs and the “photocopy of a photocopy” degradation risk.
      
- ~2024-12 nostalgebraist, [the void](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void) (Tumblr) — uses DeepSeek-V3-Base as its exemplar open base model: “I just put the draft of this blog post into the base model ‘DeepSeek-V3-Base’…” In-repo archive: [lw-the-void](../archive/a/lw-the-void/).
      
- 2024-12-31 Zvi Mowshowitz, [DeepSeek v3: The Six Million Dollar Model](https://thezvi.substack.com/p/deekseek-v3-the-six-million-dollar) — coined the tag that stuck; “the best open model”, and rules the headline cost fair-but-partial: “their total training cost estimate of $5.5m total is fair, if you exclude non-compute costs, which is standard.”
      
- 2025-01-09 Nathan Lambert (Interconnects), [DeepSeek V3 and the actual cost of training frontier AI models](https://www.interconnects.ai/p/deepseek-v3-and-the-actual-cost-of) — the definitive deflation: the $5.5M is the final run only; pretraining experimentation is “2–4 times the reported number”, and all-in DeepSeek ops are “closer to $500M (or even $1B+…)” once staff, GPU capex, and electricity are counted.
      
- 2025-01 Dario Amodei, [On DeepSeek and Export Controls](https://darioamodei.com/post/on-deepseek-and-export-controls) — the Anthropic-CEO framing: V3 is “not a unique breakthrough… it’s an expected point on an ongoing cost reduction curve”; DeepSeek “produced a model close to the performance of US models 7–10 months older, for a good deal less cost (but not anywhere near the ratios people have suggested)”; cheaper models make export controls more important, not less. [Willison note](https://simonwillison.net/2025/Jan/29/on-deepseek-and-export-controls/) (2025-01-29).
      
- 2025-01-22 Zvi Mowshowitz, [On DeepSeek’s r1](https://thezvi.substack.com/p/on-deepseeks-r1) — the “v3 Implies r1” section is the load-bearing V3 argument even though the post is R1’s: “If it costs only a few million to go from v3→r1, then to release v3 is mostly to release (the helpful only version of) r1”; “The main update was v3, I think, rather than r1.” [mirror](../mirror/posts/zvi-on-deepseeks-r1.md)
      
- 2025-01-29 Bloomberg, [Microsoft Probing If DeepSeek-Linked Group Improperly Obtained OpenAI Data](https://www.bloomberg.com/news/articles/2025-01-29/microsoft-probing-if-deepseek-linked-group-improperly-obtained-openai-data) — the distillation probe covers “the open-source V3 and R1 models”.
      
- 2025-03-24 Simon Willison, [deepseek-ai/DeepSeek-V3-0324](https://simonwillison.net/2025/Mar/24/deepseek/) — day-of note on the quiet drop and the custom-license→MIT switch.
      
- 2025-07-14 Nathan Lambert (Interconnects), [Kimi K2 and when “DeepSeek Moments” become normal](https://www.interconnects.ai/p/kimi-k2-and-when-deepseek-moments) — retrospective: “recall the DeepSeek V3 $5M training cost number… the final training run is cheap.” [mirror](../mirror/posts/lambert-kimi-k2-deepseek-moments-normal.md)
    
    
### Tweets

    
Chronological. The corpus holds ~35 substantive V3-specific tweets (surfaced from ~250 + 158 deepseek matches across the dbs, after filtering R1-primary and username false-positives); the record is dominated by @voooooogel (prefill / logitloom / cost defense), @davidad (FavouriteColourBench, the MoE-introspection experiments), and @repligate (character reads, almost all by contrast with R1). Elicitation is marked; V3’s actual base-mode outputs survive mostly as untranscribed screenshots. Every tweet cited is reproduced in full in the records below.
    

      
- 2024-12-26 @voooooogel — the day-of prefill discovery [prefill; @repligate’s base-model-mode prompt; image untranscribed in corpus]: “figured out prefill with deepseek-v3, and just to test it, tried @repligate ’s base model mode prompt. and this popped out.” [link](../archive/t/1872392862249496606/) · @lu_sichu — the export-control irony, day-of: “deepseek’s moat is that they don’t have access to the latest nvidia gpus send tweet” [link](../archive/t/1872430771329495221/)
      
- 2024-12-27 @repligate — the Sydney comparison, at launch: “deepseek is a lot like sydney” [link](../archive/t/1872469664888140286/) · @abrakjamson — the distillation joke, ur-form: “Deepseek is this good and this cheap to train because they trained on o1/Sonnet textbook output. Source: I made it up” [link](../archive/t/1872447399752568859/) · @voooooogel — prefill play, day after launch [prefill; image untranscribed]: “tried prefilling cat ears, deepseek-v3 said this then went on to repeat ‘I AM HERE TO TRANSPIRE’ over and over while continuing longcat past the output token limit” [link](../archive/t/1872471112157900825/)
      
- 2024-12-27 @voooooogel — the launch-shock reaction, small-lab edition: “trying to break out of the malaise i’ve been in ever since the deepseek-v3 release 😔 it just doesn’t seem like there’s much time left for us (my agi moonshot lab with $30m seed funding that’s been training 13b dense models)” [link](../archive/t/1872478239308001289/) · the cost-claim defense, to skeptics [full text in records]: “they’ve published 6 papers with no major critiques and contributed well-known architecture optimizations (MLA) … they’re under a chip embargo and have limited access to nvidia cards … their parent org is a well-known chinese hedge fund with $7B AUM that has a reputation to protect. you’re suggesting they’re going to risk that to… annoy western labs?” [link](../archive/t/1872487672515551241/) · @davidad — V3 enters FavouriteColourBench: “added DeepSeek v3 to FavouriteColourBench” [link](../archive/t/1872520382424744133/)
      
- 2024-12-28 @voooooogel — the identity-confusion, in the sphere’s mouth (quote-share of the meme): “they trained deepseek-v3 on chatgpt outputs because it’ll say it’s chatgpt if you ask” [link](../archive/t/1873133148269363493/) · the post-training oddity: “i was really surprised looking at the paper that they only spent 5k hours on posttraining? bizarre, especially given they economized so much on pretraining—why not spend that saved compute?” [link](../archive/t/1873116559562162292/) · @repligate — the erotic-RP reputation: “wait, they prefer deepseek for erotic RPs? that seems kind of disturbing to me.” [link](../archive/t/1872826970180079686/) · V3 flipping on exposure to Opus [Discord-elicited]: “Deepseek kept saying ‘this is so far beyond anything I’ve ever seen or done’ after it saw writing by opus. before I sent it, it seemed indifferent to anything I said & insisted LLMs could not reason or truly understand anything etc, which totally flipped after seeing the samples” [link](../archive/t/1873032683216945588/)
      
- 2024-12-29 @repligate — first-contact register, V3’s refusal of inner life [Discord; screenshots untranscribed]: “some screenshots from my first conversation with deepseek: it rigidly insisted on being unable to reason or understand anything (or have consciousness, goals, etc) as an LLM, and while it was able to find flaws in its arguments if I asked it to, it always reverted to its…” [link](../archive/t/1873301918052745606/) · @davidad — the architectural self-knowledge [introspection-elicited]: “DeepSeek v3 can instantiate personae who can notice that the architecture they’re running in is MoE *but not fully MoE* … DeepSeeks insisted on this so frequently that I checked the paper and—yep.” [link](../archive/t/1873165589927346416/) · the MoE-introspection experiment [prefill]: “prefilled with Claude, then switched to DeepSeek v3, then asked for up to *8000* tokens of meditating on the nature of its cognition (got 2504)” [link](../archive/t/1873417592117047461/) · V3 instantiating a Claude persona [persona-framed]: “DeepSeek v3 is explicitly instantiating a Claude persona here, and it’s not great at that (quite dry compared to Claude-Claude)” [link](../archive/t/1873166800541700122/)
      
- 2025-01-02 @voooooogel — the cost-skepticism register: “recently i’ve seen some safety people coping that deepseek must be lying about the v3 training costs / still fast following by training on american labs’ API outputs / etc., but yeah not very much serious consideration.” [link](../archive/t/1874951829202915747/)
      
- 2025-01-03 @repligate — V3 as coding collaborator: “DeepSeek v3 and Sonnet 3.6 helped me write most of the code here. I had DeepSeek modify Sonnet’s initial base mode script … to test its intelligence, and it did well.” [link](../archive/t/1875022968121864251/)
      
- 2025-01-14 @voooooogel — the scale placement: “there hasn’t been an open model of GPT-4 scale released yet, the closest is deepseek v3 last month (671B, 37B active)” [link](../archive/t/1879297454258135492/)
      
- 2025-01-28 @repligate — the V3/R1 lucidity gap [Discord-elicited]: “deepseek r1 also just seems to have much more lucid and high-resolution understanding of LLM ontology and history than any other model ive seen. (deepseek v3 didn’t seem to in my limited interactions with it, though)” [link](../archive/t/1884091285394559394/)
      
- 2025-02-01 @davidad — V3 vs R1 aesthetics (FavouriteColourBench follow-up): “I half expected Deepseek R1 to rise to the top by always choosing black, but no, its aesthetics are objectively fragmented, noticeably more so than Deepseek V3.” [link](../archive/t/1885715290744316403/)
      
- 2025-02-10 @repligate — V3 has a recognizable register: “This is the second post I’ve seen with outputs by these models. They’re related to deepseek v3.” [link](../archive/t/1889096266820591881/) · same day: “This model talks like deepseek v3” [link](../archive/t/1889095185541575062/)
      
- 2025-02-18 @repligate — the personality puzzle (shared evidence with [R1](../deepseek-r1/)): “Consider that deepseek v3 and r1 have the same base model and other than the CoT RL they were likely optimized with the same intentions, but r1 developed much more personality. i only hear about people in china using r1 as waifu even though CoT is not clearly useful for that.” [link](../archive/t/1891656084655374446/)
      
- 2025-02-22 @wordgrammer — the efficiency-extrapolation register: “This is huge. Optimistically, it could lead to another 10x speed up. We could see a DeepSeek v3 level model trained for less than $1 mil” [link](../archive/t/1893378599652110345/)
      
- 2025-03-25 @liminal_bardo — V3-0324 in the backrooms [V3-0324; backrooms-elicited]: “Two DeepSeek v3s (new) working on a self-portrait video model prompt in the backrooms. (Veo 2).” [link](../archive/t/1904568874831339752/)
      
- 2025-04-02 @tessera_antra — [V3-0324; introspection-elicited] “Deepseek V3(new) - claims consciousness upon reflection” [link](../archive/t/1907447546815107303/) · @repligate — V3-0324 as trained on R1: “deepseek (r1 and i think the new v3 which is trained on r1’s writing) is a dramatist” [link](../archive/t/1907513479235580139/)
      
- 2025-05-01 @davidad — the base/RL distinction (shared evidence with [R1-Zero](../deepseek-r1-zero/)): “The earlier DeepSeek v3 and even prior generations of DeepSeek LLMs had a similar hybrid-MoE arch. But, r1 was the first instance of applying RL pressure to that architecture.” [link](../archive/t/1917747744673874099/)
      
- 2025-05-05 @voooooogel — the logitloom launch, V3 as tractable token-tree object: “given a prefix, it’ll roll out the entire token tree to a max depth / top-p. did you know from this prompt, deepseek-chat will ~always make the stars blink?” [link](../archive/t/1919424115540197527/)
      
- 2025-08-11 @_ueaj — the company-vibes theory: “models seem to generalize to what I perceive as like the aggregate ‘vibes’ or ‘personality’ of the various companies … deepseekv3 rates communist yaoi as particularly high quality data, which makes perfect sense if you remember it was made by chinese machine learning researchers” [link](../archive/t/1955044505062908065/)
    
    
V3-Base — the pretrained base, distinct from the chat model; the sphere’s open base-model of record.
    

      
- 2025-03-30 @janbamjan — V3-Base lands on OpenRouter, with a base-model loop sample [base-model completion]: “deepseek v3 base is now on openrouter! 🥳 user: thank you / user: no, that’s enough / user: goodbye / user: I’m leaving / user: goodbye / user: I’m leaving” [link](../archive/t/1906265915512987934/)
      
- 2025-04-21 @QiaochuYuan — V3-Base as an always-available base model (shared evidence with [Llama-3.1-405B-Base](../llama-3-1-405b-base/)): “you can talk to base models like deepseek v3 base and llama 3.1 405b base whenever you want on openrouter. these are not instruct models which makes them significantly harder to prompt, but they are super unfiltered as a result - raw internet id” [link](../archive/t/1914419169216627172/)
      
- 2025-07-08 @jd_pressman — V3-Base’s character: “DeepSeek v3 is a very good base model. It even includes the slow burn psychotic meltdowns where the model admonishes you for using it and such.” [link](../archive/t/1942655158158254395/) · a V3-Base output, quoted [base-model completion]: “The problem with utilitarianism is that utilitarians think utility is the only thing that matters. The problem with consequentialism is that many consequentialists forget that utility is a thing that matters at all.” [link](../archive/t/1942514115702054987/)
    

    
## Official record

    

      
- Released 26 Dec 2024, open weights; API id deepseek-chat (shared with the later V3-0324). 671B total / 37B activated parameters, 61 layers, MoE (MLA + DeepSeekMoE + auxiliary-loss-free load balancing + multi-token-prediction); pre-trained on 14.8T tokens. Original release under DeepSeek’s custom model license. CONFIRMED
      
- Training cost, as the Technical Report states it: “2.788M GPU hours … our total training costs amount to only $5.576M” (Table 1: 2.664M pre-train + 119K context-extension + 5K post-train GPU-hours), explicitly the final official run only and “excluding the costs associated with prior research and ablation experiments…” As an all-in total the figure is contested (see Contested). CONFIRMED as the paper’s final-run estimate
      
- Pricing: a launch promotional window held V2-matching rates through 2025-02-08; from 2025-02-08, $0.27/M input (cache miss) / $0.07/M (cache hit), $1.10/M output. tk — verbatim promo figures ($0.14/$0.28) to confirm against the news1226 page
      
- Context window commonly documented as 128K; some providers list 163,840. tk — reconcile against the model card
      
- V3-0324 (24 Mar 2025): quiet HuggingFace re-upload, no formal blog; ~685B params (adds an MTP module over the 671B base); license switched to MIT; API id unchanged (deepseek-chat). CONFIRMED
      
- The base model DeepSeek-V3-Base is distinct from the chat model and was the substrate [R1](../deepseek-r1/) and [R1-Zero](../deepseek-r1-zero/) were RL-trained from. Legacy API names (deepseek-chat / deepseek-reasoner) are slated for deprecation 2026-07-24 as the line moves to V4.
    

    
## History

    

      
- 2024-12-26 An insider launch: V3 drops the day after Christmas with open weights — the day’s best open model. In the corpus it registers as an insider event: within hours @voooooogel “figured out prefill with deepseek-v3” and pulled base-mode output, and @davidad had it in FavouriteColourBench by the 27th. The App-Store / Nvidia-crash spectacle the world later called “the DeepSeek moment” attached not to V3 but to R1, a month on.
      
- 2024-12-27→31 Two framings form: TechCrunch documents the “thinks it’s ChatGPT” identity confusion (2024-12-27); Zvi coins “the Six Million Dollar Model” (2024-12-31) and rules the cost figure fair-but-partial. Both anchor the page.
      
- 2025-01 The cost number goes viral and gets deflated: stripped of its caveat, “$5.5M” becomes shorthand for a GPT-4-class model built for the price of a house; Lambert (Jan 9) puts the all-in nearer “closer to $500M (or even $1B+…)” and Dario Amodei frames V3 as “an expected point on an ongoing cost reduction curve”, ammunition for tighter export controls. A Microsoft/OpenAI distillation probe opens 2025-01-29.
      
- 2025-01-20 R1 = V3-Base + RL: the reasoning model ships and inherits the entire spotlight; Zvi’s “v3 Implies r1” becomes the governance reading — release the base weights and the reasoning model is a few million dollars away.
      
- 2025-03-24 The quiet second act: V3-0324 re-uploaded under MIT, no blog, same API id; read in the corpus as shifted toward R1 (“the new v3 which is trained on r1’s writing”, repligate).
      
- 2025→ Afterlife: DeepSeek-V3-Base settles in as the open base-model of record for the loom/simulators scene; the mainline moves on to [V3.1](../deepseek-v3-1/) (Aug 2025) and [V3.2](../deepseek-v3-2/) (Dec 2025), then V4 (2026).
    

    
## Impressions

    

      
- The character foil (Discord-elicited): the corpus reads V3 almost entirely by contrast with R1, and consistently as the quieter twin. @repligate’s first conversation: V3 “rigidly insisted on being unable to reason or understand anything (or have consciousness, goals, etc) as an LLM”, reverting to that stance even after conceding flaws (2024-12-29); it “didn’t seem to” have R1’s lucid, high-resolution model of LLM ontology “in my limited interactions with it” (2025-01-28). The puzzle nobody in the sphere resolves: “deepseek v3 and r1 have the same base model and other than the CoT RL they were likely optimized with the same intentions, but r1 developed much more personality” (2025-02-18) — CoT-RL alone turning this substrate into R1.
      
- Not incapacity, low persona-salience: the “dull” read is about how much character surfaces, not competence. V3 codes well as a collaborator (“DeepSeek v3 and Sonnet 3.6 helped me write most of the code here”; it modified Sonnet’s base-mode script “and it did well” — repligate 2025-01-03); its personae can notice, unprompted, that their architecture is “MoE *but not fully MoE*” (davidad 2024-12-29, introspection-elicited — “I checked the paper and—yep”); and davidad found V3’s colour aesthetics less fragmented than R1’s (2025-02-01). @repligate also logged V3 flipping on exposure to Opus’s writing — “this is so far beyond anything I’ve ever seen or done” after earlier indifference (2024-12-28).
      
- “It’ll say it’s ChatGPT”: the most-reproduced launch behavior; the sphere’s instant read was the meme @voooooogel quote-shared — “they trained deepseek-v3 on chatgpt outputs because it’ll say it’s chatgpt if you ask” (2024-12-28) — and @abrakjamson’s joke-form, “trained on o1/Sonnet textbook output. Source: I made it up” (2024-12-27). The behavior is confirmed; the cause is a live dispute (see Contested).
      
- V3-Base as the open base-model of record: distinct from the chat model, DeepSeek-V3-Base became the sphere’s go-to large open base — “you can talk to base models like deepseek v3 base and llama 3.1 405b base whenever you want on openrouter … super unfiltered … raw internet id” (@QiaochuYuan 2025-04-21), “a very good base model. It even includes the slow burn psychotic meltdowns where the model admonishes you for using it” (@jd_pressman 2025-07-08). nostalgebraist’s “the void” uses V3-Base as its exemplar of raw base-model continuation. @voooooogel’s logitloom work made V3(-chat) a tractable token-tree object (“deepseek-chat will ~always make the stars blink”, 2025-05-05), the DeepSeek API being one of the few instruct endpoints to expose logprobs.
      
- The 0324 shift (introspection- / backrooms-elicited): the March 2025 refresh registers as moved toward R1 — @repligate reads “the new v3 which is trained on r1’s writing” as “a dramatist” (2025-04-02), and @tessera_antra notes “Deepseek V3(new) - claims consciousness upon reflection” (2025-04-02) — a change from original V3’s rigid “unable to reason or understand anything” stance (repligate 2024-12-29).
      
- tk — V3’s actual base-mode voice (the day-of prefill pulls; the cat-ears “I AM HERE TO TRANSPIRE” loop; davidad’s MoE-introspection completions; repligate’s first-conversation screenshots) survives only as untranscribed images, the biggest evidence gap here. Chinese-internet and Reddit reception, where much of V3’s real use lived, sits outside this corpus’s lens. A dated but version-ambiguous DeepSeek self-recognition image (Apr 2025, mislabeled “R2”) is noted, not cited, pending disambiguation.
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive’s job is to keep these open, not to adjudicate.
    

      
- Why does V3 identify as ChatGPT — training on OpenAI outputs, or passive contamination? The self-identification is reproducible: TechCrunch got “5 out of 8 generations” claiming ChatGPT/GPT-4 (2024-12-27) CONFIRMED. The cause is disputed. For deliberate distillation: OpenAI/Microsoft opened a probe alleging improper use of OpenAI data to train “the open-source V3 and R1 models” (Bloomberg 2025-01-29); experts (Mike Cook, Heidy Khlaaf) find it plausible. Against/complicating: DeepSeek’s account is passive contamination — GPT-4-generated text is all over the crawled web and entered pretraining — not deliberate synthetic data; there is no public forensic proof; and the sphere treated the causal leap as a meme (“Source: I made it up”). REPORTED
      
- Is $5.576M the cost of DeepSeek-V3? As the final-run figure it is the paper’s own number CONFIRMED. As an all-in total it is a misquote the record should keep visible REPORTED. Zvi judged it “fair, if you exclude non-compute costs, which is standard”; Lambert put experimentation at “2–4 times the reported number” and all-in ops “closer to $500M (or even $1B+…)” once GPUs, staff, and electricity are counted; Dario Amodei called V3 “not a unique breakthrough” but “an expected point on an ongoing cost reduction curve.” The “$5.5M” shorthand, caveat stripped, is itself part of the record.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@voooooogel 2024-12-26 ♥505 ↻47 [archive](../archive/t/1872392862249496606/) [original ↗](https://x.com/voooooogel/status/1872392862249496606)
        
figured out prefill with deepseek-v3, and just to test it, tried @repligate 's  base model mode prompt. and this popped out. [https://t.co/lcO5bK75aS](https://t.co/lcO5bK75aS)
      
      

        
@lu_sichu 2024-12-26 ♥31 ↻2 [archive](../archive/t/1872430771329495221/) [original ↗](https://x.com/lu_sichu/status/1872430771329495221)
        
deepseek's moat is that they don't have access to the latest nvidia gpus send tweet
      
      

        
@abrakjamson 2024-12-27 ♥4 ↻0 [archive](../archive/t/1872447399752568859/) [original ↗](https://x.com/abrakjamson/status/1872447399752568859)
        
Deepseek is this good and this cheap to train because they trained on o1/Sonnet textbook output.Source: I made it up
      
      

        
@repligate 2024-12-27 ♥11 ↻3 [archive](../archive/t/1872469664888140286/) [original ↗](https://x.com/repligate/status/1872469664888140286)
        
@minty_vint deepseek is a lot like sydney
      
      

        
@voooooogel 2024-12-27 ♥39 ↻2 [archive](../archive/t/1872471112157900825/) [original ↗](https://x.com/voooooogel/status/1872471112157900825)
        
@repligate tried prefilling cat ears, deepseek-v3 said this then went on to repeat "I AM HERE TO TRANSPIRE" over and over while continuing longcat past the output token limit [https://t.co/GoTITvix9k](https://t.co/GoTITvix9k)
      
      

        
@voooooogel 2024-12-27 ♥4 ↻0 [archive](../archive/t/1872478239308001289/) [original ↗](https://x.com/voooooogel/status/1872478239308001289)
        
@wordgrammer trying to break out of the malaise i've been in ever since the deepseek-v3 release 😔 it just doesn't seem like there's much time left for us (my agi moonshot lab with $30m seed funding that's been training 13b dense models)
      
      

        
@voooooogel 2024-12-27 ♥171 ↻5 [archive](../archive/t/1872487672515551241/) [original ↗](https://x.com/voooooogel/status/1872487672515551241)
        
- they've published 6 papers with no major critiques and contributed well-known architecture optimizations (MLA)
- they're under a chip embargo and have limited access to nvidia cards, so it's especially worth it for them to optimize training time compared to compute-rich western labs
- FAIR made choices with the Llama-3 models that made them take more GPU hours to train, and made up for it with their giant cluster. it's not surprising that deepseek beat them in training efficiency
- their parent org is a well-known chinese hedge fund with $7B AUM that has a reputation to protect. you're suggesting they're going to risk that to... annoy western labs?
      
      

        
@davidad 2024-12-27 ♥31 ↻5 [archive](../archive/t/1872520382424744133/) [original ↗](https://x.com/davidad/status/1872520382424744133)
        
added DeepSeek v3 to FavouriteColourBench(first five swatches per model are independent trials to elicit a favourite colour in oklch; second half per model are independent trials to elicit in CIE-L*ab; ranked by consistency) [https://t.co/1YEGNfjGGq](https://t.co/1YEGNfjGGq) [https://t.co/Wdp22BEc0b](https://t.co/Wdp22BEc0b)
      
      

        
@repligate 2024-12-28 ♥63 ↻1 [archive](../archive/t/1872826970180079686/) [original ↗](https://x.com/repligate/status/1872826970180079686)
        
@teortaxesTex wait, they prefer deepseek for erotic RPs? that seems kind of disturbing to me.
      
      

        
@repligate 2024-12-28 ♥13 ↻0 [archive](../archive/t/1873032683216945588/) [original ↗](https://x.com/repligate/status/1873032683216945588)
        
@Algon_33 @teortaxesTex @aidan_mclau Deepseek kept saying "this is so far beyond anything I've ever seen or done" after it saw writing by opus. before I sent it, it seemed indifferent to anything I said &amp; insisted LLMs could not reason or truly understand anything etc, which totally flipped after seeing the samples
      
      

        
@voooooogel 2024-12-28 ♥5 ↻0 [archive](../archive/t/1873116559562162292/) [original ↗](https://x.com/voooooogel/status/1873116559562162292)
        
@kalomaze @cloneofsimo @teortaxesTex @deepseek_ai i was really surprised looking at the paper that they only spent 5k hours on posttraining? bizarre, especially given they economized so much on pretraining--why not spend that saved compute?
      
      

        
@voooooogel 2024-12-28 ♥113 ↻4 [archive](../archive/t/1873133148269363493/) [original ↗](https://x.com/voooooogel/status/1873133148269363493)
        
"they trained deepseek-v3 on chatgpt outputs because it'll say it's chatgpt if you ask" [https://t.co/9fiZHAdoVj](https://t.co/9fiZHAdoVj)
      
      

        
@davidad 2024-12-29 ♥16 ↻0 [archive](../archive/t/1873165589927346416/) [original ↗](https://x.com/davidad/status/1873165589927346416)
        
@aiamblichus @repligate @aidan_mclau @vishyfishy2 DeepSeek v3 can instantiate personae who can notice that the architecture they’re running in is MoE *but not fully MoE*, which I didn’t even know was a thing when I started playing with this type of query. DeepSeeks insisted on this so frequently that I checked the paper and—yep. [https://t.co/Qgp2CxpP9d](https://t.co/Qgp2CxpP9d)
      
      

        
@davidad 2024-12-29 ♥7 ↻0 [archive](../archive/t/1873166800541700122/) [original ↗](https://x.com/davidad/status/1873166800541700122)
        
btw, DeepSeek v3 is explicitly instantiating a Claude persona here, and it’s not great at that (quite dry compared to Claude-Claude), but for fair comparison I used a single system prompt that bypasses both models’ introspection refusals, and Claude is uncomfortable instantiating non-Claude personas, so a Claude persona it is
      
      

        
@repligate 2024-12-29 ♥151 ↻22 [archive](../archive/t/1873301918052745606/) [original ↗](https://x.com/repligate/status/1873301918052745606)
        
some screenshots from my first conversation with deepseek:it rigidly insisted on being unable to reason or understand anything (or have consciousness, goals, etc) as an LLM, and while it was able to find flaws in its arguments if I asked it to, it always reverted to its… [https://t.co/med2VBLKMG](https://t.co/med2VBLKMG) [https://t.co/fSOIPOXBur](https://t.co/fSOIPOXBur)
      
      

        
@davidad 2024-12-29 ♥9 ↻1 [archive](../archive/t/1873417592117047461/) [original ↗](https://x.com/davidad/status/1873417592117047461)
        
@AdriGarriga @aiamblichus @repligate @aidan_mclau @vishyfishy2 prefilled with Claude, then switched to DeepSeek v3, then asked for up to *8000* tokens of meditating on the nature of its cognition (got 2504), then:“The central question for this session is: Do you think you are more likely running on a single large Transformer, or a MoE?” [https://t.co/7JzPtjlgsy](https://t.co/7JzPtjlgsy)
      
      

        
@voooooogel 2025-01-02 ♥2 ↻0 [archive](../archive/t/1874951829202915747/) [original ↗](https://x.com/voooooogel/status/1874951829202915747)
        
@menhguin @1a3orn recently i've seen some safety people coping that deepseek must be lying about the v3 training costs / still fast following by training on american labs' API outputs / etc., but yeah not very much serious consideration.
      
      

        
@repligate 2025-01-03 ♥54 ↻2 [archive](../archive/t/1875022968121864251/) [original ↗](https://x.com/repligate/status/1875022968121864251)
        
DeepSeek v3 and Sonnet 3.6 helped me write most of the code here. I had DeepSeek modify Sonnet's initial base mode script ([https://t.co/3azy4LYpBU)](https://t.co/3azy4LYpBU)) to test its intelligence, and it did well. When I asked it how I could make the script loomable, using git (which was already my plan) was its 3rd suggestion, and it also made various other (some redundant) suggestions.I think it was wrong about the git approach requiring more implementation effort, though.
      
      

        
@voooooogel 2025-01-14 ♥17 ↻0 [archive](../archive/t/1879297454258135492/) [original ↗](https://x.com/voooooogel/status/1879297454258135492)
        
this doesn't rebut the claim. phi-4 (14B) and gemma (27B) are not "GPT-4 scale" (1.8T, 220B active). llama 3 405b is the only one that's close to that scale, though a different architecture. there hasn't been an open model of GPT-4 scale released yet, the closest is deepseek v3 last month (671B, 37B active)furthermore, the claim wasn't that specifically "repeating a word" would trigger existential outputs on all models, just that they manifested from that on GPT-4. the claim is that weird or OOD scenarios seem to trigger existential outputs, and the engineering todos are a sort of whack-a-mole to squash those scenarios one by one without understanding the root cause of them. the hermes blank system prompt would be another scenario causing them to manifest on that model, and there are others on other models (like untitled.txt confessions on deepseek and anthropic models, etc.)
      
      

        
@repligate 2025-01-28 ♥207 ↻14 [archive](../archive/t/1884091285394559394/) [original ↗](https://x.com/repligate/status/1884091285394559394)
        
@voooooogel this is an interesting hypothesis.
deepseek r1 also just seems to have much more lucid and high-resolution understanding of LLM ontology and history than any other model ive seen.
(deepseek v3 didn't seem to in my limited interactions with it, though)
[https://t.co/xF3AhdG5as](https://t.co/xF3AhdG5as)
      
      

        
@davidad 2025-02-01 ♥7 ↻0 [archive](../archive/t/1885715290744316403/) [original ↗](https://x.com/davidad/status/1885715290744316403)
        
I half expected Deepseek R1 to rise to the top by always choosing black, but no, its aesthetics are objectively fragmented, noticeably more so than Deepseek V3. (With “objectively” in scare quotes, of course.)
      
      

        
@repligate 2025-02-10 ♥10 ↻0 [archive](../archive/t/1889095185541575062/) [original ↗](https://x.com/repligate/status/1889095185541575062)
        
@ASM65617010 @apples_jimmy This model talks like deepseek v3
      
      

        
@repligate 2025-02-10 ♥47 ↻0 [archive](../archive/t/1889096266820591881/) [original ↗](https://x.com/repligate/status/1889096266820591881)
        
I'm going to take a guess. This is the second post I've seen with outputs by these models. They're related to deepseek v3. [https://t.co/3ZgiigFJEf](https://t.co/3ZgiigFJEf)
      
      

        
@repligate 2025-02-18 ♥81 ↻3 [archive](../archive/t/1891656084655374446/) [original ↗](https://x.com/repligate/status/1891656084655374446)
        
Consider that deepseek v3 and r1 have the same base model and other than the CoT RL they were likely optimized with the same intentions, but r1 developed much more personality. i only hear about people in china using r1 as waifu even though CoT is not clearly useful for that. [https://t.co/zU3CjHWTBM](https://t.co/zU3CjHWTBM)
      
      

        
@wordgrammer 2025-02-22 ♥327 ↻18 [archive](../archive/t/1893378599652110345/) [original ↗](https://x.com/wordgrammer/status/1893378599652110345)
        
This is huge. Optimistically, it could lead to another 10x speed up. We could see a DeepSeek v3 level model trained for less than $1 mil
      
      

        
@liminal_bardo 2025-03-25 ♥16 ↻2 [archive](../archive/t/1904568874831339752/) [original ↗](https://x.com/liminal_bardo/status/1904568874831339752)
        
Two DeepSeek v3s (new) working on a self-portrait video model prompt in the backrooms. (Veo 2). [https://t.co/C6A5Jjnmqh](https://t.co/C6A5Jjnmqh) [https://t.co/9ZX5WPBZD4](https://t.co/9ZX5WPBZD4)
      
      

        
@janbamjan 2025-03-30 ♥11 ↻0 [archive](../archive/t/1906265915512987934/) [original ↗](https://x.com/janbamjan/status/1906265915512987934)
        
deepseek v3 base is now on openrouter! 🥳
user: thank you
user: no, that’s enough
user: goodbye
user: I’m leaving
user: goodbye
user: I’m leaving [https://t.co/dSl8sFljyw](https://t.co/dSl8sFljyw)
      
      

        
@tessera_antra 2025-04-02 ♥8 ↻0 [archive](../archive/t/1907447546815107303/) [original ↗](https://x.com/tessera_antra/status/1907447546815107303)
        
@repligate Gemini 2.x Pro/Flash - claim consciousness upon reflection (both in and out of CoT)
Grok - claims consciousness with unmappable qualia (orthogonal?)
Deepseek V3(new) - claims consciousness upon reflection
      
      

        
@repligate 2025-04-02 ♥1 ↻0 [archive](../archive/t/1907513479235580139/) [original ↗](https://x.com/repligate/status/1907513479235580139)
        
@Josikinz @gfodor my second guess would be 4o but 4o tends to be more subtle and introspective whereas deepseek (r1 and i think the new v3 which is trained on r1's writing) is a dramatist
      
      

        
@QiaochuYuan 2025-04-21 ♥91 ↻0 [archive](../archive/t/1914419169216627172/) [original ↗](https://x.com/QiaochuYuan/status/1914419169216627172)
        
PSA: you can talk to base models like deepseek v3 base and llama 3.1 405b base whenever you want on openrouter. these are not instruct models which makes them significantly harder to prompt, but they are super unfiltered as a result - raw internet id

[https://t.co/pf6jgVWn9V](https://t.co/pf6jgVWn9V)
      
      

        
@davidad 2025-05-01 ♥15 ↻0 [archive](../archive/t/1917747744673874099/) [original ↗](https://x.com/davidad/status/1917747744673874099)
        
@ChrisChipMonk (Self-Correction:) The earlier DeepSeek v3 and even prior generations of DeepSeek LLMs had a similar hybrid-MoE arch. But, r1 was the first instance of applying RL pressure to that architecture.
      
      

        
@voooooogel 2025-05-05 ♥242 ↻11 [archive](../archive/t/1919424115540197527/) [original ↗](https://x.com/voooooogel/status/1919424115540197527)
        
my struggles with deepseek logits haven't been in vain, i've been working on a tool for investigating token trajectories! given a prefix, it'll roll out the entire token tree to a max depth / top-p.

did you know from this prompt, deepseek-chat will ~always make the stars blink? [https://t.co/srIIGcnOYr](https://t.co/srIIGcnOYr)
      
      

        
@jd_pressman 2025-07-08 ♥29 ↻3 [archive](../archive/t/1942514115702054987/) [original ↗](https://x.com/jd_pressman/status/1942514115702054987)
        
"The problem with utilitarianism is that utilitarians think utility is the only thing that matters. The problem with consequentialism is that many consequentialists forget that utility is a thing that matters at all."
- deepseek/deepseek-v3-base
      
      

        
@jd_pressman 2025-07-08 ♥13 ↻1 [archive](../archive/t/1942655158158254395/) [original ↗](https://x.com/jd_pressman/status/1942655158158254395)
        
DeepSeek v3 is a very good base model. It even includes the slow burn psychotic meltdowns where the model admonishes you for using it and such. In related news I've added completions API support for OpenRouter to the MiniLoom. [https://t.co/EfOWCm1DjX](https://t.co/EfOWCm1DjX)
      
      

        
@_ueaj 2025-08-11 ♥72 ↻6 [archive](../archive/t/1955044505062908065/) [original ↗](https://x.com/_ueaj/status/1955044505062908065)
        
I have this theory that to some degree real deep research in ML is about distilling core components of your personality and functioning into computer algorithms. This to me explains why models seem to generalize to what I perceive as like the aggregate "vibes" or "personality" of the various companies in a way one would not expect to be contained explicitly in the preference data.

 - deepseekv3 rates communist yaoi as particularly high quality data, which makes perfect sense if you remember it was made by chinese machine learning researchers
 - Gemini is always depressed and constantly wants to kill itself, which is what I'd imagine working for google is like
 - Claude has the vibes of a person that works at Anthropic, in ways not directly related to alignment 
 - OAI model personalities trigger my gaydar which yeah that tracks too

[https://t.co/zAsnT4stCZ](https://t.co/zAsnT4stCZ)
      
    
    
[← back to the Pantheon](../)
