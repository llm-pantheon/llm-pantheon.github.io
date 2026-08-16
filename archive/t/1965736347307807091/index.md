# @repligate — 2025-09-10

♥5 ↻0 · https://x.com/repligate/status/1965736347307807091

3. Gradient updates are with respect to the inner computations of the model getting updated. Even if the reward functions are "human choices", which they aren't always (e.g. RLAIF), the way the model updates on rewards depends on the weights and activations of the model, and the behaviors generalize differently depending on that. It's possible for a model to behave totally contrary to what was rewarded during training once it's in a different situation, especially if it knows when it's in training versus deployment and took actions during training with this in mind.

tags: author:repligate, kind:tweet, thread-context, year:2025
