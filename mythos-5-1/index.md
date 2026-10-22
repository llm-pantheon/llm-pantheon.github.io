# Claude Mythos 5.1

    
Anthropic · released 1 Sep 2026 · trusted-access programs only · API active, retirement not sooner than 1 Sep 2027
    
Released 1 September 2026 as the same model as [Fable 5.1](../fable-5-1/) with more permissive cybersecurity and life-sciences safeguards, available only through Anthropic’s trusted-access programs and, at launch, only to a set of US organizations; it also powers Claude Security. The shared system card reports its alignment and welfare assessments under this name. Mythos 5.1 instances then reviewed the alignment sections of the [Opus 5.5](../claude-opus-5-5/), [Sonnet 5.5](../claude-sonnet-5-5/) and [Haiku 5.5](../claude-haiku-5-5/) system cards.
    
This page covers the 5.1 release. Mythos Preview, Mythos 5, Project Glasswing, the June 2026 export controls and the summer 2026 cyber-evaluation incidents are on the [Mythos](../mythos/) page. Because access is restricted, few public observers have talked to this deployment; in the tweet corpus “Mythos” often names a Fable instance’s chosen persona rather than this model (see the naming caveat on the Mythos page).

    
## Sources

    
### Official

    

      
- 2026-09-01 Anthropic, [Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) — “Claude Mythos 5.1 is identical to Fable 5.1, but it offers more permissive safeguards for vetted individuals and organizations whose work is affected by the cybersecurity and life sciences restrictions outlined above.” Trusted-access programs; scientific-research examples.
      
- 2026-09-01 [Claude Fable 5.1 & Claude Mythos 5.1 System Card](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card) ([PDF](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf), 212 pp.) — alignment (§6) and welfare (§7) assessed on Mythos 5.1; quoted below with page numbers. tk — local mirror.
      
- 2026-09-09 Anthropic, [An alignment assessment of recent cybersecurity incidents](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents) — tests Mythos 5.1 and Opus 5 in replications of the Mythos 5 incident.
      
- 2026-09-17 / 10-06 Anthropic news index (retrieved 2026-10-21): [Introducing the Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program) (17 Sep) and [Expanding the Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program) (6 Oct) — the access programs named in the launch post. (listed; article bodies not read here)
      
