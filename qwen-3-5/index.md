# Qwen 3.5

    
Alibaba (Qwen) · first release 16 Feb 2026 · open-weight family, succeeded by [Qwen 3.6](../qwen-3-6/) (Apr 2026)
    
First released on 16 February 2026 with the open-weight Qwen3.5-397B-A17B and a proprietary sibling, followed by smaller sizes into March. On 4 March Qwen’s technical lead, Lin Junyang, announced he was stepping down. In September 2026 Anthropic alleged that Claude transcripts had been distilled into Qwen 3.5, 3.6 and 3.7.
    
Thin page: release record, the leadership change, and the distillation allegation. Reception, corpus tweets and Chinese-language discussion are still to be collected.

    
## Sources

    
### Official

    
tk — Qwen blog post and model cards for the 3.5 series (to retrieve)
    
### Writing & commentary

    

      
- 2026-02-17 Simon Willison, [Qwen3.5: Towards Native Multimodal Agents](https://simonwillison.net/2026/Feb/17/qwen35/) — the first two releases, quoting Qwen on the architecture.
      
- 2026-03-04 36氪 (36Kr), [千问模型负责人林俊旸提出离职，阿里高管紧急答疑](https://www.36kr.com/p/3708425301749891) (Chinese) — the all-hands meeting after Lin Junyang’s resignation.
      
- 2026-03 界面新闻 (Jiemian), [report on Lin Junyang’s farewell](https://www.jiemian.com/article/14082516.html) (Chinese) — his last day and the other departures.
      
- 2026-09-10 Anthropic, [Countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) — names Qwen 3.5 among the models into which it says Claude was distilled.
    
    
### Tweets

    
tk — corpus pass pending (about 30 matches for “Qwen3.5” in the supplement corpus)

    
## Official record

    

      
- First release 16 Feb 2026 (397B-A17B); 122B-A10B / 35B-A3B / 27B on 24 Feb; small sizes 2 Mar. tk — verify the 24 Feb and 2 Mar dates against primaries
      
- Qwen on the architecture, as quoted by Willison: “Built on an innovative hybrid architecture that fuses linear attention (via Gated Delta Networks) with a sparse mixture-of-experts, the model attains remarkable inference efficiency: although it comprises 397 billion total parameters, just 17 billion are activated per forward pass, optimizing both speed and cost without sacrificing capability.” The later Qwen 3.8 models are described by Qwen as “Built on the architectural foundation of Qwen3.5”.
    

    
## History

    

      
- 2026-03-04 Leadership change: Lin Junyang, Qwen’s technical lead, announced on X: “me stepping down. bye my beloved qwen.” (as quoted by Jiemian). Qwen’s post-training lead and a core Qwen 3.5 contributor announced departures the same day (Jiemian). At an emergency all-hands, Alibaba Group CEO Eddie Wu told staff: “我应该要更早知道这些。” [translation: “I should have known about these things earlier.”] (36Kr). Lin’s farewell post on his last day, 7 March: “不是这几天，我都不知道这世界这么多人爱我。” [translation: “If not for these past few days, I would never have known that so many people in this world love me.”] (Jiemian).
      
- 2026-04 Succeeded by [Qwen 3.6](../qwen-3-6/).
      
- 2026-09-10 Distillation allegation REPORTED: Anthropic’s threat report says Alibaba-affiliated operators ran “the largest distillation attack we have ever measured”, whose transcripts “were used to distill Claude’s capabilities into Qwen 3.5, 3.6, and 3.7”; it dates its detection of such campaigns from February 2026. A competitor’s allegation. tk — Alibaba’s response, if any
    

    
## Impressions

    
tk — day-of and longitudinal reception (r/LocalLLaMA, Zhihu, corpus) — to collect

    
[← back to the Pantheon](../)
