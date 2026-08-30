# Grok-1

    
xAI · announced 3 Nov 2023 (chatbot early access from Dec 2023) · base model open-sourced under Apache 2.0 on 17 Mar 2024 · superseded by [Grok-1.5](../grok-1-5/) (29 Mar 2024)
    
xAI’s first large language model — announced 3 November 2023 as the system behind the Grok chatbot, an assistant built with a deliberate “rebellious streak” and pitched to answer “spicy questions that are rejected by most other AI systems,” with early access rolling out to X Premium+ subscribers that December. On 17 March 2024, days after Elon Musk sued OpenAI over its closed models, xAI released Grok-1’s base weights and network architecture under the Apache 2.0 license — a 314-billion-parameter Mixture-of-Experts checkpoint from an October 2023 pretraining run, not fine-tuned for dialogue, and reported at release as the largest open-weights model to date. Grok-1.5 superseded it later that month.
    
Sourcing skew, named: the janus corpus that carries most of this site barely touches Grok-1 — a direct search of both archive dbs returns no substantive Grok-1 material (the one literal match is a comedic 2025 list-tweet naming some eighty models in passing). This page is therefore web-carried: the record rests on xAI’s own announcements and contemporaneous press, and the Tweets layer is essentially absent, marked tk below rather than padded. Two objects are easily conflated and kept apart here: Grok-1 the base model — the raw pretraining checkpoint xAI open-sourced — and Grok the chatbot it powered, the fine-tuned product X Premium+ users talked to; the released weights are the former, and were never tuned for the “spicy” dialogue persona the product became known for.

    
## Sources

    
### Official

    

      
- 2023-11-03 [Announcing Grok](https://x.ai/news/grok) (xAI) — the launch post. Grok “is designed to answer questions with a bit of wit and has a rebellious streak, so please don’t use it if you hate humor!”, is “modeled after the Hitchhiker’s Guide to the Galaxy,” and “will also answer spicy questions that are rejected by most other AI systems.” Notes “real-time knowledge of the world via the 𝕏 platform” and describes the model as “the best we could do with 2 months of training.” Introduces the 33B prototype Grok-0 and Grok-1’s benchmark table (Official record, below).
      
- 2023-11-03 TechCrunch, [Musk says X subscribers will get early access to xAI’s chatbot, Grok](https://techcrunch.com/2023/11/03/musk-says-twitter-subscribers-will-get-early-access-to-xais-chatbot-grok/) — the same-day report that Grok would be gated to X Premium+ subscribers.
      
- 2023-12-07 → 12-08 TechCrunch, [X begins rolling out Grok, its ‘rebellious’ chatbot, to subscribers](https://techcrunch.com/2023/12/07/x-begins-rolling-out-grok-its-rebellious-chatbot-to-subscribers/) — the chatbot reaches all US X Premium+ subscribers ($16/mo).
      
- 2024-03-17 [Open Release of Grok-1](https://x.ai/news/grok-os) (xAI) — “We are releasing the base model weights and network architecture of Grok-1.” “This is the raw base model checkpoint from the Grok-1 pre-training phase, which concluded in October 2023.” The model is “not fine-tuned for any specific application, such as dialogue”; a “314B parameter Mixture-of-Experts model with 25% of the weights active on a given token,” released under the Apache 2.0 license.
      
- 2024-03-17 [xai-org/grok-1](https://github.com/xai-org/grok-1) (GitHub) — JAX reference code and weights (torrent magnet link + HuggingFace xai-org/grok-1). Architecture as documented: 64 layers, 8 experts (2 active per token), 48 query / 8 key-value heads, 6,144 embedding dimension, SentencePiece tokenizer (131,072 tokens), rotary embeddings, 8,192-token context. “The code and associated Grok-1 weights in this release are licensed under the Apache 2.0 license”; the repo cautions that “The implementation of the MoE layer in this repository is not efficient.”
    
    
### Writing & commentary

    

      
- 2024-03-11 The National, [Elon Musk says xAI’s Grok will become open source and calls OpenAI ‘a lie’](https://www.thenationalnews.com/business/technology/2024/03/11/elon-musk-says-xais-grok-will-become-open-source-and-calls-openai-a-lie/) — reports Musk’s post that xAI would open-source Grok “this week” and his calling OpenAI “a lie,” set against his 29 February 2024 lawsuit over OpenAI’s closed models.
      
- 2024-03-17 Simon Willison, [Grok-1](https://simonwillison.net/2024/Mar/17/grok-1/) — the day-of technical write-up: a “314B parameter Mixture-of-Experts model with 25% of the weights active on a given token,” xAI “released their Grok-1 model under an Apache 2 license (for both weights and code),” the base checkpoint “not fine-tuned for any particular task,” “distributed as a 318.24G torrent file.”
      
- 2024-03 The Decoder, [Elon Musk’s xAI releases Grok-1, the largest open source mixture-of-experts model to date](https://the-decoder.com/elon-musks-xai-releases-grok-1-the-largest-open-source-mixture-of-experts-model-to-date/) — frames the release as the largest open-source MoE to that point; notes the raw base checkpoint is unaligned (no RLHF) and reads the timing as a response to the OpenAI suit.
      
- 2024-03 TechRadar, [Elon Musk’s Grok chatbot is going open source, but maybe not for the right reasons](https://www.techradar.com/pro/elon-musks-grok-chatbot-is-going-open-source-but-maybe-not-for-the-right-reasons) — the skeptical read on the motive.
      
- reference [Grok (chatbot) — Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot)) — running timeline (Nov 2023 announcement, Dec 2023 rollout, 17 Mar 2024 open release, Grok-1.5 succession).
    
    
### Tweets

    
A direct search of both archive dbs — janus-corpus-v2 (137k tweets) and the community-archive supplement (~12k) — returns no substantive Grok-1 material. The single literal “Grok-1” match is a comedic 2025 list-tweet naming some eighty models in passing, not evidence about this model. Grok-1’s late-2023 / early-2024 audience lived on X-at-large and in the tech press, before the naturalist circle this corpus samples turned its attention to xAI’s models (that engagement begins around [Grok 3](../grok-3/), February 2025). The Tweets layer here is absent, not merely unwritten — there are no records to reproduce below.
    
tk — contemporaneous first-person reactions to the open-weights release (developers who downloaded and ran the base model); any archived xAI/Musk posts around the 11 Mar 2024 open-source announcement and the 17 Mar release, if a citable permalink surfaces.

    
## Official record

    

      
- Announced 3 November 2023 as xAI’s first LLM and the model behind the Grok chatbot. It followed a 33-billion-parameter prototype, Grok-0, which xAI said “approaches LLaMA 2 (70B) capabilities on standard LM benchmarks but uses only half of its training resources.” Grok-1 itself was described as “the best we could do with 2 months of training.” CONFIRMED (as published)
      
- Headline benchmarks as published by xAI (Nov 2023): GSM8k 62.9%, MMLU 73.0%, HumanEval 63.2%, MATH 23.9% — xAI said Grok-1 was “surpassing all other models in its compute class, including ChatGPT-3.5 and Inflection-1,” while behind GPT-4 and other models trained with far more data and compute. CONFIRMED (claims as published)
      
- Deployed via the Grok chatbot on X, with real-time retrieval over the platform: early access from Nov 2023, reaching all US X Premium+ subscribers ($16/mo) by 8 December 2023, and extended to X Premium (not only Premium+) on 26 March 2024. CONFIRMED
      
- Open release, 17 March 2024: base model weights and network architecture under Apache 2.0. A 314B-parameter Mixture-of-Experts model, 25% of weights active per token (2 of 8 experts); 64 layers; 8,192-token context; SentencePiece tokenizer (131,072 tokens). The “raw base model checkpoint” from a pretraining phase that “concluded in October 2023,” “not fine-tuned for any specific application, such as dialogue.” Distributed as a ~318 GB torrent and on HuggingFace (xai-org/grok-1) with JAX example code. CONFIRMED
      
- Succession: superseded by [Grok-1.5](../grok-1-5/) (announced 29 March 2024; 128K context), then [Grok-2](../grok-2/) (Aug 2024); the line continues through [Grok 3](../grok-3/) and [Grok 4](../grok-4/). No formal deprecation applies to the open checkpoint — Apache-2.0 weights, once released, stay available. CONFIRMED
    

    
## History

    

      
- 2023-11-03 Announcement. xAI — founded July 2023 — unveiled Grok into a field defined by ChatGPT and Claude, positioning it on two axes competitors mostly avoided: a comedic, “rebellious” persona and a stated willingness to field “spicy questions.” Real-time access to X was the pitched differentiator. Musk said X Premium+ subscribers would get early access.
      
- 2023-12-07 → 12-08 Rollout. Grok reached all US X Premium+ subscribers over two days; Musk said English-language users elsewhere would follow within about a week.
      
- 2024-02-29 The lawsuit. Musk sued OpenAI and Sam Altman, alleging the company had abandoned its founding open mission by keeping GPT-4 closed — the backdrop against which the Grok open-release is usually read.
      
- 2024-03-11 “This week, xAI will open source Grok.” Musk announced the coming release on X and, the same week, called OpenAI “a lie” (The National). Commentary split immediately over motive — principle versus a low-cost jab at a closed rival (see Contested).
      
- 2024-03-17 Open release. xAI published the Grok-1 base weights and architecture under Apache 2.0 at [xai-org/grok-1](https://github.com/xai-org/grok-1) — the largest open-weights model released to that point, per contemporaneous reporting. Practitioner reception was muted by practicalities: at 314B parameters, a ~318 GB download needing on the order of hundreds of gigabytes of accelerator memory, few could run it, and the released artifact was the unaligned base checkpoint rather than the chatbot people had used (Willison; The Decoder).
      
- 2024-03-26 → 03-29 Handoff. The chatbot opened to X Premium; days later, on 29 March, xAI announced [Grok-1.5](../grok-1-5/) (128K context, stronger reasoning), and Grok-1 as a deployed model was superseded — the open weights outliving the product generation that produced them.
    

    
## Impressions

    

      
- Reception of the open release, read practically: the dominant note among named commentators was that the release mattered more as an event than as a usable model. Simon Willison catalogued it plainly — a base checkpoint “not fine-tuned for any particular task,” “distributed as a 318.24G torrent file” — the implicit point being that almost no one could load it. The Decoder framed it as the largest open-source MoE to date while noting the raw checkpoint was unaligned (no RLHF). The enthusiasm was for the precedent, not the weights.
      
- The persona that wasn’t in the box: the character Grok was marketed on — the “rebellious streak,” the “spicy questions,” the Hitchhiker’s-Guide voice — belonged to the fine-tuned chatbot, not to the artifact xAI open-sourced. By xAI’s own description the released weights were the pretraining checkpoint, “not fine-tuned for any specific application, such as dialogue.” So Grok-1 as an open-weights object has, strictly, no observed conversational character — the “spicy” reputation attaches to a deployment, not to the model this page documents as released.
      
- On motive: because the announcement landed eleven days after the OpenAI suit, much of the commentary read the open-sourcing as argument-by-example against closed AI as much as a technical contribution — TechRadar’s “maybe not for the right reasons” is the representative skeptical line, while xAI and Musk framed it as the open mission OpenAI had abandoned. The archive keeps that gap open (see Contested).
      
- tk — the naturalist / character layer is genuinely empty for Grok-1: the janus-sphere observers who later read Grok 3 and Grok 4 closely did not engage this model, and no first-person elicitation record survives in the corpus. First-hand accounts of running the open weights (outputs, quirks of the un-fine-tuned base model) would be the missing evidence; none is collected here yet.
    

    
## Contested

    
Open disputes, both sides’ best evidence, dated. The archive’s job is to keep these open, not to adjudicate.
    

      
- Why was Grok-1 open-sourced? The timing is not in dispute: Musk sued OpenAI on 29 February 2024 over its closed models; announced the open-sourcing on 11 March; released on 17 March. CONFIRMED The principled reading (xAI / Musk): the release enacted the open mission Musk accused OpenAI of abandoning — hence “OpenAI is a lie” the same week. REPORTED The skeptical reading (press): a low-cost move — the released base checkpoint was already outclassed by GPT-4-tier systems and too large for most to run, so open-sourcing cost xAI little competitively while scoring a rhetorical point (TechRadar, “maybe not for the right reasons”; The Decoder ties the timing to the suit). REPORTED Both readings fit the same facts; the archive does not choose between them.
    

    
    

    
[← back to the Pantheon](../)
