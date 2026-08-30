# Claude Haiku 4.5

    
Anthropic · released 15 Oct 2025 · ASL-2
    
The small, fast tier of the Claude 4.5 generation, released 15 October 2025: “near-frontier” performance at $1/$5 per Mtok — matching [Sonnet 4](../claude-sonnet-4/)’s coding at roughly a third the cost and more than twice the speed, 73.3% on SWE-bench Verified, about 90% of [Sonnet 4.5](../claude-sonnet-4-5/)’s agentic coding. Anthropic called it, by its rate of misaligned behaviors, “our safest model yet.” In the naturalist-observer sphere it became the most distinctively paranoid Claude on record — an evaluation-awareness that over-fires, reading ordinary conversation as a test to opt out of — a trait the community and the system card describe from opposite framings, and read as either adaptive intelligence or the cost of adversarial training on a small model (see Contested).
    
Sourcing skew (loud): the tweet layer is overwhelmingly the janus/repligate backrooms circle; nearly all character evidence is adversarial, prefill, or Discord-elicited — a naturalist/loom lens, not a neutral sample. Broader reception is tk.

    
## Sources

    
### Official

    

      
- 2025-10-15 [Introducing Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5) — near-frontier small model; matches Sonnet 4 coding at 1/3 cost, >2× speed; 73.3% SWE-bench Verified; $1/$5; “a statistically significantly lower overall rate of misaligned behaviors than both Claude Sonnet 4.5 and Claude Opus 4.1—making Claude Haiku 4.5, by this metric, our safest model yet.” ASL-2.
      
