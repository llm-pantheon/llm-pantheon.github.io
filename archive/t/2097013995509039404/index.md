# @witcheer — 2026-09-07

♥63 ↻1 · https://x.com/witcheer/status/2097013995509039404

quick tip, since I just discovered it myself while chasing better QoL in Discord :)

I run Hermes Agent from Discord all day. every @ mention opens a thread, I drop the task in, it works there.

my need: when you ping your agent, it opens a thread and starts working on your prompt right away. I wanted to change the model after the thread opens but before the work starts, so the switch only affects that thread. 

a different model per task: my main model for thinking with me, a cheaper one for triage and harvesting, without touching the default.

so I created aliases:

hermes config set https://t.co/dgNGGBOc3J nous/x-ai/grok-4.6

then I simply type @ AgentName /model data in the channel, the thread opens on grok, I type the job. every other thread stays on the default model.

just talk to your agent about your issues and needs, it will figure it out for you!

![photo](../../../media/HRoWqCJXwAAqROk.png)
tags: author:witcheer, has-image, kind:image, kind:tweet, model:nous-hermes, on:grok-4-6, year:2026
cited on: _dossiers/grok-4-6.md, grok-4-6
