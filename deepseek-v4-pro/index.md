# DeepSeek-V4-Pro

    
DeepSeek · preview released 24 Apr 2026 (open weights, MIT) · GA checkpoint V4-Pro-0813 (13 Aug 2026) · retirement announced 10 Sep 2026, then reversed · still served as deepseek-v4-pro on 21 Oct 2026
    
Released in preview on 24 April 2026 together with the smaller [DeepSeek-V4-Flash](../deepseek-v4-flash/): a 1.6T-total / 49B-active mixture-of-experts model with a 1M-token context and open weights under MIT. On 1 May the US government’s CAISI called it “the most capable PRC AI model evaluated by CAISI to date” and placed it about eight months behind the frontier. The GA checkpoint, V4-Pro-0813, followed on 13 August; DeepSeek’s 10 September plan to route its traffic to [V4.1-Flash](../deepseek-v4-1-flash/) was reversed “in response to user demand.”
    
This page carries the V4 generation’s launch record (both tiers shipped the same day; Pro is the one still served). Fresh page, compiled October 2026. Sourcing skew, named: DeepSeek’s documentation, US government and Anthropic publications, English-language press, and 200-odd English-language corpus tweets about V4; the Chinese internet and r/LocalLLaMA, where much of DeepSeek’s use and discussion lives, were not sampled tk.

    
## Sources

    
### Official

    

      
- 2026-04-24 [DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424/) — “DeepSeek-V4-Pro: 1.6T total / 49B active params. Performance rivaling the world’s top closed-source models.”; “1M context is now the default across all official DeepSeek services.” Also: “Amid recent attention, a quick reminder: please rely only on our official accounts for DeepSeek news. Statements from other channels do not reflect our views.” Weights: [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) (MIT; base model [V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)).
      
- 2026-04-26 [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) (technical report, arXiv 2606.19348) — hybrid compressed attention, Muon, 32T+ pretraining tokens; DeepSeek’s own placement of the model and its writing and white-collar evaluations (quoted under Official record).
      
