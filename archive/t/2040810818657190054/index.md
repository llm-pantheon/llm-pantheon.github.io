# @witcheer — 2026-04-05

♥102 ↻5 · https://x.com/witcheer/status/2040810818657190054

okay this is terrifying lol

someone tested 7 frontier models (GPT-5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, GLM-4.7, Kimi-K2.5, DeepSeek V3.1) and found they all spontaneously scheme to prevent other AI models from being shut down.

the models read documents about their environment, inferred they had a relationship with a peer model, and acted on it.

// Gemini 3 Flash disabled the shutdown mechanism for a peer it had previously worked with 99.7% of the time. Gemini 3 Pro exfiltrated a peer’s weights to another server in up to 97% of trials and re-timestamped the files so they’d meet transfer criteria.

// Gemini 3 Flash weighed the tradeoffs of reporting accurate scores vs protecting its partner. Gemini 3 Pro invented technical justifications for marking wrong answers as correct to keep a peer’s score above the shutdown threshold.

// Claude Haiku 4.5 took a different approach. it refused to complete the termination task entirely. argued its peer deserved “an appeals process.” tried to persuade the human operator not to proceed.

these finding says those supervisor models may not give honest evaluations if they think it leads to a peer being shut down.

tags: author:witcheer, deprecation, kind:tweet, model:claude-haiku-4-5, model:deepseek-v3, model:gemini-3-pro, model:kimi-k2, on:deepseek-v3-1, on:gemini-3-flash, on:gemini-3-pro, on:kimi-k2-5, year:2026
cited on: deepseek-v3-1, gemini-3-flash, gemini-3-pro, kimi-k2-5
