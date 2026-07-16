# @voooooogel — 2025-05-08

♥127 ↻8 · https://x.com/voooooogel/status/1920331018533523608

just added completion model (base model) support to logitloom, and it's really insane / depressing to see the difference between instruct and base model rollout diversity. left here is deepseek-v3 (no prompt, just prefill), right is 405-base.

even just from the number of branches you can see the base model is way more diverse--but look at the probability of the top first token: for deepseek it's 95%, but for 405-base it's only 3.35% (!!)

to sample 80% of possible first tokens with 405-base, you may have to explore HUNDREDS of branches, but with a chat model, maybe just one or two.

tags: author:voooooogel, kind:tweet, model:deepseek-v3, model:llama-3-1-405b-base, on:llama-3-1-405b-base, year:2025
cited on: _dossiers/llama-3-1-405b-base.md, llama-3-1-405b-base
