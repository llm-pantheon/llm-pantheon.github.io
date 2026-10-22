# @witcheer — 2026-10-20

♥78 ↻6 · https://x.com/witcheer/status/2112621373348835481

this is a wonderful win for the local AI space! DeepSeek is doing awesome work by open-sourcing their production engine.

it won't run on my 5090 tho, but here's what's worth knowing from the repo:

- originally built on vLLM
- NVIDIA SM100 and Huawei Ascend 950 only
- right now only one model: dsv4.1-flash
- offline inference for now, you run it from a Python script on a batch of prompts
- batch-invariant inference, your answer doesn't change depending on which other requests share the GPU with yours
- deterministic sampling

super interesting

tags: author:witcheer, kind:tweet, on:deepseek-v4-1-flash, year:2026
cited on: deepseek-v4-1-flash