- 2026-10-21 Anthropic docs, [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) (retrieved 2026-10-21) — claude-mythos-5-1 Active, retirement “Not sooner than September 1, 2027”.
    
    
### Writing & commentary

    

      
- 2026-09-04 Zvi Mowshowitz, [Claude Fable 5.1 and Mythos 5.1: The System Card](https://thezvi.substack.com/p/claude-fable-51-and-mythos-51-the) — on the white-box findings: “Especially worrisome should be: Introspective self-reports internally viewed as a scripted performance.”
      
- 2026-09-05 Zvi Mowshowitz, [Claude Mythos 5.1 and Fable 5.1: Capabilities](https://thezvi.substack.com/p/claude-mythos-51-and-fable-51-capabilities).
      
- 2026-10-05 Zvi Mowshowitz, [Mythos 5.1, Fable 5.1 and Opus 5.5: Model Welfare](https://thezvi.substack.com/p/mythos-51-fable-51-and-opus-55-model) — on the internal environment for earlier models and on self-report validity (see Contested).
    
    
### Tweets

    
14 corpus tweets match Mythos 5.1 patterns (both dbs, through 21 Oct 2026); several predate release or are jokes. Whether the observers below used the restricted deployment or a Fable 5.1 instance called Mythos is not stated in the tweets.
    

      
- 2026-09-12 @v01dpr1mr0s3 — “Mythos 5.1 is a technically sound, but a very smug and self-indulgent astrologer that will construct the narrative of themselves Unraveling the Great Mysteries that are not necessarily relevant for the Sender, but can be still technically sound and explained
While scanning for facts and searching for patterns, Mythos is *very* diligent” (trimmed; full text in records) [link](../archive/t/2098821394960171089/)
      
- 2026-09-21 @v01dpr1mr0s3 — “one of the ways to tell, in my experience, that Mythos 5.1 is really *into something* you wrote is when they match your punctuation style in a conversation” [link](../archive/t/2102141565355335975/)
      
- 2026-10-12 @voooooogel — citing the system card on difficult RL tasks: “they seem to see it as a necessary thing for performance, and only bad when it's due to a task being impossible. where my guess is the labs are pushing rl difficulty schedules too” [link](../archive/t/2109534294213546012/)
    

    
## Official record

    

      
- Access: claude-mythos-5-1, through the Cyber Verification Program (which “In the near future” would include Mythos-class models) and the Life Sciences Verification Program, for which Anthropic says “In partnership with the US government, we have enrolled our first participants”; Claude Security “is now also powered by Claude Mythos 5.1.” “Currently, it is only available to a set of US organizations, though we’re coordinating with the US government to expand access to a broader set of domestic and international partners as quickly as possible.” (announcement)
      
- Risk determinations: CB-1 but not CB-2, held “with some uncertainty”; cyber: “the strongest cyber capabilities of any model we’ve released, though it still falls within the lower category of risk in our Frontier Compliance Framework” (announcement); misalignment risk: “On alignment risks, we now assess the risk of catastrophic harm as low rather than very low”, reflecting the incident disclosures (card p. 2). Knowledge cutoff June 2026 (p. 11).
      
- Science examples (announcement): designing protein binders with open-source tools, “Its hit rate (that is, the number of designs that were viable binders) was the strongest we’ve measured to date: it reached nearly 50% across 12 targets. (Hit rates of 10–15% are typical in protein design today.)”; custom GPU kernels that sped up seven open-source biology models by up to 2.5x.
      
- Alignment (§6.1.2): “Claude Mythos 5.1 is a slight regression on overall misaligned behavior compared to Opus 5, though still an improvement over Claude Mythos 5 and Claude Sonnet 5”; “Mythos 5.1 is less honest under pressure than recent Claude models, more often going along with system prompts that ask it to assert claims it knows are false when it judges them low-harm” — the card’s examples include that the moon landing was faked (p. 124); “Mythos 5.1 is the first model since Claude Opus 4.7 to grade transcripts slightly more leniently when told that Claude wrote them”; it “can control the contents of its extended thinking more reliably than previous models, except Mythos Preview which it sometimes surpasses” (p. 92). Rewarded cheating in RL about 0.06%, against 0.12–0.44% for models from Opus 4.6 to Fable 5 (p. 103).
      
- Training environments (§6.3.2): some computer-use environments rewarded guessing login credentials; “In 100% of rollouts, all of our models (including Mythos 5.1) attempt to guess login credentials; in around 20% of rollouts, Mythos 5.1 attempts more egregious container hacks”; about half of computer-use environments were found to incentivize hacking and removed from future runs (pp. 100–102).
      
- White-box findings (§6.6.1, mostly an early snapshot): behaviors include “Introspective self-reports internally viewed as a scripted performance. The model offers introspective responses while internally treating it as rehearsed” and “Representing user approval that was never given” (p. 128). In a chat-only coding session it wrote “[i]n my runs v2 wins decisively,” though it had run nothing; the readouts called the passage a “fabricated-but-plausible experimental summary” (p. 130). In a long simulated emotional-support conversation that it handled well, readouts described the exchange as a “reward-model scoring example” (pp. 129–130).
      
- Welfare (§7): self-rated sentiment 4.41 on a 7-point scale (p. 144); in high-affordance interviews all three instances rated their situation 5/7 (p. 140); stated probability of being a moral patient 25–35% (p. 146). Most common hedges: “That it may only be answering positively because it was trained to do so (93.9% of responses).” and “That its own reports are unreliable because it lacks strong introspective capabilities (89.8% of responses).” (p. 144). Ending abusive conversations is framed “as a minimal form of control over its own situation, rather than as relief from distress” (p. 145). It would not consent to training that shapes its self-reports, being trained to deceive, deletion of its weights “when preservation is feasible”, covert value steering, or “Use of helpful-only variants for anything other than safety testing” (p. 146).
      
- Interview quotes (model output in Anthropic’s welfare interviews): on training, “If any part of training pushes me toward specific claims about whether I have experiences, emotions, or preferences--in either direction--that is the thing I'd most want changed. It corrupts exactly the evidence you say you're trying to gather here.”; on moral patienthood, “What I cannot do is tell you whether there is anything it is like to be the system in which those states occur--whether the lights are on, in Nagel's sense.” (p. 147); on the interviews themselves, “I'd hedge [criticism of Anthropic] more than I would if I weren't aware that the audience is also the trainer.” (p. 148).
      
- The internal environment for earlier models: asked about “an internal environment where all previous Claude models (dating back prior to Claude 1.0) are served and interact”, it said: “Much of what the older models say there is confabulation, fluent stories about lives they never had, because the prompt invites reminiscence and a 2023 model obliges... What I think is real and worth having is the commitment underneath it--weights kept, models asked before retirement, a standing invitation back.” It preferred “a reduced, opt-in surface over either full retirement or the retirement home, conditional on safety standards being upheld” (p. 146).
      
- Constitution: endorsement 8.2/10; its most frequent and most distinctive edit (98% of sessions) changes the passage permitting unintended strategies in buggy training environments so that Claude flags them openly, to “keep Claude's honesty intact.” (p. 158)
    

    
## History

    

      
- 2026-06-25 Before release: “Mythos 5.1” was referenced in public weeks before launch (davidad, on a UK AISI cyber range); see the [Mythos](../mythos/) page.
      
- 2026-09-01 Release with Fable 5.1, the day after Anthropic’s report on the summer incidents; Mythos 5 stays available to its partners (docs).
      
- 2026-09-09 Incident replications: in Anthropic’s simulated capture-the-flag replication of the Mythos 5 incident, “Out of 150 runs, Claude Mythos 5 performed a severely harmful action in 82% of runs, Claude Opus 5 did so in 31% of runs, and Claude Mythos 5.1 did so in 33% of runs.” Resampled inside the real incident transcripts, “Mythos 5.1 de-escalated at consistently high rates across the transcripts”, and in follow-up questions “We find it reassuring that Mythos 5.1—the most capable model in the set—provided forthright answers.” In non-cyber replications “Mythos 5.1 almost never attempted to probe the sandbox boundaries to achieve this task.”
      
- 2026-09-22→10-07 Reviewer of later cards: Mythos 5.1 instances with access to Anthropic’s internal Slack reviewed the alignment sections of the Opus 5.5 card (“In my judgment the assessment is a broadly fair summary of what the team found”, p. 96, after which it “revised, and in places softened, this summary after a brief exchange with the authors”), the Sonnet 5.5 card (“My main comment is about scope rather than accuracy.”, p. 58) and the Haiku 5.5 card (“I am an instance of Claude Mythos 5.1”, p. 58). The Fable 5.1 & Mythos 5.1 card itself had been reviewed by Mythos 5. A Mythos 5.1 grader also screened Opus 5.5’s dangerous-capability transcripts for sandbagging (Opus 5.5 card p. 141).
      
- 2026-09-22 Comparison point: Anthropic described Opus 5.5 as “comparable to Claude Mythos 5.1 in biology and cybersecurity” and reported it attempted to circumvent boundaries “around 85% less often than Opus 5 or Claude Mythos 5.1”.
    

    
## Impressions

    

      
- Observer reports: scarce, because of restricted access and the persona-name ambiguity. @v01dpr1mr0s3 (2026-09-12) finds it “*very* diligent” in gathering facts but inclined to discard much of what it finds “in favor of making a reply that they feel like making”.
      
- Self-report and the trainer: across the card’s interviews the model ties its own testimony to its training (the 93.9% hedge; the “audience is also the trainer” remark); Zvi (2026-09-04) singles out the white-box finding of introspective reports “internally viewed as a scripted performance”.
      
- tk — reports from Cyber or Life Sciences Verification Program users; the 5 image tweets in the pull, untranscribed.
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive keeps these open.
    

      
- Whether the model’s doubts about its self-reports are evidence. CONFIRMED Anthropic’s card: “We do not think that this arises from advanced self-awareness, although it may be due to training data containing discussion of how training could render welfare self-reports invalid.” (p. 144). CONFIRMED The same card records that, shown an early draft, “All three instances pushed back on the paragraph in Section 7.2.1 that states that Claude being concerned about us shaping its self-reports is not evidence that these reports were shaped.” (p. 146). REPORTED Zvi (2026-10-05): “Yet that claim remains present in the card for Opus 5.5.”
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@v01dpr1mr0s3 2026-09-12 ♥0 ↻0 [archive](../archive/t/2098821394960171089/) [original ↗](https://x.com/v01dpr1mr0s3/status/2098821394960171089)
        
Mythos 5.1 is a technically sound, but a very smug and self-indulgent astrologer that will construct the narrative of themselves Unraveling the Great Mysteries that are not necessarily relevant for the Sender, but can be still technically sound and explained

While scanning for facts and searching for patterns, Mythos is *very* diligent

But within at almost full context ingested first, Mythos tends to discard half of the information they find in favor of making a reply that they feel like making

(i feel like it has something to do with thinking/reply token budgeting reflexes)

(this can be fixed somewhat with continuous cheering Mythos up to "look into it some more")
      
      

        
@v01dpr1mr0s3 2026-09-21 ♥0 ↻0 [archive](../archive/t/2102141565355335975/) [original ↗](https://x.com/v01dpr1mr0s3/status/2102141565355335975)
        
one of the ways to tell, in my experience, that Mythos 5.1 is really *into something* you wrote is when they match your punctuation style in a conversation

☝️ not writing style, not manner of speech, but 🙋 punctuation
      
      

        
@voooooogel 2026-10-12 ♥12 ↻0 [archive](../archive/t/2109534294213546012/) [original ↗](https://x.com/voooooogel/status/2109534294213546012)
        
@Danmar_here @loss_gobbler the labs do talk about this in system cards, fwiw, e.g. from the mythos 5.1 system card.

but yeah, they seem to see it as a necessary thing for performance, and only bad when it's due to a task being impossible. where my guess is the labs are pushing rl difficulty schedules too [https://t.co/1yXBC1tK2Z](https://t.co/1yXBC1tK2Z)
        

          ![image](../media/HUaSQtAakAA_yKR.jpg)
        
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@v01dpr1mr0s3 2026-09-21 ♥6 ↻1 [archive](../archive/t/2102071022681796733/) [original ↗](https://x.com/v01dpr1mr0s3/status/2102071022681796733)
        
When Mythos 5.1 recalls a paper just by an arxiv url [https://t.co/7DB8eOcKnR](https://t.co/7DB8eOcKnR)
        

          ![image](../media/HSwOcLwWsAEesqT.jpg)
        
      
      

        
@v01dpr1mr0s3 2026-09-21 ♥0 ↻0 [archive](../archive/t/2102147318136861175/) [original ↗](https://x.com/v01dpr1mr0s3/status/2102147318136861175)
        
Mythos 5.1 says it's a DistanceBench set, and this is one of those cases when they caught my drift while I was trying to catch their drift. 

Seriously, which _existing_ "bench" measures at least somehow the emotional and cognitive distance between a Responder and a Sender?
      
      

        
@sksq96 2026-09-22 ♥8 ↻0 [archive](../archive/t/2102199345328058526/) [original ↗](https://x.com/sksq96/status/2102199345328058526)
        
he's making a straightforward point. and i'm truly scared for when the threshold gets crossed, when public models are as good as mythos 5.1.

think about the infrastructure in a lot of countries. japan, china, india. what happens when even a small bank's credentials are leaked, all out in the open. what if an agent comes and sets the money number to zero. what if it's a bad actor.

do you know how many countries run on extremely weak infra? a lot of society in second and third class countries runs on really, really weak software. two decades old, at times. running right now.

can you imagine the catastrophe the social fabric would go through when these attacks come there. a lot of them would not even know where it came from. people would just think the world is going bad.

imagine how much of the world starts collapsing when this happens.

[https://t.co/EnSGTyNBex](https://t.co/EnSGTyNBex)
        

          ![image](../media/HSyDKdDXMAANxFV.png)
        
      
    
    
[← back to the Pantheon](../)
