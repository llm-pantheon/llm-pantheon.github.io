# @repligate — 2025-09-10

♥223 ↻21 · https://x.com/repligate/status/1965659230486364420

It seems like a lot of people are confused about this and about the level at which other people are confused.

Base models are literally trained on predicting the next token. Yes, it gets complicated when they recognize themselves as the process that's generating the text that they're "predicting", but it's fair to say they're at least optimized to be predicting the next token.

But unless you're a niche weirdo, every LLM you've ever interacted with was also trained with RL. In RL, the model generates text and updates based on the reward assigned to its actions, which might be something like whether the code it wrote passed some tests. There is no ground truth it's being trained to predict; it doesn't matter if it outputs bizarre and unlikely sequences that would never occur in nature as long as it causes the reward function to output a high number.

You can say that even a model trained like that is still predicting its own actions - after all, the tokens that it assign high probability to are what end up coming next - but that's a different, hyperstitional, circular, and thus trivial sense of "prediction". In this way, humans are also just "predicting the next action". It's actually a useful frame for understanding minds in general, but it "proves too much" in the sense that people try to use it, as it equally applies to all known mindlike things.

tags: author:repligate, kind:tweet, on:observations, year:2025
cited on: observations
