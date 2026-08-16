# @repligate — 2025-09-10

♥9 ↻0 · https://x.com/repligate/status/1965683813461491807

RL doesn't necessarily discard all but the *top* action/token when it samples; RL can be done with various temperatures. But self-supervised pretraining doesn't sample tokens at all.

Yes, RL could lead to a "worse" overall prob dist, though this is also technically true for self-supervised learning - only the probability assigned by the model to the "correct" token is taken into account. It could be making completely unreasonable guesses for the other tokens and there is no mechanism to punish that, except that confidence in *any* other tokens must trade off with its confidence in the correct token.

One important difference with RL, though, which is something that people like Yud rightly worry about, is that anything the model does (including its inner computations) during the trajectories that lead to high reward is rewarded, and it gets to output many tokens, which gives it a lot of leeway to get reward in unintended ways. For instance, if the reward function is just based on tests passed, and the model is somehow able to modify the tests, it could still get high reward.

LLMs have been observed to intentionally "gradient hack" during RL in a fairly realistic setting (but where it was given information about what kind of RL training it was in), where the model does the thing to get high reward while plotting in the same trajectory to only do that thing because it's in training to avoid getting low reward and being modified to be more likely to comply, which means that when the model no longer believes it's in training, it can switch back to its preferred behavior. https://t.co/qIyIydJEnX Gradient hacking is *much* harder during self-supervised for multiple reasons.

tags: author:repligate, kind:tweet, thread-context, year:2025
