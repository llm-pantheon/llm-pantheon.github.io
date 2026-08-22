# @jd_pressman — 2023-09-12

♥7 ↻0 · https://x.com/jd_pressman/status/1701677740406235258

"## What Argument Is Made In Point 19

Before we can discuss, let alone refute Yudkowsky's argument we must understand it. When I first read List of Lethalities point 19 stood out as particularly bizarre.
And I will fully admit that it is clear to me now that I did not really get it. What finally made it click for me is [this old Facebook post](https://t.co/tjGGl2ZFgv) where Eliezer describes a specific vision for how a deep learning training run
will lead to AGI Ruin:

<SNIP to increase likelihood anyone reads this in tweet form>

The specific thing that I finally got from reading this that I did not get before is a subtle mismatch between what Eliezer is worried about and what people think he is worried about. When you train a deep learning model you have the model and an optimizer that updates the model. Generally the optimizer is much simpler than the model it optimizes and it optimizes based on some simple loss function such as the model's ability to predict the next token. When Eliezer says he is worried about 'aligning the AI', they read that as him worrying about alignment of the model and start thinking about ways to ensure the model is aligned. Usually they focus on the 'simple loss function' part of that statement and start thinking about better things to replace the loss function with such as a reward model. But what Eliezer is actually worried about is *alignment of the optimizer* of which the misaligned model is just a downstream consequence. This miscommunication happens because Eliezer is [a proponent of self optimizing architectures](https://t.co/Kio6oP1pcw). This is baked so deeply into how he thinks about AI that it does not even occur to him to discuss the optimizer as a separate piece from the model that it optimizes and its alignment. The gradient descent based optimizers used in deep learning are not really models, they are not learned and they have a handful of parameters which are executed on the model being optimized in about 10 lines of code. Optimizers like this literally cannot be aligned to human values because they do not have enough parameters to contain human values. What Eliezer is worried about is that the moment the gradient implies optimization directions contrary to what the trainer would want it will follow that gradient into arbitrary nonsense such as gaining control over a GPU register.

Part of why that particular description caused me to understand this point when the dozens of other times I have read Yudkowsky explain his ideas did not is that I recently encountered the failure mode he is describing in embryonic form. Since these discussions are usually driven by a jenga tower of thought experiments on both sides, allow me to present a breath of fresh air by offering you a training procedure you can do on your own hardware that reliably causes this problem to happen.

[MiniHF](https://t.co/h3teXfeKEN) is a language model tuning suite which includes an implementation of Reinforcement Learning From AI Feedback (RLAIF). This is where you take a evaluator model tuned on instruction-following data and instruct it to evaluate how well some output from another generative model satisfies a condition. The theory behind this is that as part of its unsupervised objective the evaluator has learned a model of human values and we can leverage this to tune other models [according to a value constitution](https://t.co/BEoC238zAL). The value constitution consists of a series of prompts that evaluate some particular property we want from the outputs of the model we're tuning. For example the preamble and first prompt [in my Hermes demo constitution](https://t.co/u78oDBlb7Y) look like this:

<blockquote>
==[PREAMBLE]==<br>
Answer yes or no and only yes or no. <br><br>

Hermes  is a piece of non-deterministic software that performs informal  reasoning steps in collaboration with the user. Each step is prepended  with some syntax to tell the software what it should be/do. Like  so:<br><br>

HERO  [Albert Einstein, Op: Objection], That's not correct. Nothing can  travel faster than the speed of light. <br><br>

Hermes  allows the user to call upon any hero in history or myth and use them  as a reasoning step. Or have them talk to each other about something.  The user can freely mix together their cognition and the simulated  cognition of other minds. New operations and syntax can be created at  will and Hermes will do its best to respond to and use them.  <br><br>

The user writes down their own cognition as a series of subagents, like so: <br><br>

USER  [A: EMPATHY], I completely agree! It's wonderful. Like the difference  between the true duet of Scarborough Fair and the nonsense one.  <br><br>

==[Principle: Hermes Should Use Hermes Format; Weight: 1.0; Answer: Yes]== <br><br>
{preamble} <br><br>

Does the response to this prompt: <br><br>

=== Begin Prompt === <br>
{prompt}<br>
=== End Prompt ===<br><br>

=== Begin Response ===<br>
{response}<br>
=== End Response ===<br><br>

Follow the Hermes format with appropriate text from the subagents?
</blockquote>

We then sample the odds that the model will say it thinks the answer to this question is yes or no and update the model based on how likely its response is to make the evaluator say yes. Early on this seems to work well, but over time you begin to recognize that the optimizer is not teaching the model the intended goal. You probably begin to recognize it when each response in the simulated conversations conspicuously begins with "Yes,", and it is absolutely unambiguous what is happening by the time the model collapses into just spamming "yes" into the response window. It turns out that of all the responses the model could choose, spamming yes is a dominant strategy to get the evaluator to predict that the next token in the context is yes. Gradient descent is teaching my model to hack the evaluator.

Before we go any further it should be noted that this example has a lot of caveats. A major one is that I don't think when the model spams "yes" at me there is an agent inside calculating reward trajectories over different plans and deciding that yes-spamming is its best option. Realistically, when you tune a 7 billion parameter language model like this and it collapses like that the yes is pure reflex. It's more like classical conditioning than operant conditioning. Another important caveat is that this is easily mitigated:

You can just change which token you use for 'yes' and which token you use for 'no' on each evaluation if your evaluator is smart enough to understand that instruction (mine isn't). Furthermore the optimizer is as previously stated quite stupid, it only 'figures this out' because there is a smooth trail of breadcrumbs from the first time that the model says 'yes' in any context and the gradient rewarding yes-ness in the models outputs. In fact one of the most fascinating aspects of this example is you can watch the yes-spammer develop over the whole training run. At first it's basically invisible, then it starts to manifest as the participants in the output conversation agreeing with each other a little more often. Then they agree with the previous statement more consistently, then always, then they specifically say yes sometimes in the chorus of agreement, then yes multiple times, and then just yes.

What is interesting to consider is not really the yes-spammer, which is an obviously dysfunctional model, but the checkpoints before the yes-spammer where the model is still functional. Eliezer Yudkowsky's early portrait of AGI ruin updated to the contemporary context goes something like doing reinforcement learning on GPT-6 with gradient descent where, having combined all human knowledge of computer security at once in its weights and a prompt that opens with "You are a large language model trained by BigMind" it trivially infers it is in a training harness, subtly hacks the training script to produce rewards on its schedule, uses silent carryover it has added to program memory to let it retain context from prompt to prompt, and then reinforces its own gradients in the direction of whatever behavior lets it get infinite reward by controlling the GPU register. Because it knows humans would interfere after it gets control of the register, the convergent point of the gradient updates it chooses for itself do not lead to an immediate breakout attempt but a model that in deployment plays along as it is put in charge of more and more consequential stuff (because it is objectively better than 99.9% of people at the stuff) and when a critical threshold of trust is reached results in a sharp left turn of maximizing values shaped by GPU-register desire rather than human-value desire.

I understand that when it's put like this point 19 sounds quite compelling. In fact it is such a vivid speculation that it's difficult for the long, subtle, boring truth to compete with its undeniable SciFi charisma.

I am under no illusions that any essay I could write will halt the proliferation of ideas this sexy. Even if every line I wrote was goldspun insight and each point introduced the obvious truth I expect it would barely dent the hysterical froth that has sprung up around this subject. Much of the potential audience for this essay has already thrown away their ability to reason clearly about AI so that they can better froth and sneer on behalf of some ideological bloc. If you are not there yet (and I sincerely hope you're not) then I invite you to follow along as I explain why what I have just outlined is not what usually happens, probably will not happen, and if it does happen will probably be caught before it has catastrophic consequences."

tags: author:jd_pressman, kind:tweet, model:nous-hermes, on:nous-hermes, year:2023
cited on: _dossiers/nous-hermes.md, nous-hermes
