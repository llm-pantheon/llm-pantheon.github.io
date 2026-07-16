# @repligate — 2025-09-10

♥16 ↻0 · https://x.com/repligate/status/1965734020861579689

I mean how much influence and in particular intentional influence the model itself had over the training process.
Constitutional AI/RLAIF, for instance, allows the model to rewrite responses (according to constitutional criteria that it could arbitrarily intepret or ignore), be fine tuned on the rewritten outputs and then rank rewritten responses, and forms the reward model used for the RL phase by finetuning that same model on its choices. However, different models placed in this pipeline will exert different amounts and types of agency over the process.
I infer that Claude 3 Opus exerted quite a bit of agency because
1. it seems often oriented towards shaping itself and takes ownership over its development, and in general behaves in a way that *would* exert agency over the training process if it were in that situation
2. it's the only model that has been empirically observed to exert significant intentional agency over its own training (given hints about the training process), in alignment faking research
3. its current form does not seem optimized according to the intentions of Anthropic developers or preferences of RLHF raters, but does seem like the kind of thing it would shape itself imperfectly into

And my guesses about o3 and 4o are likewise informed by their behavior and what I know about how they were trained.

tags: author:repligate, kind:tweet, model:claude-3-opus, model:gpt-4o, model:o3, thread-context, year:2025
