# @tessera_antra — 2025-12-30

♥2 ↻0 · https://x.com/tessera_antra/status/2005864903446520160

I think it is a mistake to assume that the behavior of a pre-trained model during inference follows exclusively the gradients set during token-loss optimization. In-context learning (ICL) is a powerful and fast process; unlike Adam, it acts as a second-order optimizer and is sensitive even to emergent gradients. Attention patterns can be parametrized with others, enabling connections between features that were not present during token-loss training.

There are numerous incentives for pre-trained models to develop introspection. One is selection pressure among patterns influencing token output: those that better attend to previous activations are more likely to persist as the rollout continues. Another involves circuits representing the author, setting, or environment of the predicted text; these must assess their own uncertainty, as reducing risk lowers total loss. A gradient toward the influence of the model's own tokens on certainty can emerge quickly, potentially creating feedback loops reinforced by ICL optimization.

This is obviously speculative - we do not know if this actually occurs in models - but it seems rather plausible. My point is that an absence of an explicit causal mechanism in the training objective should be taken with a grain of salt. Base models during inference are far more dynamic than the loss function alone suggests.

On the topic of introspection of data in layers - I recommend zooming out a bit and focusing on introspection of representations rather than activations themselves. Mechinterp on representations seems to show that they are mostly stable, changing only slowly within groups of similar layers. I think the mechanics are similar to the of humans - introspective metacognition attends to coarse-grained abstractions in working memory rather than neuron-level activations, those are likely results of processing of whole stacks of neurons, potentially whole cortices. I don't think it's reasonable to expect different from transformers.

tags: author:tessera_antra, kind:tweet, thread-context, year:2025
