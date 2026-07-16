# @voooooogel — 2025-11-30

♥16 ↻1 · https://x.com/voooooogel/status/1995021640560959536

sort of tangential, but i wonder how much of RL "not memorizing" / other training memorizing is just user message masking? afaik it's usual practice to mask environment responses (~user messages) in RL training, where in SFT it varies, and in pretraining obviously the distinction doesn't exist. (even with masked user messages, some signal on those tokens can still come through KV of course, but it's going to be weaker than directly training those tokens.)

in RL, a lot of what the model would want to verbatim memorize would be in the user messages^1 - specs, situational awareness, etc. since those messages are masked, one way for a model to accomplish this - either by happenstance or intentionally - would be to copy chunks of the desired-to-memorize text into its own messages.

that would match up with what @CFGeek mentioned in the other subthread about deliberative alignment - perhaps openai's models can quote spans of text that they happened to copy into their own reasoning during training, but if this happened infrequently, and not over the whole document, it would make sense those quotes vary somewhat in wording and the models can't quote the whole spec verbatim.

[1] and a lot would be in its own messages, too - but actually, that stuff seems to be straightforwardly memorized, people just don't think of it as memorization? RL tool use "motor movements," CoT structures, reflexive refusals, etc. all behave like memorized strings, just initially sampled from the policy instead of being sourced from the environment.

tags: author:voooooogel, kind:tweet, thread-context, year:2025
