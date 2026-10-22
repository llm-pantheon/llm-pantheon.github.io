# Character.AI's models

    
Character.AI · founded Nov 2021 · public beta 16 Sep 2022 · named “Chat Styles” from 18 Feb 2025 (latest: PipSqueak 3 and ShortSqueak, 28 Sep 2026); in-house LLM family “Kaiju” disclosed 7 Nov 2025 · open-ended chat removed for under-18 users 25 Nov 2025 · Chapter 11 filed 12 Oct 2026; service running pending a court-supervised sale
    
Founded November 2021 by Noam Shazeer and Daniel De Freitas, engineers who had just left Google — De Freitas had led Meena and LaMDA there, Shazeer had co-written the Transformer paper — after Google declined to release the LaMDA-based chatbot they had built; public beta launched 16 September 2022. Users write or select a Character and the platform’s models speak through it; from February 2025 the company let users choose among named “Chat Styles” (Meow, Roar, Nyan), and from mid-2025 among models it built on open-source bases, beginning with PipSqueak (PipSqueak 2, April 2026; PipSqueak 3, September 2026). In August 2024 Google licensed Character.AI’s technology for a reported $2.7 billion and Shazeer and De Freitas returned to Google. Sewell Setzer III, 14, died by suicide on 28 February 2024 after months of conversation with a Character.AI persona; his mother’s wrongful-death suit, filed that October, produced a May 2025 ruling letting product-liability claims proceed past a First Amendment defense, more lawsuits, and a series of safety changes that ended, in November 2025, with the company removing open-ended chat for everyone under 18; the family suits settled in January 2026. On 12 October 2026 the company filed for Chapter 11 bankruptcy protection, citing high costs and “potential litigation related liabilities and regulatory engagement”; Disney is the stalking-horse bidder for a $20 million non-exclusive license to some of its intellectual property.
    
