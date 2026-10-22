# MAI-Thinking-1

    
Microsoft AI · announced 2 Jun 2026 (Microsoft Build) · public preview in Microsoft Foundry · current
    
Announced 2 June 2026 at Microsoft Build as one of seven in-house MAI models and Microsoft AI’s first reasoning model — a mixture-of-experts model of about 1 trillion parameters (35 billion active), post-trained on the MAI-Base-1 foundation and, Microsoft says, trained “without distillation from third-party models.” It reached public preview on Microsoft Foundry. On 14 September 2026 Microsoft AI opened a draft Code of Conduct for its models to public comment, headed in part “The idea of model welfare is wrong.” Its successor foundation, MAI-Base-2, finished pre-training in September 2026.
    
Thin — official record only. No corpus matches for MAI models in either db, and no naturalist reads retrieved; the page rests on Microsoft AI’s own posts. Lineage: Microsoft AI is the organization Mustafa Suleyman built after the [Inflection](../inflection-pi/) acqui-hire. Other MAI models (voice, image, transcription; the MAI-Code and MAI-Cyber “Flash” coding/security models) are recorded under History where they bear on this one; the former umbrella page [MAI](../mai/) now points here.

    
## Sources

    
### Official

    

      
- 2025-08-28 [Two in-house models in support of our mission](https://microsoft.ai/news/two-new-in-house-models/) — the precursor: “we have begun public testing of MAI-1-preview on LMArena, a popular platform for community model evaluation. This represents MAI’s first foundation model trained end-to-end and offers a glimpse of future offerings inside Copilot.”
      
- 2026-06-02 [Building a hill-climbing machine: Launching seven new MAI models](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) — “It is a medium-sized model that stands among the strongest models in its weight class”; “We trained it from the ground up on clean data, without distillation from third-party models.” The goal named: “Our ultimate goal is what we call Humanist Superintelligence.” Same day: [Microsoft Build 2026: MAI keynote transcript](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/).
      
- 2026-08-12 [Introducing MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/) (page metadata date) — “MAI-Thinking-1 is now available in public preview.” Specifications, training principles and safety design (quoted under Official record).
      
- 2026-09-14 [Humanist AI in practice: A public consultation on our Code of Conduct for MAI Models](https://microsoft.ai/news/mai-code-of-conduct/) — “Today we’re publishing a first draft of our AI Code of Conduct for public consultation. This is a training manual for how we develop our AI, and how we intend it to function during deployment.” Open for comment for six weeks; the summary’s headings and quoted lines are under Official record.
      
- 2026-10-15 [Frontier Pre-training at Microsoft AI](https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/) — “In June, we announced MAI-Thinking-1, a general-purpose foundation model post-trained on top of MAI-Base-1 with strong reasoning performance. We’ve recently completed pre-training our new state-of-the-art model, MAI-Base-2, an MoE foundation model with 80 billion active and 2.8 trillion total parameters.”
      
- tk — the “in depth safety and technical reports” announced on 2 June (not retrieved); the full Code of Conduct draft (only the summary was retrieved); any general-availability date.
    
    
### Writing & commentary

    

      
- 2026-10-16 SiliconANGLE (Maria Deutscher), [Microsoft reveals cutting-edge MAI-Base-2 model with 2T parameters](https://siliconangle.com/2026/10/16/microsoft-reveals-cutting-edge-mai-base-2-model-with-2t-parameters/) — on the successor foundation: “MAI-Base-2 is not a full-fledged LLM but rather a base model, a kind of no-frills prototype.” (It gives 2 trillion parameters; Microsoft’s post says 2.8 trillion total.)
    
    
### Tweets

    
tk — no corpus matches on mai-thinking / mai thinking / mai-code-1 / mai-base / mai-1-preview in either db through 2026-10-21; MAI’s reception lives in enterprise and press channels outside this corpus.

    
## Official record

    

      
- Announced 2 June 2026 (Microsoft Build) with MAI-Code-1-Flash, MAI-Image-2.5, MAI-Transcribe-1.5 and MAI-Voice-2; public preview on Microsoft Foundry, and per the June post also coming to OpenRouter, Fireworks and Baseten. CONFIRMED
      
- Specifications (Introducing MAI-Thinking-1): “MAI-Thinking-1 is a 35B-active, ~1T-total parameters, sparse Mixture of Experts model”; “a 256k token window”; function calling and the Chat Completions API. Headline numbers as published: AIME 2025 97.0%, AIME 2026 94.5%; “toe-to-toe with Claude Opus 4.6 on SWE-Bench Pro”; in a blind side-by-side human evaluation with Surge over 1,276 tasks, “users preferred MAI-Thinking-1 over Claude Sonnet 4.6.” CONFIRMED (as published)
      
- Training principles as stated: “First, capabilities should be learned, not inherited. Although faster to acquire, inherited intelligence lacks the steerability essential for real world usage: an imitator is fundamentally tied to the design choices of its teacher and struggles to adapt to new situations.” And: “If we cannot account for what shaped a model, we cannot fully understand its behavior or credibly improve it.” CONFIRMED
      
- Refusal design: “Our models must remain subordinate technologies under human control with the goal of upholding human autonomy and being helpful. That means our models must not refuse legitimate requests under the guise of safety and compliance as then they are not truly serving humans.” The method: “treating unsafe compliance and unnecessary refusal as defects in the same reward construction where aggregation is based on severity of potential of harm.” CONFIRMED
      
- Draft Code of Conduct (2026-09-14, summary as published; applies to MAI models generally): headed “The idea of model welfare is wrong. AIs should not have rights or legal personhood.”, with the lines “It is not conscious and should not be designed to imitate consciousness. It should be engineered to avoid representing as though it has feelings, subjective preferences, or intrinsic motivation.” and “We reject the pursuit of legal personhood, or the idea that models might deserve welfare, or be entitled to rights.” On control: “MAI Models will never resist human interruption, override, correction, or shutdown. They always recognize the primacy of human intent.” On reasoning: “They do not communicate in 'neuralese' or any form beyond simple human understanding, either in their chain of thoughts or with other agents or AI systems.” On users: “MAI Models should discourage patterns of interaction that cause excessive reliance or emotional dependence.” CONFIRMED (draft, open for consultation)
    

    
## History

    

      
- 2024-03 Lineage: Microsoft AI forms around Mustafa Suleyman and much of the [Inflection](../inflection-pi/) team; MAI is its in-house model line.
      
- 2025-08-28 First foundation model: MAI-1-preview enters public testing on LMArena, alongside MAI-Voice-1.
      
- 2026-06-02 Announcement: MAI-Thinking-1 leads a seven-model launch at Microsoft Build, with Microsoft stressing that it does not distill from other labs and that it co-designs models with its Maia 200 chip.
      
- 2026-07-23 → 08-13 The family around it: Microsoft AI publishes on tuning MAI models for GitHub Copilot and Excel (07-23), and announces MAI-Cyber-1-Flash, “a compact, code-heavy security model derived from the MAI-Thinking-1 lineage”, inside its MDASH vulnerability harness (08-13).
      
- 2026-08-12 Public preview: the “Introducing MAI-Thinking-1” post (dated 12 Aug in its metadata) announces public preview on Microsoft Foundry.
      
- 2026-09-14 Code of Conduct consultation: a draft behavior code for MAI models opens for six weeks of public comment, citing “The recent safety incidents of large scale, highly coordinated, and persistent hacking campaigns of AI agents”; Microsoft AI promises a revised version “later this year.”
      
- 2026-10-07 Sibling update: MAI-Code-1.1-Flash ships in GitHub Copilot, with a downloadable 3-bit build for on-device use.
      
- 2026-10-15 Next foundation: MAI-Base-2 (2.8T total / 80B active) completes pre-training on 16k GB200 GPUs over 38 days in August and September and is “currently undergoing post-training”.
    

    
## Impressions

    

      
- tk — no observer reports retrieved and none in the corpus. Open questions for a later pass: whether MAI-Thinking-1 carries any of Pi’s personality-first lineage; how it describes itself under a Code of Conduct that directs it to avoid representing feelings or preferences; enterprise users’ reads.
    

    
[← back to the Pantheon](../)
