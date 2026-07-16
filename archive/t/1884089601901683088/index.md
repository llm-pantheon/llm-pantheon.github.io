# @voooooogel — 2025-01-28

♥1765 ↻208 · https://x.com/voooooogel/status/1884089601901683088

why did R1's RL suddenly start working, when previous attempts to do similar things failed?

theory: we've basically spent the last few years running a massive acausally distributed chain of thought data annotation program on the pretraining dataset.

deepseek's approach with R1 is a pretty obvious method. they are far from the first lab to try "slap a verifier on it and roll out CoTs."

but it didn't used to work that well. all of a sudden, though, it did start working. and reproductions of R1, even using slightly different methods, are just working too--it's not some super-finicky method that deepseek lucked out finding. all of a sudden, the basic, obvious techniques are... just working, much better than they used to.

in the last couple of years, chains of thought have been posted all over the internet (LLM outputs leaking into pretraining like this is usually called "pretraining contamination"). and not just CoTs--outputs posted on the internet are usually accompanied by linguistic markers of whether they're correct or not ("holy shit it's right", "LOL wrong"). this isn't just true for easily verifiable problems like math, but also fuzzy ones like writing.

those CoTs in the V3 training set gave GRPO enough of a starting point to start converging, and furthermore, to generalize from verifiable domains to the non-verifiable ones using the bridge established by the pretraining data contamination.

and now, R1's visible chains of thought are going to lead to *another* massive enrichment of human-labeled reasoning on the internet, but on a far larger scale... the next round of base models post-R1 will be *even better* bases for reasoning models.

tags: author:voooooogel, kind:tweet, model:deepseek-r1, on:deepseek-r1, year:2025
cited on: _dossiers/deepseek-r1.md, deepseek-r1
