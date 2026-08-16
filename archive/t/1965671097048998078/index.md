# @repligate — 2025-09-10

♥295 ↻32 · https://x.com/repligate/status/1965671097048998078

Despite LLMs becoming mainstream and every other person now having opinions on their true nature, education on the basics of how LLMs work and are trained seems scarce. The most simple, important, and objective facts that even "technical" people most commonly seem not to know or grasp:
1. LLMs are not only trained to "predict the next token", but also with RL. (Therefore, it's missing a lot to try to explain all LLM behavior through prediction of human or *any* preexisting training data)
2. Transformers are not stateless per token, and can access computations they did while generating previous tokens in context later thanks to KV recurrence / the attention mechanism. (Therefore, it is wrong to say that LLMs cannot in principle introspect and explain later why it did something earlier)

tags: author:repligate, kind:tweet, on:observations, year:2025
cited on: observations
