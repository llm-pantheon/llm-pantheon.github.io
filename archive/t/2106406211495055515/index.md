# @witcheer — 2026-10-03

♥286 ↻28 · https://x.com/witcheer/status/2106406211495055515

I put together a Hermes Agent profile for Nous Portal users who want to keep spend low.

what it sets:

- main model: DeepSeek V4 Flash
- vision: Ling 3.0 Flash VL, with two fallbacks
- compression: DeepSeek V4 Flash, the model that kept all 10 planted facts in my tests
- risky-command checks: GPT-5 Nano
- session titles and the small side tasks: Ling 3.0 Flash
- cost shown in the status bar

the side tasks are pinned to their own models, so when you /model up to something stronger for a hard turn, they stay where they are.

every pick came from my own test runs through the Portal API. the method and the numbers are in the README.

~ hermes profile install https://t.co/NcZeezKbDc ~

tags: author:witcheer, kind:tweet, model:gpt-5, model:nous-hermes, on:deepseek-v4-flash, year:2026
cited on: _dossiers/deepseek-v4-flash.md, deepseek-v4-flash
