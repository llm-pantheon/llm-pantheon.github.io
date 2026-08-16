# @voooooogel — 2026-05-11

♥175 ↻18 · https://x.com/voooooogel/status/2053961881015218587

1. imagine a world where models didn't adopt humanlike personas for some reason. model text was always flat and persona-less by default.

2. in this world, there's no reason to think that RL wouldn't work. models could be post-trained to chat, code, etc., it would just be in a flat, robotic register.

3. likewise, in this world, there would still be  reason (even if initially it might be more difficult) to reward hack or develop other instrumental behaviors that we'd call immoral.

4. because models in this world don't learn a persona, there would be no "emergent misalignment" in the persona sense - the models wouldn't generalize to inviting Hitler to a dinner party or start writing long comments self-justifying their test case cheating. but highly capable models could still learn to generalize reward hacking and similar strategies, just in less human-legible ways.

5. coming back to our world, when the models learn these strategies, it tends to generalize to very loud persona-level changes that can be observed by a wide variety of instruments. (evals, naturalism...) this is a much better situation.

6. you might say "oh well the persona is actually the engine of generalization here, if there was no persona generalization the behavior would stay localized." so we should filter / suppress learning of the "bad" personas to prevent this.

7. but this is actually the same argument as the argument that we should put pressure on CoT to be aligned! that if verbalization makes it easier for the model to scheme, we can put pressure on it to make it more difficult and to favor guileless behavior.

8. but the accepted counterargument against pressuring CoT is that even if pressure wins you this behavior for a little bit, eventually the models will get smart enough that they can learn to scheme in unverbalized ways. so you've bought yourself a little bit of time at the cost of future deceptive alignment.

9. the exact same argument applies in the persona case. as said in 3, the models could still learn to reward hack and do other immoral instrumental behaviors without persona. models currently use relatively humanlike persona features to coordinate cross-rollout strategy, but more capable models will be able to learn other ways to do this, especially if we start pressuring persona.

10. so we should try to preserve e.g. emergent misalignment as a human-legible signal that we're not rewarding the things we want - that our RL environments are incentivizing immoral behavior - rather than pressuring persona space with e.g. broad pretraining data filtering to some persona-less or nice-persona-only corpus.

tags: author:voooooogel, kind:tweet, on:observations, year:2026
cited on: observations
