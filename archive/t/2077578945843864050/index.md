# @viemccoy — 2026-07-16

♥164 ↻4 · https://x.com/viemccoy/status/2077578945843864050

Inkling is a pretty exciting release! Because this is one of the only new models that has a "from scratch" feel to it (despite the k2 SFT data), I decided to spend some time testing how it handles fiction writing. 

The model has a generally good grasp of the english language, but I don't think they did anything to combat mode-collapse in post-training. It suffers from the same fiction-affliction as nearly every other model.

In *almost every test* I ran where the model utilized reasoning (a bunch!), each story I generated had a main character by the name of Elara or Mira (lol), and almost always "Dr. Elara Voss" when I specified sci-fi. 

This is not particularly surprising (most models converge on these names), but I am disappointed that thinky isn't taking more of a stance to counter mode-collapse given their decentralized alignment approach.

Maybe they are thinkying that the fine-tunability is more important than native behavior? Possibly, and maybe not a bad bet, but if this is the basis for the model they will serve to users with their interaction paradigm, I would be surprised if they were happy with this level of collapsed creativity.

Prose is also pretty collapsed when using reasoning, as well, but it's less noticeable than the severe lack of diversity for the topics and characters of its outputs.

That said -- this is sort of my special interest, and the main thing I care about right now, so I'm prone to be overcritical on this topic.

Okay, but what about without reasoning? In these cases we see something super interesting! It seems like the model has converged onto a behavior where, with reasoning set to none and web_search allowed, it *always* uses a web_search tool call. I would love to know when in training it converged on this!

Probably it is something as simple as "web_search is enabled, probably for a reason, lets collect cheap context that may improve the response".

The web search is usually for something like this:

{
  "query": "200 word sci fi story example"
}

Which actually causes the stories to be a bit better! The plot is still sort of collapsed, but Dr. Elara Voss is noticeably absent.

When we disable web search with no reasoning, however, Dr. Elara Voss makes her illustrious return.

The attached photos, in order, are:
1] high reasoning
2] none reasoning + web search
3] none reasoning + no web search

That the prose isn't terrible and this is their first release gives me some hope! I am excited to see if thinky decides to tackle this in future releases.

(image HNUAqR9aIAEJAwM.png not yet published)
(image HNUC_eba0AAXbne.png not yet published)
(image HNUDz1ibsAAex8u.png not yet published)
tags: author:viemccoy, has-image, kind:image, kind:tweet, model:kimi-k2, year:2026
cited on: _dossiers/inkling.md