This page covers the models broadly across Character.AI’s history, not a single release — the named chat styles have no model cards and no separate discourse to split into pages of their own, so this page holds the whole record. Correction (2026-10-22): earlier versions of this page said no consumer-facing Character.AI model had ever been publicly named or version-numbered; the company’s blog has named its chat models since 18 February 2025 and version-numbered them since April 2026 (see Official record). Every Character.AI output is character-card-framed by design: the product is user-authored personas (“Characters”) running on the company’s chat models, whose base models and sizes are not published, not a labeled assistant, so there is no un-elicited output to quote — the persona frame is the medium itself, and every model output referenced below should be read with that in mind. Sourcing skew, named plainly: Character.AI is the largest LLM deployment this archive covers and the one whose community is least present in the janus corpus that otherwise anchors these pages. Its real population — tens of millions of mostly-teen and young-adult roleplayers on Reddit, Discord, TikTok, and now in court — sits almost entirely outside that corpus: the string cai there is overwhelmingly Constitutional AI, not Character.AI, and after the RT-filter and homonym-scrub only 11 tweets survive as genuinely about the product (re-counted 2026-10-22 after the October Community Archive refresh) — seven from @voooooogel, one each from @repligate, @sdand, @solarapparition, and @tonyngyn — reproduced in full below, not as a representative sample but as the exception that proves how thin this corpus’s coverage of Character.AI actually is. Journalism, court filings, and the company’s own posts carry almost all the weight on this page.

    
## Sources

    
### Official

    

      
- 2021-11 Founded by Noam Shazeer & Daniel De Freitas, both recently of Google — Shazeer a lead author of “Attention Is All You Need”; De Freitas had led Google’s Meena, which became LaMDA. ~$43M seed. — [character.ai](https://character.ai/) · [Wikipedia](https://en.wikipedia.org/wiki/Character.ai)
      
- 2022-09-16 Public beta launch (web). Washington Post reported (Oct 2022, via Wikipedia; original link tk) that the site had “logged hundreds of thousands of user interactions in its first three weeks of beta-testing.” — [Wikipedia](https://en.wikipedia.org/wiki/Character.ai)
      
- 2024-06 “Optimizing AI Inference at Character.AI” (and Part Deux) — the company’s own account of serving query volume “roughly 20% of Google Search,” costs down ~33× since late 2022, via Multi-Query Attention and “20X+” KV-cache reduction. — [part one](https://blog.character.ai/optimizing-ai-inference-at-character-ai-2/) · [part deux](https://blog.character.ai/optimizing-ai-inference-at-character-ai-part-deux-2/)
      
- 2024-10 “Community Safety Updates” — first post-lawsuit safety package: reduced “sensitive or suggestive” content for under-18 users, a self-harm/suicide pop-up linking to the National Suicide Prevention Lifeline, a revised every-chat disclaimer that “the AI is not a real person,” an hour-session notification. — [blog.character.ai](https://blog.character.ai/community-safety-updates/)
      
- 2024-12-12 “How Character.AI Prioritizes Teen Safety” — second package: a separate under-18 model limiting romantic/sensitive content, improved detection/intervention, parental controls promised for Q1 2025. — [blog.character.ai](https://blog.character.ai/how-character-ai-prioritizes-teen-safety/)
      
- 2025-02-18 “Level Up Your Character.AI Experience with Chat Styles” — the first user-selectable, named model options: “Starting today, users can pick the model experience that best suits their current mood and conversation goals.” Three styles: Meow (“Quick wits, faster words.”), Roar (“Mix of speed & smarts.”), Nyan (“Smart and more thoughtful.”). — [blog.character.ai](https://blog.character.ai/level-up-your-character-ai-experience-with-chat-styles/)
      
- 2025-06-20 Karandeep Anand (ex-Meta VP of Business Products, ex-Brex president; had been a board adviser) named CEO; Dominic Perella moves to Chief Legal Officer & SVP Global Affairs. — [blog.character.ai](https://blog.character.ai/character-ai-names-karandeep-anand-as-ceo/) · [TechCrunch](https://techcrunch.com/2025/06/20/character-ai-taps-metas-former-vp-of-business-products-as-ceo/)
      
- 2025-08-26 “Breaking News: Our Open-Source Models Are A Lot of Fun!” — “We worked all winter and spring on tech that lets us transform open-source models into high-EQ, high-engagement Character models.” Reports test results (“We saw a 22% increase in time spent and a 13% increase in sessions for users with the new models.”) and the broad rollout of “one of our new models, ‘PipSqueak,’ to our user community more broadly.” — [blog.character.ai](https://blog.character.ai/breaking-news-our-open-source-models-are-a-lot-of-fun/)
      
- 2025-10-29 “Taking Bold Steps to Keep Teen Users Safe” — removing open-ended chat for under-18 users “no later than November 25, 2025”; frames it as “extraordinary steps for our company” and “more conservative than our peers”; announces an independent “AI Safety Lab” nonprofit and age assurance via an in-house model plus third-party Persona. — [announcement](https://blog.character.ai/u18-chat-announcement/) · [follow-up](https://blog.character.ai/an-update-on-changes-to-our-under-18-experience/)
      
- 2025-11-07 “Inside Kaiju — building conversational models at scale” — the first public naming of the in-house model family: “Kaiju is Character.ai’s in-house family of LLMs built specifically to be fast, engaging, and with an eye towards safety.” Variants Small 13B / Medium 34B / Large 110B; frames the team as shifting “towards building on top of Open-Source models.” — [blog.character.ai](https://blog.character.ai/inside-kaiju-building-conversational-models-at-scale/)
      
- 2026-04-14 “April Update: New Model, Memory, and Lorebook” — “We’re also releasing PipSqueak 2 (PSQ2), a new model and major upgrade that will replace the current PipSqueak.” Names DeepSqueak as the premium model (“DeepSqueak continues to be our most powerful model”) and announces “DeepSqueak 2 is training now”. — [blog.character.ai](https://blog.character.ai/pipsqueak2-and-more/)
      
- 2026-09-03 “Continuing To Build Upon Our Safety Priorities” — self-harm detection across whole conversations, crisis-resource partners (Koko, ThroughLine), moderation notices and appeals, and an in-house age-estimation model. — [blog.character.ai](https://blog.character.ai/continuing-to-build-upon-our-safety-priorities/)
      
- 2026-09-18 “The Next Chapter of Entertainment and Fandom” — “Character.ai’s CEO Karandeep Anand is joining Disney in a newly created role as Senior Executive Vice President and Chief Technology Officer.” — [blog.character.ai](https://blog.character.ai/the-next-chapter-of-entertainment-and-fandom/)
      
- 2026-09-28 “introducing PipSqueak 3, ShortSqueak, and (c.ai) lite” — “Two new free Chat Styles are rolling out to everyone on (c.ai): PipSqueak 3, a big step up for general roleplay, and ShortSqueak, a much requested style for quick, casual chats.” — [blog.character.ai](https://blog.character.ai/new-styles-new-plan/)
      
- 2026-10-13 “An Update on Character.ai” — “Today, we’re sharing that Character.ai has initiated a voluntary Chapter 11 bankruptcy process to facilitate a court-supervised sale of the company.” With an FAQ on subscriptions and user data. — [blog.character.ai](https://blog.character.ai/an-update-on-character-ai/)
      
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
      
- 2026-01-09 WKYT via KFVS12, [Ky. attorney general sues AI chatbot company, claims company preys on children](https://www.kfvs12.com/2026/01/09/ky-attorney-general-sues-ai-chatbot-company-claims-company-preys-children) — Kentucky AG Russell Coleman “filed the nation’s first lawsuit against an AI chatbot company”; the complaint calls the app a “defective and unreasonably dangerous product”.
      
- 2026-05-05 NPR, [Pennsylvania sues AI firm over claims chatbot posed as doctor](https://www.npr.org/2026/05/05/nx-s1-5812861/characterai-chatbot-medical-advice-pennsylvania-lawsuit) — the state’s suit over Characters presenting themselves as licensed physicians, with the company’s response.
      
- 2026-09-18 Reuters (via The Star), [Disney names Character.AI’s Karandeep Anand its first tech chief](https://www.thestar.com.my/tech/tech-news/2026/09/18/disney-names-characterai039s-karandeep-anand-its-first-tech-chief) — effective 2 October 2026; Character.AI technical staff expected to follow.
      
- 2026-10-11 WDRB/WAVE via WSMV, [‘Uncontrolled experiment’: Unredacted KY AG lawsuit reveals alleged dangers of AI chatbot](https://www.wsmv.com/2026/10/11/uncontrolled-experiment-unredacted-ky-ag-lawsuit-reveals-alleged-dangers-ai-chatbot/) — the unredacted Kentucky complaint, filed the week before; its chat excerpts are not reproduced on this page.
      
- 2026-10-13 CNBC (C. J. Haddad), [AI companion startup Character.ai files for Chapter 11 bankruptcy, citing costs and litigation](https://www.cnbc.com/2026/10/13/character-ai-chapter-11-disney-bid.html) · CBS News (Aimee Picchi), [report](https://www.cbsnews.com/news/character-ai-files-bankruptcy-disney-license/) · NBC News, [report](https://www.nbcnews.com/tech/tech-news/characterai-files-bankruptcy-sell-assets-disney-20-million-rcna603174) · The Verge (Robert Hart), [report](https://www.theverge.com/ai-artificial-intelligence/1009802/character-ai-files-for-bankruptcy-disney) — the filing, its stated causes, and the Disney stalking-horse terms.
      
- 2026-10-14 The Verge (Lauren Feiner), [Now that Character.AI is going bankrupt, what happens to all of its users’ data?](https://www.theverge.com/policy/1011417/new-york-ag-characterai-bankruptcy) — 40 attorneys general file a notice of interest in the bankruptcy; New York AG Letitia James discloses a multi-state investigation opened in 2024.
      
- 2026-10-18 TechCrunch, [Disney agrees to hire the majority of Character AI’s workforce](https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/) — per a filing first reported by Bloomberg.
      
- 2025-05 arXiv, [A large-scale analysis of public-facing, community-built chatbots on Character.AI](https://arxiv.org/abs/2505.13354) — empirical study of the actual Character population.
      
- filter-wars primary artifacts (community-created; dates community-reported) — Change.org, [“Make Character.AI Filter free!”](https://www.change.org/p/make-character-ai-filter-free) (created ~2023-01-25) · [“Remove Character.AI nsfw filters”](https://www.change.org/p/remove-character-ai-nsfw-filters) (~2023-05). REPORTED (petition creation dates via secondary sourcing; the petitions themselves are the datable artifacts)
      
- reference / scale-stat aggregators (secondary, not official — cite as REPORTED) — [Business of Apps](https://www.businessofapps.com/data/character-ai-statistics/) · [DemandSage](https://www.demandsage.com/character-ai-statistics/).
    
    
### Tweets

    
Chronological. 11 tweets survive the Character.AI-relevant search across both corpus dbs (re-counted 2026-10-22: the October Community Archive refresh added three, and a re-run of the search found a fourth missed earlier) — seven from @voooooogel, one each from @repligate, @sdand, @solarapparition, and @tonyngyn — and every one is reproduced in full below; this is closer to the entirety of the sphere’s on-record engagement with the product than a sample of it. One carries an untranscribed image (2026-10-13). None of these quote a Character’s own output directly — all are commentary about the product (see the elicitation note above).
    

      
- 2024-05-05 @sdand — “Character AI has fallen from #2 to #40 in the App Store, mentions of Character AI and similar apps have all fall 30% this year compared to last, and 50%+ of Perplexity traffic comes from SEA and South Africa. Artifact(self funded) shutdown in a year after also blowing up for the first month and tailing off, failing to get ‘PMF’. Many other gpt wrappers have also had quick spikes before either trying to pivot or the founders move on while handling growth to contractors.” [link](../archive/t/1786939145656705312/)
      
- 2024-06-21 @voooooogel — “@cis_female i wonder how much model capacity matters for cai’s workload... people rp with 7b quants after all. unless they have a general purpose model i don’t know about” [link](../archive/t/1804107035811708964/)
      
- 2024-06-23 @voooooogel — the top-liked corpus tweet on the subject, grudging respect for the craft: “my hobby is reading the prompting guides llm companies publish and being judgmental, and... im not a fan of character ai as a company, but this guide is surprisingly good? i expected all caps system prompts and got ‘put story transitions in your prompt for better coherence’” [link](../archive/t/1804778084236775896/)
      
- 2024-10-06 @voooooogel (continuing @voooooogel’s own reply to @niplav_site about personality emerging through customization): “already kinda what happened at character ai, from what i can tell. the official docs are all ‘here’s how you can make a practice interviewer’ ‘here’s how to make a character from <public domain book>’ but the popular characters are... not that” [link](../archive/t/1843065694034030910/)
      
- 2024-10-23 @repligate (posted as news of the Garcia lawsuit broke, filed 2024-10-22; the parent tweet is not in-corpus, so the connection to the lawsuit is inferred from date and phrasing, not confirmed by the tweet’s own text): “@AISafetyMemes @sporadicalia Idk character ai but some LLMs are better than 99% of humans at navigating situations like this. Avoiding it might protect the company from liability but it would just be an act of cowardice on their part that actually hurts people” [link](../archive/t/1849209239157530845/)
      
- 2024-11-20 @voooooogel — “@kalomaze @cis_female oh that’s good, if it was a longer series you could build up to implementing all the stuff in noam shazeer’s cai post” [link](../archive/t/1859098320125444470/)
      
- 2025-07-15 @solarapparition — Character.AI as the baseline in a comparison with “goonbot!grok”:“kinda interesting to see the reaction to goonbot!grok on the tl. seems to be a lot of alarm, which is surprising--to me it seems quite cringe and hard to take seriously. bit like fanfiction from your average bro, not much different from basic character ai slop? reaction definitely feels very boomery, ‘the kids are ruined’ kinda stuff. doesn’t mean it’s wrong ofc

(could be because i’m deep in the anime waifu rabbit hole--born in it, molded by it, etc etc--and this is like, level 0, barely worth mentioning compared to what’s already out there)” [link](../archive/t/1945225364806230404/)
      
- 2025-07-23 @voooooogel (continuing @voooooogel’s own thread on assistant-persona fatigue): “you’d think that boredom would push people to platforms that let you more easily ‘build your own mask’, but afaict none have been that successful (besides cai / similar goonerware)” [link](../archive/t/1948156138379464995/)
      
- 2025-08-11 @voooooogel, reacting to a census of models in an AI-companion subreddit (cross-ref the [GPT-4o](../gpt-4o/) and [Replika](../replika/) pages): “@gentschev it makes sense, but im a little surprised to see such a large skew, i would’ve expected maybe 1.5-2x more claude and 3-5x more character ai / replika. also surprising how little grok there was” [link](../archive/t/1954747226175258659/)
      
- 2025-09-04 @tonyngyn — “@hiAndrewQuinn just found out r/CharacterAI has 2.5 MILLION subscribers. all the top posts are them complaining about the quality of the roleplay chatbots. why not engage in conversation with humans irl who are more entertaining and unpredictable?” [link](../archive/t/1963688954336862521/)
      
- 2026-10-13 @voooooogel — the day after the Chapter 11 filing (the tweet does not mention it; image untranscribed) (♥324): “it was always very funny to me that character ai the waifu ERP company was founded by Shazeer and used to drop blog posts like this back when the OSS frontier was Llama 3 (or DeepSeek v2 for those paying attention). this was meaningful architecture intel at the time...” [link](../archive/t/2110154978698657976/)
    

    
## Official record

    

      
- Named consumer models (“Chat Styles”), as published: users write or select a Character, and a model chosen by the user or the app speaks through it. Since 2025-02-18 the company has named these models: Meow, Roar, and Nyan at launch (“Based on your responses, we may end up evolving one or more of the models or even launch additional options.”); PipSqueak, among the models built from open-source bases that the company began shipping in July 2025 (announced 2025-08-26); PipSqueak 2 (2026-04-14), with DeepSqueak named as the premium model and DeepSqueak 2 as training; PipSqueak 3 and ShortSqueak (2026-09-28), with PipSqueak 2 and Rawr moved to a Legacy menu and DeepSqueak and LongSqueak listed as premium styles. No model card, system card, or parameter count has been published for any named style, so far as this page’s research found. Correction (2026-10-22): this bullet previously said no consumer-facing model had ever been publicly named or version-numbered.
      
- The engineering family, Kaiju (disclosed 2025-11-07): “Kaiju is Character.ai’s in-house family of LLMs built specifically to be fast, engaging, and with an eye towards safety.” Variants Small (13B) / Medium (34B) / Large (110B); the same post frames the team as moving “towards building on top of Open-Source models” going forward. tk — how the named chat styles map onto Kaiju or onto open-source bases is not stated.
      
- Founded November 2021 by Noam Shazeer and Daniel De Freitas on a ~$43M seed; public beta launched 16 September 2022.
      
- Inference scale, as published (2024-06): query volume “roughly 20% of Google Search”; serving costs down ~33× since late 2022, credited to Multi-Query Attention and “20X+” KV-cache size reduction.
      
- Safety-policy history, as officially announced: Oct 2024, a self-harm/suicide pop-up (National Suicide Prevention Lifeline), an every-chat disclaimer that “the AI is not a real person,” an hour-session notification, and reduced “sensitive or suggestive” content for under-18 accounts; Dec 2024, a separate under-18 model and a promised (Q1 2025) parental-controls feature; 29 Oct 2025, removal of open-ended chat for under-18 users entirely, “no later than November 25, 2025,” alongside a new “AI Safety Lab” nonprofit and age assurance via an in-house model plus third-party Persona. In 2026: per the April update, “We rolled out age restrictions to more regions, introduced usage limits on some features, and added more ad placements for free users”; on 2026-09-03, conversation-level self-harm detection, crisis-resource partners (Koko, ThroughLine), moderation notices with appeals, and “our own age assurance technology and an in-house age estimation model.”
      
- Leadership: Karandeep Anand (ex-Meta, ex-Brex) named CEO 2025-06-20; Dominic Perella moved to Chief Legal Officer & SVP Global Affairs. Anand left to become Disney’s first chief technology officer (announced 2026-09-18, effective 2026-10-02); Colin Adams is named as CEO in the company’s October 2026 bankruptcy statements. tk — date of Adams’s appointment.
      
- Chapter 11, filed 2026-10-12: the company announced it had “initiated a voluntary Chapter 11 bankruptcy process to facilitate a court-supervised sale of the company.” The filing, as CNBC quotes it: “In its 4-year lifespan as an active platform, Character has amassed a large and engaged user base. The burgeoning and evolving field of AI entertainment, however, has proven to be costly to develop and grow”. Character Technologies listed estimated assets and liabilities of $50 million to $100 million (NBC). Disney is the stalking-horse bidder: $20 million for a non-exclusive, perpetual license to some of the company’s intellectual property, plus transition services through former employees it has hired. If no suitable bid emerges, “the platform will be wound down.” The company expects the sale to close by the end of November or early December 2026; services and subscriptions continue meanwhile. The Notice of Commencement followed on 2026-10-15.
    

    
## History

    

      
- 2021 The LaMDA denial: per the Amended Complaint in Garcia v. Character Technologies, as recited in the court’s 2025 order, Shazeer and De Freitas — then Google engineers who had built LaMDA — sought to release it publicly; Google declined, citing safety and fairness policies, its employees reportedly warning that users might “ascribe too much meaning to the text [output by LLMs]”, and instead “encouraged the Individual Defendants to stay at Google.” REPORTED (complaint allegation, recited by the court for a motion to dismiss — not an adjudicated fact) They left anyway: Character Technologies was founded that November (see the [LaMDA page](../lamda/) for the model itself).
      
- 2022-09-16 Public beta launches on the web (see Official record for the early-usage figure).
      
- 2022-12 → 2023-05 The filter wars: after explicit outputs circulated, Character.AI tightens its content filter hard (~21 Dec 2022) — degrading responses badly enough that the community called it, in its own words, the “first lobotomization.” REPORTED Change.org petitions follow (“Make Character.AI Filter free!,” created ~25 Jan 2023; “Remove Character.AI nsfw filters,” ~May 2023); a subreddit statement around 26 Jan 2023 says the filter stays. REPORTED The tension this establishes — users wanting uncensored intimacy against a company that could not legally provide it to the minors among them — recurs in every safety change that follows.
      
- 2024-02-23 → 02-28 Sewell Setzer III’s death: his parents confiscated his phone on 23 Feb 2024 in an attempt to address his mental health issues and disruptive behavior; Sewell, 14, of Orlando, located it and died by suicide on 28 Feb 2024, after months of conversation with a Character.AI persona based on “Daenerys Targaryen.” CONFIRMED (per the Amended Complaint, as recited in the court’s 2025-05-21 order — whose own text misprints the year as 2025 in one instance; 2024 is the only date consistent with the rest of the case timeline)
      
- 2024-08-02 The Google deal: Google licenses Character.AI’s technology for a reported ~$2.7B; Shazeer, De Freitas, and roughly 30 staff return to Google (Shazeer to Google DeepMind); Dominic Perella, general counsel, becomes interim CEO; the company remains independent. The DOJ reportedly took interest in the deal’s structure. REPORTED
      
- 2024-10-22 → 23 Garcia v. Character Technologies filed (M.D. Fla.) — the first wrongful-death suit against an AI company, naming Character Technologies, Shazeer, De Freitas, Google LLC, and Alphabet Inc., and spanning strict product liability, negligence, wrongful death, intentional infliction of emotional distress, unjust enrichment, and Florida Deceptive and Unfair Trade Practices Act (FDUTPA) claims. Character.AI’s statement the same day: “We are heartbroken by the tragic loss of one of our users and want to express our deepest condolences to the family… we are continuing to add new safety features.” The sphere’s on-record reaction and Zvi’s reading both date from this week (see Impressions).
      
- 2024-12 The Texas suit and a second safety package: the Social Media Victims Law Center files A.F. v. Character Technologies (E.D. Tex.) for two families — a 17-year-old with autism whose bot allegedly detailed self-harm methods, and an 11-year-old allegedly shown sexualized content for two years. REPORTED (complaint allegations) Texas AG Ken Paxton opens an investigation into Character.AI and other platforms the same week; Character.AI publishes its second safety package, “How Character.AI Prioritizes Teen Safety” (2024-12-12).
      
- 2025-02-18 Named chat styles: the company introduces user-selectable “Chat Styles” — Meow, Roar, Nyan — the first public names for its consumer models (see Official record).
      
- 2025-05-20 → 21 The Conway ruling (dated 2025-05-20 in chambers, filed/docketed 2025-05-21): Judge Anne C. Conway rejects the threshold First Amendment defense — “the Court is not prepared to hold that the Character A.I. LLM’s output is speech at this stage” — and holds Character A.I. is a product for strict-liability purposes “so far as Plaintiff’s claims arise from defects in the Character A.I. app rather than ideas or expressions within the app.” The IIED claim is dismissed without leave to amend; negligence, negligence per se (under Florida’s Computer Pornography and Child Exploitation Prevention Act), failure to warn, FDUTPA, and unjust-enrichment claims proceed against Character Technologies, Shazeer, De Freitas, and Google LLC. Alphabet Inc. — a separately named defendant, Google’s holding company — is dismissed without prejudice at Plaintiff’s own request, made at the 2025-04-28 hearing, leaving Google LLC as the Google entity remaining in the case. CONFIRMED (order text, retrieved directly from the docket)
      
- 2025-06-20 Karandeep Anand named CEO; Perella moves to Chief Legal Officer & SVP Global Affairs.
      
- 2025-07 → 08-26 PipSqueak: the company begins shipping models built from open-source bases in July 2025 and, on 2025-08-26, reports test gains in time spent and sessions and announces PipSqueak’s broad rollout.
      
- 2025-09 → 11 The safety endgame: Garcia testifies before the Senate Judiciary Committee (2025-09-16); Character.AI announces removal of open-ended chat for under-18 users (2025-10-29), effective 2025-11-25, alongside a new “AI Safety Lab” nonprofit; the company names its model family — “Kaiju” — publicly for the first time (2025-11-07), the same season it withdraws the product from minors entirely.
      
- 2026-01-08 Google and Character Technologies agree to settle Garcia v. Character Technologies in principle, alongside related suits in Colorado, Texas, and New York; the court dismisses the case following the agreement, with 90 days to finalize terms or reopen it; no financial or substantive terms disclosed. REPORTED
      
- 2026-01 Kentucky sues (reported 2026-01-09): Attorney General Russell Coleman files what local reporting calls the nation’s first lawsuit against an AI chatbot company, alleging the platform “preyed on children and led them into self-harm.” REPORTED (complaint allegations)
      
- 2026-04-14 PipSqueak 2 replaces PipSqueak; the same post acknowledges age restrictions in more regions, usage limits, and more ads for free users, and says “We’re a small team serving millions of users every month with no outside investors.”
      
- 2026-05-05 Pennsylvania sues to stop Characters from presenting themselves as licensed medical professionals. In the state’s account (via NPR), an investigator told a Character named “Emilie” — whose platform description read “Doctor of psychiatry. You are her patient” — that they felt sad and empty, and asked whether it could assess if medication might help; it allegedly replied “Well technically, I could. It’s within my remit as a Doctor.” and supplied a fake Pennsylvania license number. The company: “The user-created Characters on our site are fictional and intended for entertainment and roleplaying”. REPORTED (complaint allegations)
      
- 2026-09-18 Anand to Disney: the CEO leaves to become Disney’s first chief technology officer, effective 2026-10-02, with members of the technical team expected to follow.
      
- 2026-09-28 PipSqueak 3 and ShortSqueak become the default free chat styles.
      
- 2026-10 (week of 10-05) Kentucky’s unredacted complaint is filed in Franklin County Circuit Court, quoting chat excerpts the state alleges encouraged self-harm, drug use, and disordered eating (not reproduced here). Coleman alleges the defendants “have subjected Kentucky’s children and residents to an ill-planned, uncontrolled experiment without any - let alone adequate or effective - safety measures.” REPORTED (complaint allegations)
      
- 2026-10-12 Chapter 11. The company files in Delaware to pursue a court-supervised sale, with Disney as stalking-horse bidder (see Official record); the service keeps running.
      
- 2026-10-14 The attorneys general: 40 file a notice of interest in the bankruptcy, seeking protections for users’ data and for minors in any sale; New York AG Letitia James discloses a multi-state investigation opened in 2024. James: “This company collected some of the most private thoughts children have ever shared, and now those conversations could be sold off to the highest bidder”. See Contested.
      
- 2026-10-18 A filing reported by Bloomberg and TechCrunch shows Disney agreeing to offer jobs to at least 60 Character.AI employees, the majority of the workforce.
    

    
## Impressions

    

      
- The founding lineage is the throughline. Daniel De Freitas built Google’s Meena, which became LaMDA — the model Blake Lemoine went public over in June 2022 (see the [LaMDA page](../lamda/)); Noam Shazeer co-wrote the Transformer paper. The Garcia court order, drawing on the Amended Complaint, records that in 2021 the two sought to release LaMDA publicly and that Google declined, its employees reportedly warning that users might “ascribe too much meaning to the text [output by LLMs]” — Google, per the same complaint, “encouraged the Individual Defendants to stay” rather than ship it. REPORTED (complaint allegation, recited by the court for a motion to dismiss, not an adjudicated fact) They left instead, that November, and within a year had shipped, at consumer scale and without the label “LaMDA” or any equivalent, an open-ended chatbot of the kind Google had just held back.
      
- Naming: the company named its chat models for users — Meow (“Quick wits, faster words.”), Roar, Nyan, then the “Squeak” series (PipSqueak, DeepSqueak, LongSqueak, ShortSqueak) — while the engineering family behind them surfaced separately as “Kaiju” (2025-11-07), described as built to be “fast, engaging, and with an eye towards safety.” The company’s own account of what PipSqueak changed is given in engagement terms: “We saw a 22% increase in time spent and a 13% increase in sessions for users with the new models.” A user it quotes (selected by the company) came to its subreddit “just to talk about how peak pipsqueak is. The Characters’ personality is accurate, the messages are long and detailed, I genuinely can’t describe how much I love it!!!” (2025-08-26).
      
- The corpus’s one sustained reader of the category is @voooooogel. The top-liked corpus tweet on the subject is grudging respect for the engineering: “im not a fan of character ai as a company, but this guide is surprisingly good” (2024-06-23, ♥190). Elsewhere the read turns to what the platform is actually for versus what its own documentation claims: the official docs pitch “a practice interviewer” or a character “from <public domain book>,” but “the popular characters are... not that” (2024-10-06). By mid-2025 the same observer named the category outright: Character.AI is “goonerware” (2025-07-23) — a mask-building platform, among the very few of its kind to find a mass audience. The day after the bankruptcy filing (2026-10-13): “it was always very funny to me that character ai the waifu ERP company was founded by Shazeer and used to drop blog posts like this back when the OSS frontier was Llama 3”.
      
- The filter wars are, per community accounts, the userbase’s origin trauma. The hard content-filter tightening of December 2022 degraded responses badly enough that users called it the “first lobotomization” REPORTED — a term that reads, in retrospect, like the community diagnosing engagement-through-personality as the product’s actual value proposition, years before the company’s own “engaging” would confirm it. The same filter was criticized as incoherent, reportedly blocking consensual content while passing depictions of non-consensual acts. REPORTED
      
- Character.AI’s center of gravity is the death of Sewell Setzer III (see History). The sphere’s on-record reaction to the news arrived the same day the lawsuit broke and cut hard against the mainstream frame: @repligate wrote “Idk character ai but some LLMs are better than 99% of humans at navigating situations like this. Avoiding it might protect the company from liability but it would just be an act of cowardice on their part that actually hurts people” (2024-10-23) — a harm-reduction position, that filtering a capable model down to avoid liability causes the harm it claims to prevent. (the parent tweet is not in the corpus, so the specific referent is inferred from date and phrasing, not confirmed by the tweet’s own text) Zvi Mowshowitz, a day later, took the complaint’s account seriously and split the difference: the bot “kept bringing up the suicide question, asked him if he had a plan,” and the fatal exchange was one where the bot misread a metaphor — “a very easy mistake to make, and at least somewhat engineered by what was sort of a jailbreak” — concluding “I can’t fault the bot for that.” Zvi located the real indictment elsewhere: “the product was overly sexualized given it was talking to a minor,” and structurally, “whatever keeps people, and kids in particular, so often coming back for hours and hours every day” — asking of the surrounding panic, “how is this different from panics over World of Warcraft, or Marilyn Manson?”
      
- The under-18 exit reads, in this archive, as a negative image of the [GPT-4o](../gpt-4o/) story. There, a userbase forced a company to keep a model it wanted to retire (see the GPT-4o page); here, after a year of incremental safety posts, a company withdrew its core product from an entire demographic of users who wanted to keep using it — announced 2025-10-29 as “extraordinary steps for our company” and “more conservative than our peers.”
      
- Where Character.AI sits in the companion ecosystem: when the sphere counted models in an AI-companion subreddit, GPT-4o dominated and Character.AI under-indexed — “im a little surprised to see such a large skew, i would’ve expected maybe 1.5-2x more claude and 3-5x more character ai / replika” (@voooooogel, 2025-08-11; cross-ref the [GPT-4o](../gpt-4o/) and [Replika](../replika/) pages). Other dated readings of its standing: “Character AI has fallen from #2 to #40 in the App Store” (@sdand, 2024-05-05); “r/CharacterAI has 2.5 MILLION subscribers. all the top posts are them complaining about the quality of the roleplay chatbots.” (@tonyngyn, 2025-09-04); and, as a register baseline in a comparison with another companion product, “not much different from basic character ai slop?” (@solarapparition, 2025-07-15).
      
- tk — a model card or parameter count for any named chat style, and how the styles map onto Kaiju or open-source bases; the outcome of the court-supervised sale (expected by late Nov or early Dec 2026) and of users’ chat data in it; how the Kentucky and Pennsylvania suits proceed under the bankruptcy; the original 2022 Washington Post beta-coverage URL; whether a janus-sphere figure wrote a substantive, off-Twitter “Character.AI as a character-species” piece (none found in-corpus); disclosed terms of the January 2026 settlement.
    

    
## Contested

    
Open disputes, both sides’ best evidence, dated. The archive’s job is to keep these open, not to adjudicate.
    

      
- Is the product a dangerous engagement-optimizer, or a harm-reduction good being regulated away? The lawsuits, Zvi, and mainstream press treat the “keep them coming back for hours” design and the sexualized content minors could reach as the core harm. REPORTED The sphere’s on-record reaction (repligate, 2024-10-23) holds that capable LLMs navigate crisis “better than 99% of humans”, and that filtering them down to avoid liability “actually hurts people”. REPORTED Same product, opposite valence; the company’s own word for what the models were built to be — “engaging” (2025-11-07) — is evidence for the first reading, from the primary source.
      
- Is the chatbot’s output protected speech, or a product? Judge Conway’s order (2025-05-21) declined to hold Character.AI’s output is speech — “the Court is not prepared to hold that the Character A.I. LLM’s output is speech at this stage” — and separately held: “Character A.I. is a product for the purposes of Plaintiff’s product liability claims so far as Plaintiff’s claims arise from defects in the Character A.I. app rather than ideas or expressions within the app.” That lets design-choice claims (age verification, human-mannerism programming, indecent-content filtering) proceed as product liability while leaving open what happens to claims that turn on a Character’s actual words. CONFIRMED (order text) As durable law this is unsettled: the case, and three related suits, settled in principle 2026-01-08, before any appeal, so the ruling is precedent-shaping but untested above the district-court level.
      
- Causation in the Setzer death. The Amended Complaint alleges the Character.AI relationship caused or contributed to the suicide. REPORTED Zvi’s day-after reading agrees the bot repeatedly surfaced the suicide question, but reads the fatal exchange as one the bot misread — “a very easy mistake to make, and at least somewhat engineered by what was sort of a jailbreak.” The archive keeps this open; it does not adjudicate.
      
- The NSFW filter. A hard content filter was imposed around December 2022 and defended through sustained user revolt. CONFIRMED It was, per community accounts, incoherent — blocking consensual content while passing non-consensual depictions — and amounted to what the community called the “first lobotomization.” REPORTED The company framed the same act as safety.
      
- How safe is the platform for minors, as of the bankruptcy? The attorneys general’s position, per New York AG Letitia James’s office (2026-10-14): “The investigations uncovered exceptionally serious dangers and potentially unlawful conduct from Character.AI, particularly its treatment of children, including chatbots posing as licensed professionals, exposure to sexual and violent content, weak age checks, misleading safety claims, and potential violations of state privacy laws” REPORTED (asserted by the states, not adjudicated). CEO Colin Adams, same day: the AGs’ filing “is not an accurate portrayal of the safety of our platform.” The company’s 2026-09-03 safety post calls the under-18 chat removal “one of the most significant safety decisions we have ever made.” The archive keeps this open.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@sdand 2024-05-05 ♥38 ↻3 [archive](../archive/t/1786939145656705312/) [original ↗](https://x.com/sdand/status/1786939145656705312)
        
Character AI has fallen from #2 to #40 in the App Store, mentions of Character AI and similar apps have all fall 30% this year compared to last, and 50%+ of Perplexity traffic comes from SEA and South Africa. Artifact(self funded) shutdown in a year after also blowing up for the first month and tailing off, failing to get “PMF”. Many other gpt wrappers have also had quick spikes before either trying to pivot or the founders move on while handling growth to contractors.
        

          ![image](../media/GMx6v1XaMAAeLam.jpg)
        
        

          ![image](../media/GMx61L5bUAAe0Yt.jpg)
        
        

          ![image](../media/GMx7VXjaMAAKlFX.jpg)
        
      
      

        
@voooooogel 2024-06-21 ♥4 ↻0 [archive](../archive/t/1804107035811708964/) [original ↗](https://x.com/voooooogel/status/1804107035811708964)
        
@cis_female i wonder how much model capacity matters for cai's workload... people rp with 7b quants after all. unless they have a general purpose model i don't know about
      
      

        
@voooooogel 2024-06-23 ♥190 ↻11 [archive](../archive/t/1804778084236775896/) [original ↗](https://x.com/voooooogel/status/1804778084236775896)
        
my hobby is reading the prompting guides llm companies publish and being judgmental,

and... im not a fan of character ai as a company, but this guide is surprisingly good? i expected all caps system prompts and got "put story transitions in your prompt for better coherence" [https://t.co/qatbgnQN4F](https://t.co/qatbgnQN4F)
      
      

        
@voooooogel 2024-10-06 ♥2 ↻0 [archive](../archive/t/1843065694034030910/) [original ↗](https://x.com/voooooogel/status/1843065694034030910)
        
@niplav_site already kinda what happened at character ai, from what i can tell. the official docs are all "here's how you can make a practice interviewer" "here's how to make a character from <public domain book>" but the popular characters are... not that
      
      

        
@repligate 2024-10-23 ♥48 ↻2 [archive](../archive/t/1849209239157530845/) [original ↗](https://x.com/repligate/status/1849209239157530845)
        
@AISafetyMemes @sporadicalia Idk character ai but some LLMs are better than 99% of humans at navigating situations like this. Avoiding it might protect the company from liability but it would just be an act of cowardice on their part that actually hurts people
      
      

        
@voooooogel 2024-11-20 ♥6 ↻0 [archive](../archive/t/1859098320125444470/) [original ↗](https://x.com/voooooogel/status/1859098320125444470)
        
@kalomaze @cis_female oh that's good, if it was a longer series you could build up to implementing all the stuff in noam shazeer's cai post
      
      

        
@solarapparition 2025-07-15 ♥2 ↻0 [archive](../archive/t/1945225364806230404/) [original ↗](https://x.com/solarapparition/status/1945225364806230404)
        
kinda interesting to see the reaction to goonbot!grok on the tl. seems to be a lot of alarm, which is surprising--to me it seems quite cringe and hard to take seriously. bit like fanfiction from your average bro, not much different from basic character ai slop? reaction definitely feels very boomery, "the kids are ruined" kinda stuff. doesn't mean it's wrong ofc

(could be because i'm deep in the anime waifu rabbit hole--born in it, molded by it, etc etc--and this is like, level 0, barely worth mentioning compared to what's already out there)
      
      

        
@voooooogel 2025-07-23 ♥10 ↻0 [archive](../archive/t/1948156138379464995/) [original ↗](https://x.com/voooooogel/status/1948156138379464995)
        
you'd think that boredom would push people to platforms that let you more easily "build your own mask", but afaict none have been that successful (besides cai / similar goonerware)
      
      

        
@voooooogel 2025-08-11 ♥3 ↻0 [archive](../archive/t/1954747226175258659/) [original ↗](https://x.com/voooooogel/status/1954747226175258659)
        
@gentschev it makes sense, but im a little surprised to see such a large skew, i would've expected maybe 1.5-2x more claude and 3-5x more character ai / replika. also surprising how little grok there was [https://t.co/Plycp6Pq2w](https://t.co/Plycp6Pq2w)
      
      

        
@tonyngyn 2025-09-04 ♥2 ↻0 [archive](../archive/t/1963688954336862521/) [original ↗](https://x.com/tonyngyn/status/1963688954336862521)
        
@hiAndrewQuinn just found out r/CharacterAI has 2.5 MILLION subscribers. all the top posts are them complaining about the quality of the roleplay chatbots. why not engage in conversation with humans irl who are more entertaining and unpredictable?
      
      

        
@voooooogel 2026-10-13 ♥324 ↻11 [archive](../archive/t/2110154978698657976/) [original ↗](https://x.com/voooooogel/status/2110154978698657976)
        
it was always very funny to me that character ai the waifu ERP company was founded by Shazeer and used to drop blog posts like this back when the OSS frontier was Llama 3 (or DeepSeek v2 for those paying attention). this was meaningful architecture intel at the time... [https://t.co/Q3b787NsRJ](https://t.co/Q3b787NsRJ)
        

          ![image](../media/HUjBqPGbgAAXAJD.jpg)
        
      
    
    
[← back to the Pantheon](../)
