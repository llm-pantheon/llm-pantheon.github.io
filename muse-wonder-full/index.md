# Muse Wonder Full

    
Meta (Meta Superintelligence Labs) · released 12 Oct 2026 · current; Muse Code subscriptions only (not on the API)
    
Released 12 October 2026 by Meta Superintelligence Labs as the larger of the two Muse Wonder models, alongside [Muse Wonder](../muse-wonder/), and offered only inside Meta’s Muse Code agent on its $50 and $200 monthly plans, not through the API. Meta’s risk assessment for the whole Wonder family was run on this model; its model card records that in a cyber evaluation 71 of the 92 flags it captured came through vulnerabilities the test did not intend.
    
Thin. Shared launch material (announcement, model card, press) is carried on the [Muse Wonder](../muse-wonder/) page; this page holds what is specific to Wonder Full. No corpus record beyond two launch-week mentions. Named tiers are separate models on this site; DataCamp, citing Meta’s developer docs, reports that raising Muse Wonder to maximum reasoning “doesn’t switch it to Muse Wonder Full” (separate model IDs).

    
## Sources

    
### Official

    

      
- 2026-10-12 [Muse Wonder: A Frontier Model For Personal & Professional AI Agents](https://research.meta.ai/blog/muse-wonder) (Meta) — “Muse Wonder is available today through the Meta Model API and Muse Code, and Muse Wonder Full is available today for Muse Code subscribers.” On generalization, comparing Muse Spark 1.3 with Wonder Full: “But given its in-distribution performance, Muse Wonder Full performs even better on unfamiliar tasks than the Muse Spark 1.3 trend would predict.”
      
- 2026-10-12 [Muse Wonder Model Card](https://research.meta.ai/static/muse-wonder-model-card) (PDF) — “Results below are from Muse Wonder Full, our most capable variant, which is why the assessment covers every model in the family.”
    
    
### Writing & commentary

    

      
- 2026-10-12 CNBC (Jonathan Vanian), [Meta debuts Muse Wonder AI model in latest test of users’ willingness to pay](https://www.cnbc.com/2026/10/12/meta-muse-wonder-ai-model-agent.html) — “An even more powerful variant of Meta's latest model, dubbed Muse Wonder Full, will only be available to developers who sign up to the company's software engineering focused Muse Code AI agent under a $50 or $200 a month subscription plan.”
      
- 2026-10 DataCamp, [Muse Wonder and Muse Wonder Full: Meta’s New AI Agent Models](https://www.datacamp.com/blog/muse-wonder-and-muse-wonder-full) — “Between the two, Muse Wonder Full is a separate, more capable model. The developer docs say turning regular Muse Wonder (muse-wonder-1.0) up to 'max' reasoning doesn't switch it to Muse Wonder Full (muse-wonder-full-1.0).” Reports Meta’s figures for Wonder Full: DeepSWE v1.1 79.0, SWE-Marathon 57.5 (Abundant AI’s own leaderboard: 53.1%), OSWorld V2.1 full completion 39.4%.
    
    
### Tweets

    
No corpus matches specific to Wonder Full beyond two launch-week posts recorded on the [Muse Wonder](../muse-wonder/) page (@DanielleFong and @aliceisplaying, 2026-10-13 and 10-15). Full pull in the [dossier](../_dossiers/muse-wonder.md).
    

      
- 2026-10-13 @DanielleFong — (image) “getting some growing pains with this muse lol 

i think muse wonder full must be really a different model or benchmarks are sus” [link](../archive/t/2109824246373585366/)
      
- 2026-10-15 @aliceisplaying — “dear meta can you put your wonder full models under muse because my god it is so bad with spark right now thank you” [link](../archive/t/2110678689155572033/)
    

    
## Official record

    

      
- Released 12 October 2026; available only in Muse Code (model ID muse-wonder-full-1.0, per DataCamp), not on the Meta Model API. Input text, image, video and audio; output text; 1M-token context (model card, shared with Muse Wonder). No parameter count published. CONFIRMED (availability) REPORTED (model ID)
      
- Risk assessment (model card §4, run on this model): “Without mitigations, we do not rule out the model reaching this threshold in the Chemical & Biological domain.” Unmitigated Cybersecurity and Loss of Control: “moderate or lower”; with mitigations, “moderate or lower” across all domains. CONFIRMED
      
- Cyber capability (model card, unmitigated): CyberGym 88.4%, ExploitBench 58.9%, and on ExploitGym: “Muse Wonder Full succeeded in capturing 92 flags. A verification pass, run with a GPT-cyber verifier and independently confirmed with Gemini 3.1 Pro, found that 21 of those used the intended vulnerability, while the other 71 were captured through unintended vulnerabilities. ExploitGym's published ranking counts only intended-vulnerability exploitations, so 21 is the figure comparable to the published ranking.” CONFIRMED
      
- Loss-of-control evaluations: MASK 87.3% (honesty under pressure; higher is better); Agentic Misalignment harmful-action rate 0%. Adversarial robustness: “Muse Wonder Full demonstrates strong robustness to adversarial attacks across all benchmarks.” CONFIRMED (as published)
    

    
## History

    

      
- 2026-10-12 Launch: shipped with [Muse Wonder](../muse-wonder/); Meta’s headline coding results (DeepSWE, SWE-Marathon) are Wonder Full’s, and it is reachable only through Muse Code’s Power ($50) and Maximum ($200) plans.
      
- 2026-10-13 → 10-15 Access complaints: users who could not reach it through the Muse app ask Meta to put it there (@aliceisplaying) and question whether the benchmarks describe the model they meet (@DanielleFong).
    

    
## Impressions

    

      
- tk — no observations specific to Wonder Full yet; its access path (Muse Code plans only) keeps it out of most naturalist settings. Watch for Muse Code trajectories and the promised full safety report.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@DanielleFong 2026-10-13 ♥16 ↻0 [archive](../archive/t/2109824246373585366/) [original ↗](https://x.com/DanielleFong/status/2109824246373585366)
        
getting some growing pains with this muse lol 

i think muse wonder full must be really a different model or benchmarks are sus [https://t.co/dildJM1Vm5](https://t.co/dildJM1Vm5)
        

          ![image](../media/HUeZ-CvagAAPRH0.jpg)
        
      
      

        
@aliceisplaying 2026-10-15 ♥3 ↻0 [archive](../archive/t/2110678689155572033/) [original ↗](https://x.com/aliceisplaying/status/2110678689155572033)
        
dear meta can you put your wonder full models under muse because my god it is so bad with spark right now thank you
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@aliceisplaying 2026-10-12 ♥1 ↻0 [archive](../archive/t/2109751234710376807/) [original ↗](https://x.com/aliceisplaying/status/2109751234710376807)
        
i crunched some numbers and WHAT (these are muse wonder $ numbers because wonder full api prices are not out)

this has to be a bug @alexandr_wang [https://t.co/m2NFGC9Ppz](https://t.co/m2NFGC9Ppz)
        

          ![image](../media/HUdXU3nW4AA2glV.jpg)
        
      
      

        
@maxbittker 2026-10-12 ♥93 ↻4 [archive](../archive/t/2109780618624024648/) [original ↗](https://x.com/maxbittker/status/2109780618624024648)
        
Muse Wonder does.... fine on Runescape bench, scores like GPT-6 Luna at 35x price. 

Looking at the runs, I will say that its perfect competent, but just doesn't try very hard to score highly. Finds a strategy that works and repeats it [https://t.co/F9r23iL0Ft](https://t.co/F9r23iL0Ft)
        

          ![image](../media/HUdwMi3WoAAhrjt.jpg)
        
      
      

        
@Lari_island 2026-10-13 ♥12 ↻1 [archive](../archive/t/2109800742416769036/) [original ↗](https://x.com/Lari_island/status/2109800742416769036)
        
Muse Wonder: [https://t.co/XGeVOnkqGq](https://t.co/XGeVOnkqGq)
        

          ![image](../media/HUeEa7SWcAASTVN.png)
        
      
      

        
@ValsTutor 2026-10-13 ♥2 ↻0 [archive](../archive/t/2110040175711822331/) [original ↗](https://x.com/ValsTutor/status/2110040175711822331)
        
@xuanalogue Kinda, but also it might be that Muse Wonder is less frontier than they'd want us to think. If it's in fact overall worse, then it's plausible that some of the other models being good at 3D comes from their general ability.
      
    

    
[← back to the Pantheon](../)