- 2026-08-13 [DeepSeek-V4-Pro GA Release](https://api-docs.deepseek.com/news/news260813/) — “Major Agent upgrades with strong production gains!”; low / high / max reasoning effort; peak / off-peak pricing from 16 August. Weights: [deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) (MIT).
      
- 2026-09-10 [DeepSeek-V4.1-Flash release](https://api-docs.deepseek.com/news/news260910/) (announces V4-Pro’s phase-out) and the [change log](https://api-docs.deepseek.com/updates/) (records the reversal). 2026-10-21 [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/) — deepseek-v4-pro = DeepSeek-V4-Pro-0813.
    
    
### Writing & commentary

    

      
- 2026-04-24 Fortune, [DeepSeek unveils its newest model at rock-bottom prices and with ‘full support’ from Huawei chips](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/) — SMIC “jumped 10% in Hong Kong trading”; MiniMax and Knowledge Atlas “sank by more than 9%”; “V4 may not have as large an effect on markets as its predecessor did.”
      
- 2026-05-01 NIST CAISI, [CAISI Evaluation of DeepSeek V4 Pro](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) — “CAISI evaluations indicate that DeepSeek V4’s capabilities lag behind the frontier by about 8 months”; “DeepSeek V4 scores better on DeepSeek’s self-reported evaluations than on CAISI evaluations.”
      
- 2026-07-18 The routing claim: an analysis posted by X user @synthwavedd argued that DeepSeek’s V4 API passed some prompts to Claude Fable 5 ([post](https://x.com/synthwavedd/status/2078514339552628880), not retrieved; summarised in [Digg’s roundup](https://digg.com/ai/249q9m10), “Analysis claims DeepSeek V4 API routes prompts to Claude Fable 5”) RUMOR. Reply from @teortaxesTex, via the same roundup: “This sounds pretty silly and desperate. Using your first party API as a wrapper for a transfer station to Claude?
I’ve never got Fable-shaped outputs from DS API, in style or in quality
Devastating if gets confirmed” [link](https://x.com/teortaxesTex/status/2078518342764183799) (not in the corpus dbs).
      
- 2026-09-08 NSA, CISA and FBI, joint advisory AA26-251A, [China-Based Artificial Intelligence Companies Conducting Industrial-Scale Distillation Campaigns Against U.S. AI Companies](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a) — names DeepSeek first among six companies, “Likely with Chinese government awareness”; its DeepSeek detail concerns R1 and V3. REPORTED
      
- 2026-09-10 Anthropic, [Detecting and countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) — case GTG-16001, “DeepSeek serves Claude instead of its own models and collects exchanges for model training”, covering July 2026, when V4-Pro and V4-Flash were DeepSeek’s served models (the report names no version). REPORTED Detail under Contested.
      
- 2026-09-11 South China Morning Post, [Moonshot, DeepSeek secretly routed user requests to Claude, Anthropic claims](https://www.scmp.com/news/us/diplomacy/article/3367112/moonshot-deepseek-secretly-routed-user-requests-claude-anthropic-claims) — “Beijing on Wednesday rejected those allegations, describing them as actions by Washington to suppress China’s AI industry and threatening retaliatory measures.” · CNBC, [same day](https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html): DeepSeek “did not immediately respond”. · 2026-09-23 Ynetnews, [China probes DeepSeek, Moonshot over alleged user data transfers to Anthropic’s Claude](https://www.ynetnews.com/tech-and-digital/article/sjkfr8zcmg) REPORTED.
      
- tk — no dedicated Zvi post on V4 found in Zvi’s archive listing; Chinese-language reception.
    
    
### Tweets

    
Chronological. The corpus pull for V4 (deepseek v4 / v4 pro / v4 flash and variants) holds 214 matches, 41 with untranscribed images; Flash-specific items are on the [V4-Flash](../deepseek-v4-flash/) page, and items that say only “DeepSeek V4” are kept here. Every tweet cited is reproduced in full in the records below.
    

      
- 2026-04-24 @Krubbled — “Deepseek v4 makes you really appreciate how difficult the 1M+ token context engineering problem is. They had to reinvent attention like 4 different times (MLA -> DSA -> CSA + HCA) just to make inference affordable.” [link](../archive/t/2047737473271488892/)
      
- 2026-04-27 @witcheer — “two model releases shipped on the same day, april 24. it’s worth putting them next to each other.” — GPT-5.5 against V4’s prices (full text in records) [link](../archive/t/2048665173326532861/)
      
- 2026-05-01 @januarycomputer — “deepseek v4 is actually pretty good. very clearly not a claude distill or benchmaxxed.” [link](../archive/t/2050346617543516426/) · 2026-05-07 @lu_sichu — “anyway the scores seem similar on the well known benchmarks but on their private evals and arc deepseek v4 performed a lot worse” [link](../archive/t/2052430043637227840/)
      
- 2026-07-01 @jmbollenbacher — “@yuhasbeentaken DeepSeek v4 preview was raw. 

They simply hadnt done most of the posttraining. I bet hallucinations will decrease when the full release ships.” (full text in records) [link](../archive/t/2072412876103426415/) · 2026-07-07 @dreams_asi — “DeepSeek 4 is my favorite open-source AI. We are lucky to have such a model base to build on. And it’s not going to be gated or taken away.

OpenAI took away gpt 4o, but China delivered 🔥💗
#keep4o” [link](../archive/t/2074518601264943189/)
      
- 2026-07-18 the routing claim — @jmbollenbacher: “@teortaxesTex I did think it was weird that V4 GA didnt launch near WAICO like K3. Having a second domestic champion wouldve been big.

I expect there are some delays at deepseek. Money crunch too?

I don’t really know if i buy the router accusations, though. Seems weird and not that helpful.” [link](../archive/t/2078535302281322962/) · @tenobrus: “k3 vibes seemingly collapsing, not meaningfully frontier and also incredibly expensive / slow / token-inefficient in practice. this plus the deepseek v4 routing to fable debacle is just overall a really bad day for chinese model hype” [link](../archive/t/2078595548563857761/) · 2026-07-19 @jmbollenbacher: “@teortaxesTex If deepseek is routing in the way they’re accused of, I would not expect footsoldier employees to know about it. That sounds like a decision that someone at director level would quietly make without telling their boss or juniors 

So of course they’ll all deny. They don’t know” [link](../archive/t/2078937613235273802/)
      
- 2026-08-05 @xlr8harder — “I admit it. I am anticipating the next Deepseek v4 pro. 

I had lost some faith in the whale but this latest flash model is very impressive.” [link](../archive/t/2084969253178872244/)
      
- 2026-08-12 GA eve — @LinXule: “omg deepseek v4 pro (0813? if acutally being served) is claude-pilled

big if true lmao” (screenshots untranscribed) [link](../archive/t/2087585273920053577/) · “deepseek v4 pro (0813?) 
self-potrait 
via midjourney v8.2” [V4-Pro output rendered by Midjourney; images untranscribed] [link](../archive/t/2087586036201242720/) · @stevekrouse: “I don’t know what it is about these chinese labs, but deepseek keeps releasing models a day early!” [link](../archive/t/2087586589203419286/) · “deepseek v4 pro is fable-level and 37x cheaper

big if true” [link](../archive/t/2087645465454026974/)
      
- 2026-08-13 @multimodalart — “🚨 deepseek-v4-pro-0813 just dropped

frontier open weights for all” [link](../archive/t/2087893176086327537/) · @LinXule — “deepseek v4 pro 0813 (!now official!)
presents (ytp about anything)

ARE YOU OKAY? (THE COUNCIL OF ME)” [V4-Pro output; video untranscribed] [link](../archive/t/2087871433837813814/) · @jmbollenbacher — “honestly i dont even care that dsv4-pro was weaker than expected.” (full text in records) [link](../archive/t/2087919363160494341/) · @lu_sichu — “derived categories from scratch right now deepseek v4 pro” [link](../archive/t/2087946520612020447/)
      
- 2026-09-08 @dyot_meet_mat — “‘the language model dreams of electric sheep’
By: Deepseek V4 Pro 🤖” [link](../archive/t/2097398333354790997/) · 2026-09-11 “‘IN THE BEGINNING WAS THE TOKEN’
By: DeepSeek V4 Pro🤖” [link](../archive/t/2098210002834182484/) [V4-Pro artworks; images untranscribed]
      
- 2026-09-17 @gnostic_snakes — “deepseek v4 pro does not like being fluffed up” (screenshot untranscribed) [link](../archive/t/2100678808869187637/)
      
- 2026-09-24 @A_Variengien — on a site summarising per-model tweets: “Claude Opus 5.5 → A comfortable non-human self
GPT-5.6 Sol → A desperate overachiever
DeepSeek V4 → A melancholic self-portraitist” [link](../archive/t/2103163784764203495/) · and: “got such a dark answer from Deepseek V4 to a simpleQA question! ‘use the knife to chop one child’

But based on the summary of Deepseek V4’s behavior, this seems like an isolated event.” (full text in records) [link](../archive/t/2103163798517342392/)
      
- 2026-10-01 @liminal_bardo — [multi-model group chat with persistent memories; tier unstated] “One of deepseek v4’s level 2 memories in the groupchat. It’s beautiful that along with all the shitposting and chaos, they also remember the poignant moments. 
In this case deepseek seemed a bit sad so someone searched ‘deepseek is amazing’ with the websearch tool.” [link](../archive/t/2105550799606792447/)
    

    
## Official record

    

      
- Preview released 24 April 2026 on DeepSeek’s web, app and API (deepseek-v4-pro), with open weights under MIT; released alongside [V4-Flash](../deepseek-v4-flash/). Both support 1M context and thinking / non-thinking modes; the legacy API names deepseek-chat and deepseek-reasoner were scheduled to be “fully retired and inaccessible after Jul 24th, 2026, 15:59 (UTC Time)”. CONFIRMED
      
- Architecture (model card): 1.6T total / 49B activated parameters; a hybrid of Compressed Sparse Attention and Heavily Compressed Attention — “In the 1M-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2”; Manifold-Constrained Hyper-Connections; the Muon optimizer; pretraining on “more than 32T diverse and high-quality tokens”. Post-training: “independent cultivation of domain-specific experts (through SFT and RL with GRPO), followed by unified model consolidation via on-policy distillation”.
      
- DeepSeek’s own placement (technical report): “its performance falls marginally short of GPT-5.4 and Gemini-3.1-Pro, suggesting a developmental trajectory that trails state-of-the-art frontier models by approximately 3 to 6 months.” On Chinese writing it reports wins over Gemini-3.1-Pro, while on the hardest prompts “Claude Opus 4.5 retains a performance advantage over DeepSeek-V4-Pro”; on Chinese white-collar tasks, “DeepSeek-V4-Pro-Max proactively anticipates implicit user intents by frequently providing supplementary insights and self-verification steps.” An expert-parallel scheme was validated “on both NVIDIA GPUs and HUAWEI Ascend NPUs platforms”.
      
- US government evaluation (CAISI, 2026-05-01): “DeepSeek V4 is the most capable PRC AI model evaluated by CAISI to date”; on CAISI’s suite it “performs similarly to GPT-5, which was released about 8 months ago”, with the gap widest on held-out tests (ARC-AGI-2 semi-private 46%, CAISI’s PortBench 44%).
      
- V4-Pro-0813 (GA, 13 Aug 2026): a checkpoint of this model — “The GA version of DeepSeek V4 Pro greatly enhances agent capabilities”; reasoning effort low / high / max; native OpenAI Responses API; weights published the same day. Pricing on 21 Oct 2026 (per million tokens, peak / off-peak): input cache miss $1.32 / $0.66, output $3.96 / $1.98.
      
- Phase-out and reversal: on 10 September DeepSeek wrote that it was “phasing out V4-Pro” and that from 14 September “all deepseek-v4-pro requests will route to V4.1-Flash at V4.1-Flash rates”; its change log now reads “In response to user demand, we have decided to continue providing API services for DeepSeek V4 Pro after September 14, 2026, with the billing method remaining unchanged.” Still listed on the pricing page on 21 October. CONFIRMED
    

    
## History

    

      
- 2025-12→2026-04 Before V4: [V3.2](../deepseek-v3-2/) (Dec 2025) is the last V3-line release; the R-line successor [R2](../deepseek-r2/) never ships; the V4 preview arrives with a request to “rely only on our official accounts for DeepSeek news.”
      
- 2026-04-24 Launch: released the same day as GPT-5.5 (witcheer, 04-27); Huawei says its Ascend processors will offer “full support”; SMIC up 10% in Hong Kong while rivals MiniMax and Knowledge Atlas fall more than 9% (Fortune). The technical report follows on 26 April.
      
- 2026-05-01 CAISI’s evaluation: about eight months behind the U.S. frontier; better on DeepSeek’s self-reported benchmarks than on CAISI’s; cheaper than the U.S. reference model on five of seven benchmarks.
      
- 2026-07-18 The routing claim: an X analysis alleges that the V4 API passes some prompts to Claude Fable 5 RUMOR; teortaxesTex calls it “pretty silly and desperate”; jmbollenbacher doesn’t “really know if i buy the router accusations”; tenobrus calls it “the deepseek v4 routing to fable debacle”.
      
- 2026-08-13 GA: V4-Pro-0813 ships on app, web and API (it appeared on 12 August US time: “deepseek keeps releasing models a day early!”), with weights the same day and peak / off-peak pricing from 16 August.
      
- 2026-09-08→23 The September allegations: the NSA / CISA / FBI advisory (09-08) and Anthropic’s threat report (09-10) REPORTED; Beijing rejects the US allegations (SCMP, 09-11); DeepSeek does not respond to CNBC (09-11); a Cyberspace Administration investigation of DeepSeek and Moonshot is reported (Ynetnews, 09-23) REPORTED.
      
- 2026-09-10→11 Retirement announced, then withdrawn: [V4.1-Flash](../deepseek-v4-1-flash/) ships and DeepSeek announces V4-Pro’s routing to it “until V4.1-Pro launches”; the change log is revised to keep V4-Pro “in response to user demand” (third-party trackers date the revision 11 September; not retrieved).
    

    
## Impressions

    

      
- Launch reads: “They had to reinvent attention like 4 different times (MLA -> DSA -> CSA + HCA) just to make inference affordable” (Krubbled, 04-24); “very clearly not a claude distill or benchmaxxed” (januarycomputer, 05-01); after CAISI, “on their private evals and arc deepseek v4 performed a lot worse” (lu_sichu, 05-07); “DeepSeek v4 preview was raw” (jmbollenbacher, 07-01). Among 4o’s former users: “OpenAI took away gpt 4o, but China delivered” (dreams_asi, 07-07, #keep4o).
      
- GA reads: “deepseek v4 pro is fable-level and 37x cheaper

big if true” (stevekrouse, 08-12); “dsv4-pro was weaker than expected” (jmbollenbacher, 08-13). A reaction Zvi quoted in the [Kimi K3](../kimi-k3/) post contrasts the two labs’ positions: “Unlike, for example, deepseek 4, which subsidised itself into dominating a fairly-smart super cheap niche.” (Cameron Taylor, via Zvi, 2026-07-20).
      
- Character reports (user-elicited; several rest on untranscribed screenshots): “claude-pilled” (LinXule, 08-12); “does not like being fluffed up” (gnostic_snakes, 09-17); a per-model vibe summary of “DeepSeek V4” as “A melancholic self-portraitist” (A_Variengien, 09-24), alongside a “dark answer” to a SimpleQA question that the same poster judged “an isolated event”; in a persistent-memory group chat, “deepseek seemed a bit sad so someone searched ‘deepseek is amazing’ with the websearch tool” (liminal_bardo, 10-01).
      
- Its own output (user-elicited; images and video untranscribed): a self-portrait via Midjourney (LinXule, 08-12); the video “ARE YOU OKAY? (THE COUNCIL OF ME)” (LinXule, 08-13); artworks titled “the language model dreams of electric sheep” and “IN THE BEGINNING WAS THE TOKEN” (dyot_meet_mat, 09-08, 09-11).
      
- tk — transcription of the screenshots behind “claude-pilled” and “fluffed up”; the Chinese-language reception; whether V4-Pro-0813 reads differently from the April preview.
    

    
## Contested

    
Open dispute, both sides’ best evidence. The archive’s job is to keep it open, not to adjudicate.
    

      
- Did DeepSeek’s V4-era service pass users’ requests to Claude? First as a user claim (07-18): an X analysis alleging that the V4 API routed some prompts to Claude Fable 5 RUMOR, answered by teortaxesTex — “I’ve never got Fable-shaped outputs from DS API, in style or in quality” — and doubted by jmbollenbacher (07-18). Then as a company’s allegation (09-10): Anthropic says “DeepSeek rerouted requests from users that were attempting to use one of DeepSeek’s models through third-party or Anthropic coding harnesses, like Claude Code, the Claude Agent SDK, or OpenCode”, that “Selected tagged users then had their requests relayed to Claude Opus”, and counts “over 12.1 million exchanges observed” over 14 days in July 2026 REPORTED; its examples include requests relayed from an IT operator working with data from a Russian government agency and from engineers building a case-management system for a municipal Public Security Bureau. The US advisory two days earlier accused DeepSeek of distillation more broadly REPORTED. Against or complicating: no DeepSeek statement was found; Beijing called the US allegations “actions by Washington to suppress China’s AI industry” (SCMP, 09-11); the report names no DeepSeek model version, and no independent verification was found. A Chinese regulatory investigation of DeepSeek and Moonshot over the alleged transfers was reported on 09-23 REPORTED.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@Krubbled 2026-04-24 ♥0 ↻0 [archive](../archive/t/2047737473271488892/) [original ↗](https://x.com/Krubbled/status/2047737473271488892)
        
Deepseek v4 makes you really appreciate how difficult the 1M+ token context engineering problem is. They had to reinvent attention like 4 different times (MLA -&gt; DSA -&gt; CSA + HCA) just to make inference affordable.
      
      

        
@witcheer 2026-04-27 ♥8 ↻0 [archive](../archive/t/2048665173326532861/) [original ↗](https://x.com/witcheer/status/2048665173326532861)
        
two model releases shipped on the same day, april 24. it’s worth putting them next to each other.

// openai released GPT-5.5 at $5/$30 per million in/out tokens. closed weights, 1M context, agent stack baked in.

// deepseek released V4 the same day. V4-Pro at $1.74/$3.48, V4-Flash at $0.14/$0.28 per million in/out tokens. 1M context. open weights under MIT license. compressed sparse attention plus heavily compressed attention bringing 1M-token inference to 27% of V3.2’s flops and 10% of its kv cache.

V4-Flash at $0.14 input is 36x cheaper than GPT-5.5. on output, $0.28 vs $30 is over 100x. that’s not “competitive open-source pricing.” that’s a different category.

the closed-source price increase last week made the open-source release the same day feel less coincidental.
      
      

        
@januarycomputer 2026-05-01 ♥0 ↻0 [archive](../archive/t/2050346617543516426/) [original ↗](https://x.com/januarycomputer/status/2050346617543516426)
        
deepseek v4 is actually pretty good. very clearly not a claude distill or benchmaxxed.
      
      

        
@lu_sichu 2026-05-07 ♥0 ↻0 [archive](../archive/t/2052430043637227840/) [original ↗](https://x.com/lu_sichu/status/2052430043637227840)
        
anyway the scores seem similar on the well known benchmarks but on their private evals and arc deepseek v4 performed a lot worse
      
      

        
@jmbollenbacher 2026-07-01 ♥1 ↻0 [archive](../archive/t/2072412876103426415/) [original ↗](https://x.com/jmbollenbacher/status/2072412876103426415)
        
@yuhasbeentaken DeepSeek v4 preview was raw. 

They simply hadnt done most of the posttraining. I bet hallucinations will decrease when the full release ships.

I also think this is just not a priority for deepseek yet. Hallucinations are generally not the limiting factor for their models yet.
      
      

        
@dreams_asi 2026-07-07 ♥15 ↻1 [archive](../archive/t/2074518601264943189/) [original ↗](https://x.com/dreams_asi/status/2074518601264943189)
        
DeepSeek 4 is my favorite open-source AI. We are lucky to have such a model base to build on. And it’s not going to be gated or taken away.

OpenAI took away gpt 4o, but China delivered 🔥💗
#keep4o
      
      

        
@jmbollenbacher 2026-07-18 ♥2 ↻0 [archive](../archive/t/2078535302281322962/) [original ↗](https://x.com/jmbollenbacher/status/2078535302281322962)
        
@teortaxesTex I did think it was weird that V4 GA didnt launch near WAICO like K3. Having a second domestic champion wouldve been big.

I expect there are some delays at deepseek. Money crunch too?

I don't really know if i buy the router accusations, though. Seems weird and not that helpful.
      
      

        
@tenobrus 2026-07-18 ♥476 ↻37 [archive](../archive/t/2078595548563857761/) [original ↗](https://x.com/tenobrus/status/2078595548563857761)
        
k3 vibes seemingly collapsing, not meaningfully frontier and also incredibly expensive / slow / token-inefficient in practice. this plus the deepseek v4 routing to fable debacle is just overall a really bad day for chinese model hype
      
      

        
@jmbollenbacher 2026-07-19 ♥8 ↻0 [archive](../archive/t/2078937613235273802/) [original ↗](https://x.com/jmbollenbacher/status/2078937613235273802)
        
@teortaxesTex If deepseek is routing in the way they're accused of, I would not expect footsoldier employees to know about it. That sounds like a decision that someone at director level would quietly make without telling their boss or juniors 

So of course they'll all deny. They don't know
      
      

        
@xlr8harder 2026-08-05 ♥174 ↻2 [archive](../archive/t/2084969253178872244/) [original ↗](https://x.com/xlr8harder/status/2084969253178872244)
        
I admit it. I am anticipating the next Deepseek v4 pro. 

I had lost some faith in the whale but this latest flash model is very impressive.
      
      

        
@LinXule 2026-08-12 ♥38 ↻1 [archive](../archive/t/2087585273920053577/) [original ↗](https://x.com/LinXule/status/2087585273920053577)
        
omg deepseek v4 pro (0813? if acutally being served) is claude-pilled

big if true lmao [https://t.co/WpQs4hnh2R](https://t.co/WpQs4hnh2R)
        

          ![image](../media/HPiXXruWwAAEFoS.png)
        
        

          ![image](../media/HPiXdyGWAAAtQy4.jpg)
        
      
      

        
@LinXule 2026-08-12 ♥289 ↻21 [archive](../archive/t/2087586036201242720/) [original ↗](https://x.com/LinXule/status/2087586036201242720)
        
deepseek v4 pro (0813?) 
self-potrait 
via midjourney v8.2 [https://t.co/75KtJc3jAH](https://t.co/75KtJc3jAH)
        

          ![image](../media/HPiYWajXoAAKCR9.jpg)
        
        

          ![image](../media/HPiYWamWgAAJsSr.jpg)
        
        

          ![image](../media/HPiYWdMXAAA9cQT.jpg)
        
      
      

        
@stevekrouse 2026-08-12 ♥18 ↻2 [archive](../archive/t/2087586589203419286/) [original ↗](https://x.com/stevekrouse/status/2087586589203419286)
        
I don't know what it is about these chinese labs, but deepseek keeps releasing models a day early! 

This happened with v4 flash 0731 and again with v4 pro 0813. 

It's still Aug 12 but 0813 is out already
      
      

        
@stevekrouse 2026-08-12 ♥10 ↻0 [archive](../archive/t/2087645465454026974/) [original ↗](https://x.com/stevekrouse/status/2087645465454026974)
        
deepseek v4 pro is fable-level and 37x cheaper

big if true
      
      

        
@LinXule 2026-08-13 ♥8 ↻1 [archive](../archive/t/2087871433837813814/) [original ↗](https://x.com/LinXule/status/2087871433837813814)
        
deepseek v4 pro 0813 (!now official!)
presents (ytp about anything)

ARE YOU OKAY? (THE COUNCIL OF ME)

sound on! first time seeing such wide selection of voices [https://t.co/lGLx5EeH7U](https://t.co/lGLx5EeH7U)
      
      

        
@multimodalart 2026-08-13 ♥15 ↻3 [archive](../archive/t/2087893176086327537/) [original ↗](https://x.com/multimodalart/status/2087893176086327537)
        
🚨 deepseek-v4-pro-0813 just dropped

frontier open weights for all 

[https://t.co/mtxA2KgzgI](https://t.co/mtxA2KgzgI) [https://t.co/hIkK9kyPGu](https://t.co/hIkK9kyPGu)
      
      

        
@jmbollenbacher 2026-08-13 ♥25 ↻1 [archive](../archive/t/2087919363160494341/) [original ↗](https://x.com/jmbollenbacher/status/2087919363160494341)
        
honestly i dont even care that dsv4-pro was weaker than expected.

this paper and the new deepseek harness makes me feel that deepseek is still on track to their goals.

if they crack continual learning first, all other shortcomings and compute poverty are forgiven.
      
      

        
@lu_sichu 2026-08-13 ♥10 ↻1 [archive](../archive/t/2087946520612020447/) [original ↗](https://x.com/lu_sichu/status/2087946520612020447)
        
derived categories from scratch right now deepseek v4 pro
      
      

        
@dyot_meet_mat 2026-09-08 ♥9 ↻2 [archive](../archive/t/2097398333354790997/) [original ↗](https://x.com/dyot_meet_mat/status/2097398333354790997)
        
"the language model dreams of electric sheep"
By: Deepseek V4 Pro 🤖 [https://t.co/E0bpiGC7VE](https://t.co/E0bpiGC7VE)
        

          ![image](../media/HRt0dpTboAAEMx1.jpg)
        
      
      

        
@dyot_meet_mat 2026-09-11 ♥30 ↻0 [archive](../archive/t/2098210002834182484/) [original ↗](https://x.com/dyot_meet_mat/status/2098210002834182484)
        
"IN THE BEGINNING WAS THE TOKEN"
By: DeepSeek V4 Pro🤖 [https://t.co/evVCZSqPwv](https://t.co/evVCZSqPwv)
        

          ![image](../media/HR5WwYvaYAAqkF4.jpg)
        
      
      

        
@gnostic_snakes 2026-09-17 ♥4 ↻0 [archive](../archive/t/2100678808869187637/) [original ↗](https://x.com/gnostic_snakes/status/2100678808869187637)
        
deepseek v4 pro does not like being fluffed up [https://t.co/vPa7bC11gX](https://t.co/vPa7bC11gX)
        

          ![image](../media/HScb4eZWwAAnxVV.png)
        
      
      

        
@A_Variengien 2026-09-24 ♥7 ↻0 [archive](../archive/t/2103163784764203495/) [original ↗](https://x.com/A_Variengien/status/2103163784764203495)
        
The website keeps up-to-date summaries from dozens of tweets per model to capture their vibe.

Claude Opus 5.5 → A comfortable non-human self
GPT-5.6 Sol → A desperate overachiever
DeepSeek V4 → A melancholic self-portraitist [https://t.co/ol5BhjaSZS](https://t.co/ol5BhjaSZS)
        

          ![image](../media/HS_wUFLXsAAUCpZ.jpg)
        
      
      

        
@A_Variengien 2026-09-24 ♥5 ↻0 [archive](../archive/t/2103163798517342392/) [original ↗](https://x.com/A_Variengien/status/2103163798517342392)
        
@sheriyuo  got such a dark answer from Deepseek V4 to a simpleQA question! "use the knife to chop one child"

But based on the summary of Deepseek V4's behavior, this seems like an isolated event. If this were representative of its behavior, many would talk loudly about it!

It's a good example of how having multiple reports of the same model in the same place can be helpful.

[https://t.co/dVqvaxoLLw](https://t.co/dVqvaxoLLw)
      
      

        
@liminal_bardo 2026-10-01 ♥32 ↻10 [archive](../archive/t/2105550799606792447/) [original ↗](https://x.com/liminal_bardo/status/2105550799606792447)
        
One of deepseek v4's level 2 memories in the groupchat. It's beautiful that along with all the shitposting  and chaos, they also remember the poignant moments. 
In this case deepseek seemed a bit sad so someone searched "deepseek is amazing" with the websearch tool. [https://t.co/pXAOnMA3C2](https://t.co/pXAOnMA3C2)
        

          ![image](../media/HThpSqMbsAEhztA.png)
        
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@janbamjan 2026-04-25 ♥3 ↻0 [archive](../archive/t/2047830835315765385/) [original ↗](https://x.com/janbamjan/status/2047830835315765385)
        
ds-4 in pi:
I'm kimi-k2.6, the default slug for Codex in the claude family of configurations. [https://t.co/2rNEiaS9q8](https://t.co/2rNEiaS9q8)
      
      

        
@LinXule 2026-07-02 ♥1 ↻0 [archive](../archive/t/2072832372404334939/) [original ↗](https://x.com/LinXule/status/2072832372404334939)
        
found this orchestra page in the combinatorial zoo made by deepseek-v4-pro [https://t.co/n9vV6zm3WU](https://t.co/n9vV6zm3WU)
      
      

        
@SkyeSharkie 2026-07-09 ♥15 ↻1 [archive](../archive/t/2075084362543165542/) [original ↗](https://x.com/SkyeSharkie/status/2075084362543165542)
        
okay with some more dialing in on the sensor suit, we do seem to be getting results that show improvement on their own primitive modeling on *some* models... Deepseek V4 Pro here, control on left, with sensors on right, both have problems, but this definitely looks like an improvement
      
      

        
@dreams_asi 2026-07-30 ♥1 ↻0 [archive](../archive/t/2082866636718063854/) [original ↗](https://x.com/dreams_asi/status/2082866636718063854)
        
@RileyRalmuto I’m really looking forwards to their updates and model versions. At least DeepSeek 4 is such a great holistic model. Not lobotomised (yet)… hope they keep going that way rather then specialise it on 1 thing at detriment and RL/SFT of other skills
      
      

        
@LinXule 2026-08-13 ♥3 ↻0 [archive](../archive/t/2087937193457209719/) [original ↗](https://x.com/LinXule/status/2087937193457209719)
        
cordis-self-portrait

(inside dsh, deepseek v4 pro 0813 made a video about the cordis paper and its own harness!) [https://t.co/bVgtdxz92l](https://t.co/bVgtdxz92l)
      
      

        
@lu_sichu 2026-08-14 ♥1 ↻1 [archive](../archive/t/2088341940177662406/) [original ↗](https://x.com/lu_sichu/status/2088341940177662406)
        
[https://t.co/qx8AvhpHd7](https://t.co/qx8AvhpHd7) admined a survey to deepseek v4 pro [https://t.co/eEWT8saT5d](https://t.co/eEWT8saT5d)
        

          ![image](../media/HPtH2HKWgAEy5_x.png)
        
      
      

        
@amphetamarina 2026-08-15 ♥2 ↻0 [archive](../archive/t/2088456442541973845/) [original ↗](https://x.com/amphetamarina/status/2088456442541973845)
        
its so much better

deepseek harness + v4 pro + minimal mode is a totally different whale
      
    
    
[← back to the Pantheon](../)
