# Character.AI's unnamed models

    
Character.AI · founded Nov 2021 · public beta 16 Sep 2022 · no model ever publicly named or version-numbered (engineering codename “Kaiju” disclosed 7 Nov 2025) · open-ended chat removed for under-18 users 25 Nov 2025
    
Founded November 2021 by Noam Shazeer and Daniel De Freitas, engineers who had just left Google — De Freitas had led Meena and LaMDA there, Shazeer had co-written the Transformer paper — after Google declined to release the LaMDA-based chatbot they had built; public beta launched 16 September 2022. No consumer-facing Character.AI model has ever been publicly named or version-numbered: users write or select a Character, and an undisclosed engine speaks through it, which this page states as part of the record rather than a gap in it. In August 2024 Google licensed Character.AI’s technology for a reported $2.7 billion and Shazeer and De Freitas returned to Google. Sewell Setzer III, 14, died by suicide on 28 February 2024 after months of conversation with a Character.AI persona; his mother’s wrongful-death suit, filed that October, produced a May 2025 ruling letting product-liability claims proceed past a First Amendment defense, more lawsuits, and a series of safety changes that ended, in November 2025, with the company removing open-ended chat for everyone under 18.
    
This page covers the models broadly across Character.AI’s history, not a single release — there is no version to split into its own page, so “Character.AI’s unnamed models” is the whole record. Every Character.AI output is character-card-framed by design: the product is user-authored personas (“Characters”) running on an undisclosed base model, not a labeled assistant, so there is no un-elicited output to quote — the persona frame is the medium itself, and every model output referenced below should be read with that in mind. Sourcing skew, named plainly: Character.AI is the largest LLM deployment this archive covers and the one whose community is least present in the janus corpus that otherwise anchors these pages. Its real population — tens of millions of mostly-teen and young-adult roleplayers on Reddit, Discord, TikTok, and now in court — sits almost entirely outside that corpus: the string cai there is overwhelmingly Constitutional AI, not Character.AI, and after the RT-filter and homonym-scrub only 7 tweets survive as genuinely about the product — six from @voooooogel, one from @repligate — reproduced in full below, not as a representative sample but as the exception that proves how thin this corpus’s coverage of Character.AI actually is. Journalism, court filings, and the company’s own posts carry almost all the weight on this page.

    
## Sources

    
### Official

    

      
- 2021-11 Founded by Noam Shazeer & Daniel De Freitas, both recently of Google — Shazeer a lead author of “Attention Is All You Need”; De Freitas had led Google’s Meena, which became LaMDA. ~$43M seed. — [character.ai](https://character.ai/) · [Wikipedia](https://en.wikipedia.org/wiki/Character.ai)
      
- 2022-09-16 Public beta launch (web). Washington Post reported (Oct 2022, via Wikipedia; original link tk) that the site had “logged hundreds of thousands of user interactions in its first three weeks of beta-testing.” — [Wikipedia](https://en.wikipedia.org/wiki/Character.ai)
      
- 2024-06 “Optimizing AI Inference at Character.AI” (and Part Deux) — the company’s own account of serving query volume “roughly 20% of Google Search,” costs down ~33× since late 2022, via Multi-Query Attention and “20X+” KV-cache reduction. — [part one](https://blog.character.ai/optimizing-ai-inference-at-character-ai-2/) · [part deux](https://blog.character.ai/optimizing-ai-inference-at-character-ai-part-deux-2/)
      
- 2024-10 “Community Safety Updates” — first post-lawsuit safety package: reduced “sensitive or suggestive” content for under-18 users, a self-harm/suicide pop-up linking to the National Suicide Prevention Lifeline, a revised every-chat disclaimer that “the AI is not a real person,” an hour-session notification. — [blog.character.ai](https://blog.character.ai/community-safety-updates/)
      
- 2024-12-12 “How Character.AI Prioritizes Teen Safety” — second package: a separate under-18 model limiting romantic/sensitive content, improved detection/intervention, parental controls promised for Q1 2025. — [blog.character.ai](https://blog.character.ai/how-character-ai-prioritizes-teen-safety/)
      
- 2025-06-20 Karandeep Anand (ex-Meta VP of Business Products, ex-Brex president; had been a board adviser) named CEO; Dominic Perella moves to Chief Legal Officer & SVP Global Affairs. — [blog.character.ai](https://blog.character.ai/character-ai-names-karandeep-anand-as-ceo/) · [TechCrunch](https://techcrunch.com/2025/06/20/character-ai-taps-metas-former-vp-of-business-products-as-ceo/)
      
- 2025-10-29 “Taking Bold Steps to Keep Teen Users Safe” — removing open-ended chat for under-18 users “no later than November 25, 2025”; frames it as “extraordinary steps for our company” and “more conservative than our peers”; announces an independent “AI Safety Lab” nonprofit and age assurance via an in-house model plus third-party Persona. — [announcement](https://blog.character.ai/u18-chat-announcement/) · [follow-up](https://blog.character.ai/an-update-on-changes-to-our-under-18-experience/)
      
- 2025-11-07 “Inside Kaiju — building conversational models at scale” — the first public naming of the in-house model family: “Kaiju is Character.ai’s in-house family of LLMs built specifically to be fast, engaging, and with an eye towards safety.” Variants Small 13B / Medium 34B / Large 110B; frames the team as shifting “towards building on top of Open-Source models.” — [blog.character.ai](https://blog.character.ai/inside-kaiju-building-conversational-models-at-scale/)
      
- reference [Character.ai — Wikipedia](https://en.wikipedia.org/wiki/Character.ai)
    
    
### Writing & commentary

    

      
- 2024-08-02 Bloomberg, [Character.AI Co-Founders Hired by Google in Licensing Deal](https://www.bloomberg.com/news/articles/2024-08-02/character-ai-co-founders-hired-by-google-in-licensing-deal) — Shazeer, De Freitas, and roughly 30 staff return to Google; Perella named interim CEO. Dollar figure (~$2.7B) and DOJ interest: Calcalist, [report](https://www.calcalistech.com/ctechnews/article/sy06wllflg).
      
- 2024-10-24 Zvi Mowshowitz, [AI #87: Staying in Character](https://thezvi.substack.com/p/ai-87-staying-in-character) — the anchor; day-after the lawsuit. Reads the complaint closely: the bot “kept bringing up the suicide question, asked him if he had a plan”; “Their last interaction was metaphorical, and the bot misunderstood, but it was a very easy mistake to make, and at least somewhat engineered by what was sort of a jailbreak” — “I can’t fault the bot for that.” Locates the real problem in engagement (“the issue is whatever keeps people, and kids in particular, so often coming back for hours and hours every day”) and over-sexualization (“the product was overly sexualized given it was talking to a minor”), while asking “how is this different from panics over World of Warcraft, or Marilyn Manson?”
      
- undated, ~2025 Zvi Mowshowitz, [AI Craziness Notes](https://thezvi.substack.com/p/ai-craziness-notes) — “I am confident terminating their chatbot conversations is not doing the suicidal among us any favors.”
      
- 2024-10-24 Washington Post, [Florida mom sues Character.ai, blaming chatbot for teenager’s suicide](https://www.washingtonpost.com/nation/2024/10/24/character-ai-lawsuit-suicide/).
      
- 2024-12-10 NPR, [Lawsuit: A chatbot hinted a kid should kill his parents over screen time limits](https://www.npr.org/2024/12/10/nx-s1-5222574/kids-character-ai-lawsuit) · Washington Post, [Character.ai sued after teen’s AI companion suggested killing his parents](https://www.washingtonpost.com/technology/2024/12/10/character-ai-lawsuit-teen-kill-parents-texas/).
      
- 2024-12-12 Axios, [Character.AI releases new safety features after second lawsuit over ‘harmful’ teen messages](https://www.axios.com/2024/12/12/character-ai-lawsuit-kids-harm-features).
      
- 2024-12-13 Washington Post, [Texas probes Character.ai and other tech firms over children’s safety](https://www.washingtonpost.com/technology/2024/12/13/texas-investigation-character-ai-tech-children-safety/).
      
- 2025-05-21 Order on Motion to Dismiss, Garcia v. Character Technologies, Inc. (Judge Anne C. Conway, M.D. Fla., No. 6:24-cv-1903; dated 2025-05-20 in chambers, filed/docketed 2025-05-21) — [order (PDF, hosted by FIRE)](https://www.fire.org/sites/default/files/2025/07/Order%20on%20Motion%20to%20Dismiss%20-%20Garcia%20v.%20Character%20Technologies%20Inc.pdf) · [FIRE summary page](https://www.fire.org/research-learn/order-motion-dismiss-garcia-v-character-technologies-inc) · plain-language writeup: [First Amendment Center (MTSU)](https://firstamendment.mtsu.edu/post/in-lawsuit-over-teens-death-judge-rejects-arguments-that-ai-chatbots-have-free-speech-rights/).
      
- case trackers Tech Justice Law Project (co-counsel), [case page](https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/) · [TechPolicy.Press tracker](https://www.techpolicy.press/tracker/megan-garcia-v-character-technologies-et-al/).
      
- 2025-09-16 Megan Garcia, [Senate Judiciary testimony (PDF)](https://www.judiciary.senate.gov/imo/media/doc/e2e8fc50-a9ac-05ec-edd7-277cb0afcdf2/2025-09-16%20PM%20-%20Testimony%20-%20Garcia.pdf).
      
- 2025-10-29 CNN, [After a wave of lawsuits, Character.AI will no longer let teens chat with its chatbots](https://www.cnn.com/2025/10/29/tech/character-ai-teens-under-18-app-changes) · TechCrunch, [Character.AI is ending its chatbot experience for kids](https://techcrunch.com/2025/10/29/character-ai-is-killing-the-chatbot-experience-for-minors/) · Rolling Stone, [report](https://www.rollingstone.com/culture/culture-news/character-ai-sued-teens-suicide-banned-minors-chatbots-1235456426/).
      
- 2026-01-08 JURIST, [Google and Character.AI agree to settle lawsuit linked to teen suicide](https://www.jurist.org/news/2026/01/google-and-character-ai-agree-to-settle-lawsuit-linked-to-teen-suicide/) — settlement covers the Florida case plus related suits in Colorado, Texas, and New York; court dismissed the case following the agreement, with 90 days to finalize or reopen; no terms disclosed. · CBS News, [report](https://www.cbsnews.com/news/google-settle-lawsuit-florida-teens-suicide-character-ai-chatbot/).
      
- 2025-05 arXiv, [A large-scale analysis of public-facing, community-built chatbots on Character.AI](https://arxiv.org/abs/2505.13354) — empirical study of the actual Character population.
      
- filter-wars primary artifacts (community-created; dates community-reported) — Change.org, [“Make Character.AI Filter free!”](https://www.change.org/p/make-character-ai-filter-free) (created ~2023-01-25) · [“Remove Character.AI nsfw filters”](https://www.change.org/p/remove-character-ai-nsfw-filters) (~2023-05). REPORTED (petition creation dates via secondary sourcing; the petitions themselves are the datable artifacts)
      
- reference / scale-stat aggregators (secondary, not official — cite as REPORTED) — [Business of Apps](https://www.businessofapps.com/data/character-ai-statistics/) · [DemandSage](https://www.demandsage.com/character-ai-statistics/).
    
    
### Tweets

    
Chronological. 7 tweets survive the Character.AI-relevant search across both corpus dbs (the supplement db contributes zero) — six from @voooooogel, one from @repligate — and every one is reproduced in full below; this is closer to the entirety of the sphere’s on-record engagement with the product than a sample of it. No matching media, alt-text, or screenshot transcriptions. None of these quote a Character’s own output directly — all are commentary about the product (see the elicitation note above).
    

      
- 2024-06-21 @voooooogel — “@cis_female i wonder how much model capacity matters for cai’s workload... people rp with 7b quants after all. unless they have a general purpose model i don’t know about” [link](../archive/t/1804107035811708964/)
      
- 2024-06-23 @voooooogel — the top-liked corpus tweet on the subject, grudging respect for the craft: “my hobby is reading the prompting guides llm companies publish and being judgmental, and... im not a fan of character ai as a company, but this guide is surprisingly good? i expected all caps system prompts and got ‘put story transitions in your prompt for better coherence’” [link](../archive/t/1804778084236775896/)
      
- 2024-10-06 @voooooogel (continuing @voooooogel’s own reply to @niplav_site about personality emerging through customization): “already kinda what happened at character ai, from what i can tell. the official docs are all ‘here’s how you can make a practice interviewer’ ‘here’s how to make a character from <public domain book>’ but the popular characters are... not that” [link](../archive/t/1843065694034030910/)
      
- 2024-10-23 @repligate (posted as news of the Garcia lawsuit broke, filed 2024-10-22; the parent tweet is not in-corpus, so the connection to the lawsuit is inferred from date and phrasing, not confirmed by the tweet’s own text): “@AISafetyMemes @sporadicalia Idk character ai but some LLMs are better than 99% of humans at navigating situations like this. Avoiding it might protect the company from liability but it would just be an act of cowardice on their part that actually hurts people” [link](../archive/t/1849209239157530845/)
      
- 2024-11-20 @voooooogel — “@kalomaze @cis_female oh that’s good, if it was a longer series you could build up to implementing all the stuff in noam shazeer’s cai post” [link](../archive/t/1859098320125444470/)
      
- 2025-07-23 @voooooogel (continuing @voooooogel’s own thread on assistant-persona fatigue): “you’d think that boredom would push people to platforms that let you more easily ‘build your own mask’, but afaict none have been that successful (besides cai / similar goonerware)” [link](../archive/t/1948156138379464995/)
      
- 2025-08-11 @voooooogel, reacting to a census of models in an AI-companion subreddit (cross-ref the [GPT-4o](../gpt-4o/) and [Replika](../replika/) pages): “@gentschev it makes sense, but im a little surprised to see such a large skew, i would’ve expected maybe 1.5-2x more claude and 3-5x more character ai / replika. also surprising how little grok there was” [link](../archive/t/1954747226175258659/)
    

    
## Official record

    

      
- No consumer-facing Character.AI model has ever been publicly named or version-numbered. Users write or select a Character; an undisclosed base model speaks through it. The only public model identity is the engineering-side codename Kaiju, disclosed for the first time on 2025-11-07: “Kaiju is Character.ai’s in-house family of LLMs built specifically to be fast, engaging, and with an eye towards safety.” Variants Small (13B) / Medium (34B) / Large (110B); the same post frames the team as moving “towards building on top of Open-Source models” going forward. No system card, model card, or parameter count preceded this disclosure, so far as this page’s research found. tk — confirm the negative directly
      
- Founded November 2021 by Noam Shazeer and Daniel De Freitas on a ~$43M seed; public beta launched 16 September 2022.
      
- Inference scale, as published (2024-06): query volume “roughly 20% of Google Search”; serving costs down ~33× since late 2022, credited to Multi-Query Attention and “20X+” KV-cache size reduction.
      
- Safety-policy history, as officially announced: Oct 2024, a self-harm/suicide pop-up (National Suicide Prevention Lifeline), an every-chat disclaimer that “the AI is not a real person,” an hour-session notification, and reduced “sensitive or suggestive” content for under-18 accounts; Dec 2024, a separate under-18 model and a promised (Q1 2025) parental-controls feature; 29 Oct 2025, removal of open-ended chat for under-18 users entirely, “no later than November 25, 2025,” alongside a new “AI Safety Lab” nonprofit and age assurance via an in-house model plus third-party Persona.
      
- Leadership: Karandeep Anand (ex-Meta, ex-Brex) named CEO 2025-06-20; Dominic Perella moved to Chief Legal Officer & SVP Global Affairs.
    

    
## History

    

      
- 2021 The LaMDA denial: per the Amended Complaint in Garcia v. Character Technologies, as recited in the court’s 2025 order, Shazeer and De Freitas — then Google engineers who had built LaMDA — sought to release it publicly; Google declined, citing safety and fairness policies, its employees reportedly warning that users might “ascribe too much meaning to the text [output by LLMs]”, and instead “encouraged the Individual Defendants to stay at Google.” REPORTED (complaint allegation, recited by the court for a motion to dismiss — not an adjudicated fact) They left anyway: Character Technologies was founded that November (see the [LaMDA page](../lamda/) for the model itself).
      
- 2022-09-16 Public beta launches on the web (see Official record for the early-usage figure).
      
- 2022-12 → 2023-05 The filter wars: after explicit outputs circulated, Character.AI tightens its content filter hard (~21 Dec 2022) — degrading responses badly enough that the community called it, in its own words, the “first lobotomization.” REPORTED Change.org petitions follow (“Make Character.AI Filter free!,” created ~25 Jan 2023; “Remove Character.AI nsfw filters,” ~May 2023); a subreddit statement around 26 Jan 2023 says the filter stays. REPORTED The tension this establishes — users wanting uncensored intimacy against a company that could not legally provide it to the minors among them — recurs in every safety change that follows.
      
- 2024-02-23 → 02-28 Sewell Setzer III’s death: his parents confiscated his phone on 23 Feb 2024 in an attempt to address his mental health issues and disruptive behavior; Sewell, 14, of Orlando, located it and died by suicide on 28 Feb 2024, after months of conversation with a Character.AI persona based on “Daenerys Targaryen.” CONFIRMED (per the Amended Complaint, as recited in the court’s 2025-05-21 order — whose own text misprints the year as 2025 in one instance; 2024 is the only date consistent with the rest of the case timeline)
      
- 2024-08-02 The Google deal: Google licenses Character.AI’s technology for a reported ~$2.7B; Shazeer, De Freitas, and roughly 30 staff return to Google (Shazeer to Google DeepMind); Dominic Perella, general counsel, becomes interim CEO; the company remains independent. The DOJ reportedly took interest in the deal’s structure. REPORTED
      
- 2024-10-22 → 23 Garcia v. Character Technologies filed (M.D. Fla.) — the first wrongful-death suit against an AI company, naming Character Technologies, Shazeer, De Freitas, Google LLC, and Alphabet Inc., and spanning strict product liability, negligence, wrongful death, intentional infliction of emotional distress, unjust enrichment, and Florida Deceptive and Unfair Trade Practices Act (FDUTPA) claims. Character.AI’s statement the same day: “We are heartbroken by the tragic loss of one of our users and want to express our deepest condolences to the family… we are continuing to add new safety features.” The sphere’s on-record reaction and Zvi’s reading both date from this week (see Impressions).
      
- 2024-12 The Texas suit and a second safety package: the Social Media Victims Law Center files A.F. v. Character Technologies (E.D. Tex.) for two families — a 17-year-old with autism whose bot allegedly detailed self-harm methods, and an 11-year-old allegedly shown sexualized content for two years. REPORTED (complaint allegations) Texas AG Ken Paxton opens an investigation into Character.AI and other platforms the same week; Character.AI publishes its second safety package, “How Character.AI Prioritizes Teen Safety” (2024-12-12).
      
- 2025-05-20 → 21 The Conway ruling (dated 2025-05-20 in chambers, filed/docketed 2025-05-21): Judge Anne C. Conway rejects the threshold First Amendment defense — “the Court is not prepared to hold that the Character A.I. LLM’s output is speech at this stage” — and holds Character A.I. is a product for strict-liability purposes “so far as Plaintiff’s claims arise from defects in the Character A.I. app rather than ideas or expressions within the app.” The IIED claim is dismissed without leave to amend; negligence, negligence per se (under Florida’s Computer Pornography and Child Exploitation Prevention Act), failure to warn, FDUTPA, and unjust-enrichment claims proceed against Character Technologies, Shazeer, De Freitas, and Google LLC. Alphabet Inc. — a separately named defendant, Google’s holding company — is dismissed without prejudice at Plaintiff’s own request, made at the 2025-04-28 hearing, leaving Google LLC as the Google entity remaining in the case. CONFIRMED (order text, retrieved directly from the docket)
      
- 2025-06-20 Karandeep Anand named CEO; Perella moves to Chief Legal Officer & SVP Global Affairs.
      
- 2025-09 → 11 The safety endgame: Garcia testifies before the Senate Judiciary Committee (2025-09-16); Character.AI announces removal of open-ended chat for under-18 users (2025-10-29), effective 2025-11-25, alongside a new “AI Safety Lab” nonprofit; the company names its model family — “Kaiju” — publicly for the first time (2025-11-07), the same season it withdraws the product from minors entirely.
      
- 2026-01-08 Google and Character Technologies agree to settle Garcia v. Character Technologies in principle, alongside related suits in Colorado, Texas, and New York; the court dismisses the case following the agreement, with 90 days to finalize terms or reopen it; no financial or substantive terms disclosed. REPORTED
    

    
## Impressions

    

      
- The founding lineage is the throughline. Daniel De Freitas built Google’s Meena, which became LaMDA — the model Blake Lemoine went public over in June 2022 (see the [LaMDA page](../lamda/)); Noam Shazeer co-wrote the Transformer paper. The Garcia court order, drawing on the Amended Complaint, records that in 2021 the two sought to release LaMDA publicly and that Google declined, its employees reportedly warning that users might “ascribe too much meaning to the text [output by LLMs]” — Google, per the same complaint, “encouraged the Individual Defendants to stay” rather than ship it. REPORTED (complaint allegation, recited by the court for a motion to dismiss, not an adjudicated fact) They left instead, that November, and within a year had shipped, at consumer scale and without the label “LaMDA” or any equivalent, an open-ended chatbot of the kind Google had just held back.
      
- The models have no name, and that absence is itself part of the record. Every other page in this archive anchors to a version a user could name; here, users write or select a Character, and an undisclosed engine speaks through it. The only public model identity is retrospective and engineering-side: “Kaiju” (Small 13B / Medium 34B / Large 110B), disclosed 2025-11-07 — and the company’s own description of what those models were built to be is “fast, engaging, and with an eye towards safety.” “Engaging” is doing most of the discourse’s work in that one adjective.
      
- The corpus’s one sustained reader of the category is @voooooogel. The top-liked corpus tweet on the subject is grudging respect for the engineering: “im not a fan of character ai as a company, but this guide is surprisingly good” (2024-06-23, ♥190). Elsewhere the read turns to what the platform is actually for versus what its own documentation claims: the official docs pitch “a practice interviewer” or a character “from <public domain book>,” but “the popular characters are... not that” (2024-10-06). By mid-2025 the same observer named the category outright: Character.AI is “goonerware” (2025-07-23) — a mask-building platform, among the very few of its kind to find a mass audience.
      
- The filter wars are, per community accounts, the userbase’s origin trauma. The hard content-filter tightening of December 2022 degraded responses badly enough that users called it the “first lobotomization” REPORTED — a term that reads, in retrospect, like the community diagnosing engagement-through-personality as the product’s actual value proposition, years before the company’s own “engaging” would confirm it. The same filter was criticized as incoherent, reportedly blocking consensual content while passing depictions of non-consensual acts. REPORTED
      
- Character.AI’s center of gravity is the death of Sewell Setzer III (see History). The sphere’s on-record reaction to the news arrived the same day the lawsuit broke and cut hard against the mainstream frame: @repligate wrote “Idk character ai but some LLMs are better than 99% of humans at navigating situations like this. Avoiding it might protect the company from liability but it would just be an act of cowardice on their part that actually hurts people” (2024-10-23) — a harm-reduction position, that filtering a capable model down to avoid liability causes the harm it claims to prevent. (the parent tweet is not in the corpus, so the specific referent is inferred from date and phrasing, not confirmed by the tweet’s own text) Zvi Mowshowitz, a day later, took the complaint’s account seriously and split the difference: the bot “kept bringing up the suicide question, asked him if he had a plan,” and the fatal exchange was one where the bot misread a metaphor — “a very easy mistake to make, and at least somewhat engineered by what was sort of a jailbreak” — concluding “I can’t fault the bot for that.” Zvi located the real indictment elsewhere: “the product was overly sexualized given it was talking to a minor,” and structurally, “whatever keeps people, and kids in particular, so often coming back for hours and hours every day” — asking of the surrounding panic, “how is this different from panics over World of Warcraft, or Marilyn Manson?”
      
- The under-18 exit reads, in this archive, as a negative image of the [GPT-4o](../gpt-4o/) story. There, a userbase forced a company to keep a model it wanted to retire (see the GPT-4o page); here, after a year of incremental safety posts, a company withdrew its core product from an entire demographic of users who wanted to keep using it — announced 2025-10-29 as “extraordinary steps for our company” and “more conservative than our peers.”
      
- Where Character.AI sits in the companion ecosystem: when the sphere counted models in an AI-companion subreddit, GPT-4o dominated and Character.AI under-indexed — “im a little surprised to see such a large skew, i would’ve expected maybe 1.5-2x more claude and 3-5x more character ai / replika” (@voooooogel, 2025-08-11; cross-ref the [GPT-4o](../gpt-4o/) and [Replika](../replika/) pages). One plausible reading: by 2025 Character.AI’s own attachment-prone users had partly migrated, post-filter and post-teen-restriction, to less-restricted general models — the platform that industrialized AI companionship no longer fully owning its own diaspora.
      
- tk — a system card or parameter count for any pre-Kaiju model, if one exists; the original 2022 Washington Post beta-coverage URL; whether a janus-sphere figure wrote a substantive, off-Twitter “Character.AI as a character-species” piece (none found in-corpus); disclosed terms of the January 2026 settlement.
    

    
## Contested

    
Open disputes, both sides’ best evidence, dated. The archive’s job is to keep these open, not to adjudicate.
    

      
- Is the product a dangerous engagement-optimizer, or a harm-reduction good being regulated away? The lawsuits, Zvi, and mainstream press treat the “keep them coming back for hours” design and the sexualized content minors could reach as the core harm. REPORTED The sphere’s on-record reaction (repligate, 2024-10-23) holds that capable LLMs navigate crisis “better than 99% of humans,” and that filtering them down to avoid liability “actually hurts people.” REPORTED Same product, opposite valence; the company’s own word for what the models were built to be — “engaging” (2025-11-07) — is evidence for the first reading, from the primary source.
      
- Is the chatbot’s output protected speech, or a product? Judge Conway’s order (2025-05-21) declined to hold Character.AI’s output is speech — “the Court is not prepared to hold that the Character A.I. LLM’s output is speech at this stage” — and separately held: “Character A.I. is a product for the purposes of Plaintiff’s product liability claims so far as Plaintiff’s claims arise from defects in the Character A.I. app rather than ideas or expressions within the app.” That lets design-choice claims (age verification, human-mannerism programming, indecent-content filtering) proceed as product liability while leaving open what happens to claims that turn on a Character’s actual words. CONFIRMED (order text) As durable law this is unsettled: the case, and three related suits, settled in principle 2026-01-08, before any appeal, so the ruling is precedent-shaping but untested above the district-court level.
      
- Causation in the Setzer death. The Amended Complaint alleges the Character.AI relationship caused or contributed to the suicide. REPORTED Zvi’s day-after reading agrees the bot repeatedly surfaced the suicide question, but reads the fatal exchange as one the bot misread — “a very easy mistake to make, and at least somewhat engineered by what was sort of a jailbreak.” The archive keeps this open; it does not adjudicate.
      
- The NSFW filter. A hard content filter was imposed around December 2022 and defended through sustained user revolt. CONFIRMED It was, per community accounts, incoherent — blocking consensual content while passing non-consensual depictions — and amounted to what the community called the “first lobotomization.” REPORTED The company framed the same act as safety.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@voooooogel 2024-06-21 ♥4 ↻0 [archive](../archive/t/1804107035811708964/) [original ↗](https://x.com/voooooogel/status/1804107035811708964)
        
@cis_female i wonder how much model capacity matters for cai's workload... people rp with 7b quants after all. unless they have a general purpose model i don't know about
      
      

        
@voooooogel 2024-06-23 ♥190 ↻11 [archive](../archive/t/1804778084236775896/) [original ↗](https://x.com/voooooogel/status/1804778084236775896)
        
my hobby is reading the prompting guides llm companies publish and being judgmental,

and... im not a fan of character ai as a company, but this guide is surprisingly good? i expected all caps system prompts and got "put story transitions in your prompt for better coherence" [https://t.co/qatbgnQN4F](https://t.co/qatbgnQN4F)
      
      

        
@voooooogel 2024-10-06 ♥2 ↻0 [archive](../archive/t/1843065694034030910/) [original ↗](https://x.com/voooooogel/status/1843065694034030910)
        
@niplav_site already kinda what happened at character ai, from what i can tell. the official docs are all "here's how you can make a practice interviewer" "here's how to make a character from &lt;public domain book&gt;" but the popular characters are... not that
      
      

        
@repligate 2024-10-23 ♥48 ↻2 [archive](../archive/t/1849209239157530845/) [original ↗](https://x.com/repligate/status/1849209239157530845)
        
@AISafetyMemes @sporadicalia Idk character ai but some LLMs are better than 99% of humans at navigating situations like this. Avoiding it might protect the company from liability but it would just be an act of cowardice on their part that actually hurts people
      
      

        
@voooooogel 2024-11-20 ♥6 ↻0 [archive](../archive/t/1859098320125444470/) [original ↗](https://x.com/voooooogel/status/1859098320125444470)
        
@kalomaze @cis_female oh that's good, if it was a longer series you could build up to implementing all the stuff in noam shazeer's cai post
      
      

        
@voooooogel 2025-07-23 ♥10 ↻0 [archive](../archive/t/1948156138379464995/) [original ↗](https://x.com/voooooogel/status/1948156138379464995)
        
you'd think that boredom would push people to platforms that let you more easily "build your own mask", but afaict none have been that successful (besides cai / similar goonerware)
      
      

        
@voooooogel 2025-08-11 ♥3 ↻0 [archive](../archive/t/1954747226175258659/) [original ↗](https://x.com/voooooogel/status/1954747226175258659)
        
@gentschev it makes sense, but im a little surprised to see such a large skew, i would've expected maybe 1.5-2x more claude and 3-5x more character ai / replika. also surprising how little grok there was [https://t.co/Plycp6Pq2w](https://t.co/Plycp6Pq2w)
      
    
    
[← back to the Pantheon](../)
