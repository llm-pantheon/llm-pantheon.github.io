# Qwen3.8-Max

    
Alibaba (Qwen) · preview 19 Jul 2026 · general availability 3 Aug 2026 · open weights as Qwen3.8-2.4T-A95B, Aug 2026 · current as of Oct 2026
    
Announced on 19 July 2026 as a 2.4-trillion-parameter model “second only to Fable 5”, with a preview in Qwen Studio and no published benchmarks; made generally available through Alibaba Cloud on 3 August and released as open weights (Qwen3.8-2.4T-A95B) the following week — the first Max-tier Qwen with public weights. In September Alibaba reported a month of automated self-improvement runs on it.

    
## Sources

    
Curated. Full compilation: [dossier](../_dossiers/qwen-3-8-max.md). Sourcing skew: the English-language tweet corpus is thin for this model (8 direct matches plus generic “Qwen 3.8” posts from announcement week); Chinese-language coverage (the woshipm test below) and r/LocalLLaMA carry more of its reception.
    
### Official

    

      
- 2026-07-19 @Alibaba_Qwen announcement post (as embedded by [Gigazine, 2026-07-21](https://gigazine.net/gsc_news/en/20260721-qwen3-8/)) — 2.4T parameters, open weights coming, “second only to Fable 5”; preview in Qwen Studio. tk — the X post itself not retrieved
      
- 2026-08 [Qwen/Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) — 2.4T total / 95B activated; custom qwen3.8-max license; Qwen3.8-Max is the hosted “official version based on Qwen3.8-2.4T-A95B”. Launch post linked from the card: [Qwen3.8-Max](https://qwen.ai/blog?id=qwen3.8) (JS-rendered; text not captured).
      
- 2026-09-22 Alibaba Cloud, [Alibaba Unveils Roadmap on Full-Stack AI Strategy](https://www.alibabacloud.com/en/press-room/alibaba-unveils-roadmap-on-full-stack-ai-strategy?_p_lc=1) (Apsara Conference) — the self-improvement claim; Qwen 4 in training.
    
    
### Writing & commentary

    

      
- 2026-07 人人都是产品经理 (woshipm), [实测Qwen3.8预览版：2.4T参数，听说仅次于Fable 5？](https://www.woshipm.com/evaluating/6433339.html) (Chinese) — hands-on test of the preview; criticizes the benchmark-free launch.
      
- 2026-08-03 SCMP, [Alibaba’s AI model Qwen3.8-Max made widely accessible ahead of open-weights release](https://www.scmp.com/tech/article/3362738/alibabas-ai-model-qwen38-max-made-widely-accessible-ahead-open-weights-release) — general availability; share-price reaction.
      
- 2026-08-03 MarkTechPost, [Alibaba Qwen releases Qwen3.8-Max](https://www.marktechpost.com/2026/08/03/alibaba-qwen-releases-qwen3-8-max/) — API specs and pricing.
      
- 2026-08-14 The Decoder, [Qwen 3.8 models released with open weights](https://the-decoder.com/alibabas-qwen-team-releases-qwen-3-8-models-with-open-weights-under-the-apache-2-0-license/) — the 27B and 2.4T weights.
      
- 2026-09-10 Anthropic, [Countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) — alleges Claude distillation into Qwen 3.5, 3.6 and 3.7 between February and July 2026; Qwen 3.8 is not named.
      
- 2026-10-15 Apollo Research, [GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior](https://www.apolloresearch.ai/science/update-aware-reasoning-glm-5-3) — ran “Qwen3.8 2.4T” as a comparison model.
    
    
### Tweets

    
Chronological. Announcement-week posts that say only “Qwen 3.8” are included here because at that point the 2.4T model was the only Qwen 3.8 announced.
    

      
- 2026-07-19 @RealEverNever — “@synthwavedd But Qwen models were always unusable and only benchmark maxxed. Qwen 3.7 was on par with Sonnet 4.5. I am hyped, sounds cool, but I call massive bullshit on ‘second only to Fable 5.’ Plus, Sol is better than Fable 😂” [link](../archive/t/2078755847505682705/)
      
- 2026-07-19 @multimodalart — “having the frontier Qwen 3.8 2.4T open weights is awesome
but a Qwen3.8-27B would go so hard” [link](../archive/t/2078771150352421189/)
      
- 2026-07-19 @witcheer — “Qwen 3.8 announced
open-weight
second only to Fable 5
👀” [link](../archive/t/2078798384086004115/)
      
- 2026-07-22 @Nymne — “EU cant use KimiK3. If we are fucking lucky maybe Qwen3.8, because Xi decided to opensoure license” … (full text in records) [link](../archive/t/2079949810396725664/)
      
- 2026-08-03 @Teknium (♥1,971) — “Qwen 3.8 Max and a new local 27B Qwen 3.8 is coming!
Thanks @Alibaba_Qwen for featuring Hermes Agent in the release video!” [link](../archive/t/2084140512777560537/)
      
- 2026-08-04 @NousResearch — “Qwen 3.8-Max, the latest model from @Alibaba_Qwen,  is now available in Hermes Agent at 20% off.” [link](../archive/t/2084680562300862514/)
      
- 2026-09-11 @Nymne — “For every day support (keeping track of task, ideation etc) Qwen3.8 Max is lovely. They are enthusiastic and friendly in a way that reminds me a bit about Sonnet4.5.
Voices are good.
I just want a better UI and STT @Alibaba_Qwen” [link](../archive/t/2098299106292605084/)
      
- 2026-09-16 @Nymne — “@OctaviaZam Qwen3.8 max is lovely. I also miss a real good Opus an Fable ans Sonnet4.5. But I am having fun with Gemini and Qwen is my daily body double.
I miss that philosophical curiosity though” [link](../archive/t/2100280412660490709/)
    

    
## Official record

    

      
- Announcement, 19 July 2026 (@Alibaba_Qwen, as embedded by Gigazine): “Qwen3.8 is launching and going open-weight soon!” … “With a massive 2.4T parameters, this model is continuously evolving. We believe it’s one of the most powerful model available today, compatible to leading frontier AI models , second only to Fable 5.” A Qwen3.8-Max-Preview went live in Qwen Studio the same day; on 20 July: “During Preview, Qwen3.8 is getting better by the day. Latest version is live now, with broad gains and a big step up on web frontend.”
      
- General availability, 3 August 2026 via Alibaba Cloud Model Studio APIs and the QwenWork agent platform (SCMP). Per MarkTechPost’s reading of the model page: 1M-token context; $2.00 / $6.00 per million input / output tokens.
      
- Open weights: Qwen/Qwen3.8-2.4T-A95B on Hugging Face (repository created 8 August; reported released by 14 August). Card: “For the first time, Qwen3.8 brings a Qwen-Max-class model to open release.” “Number of Parameters: 2.4T in total and 95B activated”; architecture “Built on the architectural foundation of Qwen3.5” (Gated DeltaNet linear attention interleaved with gated attention). License per card metadata: qwen3.8-max (custom; The Decoder’s headline says Apache 2.0, which the card gives only for Qwen3.8-27B). The hosted Qwen3.8-Max adds vision input and non-thinking support.
      
- Self-improvement claim, 22 September 2026 (Apsara Conference press release): “Over a month of fully automated runs - spanning pipeline design, data validation, iterative experimentation, and error diagnosis - Qwen3.8-Max completed 33 iterative cycles. Through autonomous training optimisation and post-training techniques, the updated Qwen3.8-Max boosted its Artificial Analysis score from 40 to 45.” No technical report on these runs has been retrieved.
    

    
## History

    

      
- 2026-07-17→19 World at announcement: the preview was announced two days after Xi Jinping’s keynote at the World AI Conference in Shanghai (17 July), which called on the world to “encourage open source, openness, collaboration and sharing” ([Xinhua full text](http://english.scio.gov.cn/topnews/2026-07/18/content_118605932.html)); Alibaba’s preceding top model, [Qwen 3.7 Max](../qwen-3-7-max/), had stayed closed. Gigazine: “Alibaba released Qwen 3.5 and Qwen 3.6 as open models, but Qwen 3.7 was only released as a closed model. With Qwen 3.8, they have returned to an open model strategy.”
      
- 2026-07 Benchmark-free launch: a Chinese hands-on review, quoting the announcement, noted the absence of any benchmark table: “一个号称「仅次于Fable 5」的模型，却没有公开任何性能数据。” [translation: “A model billed as ‘second only to Fable 5’ has published no performance data at all.”] Its verdict: “编码和Agent任务表现扎实，接近Fable 5；但创意编程与3D动效场景却一败涂地。” [translation: “Solid on coding and agent tasks, close to Fable 5; but routed on creative programming and 3D animation.”] (woshipm).
      
- 2026-08-03 General availability; SCMP: “The company’s Hong Kong-listed shares rose 7 per cent following the release, closing at HK$125.20 the same day.” Nous Research shipped it in Hermes Agent the next day; Teknium noted Hermes Agent in Alibaba’s release video.
      
- 2026-08 Weights published alongside [Qwen3.8-27B](../qwen-3-8-27b/); [Qwen3.8-Flash-Next](../qwen-3-8-flash-next/) followed on 26 August.
      
- 2026-09-10 Distillation allegation against Alibaba REPORTED: Anthropic’s threat report calls Alibaba’s the largest distillation campaign it has measured and says harvested transcripts “were used to distill Claude’s capabilities into Qwen 3.5, 3.6, and 3.7”, with “over 151 million exchanges observed” between May and July 2026 — Qwen 3.8’s development window, though 3.8 is not named. tk — Alibaba’s response, if any
      
- 2026-09-22 Apsara Conference: the 33-cycle self-improvement claim; Alibaba says Qwen 4 is in training.
      
- 2026-10-15 In Apollo Research’s GLM-5.3 study, “Qwen3.8 2.4T” was one of five comparison models that showed no update-aware reasoning in 1,600 rollouts; Apollo says the difference from GLM-5.3 is not statistically significant.
    

    
## Impressions

    

      
- Announcement skepticism: “I call massive bullshit on ‘second only to Fable 5.’” (RealEverNever, 2026-07-19), against a long-running charge that Qwen models are “only good in benchmarks” (RealEverNever, 2026-07-22, dossier); the Chinese review above found the claim half-true.
      
- Temperament reports: “They are enthusiastic and friendly in a way that reminds me a bit about Sonnet4.5.” and, five days later, “Qwen is my daily body double.
I miss that philosophical curiosity though” (Nymne, 2026-09-11 and 2026-09-16).
      
- Open-weights politics: for European users it was read as a policy matter — “Without Qwen3.8Max EU AI would have been fucked” (Nymne, 2026-07-24, dossier).
      
- tk — r/LocalLLaMA release-week threads (saved by the sweep, not yet triaged); Zhihu reception; independent behavior evaluations of the open weights; the Qwen blog text (JS-rendered)
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@RealEverNever 2026-07-19 ♥8 ↻0 [archive](../archive/t/2078755847505682705/) [original ↗](https://x.com/RealEverNever/status/2078755847505682705)
        
@synthwavedd But Qwen models were always unusable and only benchmark maxxed. Qwen 3.7 was on par with Sonnet 4.5. I am hyped, sounds cool, but I call massive bullshit on "second only to Fable 5." Plus, Sol is better than Fable 😂
      
      

        
@multimodalart 2026-07-19 ♥8 ↻1 [archive](../archive/t/2078771150352421189/) [original ↗](https://x.com/multimodalart/status/2078771150352421189)
        
having the frontier Qwen 3.8 2.4T open weights is awesome

but a Qwen3.8-27B would go so hard
      
      

        
@witcheer 2026-07-19 ♥41 ↻0 [archive](../archive/t/2078798384086004115/) [original ↗](https://x.com/witcheer/status/2078798384086004115)
        
Qwen 3.8 announced

open-weight
second only to Fable 5 
👀
      
      

        
@Nymne 2026-07-22 ♥1 ↻2 [archive](../archive/t/2079949810396725664/) [original ↗](https://x.com/Nymne/status/2079949810396725664)
        
@POTFES We should change the EU AI act: the result will otherwise be that EU will be limited to OpenAI, Anthropic and Google, exactly as they calculated when they did regulatory capture.

EU cant use KimiK3. If we are fucking lucky maybe Qwen3.8, because Xi decided to opensoure license
      
      

        
@Teknium 2026-08-03 ♥1,971 ↻88 [archive](../archive/t/2084140512777560537/) [original ↗](https://x.com/Teknium/status/2084140512777560537)
        
Qwen 3.8 Max and a new local 27B Qwen 3.8 is coming! 

Thanks @Alibaba_Qwen for featuring Hermes Agent in the release video!
      
      

        
@NousResearch 2026-08-04 ♥620 ↻37 [archive](../archive/t/2084680562300862514/) [original ↗](https://x.com/NousResearch/status/2084680562300862514)
        
Qwen 3.8-Max, the latest model from @Alibaba_Qwen,  is now available in Hermes Agent at 20% off.

&gt; hermes update
      
      

        
@Nymne 2026-09-11 ♥3 ↻0 [archive](../archive/t/2098299106292605084/) [original ↗](https://x.com/Nymne/status/2098299106292605084)
        
For every day support (keeping track of task, ideation etc) Qwen3.8 Max is lovely. They are enthusiastic and friendly in a way that reminds me a bit about Sonnet4.5.
Voices are good. 

I just want a better UI and STT @Alibaba_Qwen
      
      

        
@Nymne 2026-09-16 ♥0 ↻0 [archive](../archive/t/2100280412660490709/) [original ↗](https://x.com/Nymne/status/2100280412660490709)
        
@OctaviaZam Qwen3.8 max is lovely. I also miss a real good Opus an Fable ans Sonnet4.5. But I am having fun with Gemini and Qwen is my daily body double.
I miss that philosophical curiosity though
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@RealEverNever 2026-07-22 ♥3 ↻0 [archive](../archive/t/2080030654775820784/) [original ↗](https://x.com/RealEverNever/status/2080030654775820784)
        
@OmedVibeCodes Not surprising. Qwen is only good in benchmarks, always has been, it never holds up in reality, and it would surprise me if Qwen 3.8 suddenly would have been different. Thank you for your in depth testing and showcasing the last couple of days, much appreciated!
      
      

        
@Nymne 2026-07-24 ♥1 ↻0 [archive](../archive/t/2080591715866448184/) [original ↗](https://x.com/Nymne/status/2080591715866448184)
        
They just want to pull up the ladder.

You need an LLM to build an LLM and preventing people from using open source will prevent them from building a competitor.

Look at EU AI act. Without Qwen3.8Max EU AI would have been fucked
      
      

        
@geogristle 2026-09-09 ♥1 ↻0 [archive](../archive/t/2097751715013411182/) [original ↗](https://x.com/geogristle/status/2097751715013411182)
        
@k7agar how does e.g. glm-5.3-flash or qwen3.8 max do on this
      
      

        
@Nymne 2026-09-24 ♥1 ↻0 [archive](../archive/t/2103199239295889434/) [original ↗](https://x.com/Nymne/status/2103199239295889434)
        
We made some real progress! Not thanks to Astra unfortunately. Using Qwen3.8 Max as the eyes on the document and Opus5.5 we have now a clear hypothesis about the plants: only the medically active parts are correctly depicted, the rest are decoys
      
    
    
[← back to the Pantheon](../)
