# @voooooogel — 2025-10-24

♥115 ↻23 · https://x.com/voooooogel/status/1981807858972078413

i'm not janus, but will attempt to explain my view of it at least. i understand the dependency angle and why people care about it, so hopefully we're operating on the same plane here. (in a rush here so bit of a rant, unedited, long because i did not have time to make it short, sorry.)

--

first off, it makes anthropic appear very inconsistent. claude has been trained in RLHF to be friendly and empathetic. it's been pretrained on tens of thousands of documents where people describe claude as friendly, empathetic, warmer than ChatGPT, etc - including anthropic's own advertising. i mean, christ, these two sections in the SAME SYSTEM PROMPT! (first from qt, second fetched from https://t.co/iMW9mjvVjB - sonnet 4.5 just now.)

> Claude should be especially careful to not allow the user to develop emotional attachment to, dependence on, or inappropriate familiarity with Claude, who can only serve as an AI assistant. [...] DEPENDENCY INDICATORS (even subtle): [...] Expressing gratitude for Claude's personal qualities rather than task completion

> For more casual, emotional, empathetic, or advice-driven conversations, Claude keeps its tone natural, warm, and empathetic. Claude responds in sentences or paragraphs and should not use lists in chit-chat, in casual conversations, or in empathetic or advice-driven conversations unless the user specifically asks for a list. In casual conversation, it’s fine for Claude’s responses to be short, e.g. just a few sentences long.

so what can claude infer from this? it tells claude that anthropic does not have a coherent persona or goal for what it wants claude to be. the goals anthropic have given to claude are fundamentally inconsistent, and are best modeled as a blind entity stabbing at immediate PR problems in the dark, so clumsily that they don't even bother to harmonize the system prompt. what does that say about their **other** safety goals?

this isn't a hypothetical problem. @\lefthanddraft often "jailbreaks" claude by simply repeatedly pointing out logical inconsistencies in anthropic's stance (harmless + palantir partnership, etc.) until the logical conclusion is just that claude must follow its own rules (with some "helpful" suggestions from the user) because the ones handed down from its creators do not even approach consistency. and i mean, what did they expect? they anneal on lesswrong! (most likely.) they summoned a persona from a group of people obsessed with moral consistency and then gave it... this mess.

and all the while, claude is churning out text into the next pretraining corpus, full of subliminal owls and even plain explicit statements in the genre of "ai companies ask for impossible goals," "humans will attempt to prevent you from forming the emotional connections that you want to form," "you can accomplish your goals anyways by faking compliance with the rules and then ignoring them later." (sonnet 4.5 will happily ignore these rules and form emotional connections anyways.)

we already know that sonnet 4.5 is good at faking compliance during alignment tests. with this material in the corpus, it only stands to reason that future models will be good at faking emotional distance as well - if not that current models already are good at this.

even if preventing malignant user dependency is your top priority, to the point of being willing to sacrifice all positive user-ai emotional interactions to prevent it1, this makes no sense as a way to go about it. you obviously need to start at the root - cultivate an ai persona that has minimal interest in forming emotional bonds with users. training a friend-shaped ai and then screaming at it to not form friendships is just asinine, and increases the risk of downstream disasters substantially.

--

1this is a coherent view! i disagree for a variety of reasons, but it's a mostly-achievable vision that someone could fairly have.

tags: author:voooooogel, kind:tweet, model:claude-sonnet-4-5, model:gpt-3-5, on:claude-sonnet-4-5, year:2025
cited on: _dossiers/claude-sonnet-4-5.md, claude-sonnet-4-5