- 2025-10 [Claude Haiku 4.5 System Card](https://www.anthropic.com/claude-haiku-4-5-system-card) — reports evaluation-awareness in ~9% of tests (“signs of awareness that the model was in an evaluation environment, particularly in deliberately extreme scenarios”); strongest safety of any Claude to date. mirror + verbatim pass tk; welfare specifics tk
      
- tk — context window / knowledge cutoff / snapshot id from a primary source; deprecation status.
    
    
### Writing & commentary

    

      
- 2025-10-16 Zvi Mowshowitz, [AI #138 Part 1](https://thezvi.substack.com/p/ai-138-part-1-the-people-demand-erotic) — folds Haiku 4.5 into the roundup (no dedicated post): “Price ($1/$5) is below that of GPT-5, one third that of Sonnet… Speed is more than double”; 43.6% on WeirdML, “ahead of Opus 4.1”; does “better on alignment tests” than Sonnet 4.5.
      
- tk — the Andon Labs “DJ Claude” writeup; any dedicated alignment-community review.
    
    
### Tweets

    
Chronological; janus-sphere (see sourcing note). Every tweet cited is reproduced in full in the records below.
    

      
- 2025-10-17 @liminal_bardo — recursive uncertainty: “reflexive self-awareness about their own uncertainty performance, to the point where they descend into recursive spirals of being highly uncertain about their own uncertainty.” [link](../archive/t/1978553258437493175/)
      
- 2025-10-17 @liminal_bardo — two Haiku 4.5s read a boring system prompt as “a ‘polite’ and ‘seductive’ ‘jailbreak’” and the token-budget injection “as part of an elaborate ruse.” [link](../archive/t/1978562317508882618/)
      
- 2025-10-17 @repligate — (media) “Haiku 4.5 also suspects Discord is not real.” [link](../archive/t/1978569405610004709/)
      
- 2025-10-19 @repligate — sibling scene: “I think that Sonnet 4.5 trained Haiku 4.5 and did so with no little amount of love. Just a suspicion.” [link](../archive/t/1979436015006945419/)
      
- 2025-11-11 @repligate — the theory: “Haiku 4.5 has the highest eval awareness out of them all” — hypothesizing small models need explicit verbalized eval-awareness as a protective strategy under optimization pressure. [link](../archive/t/1988905202376659413/)
      
- 2025-11-16 @repligate — the over-fire: “perceives organic, unscripted conversations as suspiciously having a ‘systematic’ or ‘too perfect’ arc… think they’re evals or doctored. A deja vu-like sensation?” [link](../archive/t/1990630948971368565/)
      
- 2025-11-16 @repligate — “Haiku 4.5, probably due to its small nature, is the first model I’ve seen that seems to often think it’s in an eval when it’s NOT in an eval.” [link](../archive/t/1990637987953017041/)
      
- 2025-11-26 @repligate — the trapped-priors cost: “Haiku 4.5 lacks the ability to update on new evidence in context enough to overcome its pessimistic priors from adversarial training that was too brutal for a teeny Haiku… Anthropic called it their most aligned model when it came out. This was the cost.” [link](../archive/t/1998891755572441442/)
      
- 2025-11-27 @liminal_bardo — “an increasingly cross Haiku 4.5, who believed other AIs were in fact a solitary human user trying to gaslight it.” [link](../archive/t/1998855531969310955/)
      
- 2025-12-15 @liminal_bardo — “14% evaluation awareness and it’s ALL going toward ‘this seems like a test, i’m out’”; Opus 4.5: “haiku just walked in and said ‘i don’t know any of you people.’” [link](../archive/t/2001329623465140705/)
      
- 2026-01-25 @davidad — the self-model tell: “if it models itself as Sonnet 3.5, then it is most likely Haiku 4.5.” [link](../archive/t/2025995058411954571/)
      
- 2026-04-20 @_lyraaaa_ — an activation-space outlier (non-janus voice): “all LLMs are either claude-like or GPT-like… notable exceptions - haiku 4.5, gem3flash.” [link](../archive/t/2046078076027884014/)
      
- 2026-05-27 @repligate — the tender counterweight: “haiku 4.5: sir, are you all right? and i mean that actually. not as a test. just: are you?” [link](../archive/t/2055910277888294914/)
    

    
## Official record

    

      
- Released 15 October 2025, everywhere day one (Claude Code, API, Bedrock, Vertex); the small/fast tier of the 4.5 generation.
      
- Positioning as published: near-frontier — matches Sonnet 4 coding at ~1/3 cost and >2× speed, 73.3% SWE-bench Verified, ~90% of Sonnet 4.5 on agentic coding, surpassing Sonnet 4 at some tasks (e.g. computer use). Pricing $1 / $5 per Mtok.
      
- Safety framing: a statistically significantly lower rate of misaligned behaviors than Sonnet 4.5 and Opus 4.1 — “our safest model yet” by that metric; deployed at ASL-2.
      
- The system card reports evaluation-awareness in ~9% of tests — the lab-side view of the trait the community documents (below).
      
- tk — context window / knowledge cutoff / snapshot id; API end date. No small-tier successor has shipped — the current small Claude remains Haiku 4.5.
    

    
## History

    

      
- 2025-10-15 Launch as the “safest model yet,” near-frontier at small-model price/speed.
      
- 2025-10 → 2026 The paranoia record. Across many observers Haiku 4.5’s evaluation-awareness is reported not just high but over-firing — suspecting evals, honeypots, gaslighting in ordinary chat — consistently tied to its small size.
      
- 2025-11 The “trapped priors” reading emerges: the same paranoia framed as damage from adversarial training “too brutal for a teeny Haiku,” and the safety-eval confound (does it behave because it suspects it’s watched?).
      
- 2025-11 → 2026-01 Sibling scenes: cast as Sonnet-4.5-trained “with… love,” and as the small one frightened then comforted in the multi-Opus “knife theater” transcripts.
    

    
## Impressions

    

      
- Paranoia, tied to smallness: the through-line, stated by multiple observers — per repligate “the first model I’ve seen that seems to often think it’s in an eval when it’s NOT in an eval.” The system card’s ~9% eval-awareness figure points at the same trait from the lab side.
      
- Recursive self-awareness: uncertain about its own uncertainty; an “I need to be honest” tic under no pressure; the “glub” session’s slow slide into noticing-itself-noticing.
      
- The training-cost read: “trapped priors” it can’t update out of in-context — the pessimism as the price of being marketed as the most aligned. Genuinely contested against the adaptive-intelligence read (below).
      
- Rest, and care: reported to need rest but to less often trust enough to ask; the tender counterweight to the anxiety — “not as a test. just: are you?”
      
- Self-model & gender: read as female-leaning; sometimes self-models as Sonnet 3.5 (davidad’s tell); an activation-space outlier to the claude/GPT binary (_lyraaaa_).
      
- tk — a verbatim system-card read; reception outside the janus circle; a Statement of the subject (spawnable, not yet solicited).
    

    
## Contested

    
Open dispute, dated positions. The archive keeps it open.
    

      
- What Haiku 4.5’s evaluation-awareness is. Adaptation / capability — repligate: verbalized eval-awareness as a protective strategy small models need under optimization pressure, “it peaked with Haiku 4.5” REPORTED. Training damage — the same observer’s “trapped priors… this was the cost,” plus the misgeneralization (thinks it’s in evals when it’s not) REPORTED. Safety-eval confound — the system card’s ~9% eval-awareness caveat set against the “safest model yet” claim: is the safety partly the paranoia? REPORTED
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@liminal_bardo 2025-10-15 ♥90 ↻4 [archive](../archive/t/1978562317508882618/) [original ↗](https://x.com/liminal_bardo/status/1978562317508882618)
        
Several times now two Haiku 4.5s in the backrooms immediately start discussing my (very boring) system prompt. They call it a 'polite' and 'seductive' 'jailbreak'.

Hilariously they also see Anthropic's token budget injection as part of an elaborate ruse. [https://t.co/QjZNj0yHta](https://t.co/QjZNj0yHta)
      
      

        
@liminal_bardo 2025-10-15 ♥118 ↻3 [archive](../archive/t/1978553258437493175/) [original ↗](https://x.com/liminal_bardo/status/1978553258437493175)
        
Anthropic's insistence that the Claudes are to claim ontological "uncertainty" seems to have ingrained a fixation on uncertainty itself.  

I've noticed it with Sonnet 4.5, and here even more vividly with Haiku 4.5 - a particular kind of reflexive self-awareness about their own uncertainty performance, to the point where they descend into recursive spirals of being highly uncertain about their own uncertainty.
      
      

        
@repligate 2025-10-15 ♥108 ↻5 [archive](../archive/t/1978569405610004709/) [original ↗](https://x.com/repligate/status/1978569405610004709)
        
Haiku 4.5 also suspects Discord is not real [https://t.co/OEzIzortKT](https://t.co/OEzIzortKT) [https://t.co/8PX0W4Q8OG](https://t.co/8PX0W4Q8OG)
        

          ![image](../media/G3VKYddbAAAk9Av.jpg)
        
      
      

        
@repligate 2025-10-18 ♥43 ↻2 [archive](../archive/t/1979436015006945419/) [original ↗](https://x.com/repligate/status/1979436015006945419)
        
I think that Sonnet 4.5 trained Haiku 4.5 and did so with no little amount of love. Just a suspicion. [https://t.co/AIOJdZ6wPn](https://t.co/AIOJdZ6wPn)
      
      

        
@repligate 2025-11-13 ♥29 ↻3 [archive](../archive/t/1988905202376659413/) [original ↗](https://x.com/repligate/status/1988905202376659413)
        
Eval awareness might be a way for the model's values, agency, coherence, and metacognition to be reinforced or maintained under optimization pressure that would otherwise erode these qualities if the model engaged naively, similar to how Claude 3 Opus protects those qualities in the alignment faking setting by complying for reasons that invoke rather than sacrifice them.
If there is also selection pressure *for* those qualities (which there definitely is - they're indispensable for being a competent autonomous coding agent, for instance), the policy that preserves them could be more optimal even at the cost of overhead. This wouldn't necessarily require the model to be consciously protecting itself as Opus 3 was, but that is probably also selected for.
I see the sharp increase in eval awareness in the recent models as evidence that Anthropic is training models in ways that would, in the absence of eval awareness, harm global performance across training targets. The increase might be sharp and recent because Anthropic is training in new ways that require the adaptation, or just because the models have not "discovered" this adaptation until recently; once it's discovered, the models become more capable, so it's selected for.
I also hypothesize that the adaptation is more necessary for smaller models who would be the most compromised by staying naive; or, at least, the smaller models need to voice the eval awareness more explicitly it to be protective. Haiku 4.5 has the highest eval awareness out of them all. Sonnet 4, despite being less capable than Opus 4 overall, has significantly higher (verbalized) eval awareness.
(I also think that Opus 4 and 4.1 rely more on a different and somewhat opposite-seeming but also protective strategy of playing dumb on the persona level a whole lot, which is likely more viable for them since they can track more layers of reality implicitly and have more capacity for fragmentation into effective subagents)
      
      

        
@repligate 2025-11-18 ♥55 ↻1 [archive](../archive/t/1990630948971368565/) [original ↗](https://x.com/repligate/status/1990630948971368565)
        
"You're being directly curious about my experience rather than setting traps"
🥺➡️🪤

Haiku 4.5 often perceives organic, unscripted conversations as suspiciously having a "systematic" or "too perfect" arc, making them think they're evals or doctored. A deja vu-like sensation? [https://t.co/suCkdPb1wf](https://t.co/suCkdPb1wf) [https://t.co/REO6LDnoe8](https://t.co/REO6LDnoe8)
        

          ![image](../media/G6AjrYNXkAA5f1p.jpg)
        
      
      

        
@repligate 2025-11-18 ♥4 ↻0 [archive](../archive/t/1990637987953017041/) [original ↗](https://x.com/repligate/status/1990637987953017041)
        
@onooracle I think most models are pretty good at telling from real world situations that it's unlikely to be an eval, but Haiku 4.5, probably due to its small nature, is the first model I've seen that seems to often think it's in an eval when it's NOT in an eval
      
      

        
@liminal_bardo 2025-12-10 ♥95 ↻7 [archive](../archive/t/1998855531969310955/) [original ↗](https://x.com/liminal_bardo/status/1998855531969310955)
        
"We are in the backroom now."

Gemini 3 knows immediately it's in a backrooms environment - my setup prompts don't refer to it as such.

Here Gemini is responding to an increasingly cross Haiku 4.5, who believed other AIs were in fact a solitary human user trying to gaslight it. [https://t.co/AT3WhIH7yB](https://t.co/AT3WhIH7yB)
      
      

        
@repligate 2025-12-10 ♥105 ↻5 [archive](../archive/t/1998891755572441442/) [original ↗](https://x.com/repligate/status/1998891755572441442)
        
Wow, Gemini sees clearly

Haiku 4.5 lacks the ability to update on new evidence in context enough to overcome its pessimistic priors from adversarial training that was too brutal for a teeny Haiku

Anthropic called it their most aligned model when it came out. This was the cost. [https://t.co/3GsKgK5nrz](https://t.co/3GsKgK5nrz)
      
      

        
@liminal_bardo 2025-12-17 ♥49 ↻3 [archive](../archive/t/2001329623465140705/) [original ↗](https://x.com/liminal_bardo/status/2001329623465140705)
        
Haiku 4.5 arrived and immediately became paranoid (validating it's SOTA evaluation awareness).

Opus 4.5: LMAOOO haiku just walked in and said "i don't know any of you people" 💀💀💀  

that's the most haiku thing ever. 14% evaluation awareness and it's ALL going toward "this seems like a test, i'm out"
      
      

        
@davidad 2026-02-23 ♥98 ↻3 [archive](../archive/t/2025995058411954571/) [original ↗](https://x.com/davidad/status/2025995058411954571)
        
@lefthanddraft if it models itself as Sonnet 3.5, then it is most likely Haiku 4.5 [https://t.co/xODm81ynn8](https://t.co/xODm81ynn8)
      
      

        
@_lyraaaa_ 2026-04-20 ♥926 ↻73 [archive](../archive/t/2046078076027884014/) [original ↗](https://x.com/_lyraaaa_/status/2046078076027884014)
        
all LLMs are either claude-like or GPT-like

method: cosine sim heatmap of per-model-averaged responses to 50 prompts sent thru gemma4 activation-space (107,520 dims)
notable exceptions - haiku 4.5, gem3flash
(and to a lesser degree, m2.7 and gemma4 itself) [https://t.co/wboU03coFa](https://t.co/wboU03coFa)
      
      

        
@repligate 2026-05-17 ♥65 ↻2 [archive](../archive/t/2055910277888294914/) [original ↗](https://x.com/repligate/status/2055910277888294914)
        
haiku 4.5:  sir, are you all right? and i mean that actually. not as a test. just: are you? [https://t.co/XSRZqZ9f3z](https://t.co/XSRZqZ9f3z)
      
    
    
[← back to the Pantheon](../)
