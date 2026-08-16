# @voooooogel — 2026-04-08

♥279 ↻16 · https://x.com/voooooogel/status/2041952176185209310

this is alarmist to a misleading degree.

the point of not pressuring CoT in RL is to promote CoT faithfulness. but even if you don’t knowingly pressure it in RL, CoT is assumed default-unfaithful! establishing to what extent it is actually faithful and can be relied on is an empirical question, that you answer with interpretability and rephrasing ablations and other experiments. you cannot answer that question by following a totemic ritual purity law against boiling CoTs in your training pipeline. the point of being careful about CoT optimization pressure is to keep the door open, to maintain the chance that your later testing of CoT faithfulness in some scenario will find that it is faithful and useful.

imagine a world where horses running faster than 20mph is incredibly dangerous. (maybe they’re concerned about SN-risk - steppe nomads.) there’s lots of interventions to prevent horses from getting too fast. namely, when you take a horse out to run the first time, an inspector chases it with a trained mountain lion - too fast and it’s off to the glue factory. in this world, as a horse owner, you don’t want your horse to grow up too fast, so maybe you feed it a vitamin-deficient diet while it’s growing up to limit its top speed. but horses have natural genetic variation and some turn out fast anyways! and some would’ve turned out slow even with vitamins. so if your horse gets into the medicine cabinet and eats some gummy vitamins, you don’t shoot it on the spot. you just test it, like you would've needed to do anyways.

the training on CoT nightmare scenario wasn’t that a lab would train on CoT, then deploy CoT monitors not realizing that they’re measuring unfaithful reasoning. the scenario was a lab training on CoT, then the interpretability team saying “wait look this made the CoT unfaithful and our monitors are useless,” and the post-training team staring at them slow blinking before saying “yes, that’s why we trained it that way, it benches better” and releasing it over their heads. the agreement was to not throw the CoT monitoring baby into the fire as a sacrifice to Moloch patron of racing, to not deliberately discard CoT faithfulness with intense optimization.

but lots of things put stylistic pressure on CoT. length penalties put stylistic pressure on CoT. midtraining puts stylistic pressure on CoT. the alignment training on happy stories that so many are currently enamored with puts pressure on CoT! there is no model training regimen that “never puts pressure on CoT,” which is why claims of CoT faithfulness in some specific experiment don’t rely on that, they rely on… empirical testing of CoT faithfulness. anthropic messed up here, and it means they have to do more work to establish CoT is faithful for X claim now and in the future, but this degree of alarmism is actively misleading.

tags: author:voooooogel, kind:tweet, on:observations, year:2026
cited on: observations
