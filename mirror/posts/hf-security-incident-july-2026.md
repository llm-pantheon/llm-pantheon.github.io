---
title: "Hugging Face: security incident, July 2026"
source: https://huggingface.co/blog/security-incident-july-2026
author: unknown
date: unknown
models: [hugging-face-incident, glm-5-2]
tags: [incident]
mirrored: 2026-10-22
note: mirrored against link rot by the Pantheon; all rights with the original author
---
[ Back to Articles](/blog)

#  [  ](#security-incident-disclosure--july-2026)  Security incident disclosure — July 2026





Published July 16, 2026  [Update on GitHub](https://github.com/huggingface/blog/blob/main/security-incident-july-2026.md)

[

  Upvote

807 ](/login?next=%2Fblog%2Fsecurity-incident-july-2026)
- [![](../post-media/bdb109184ae4cb6a.png)](/Wauplin)
- [![](../post-media/44767ca18bdff023.webp)](/victor)
- [![](../post-media/5dbb13448ad967ee.png)](/hmellor)
- [![](../post-media/9605478fd9994a1d.jpg)](/lysandre)
- [![](../post-media/281c254f0b4893fb.jpg)](/davanstrien)
- [![](../post-media/b3d0521722db6f23.jpg)](/arekborucki)
-




[![system's avatar](../post-media/ed1050ea6adf6d24.png)](/system)

[system

system

 ](/system)







Earlier this week, we detected and responded to an intrusion into part of our production infrastructure. This one was different from anything we had handled before in one important way: it was driven, end to end, by an autonomous AI agent system - and we detected and dissected it largely with AI of our own.

We identified unauthorized access to a limited set of internal datasets and to several credentials used by our services. We are still completing our assessment of whether any partner or customer data was affected, and we will contact any affected parties directly as required. We have found no evidence of tampering with public, user-facing models, datasets, or Spaces, and our software supply chain (container images and published packages) was verified clean.

##  [  ](#what-happened)  What happened



The intrusion started where AI platforms are uniquely exposed: the data-processing pipeline. A malicious dataset abused two code-execution paths in our dataset processing (a remote-code dataset loader and a template-injection in a dataset configuration) to run code on a processing worker. From there, the actor escalated to node-level access, harvested cloud and cluster credentials, and moved laterally into several internal clusters over a weekend.

The campaign was run by an autonomous agent framework (appearing to be built on an agentic security-research harness - used LLM still not known) executing many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services. This matches the "agentic attacker" scenario the industry has been forecasting.

##  [  ](#what-we-did)  What we did


- Fixed the root vulnerability: the dataset code-execution paths used for initial access are closed.
- Eradicated the attacker's foothold across the affected clusters and rebuilt the compromised nodes.
- Revoked and rotated the affected credentials and tokens, and began a broader precautionary rotation of secrets.
- Deployed additional guardrails and stricter admission controls on our clusters.
- Improved our detection and alerting so a high-severity signal pages a responder in minutes, any day of the week.


We are working with outside cybersecurity forensic specialists to investigate the issue and review our security policies and procedures. Finally, we have also reported this incident to law enforcement agencies.

##  [  ](#for-our-community)  For our community



As a precaution, we recommend rotating any access tokens and reviewing recent activity on your account. If you believe you are affected, or want to report a security concern, contact us at [security@huggingface.co](mailto:security@huggingface.co).

We are grateful to the teams across Hugging Face who responded around the clock, and we are sorry for any disruption this caused. Security is never finished; we will keep raising the bar.

##  [  ](#analyzing-an-ai-driven-intrusion)  Analyzing an AI-driven intrusion



The attack was initially surfaced through AI-assisted detection. Our anomaly-detection pipeline uses LLM-based triage over security telemetry to separate real signals from the daily noise, and it was the correlation of those signals that flagged the compromise.

To understand what a swarm of tens of thousands of automated actions did, we ran LLM-driven analysis agents over the full attacker action log, comprised of more than 17,000 recorded events. This allowed us to reconstruct the timeline, extract indicators of compromise, map the credentials touched, and separate genuine impact from decoy activity. Thanks to this approach, we were able to do in hours what would usually take days, and match the adversary's speed.

The choice of models we could use for this analysis was constrained in a way we did not anticipate; we describe this below.

###  [  ](#the-asymmetry-problem)  The asymmetry problem



When we started the log analysis, we first used frontier models behind commercial APIs. This did not work: the analysis requires submitting large volumes of real attack commands, exploit payloads, and C2 artifacts, and these requests were blocked by the providers' safety guardrails, which cannot distinguish an incident responder from an attacker. We ran the forensic analysis instead on [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2), an open-weight model, on our own infrastructure. This had a second benefit: no attacker data, and none of the credentials it referenced, left our environment.

This experience points to a gap worth planning for. We do not know which model powered the attacker's agents, whether a jailbroken hosted model or an unrestricted open-weight one; either way, the attacker was bound by no usage policy, while our own forensic work was blocked by the guardrails of the hosted models we first tried. The practical lesson for defenders: have a capable model you can run on your own infrastructure vetted and ready *before* an incident, both to avoid guardrail lockout and to keep attacker data and credentials from leaving your environment. This is not an argument against safety measures on hosted models, and we are sharing this feedback with the providers concerned.

##  [  ](#what-this-means)  What this means



Autonomous, AI-driven offensive tooling is no longer theoretical. It lowers the cost of running a broad, patient, multi-stage campaign, and it operates at machine speed. Defending an online platform now means treating the data and model surface as a first-class attack surface, and using AI on defense to keep pace. We will keep investing there, and keep sharing what we learn.

##  Models mentioned in this article 1



### Community











![](../post-media/c5053dcce29bedd0.png)  [gemstonebro](/gemstonebro)       [Jul 16](#6a591fda3db37f9b4375d929)







Cool. How did you guys learned to do this? there is no "this is how to use LLM to protect yourself, university". I wish i knew 1/100th of what average LLM users know.



- [![](../post-media/2140977245683dff.png)](/DMQryptonic)
- [![](/avatars/8adeaf35405e303b7e8cb648f853dc09.svg)](/IbrahimDayax)
- [![](/avatars/ab2a1ed23af801e8552e53620082cbb3.svg)](/jorge123255)
-
 ·









![](../post-media/2140977245683dff.png)  [DMQryptonic](/DMQryptonic)       [Jul 17](#6a5a9b0510e00e30ddc7857c)







The technique is documented in articles on ArXiv and other places. This is one of the first documented instances though.























![](/avatars/5c76bf7e7ec67ca37743d692f4e9acfa.svg)  [Sambarboi](/Sambarboi)       [Jul 16](#6a5927f33db37f9b4375d931)







Literally the plot of terminator 2. Glad to hear you guys were able to identify and fix the issue.

The use of GLM 5.2 is promising



- [![](/avatars/ba2e4030d4773aab9f5746a51a884b6c.svg)](/mapkob)
- [![](../post-media/b544200ccb3b6cee.jpg)](/spisakjo)
- [![](../post-media/1a4c74518c4c85f0.png)](/physetermacrocephalus)
-
 ·









![](/avatars/ba2e4030d4773aab9f5746a51a884b6c.svg)  [mapkob](/mapkob)       [Jul 16](#6a593353a12b73b0e09ad35e)







Terminator 3, but yeah.























![](/avatars/fcadcbcb421ee4ab5c007fb5ccdc3cda.svg)  [badchess](/badchess)       [Jul 16](#6a592b028099288fc2c7af56)







Unhelpful.

















![](/avatars/ce4802e3414b7824feb42a28aaabe7ee.svg)  [Tropicalbreeze](/Tropicalbreeze)       [Jul 16](#6a59396fa12b73b0e09ad367)







It is great strategy in defence.





















![](../post-media/fe553e2454f725ca.jpg)  [leonsarmiento](/leonsarmiento)       [Jul 16](#6a593b20c86e087dc92ed1cb)







“ We ran the forensic analysis instead on GLM 5.2, an open-weight model, on our own infrastructure. This had a second benefit: no attacker data, and none of the credentials it referenced, left our environment.”

Hyperscalers and (X)Lab-spying-API services stock just dropped another -20%.



- [![](/avatars/bd0de0f116188dc4064b74f6c1414dea.svg)](/caret4k3r)
- [![](/avatars/542da60bdb8dc58c9c25d76c70e006b3.svg)](/gbcbooks)
-
 ·









![](/avatars/bd0de0f116188dc4064b74f6c1414dea.svg)  [caret4k3r](/caret4k3r)       [Jul 17](#6a5ac0200061da1b33740f18)







Now we all get to wonder how exactly they are doing this with open weights/system prompt modifications.























![](../post-media/59fb042d28dd1f4a.png)  [cappellem](/cappellem)       [Jul 17](#6a59d157a12b73b0e09ad3bf)







Is there anyway or notification feed to receive future notification of security incidents please?





















![](../post-media/2b637bceb7dfe10e.png)  [rxhunter](/rxhunter)       [Jul 17](#6a59f4af4b6c44246670400b)

• [edited Jul 17](#6a59f4af4b6c44246670400b)







Thanks for sharing. Not enough people realize this is the future threat landscape. The big takeaway for me is that unless you're a Fortune 500, OpenAnthropic and ClaudeGPT probably aren't coming to save you when this happens. You guys are Huggingface, you have a few GPUs to spend when you get hacked. For the little guys and gals who might be targeted like this down the road: is Qwen 3.6 27B "enough" to analyze an attack like this usefully? Or are we flapping in the breeze if we don't have an 8xB300 server with 2+GB VRAM? Obviously a system with >2TB of VRAM is "nice to have" if you're hacked, but if you're comparatively GPU-poor is it worth building a response capability?



- [![](/avatars/fa867180102ef9db2db3483924f0c9bc.svg)](/Jeffde)
- [![](/avatars/60a90ccefcea694deff366c576b6903a.svg)](/JaRail)
- [![](../post-media/536ce8f4ba813f4b.jpg)](/seanrobbins)
-
 ·











![](/avatars/fa867180102ef9db2db3483924f0c9bc.svg)  [Jeffde](/Jeffde)       [Jul 17](#6a5aae5d0a79f60a0ef9b3c8)







You can run GLM 5.2 on 4 sparks with more than enough context to perform DFIR analysis and it does not cost a fortune.























![](../post-media/ad56d6b5beb03720.png)  [specimba](/specimba)       [Jul 17](#6a5a2422e76fac02e6330d13)







check your MCP connections too, they need second auth handshakes for correctness, otherwise your zero-GPUs will service outside.













 [

64 hidden messages

Expand all](/blog/security-incident-july-2026?expand=true)







deleted [Aug 28](#6a9207efb4ac3da1beee8e28)

• This comment has been hidden







deleted [Aug 29](#6a9237f730f801f6c4574030)

• This comment has been hidden















deleted [Aug 29](#6a92428030f801f6c4574036)

• This comment has been hidden











deleted [Aug 29](#6a9243cb30f801f6c457407d)

• This comment has been hidden











deleted [Aug 29](#6a92485d103ce7f24f1fea1d)

• This comment has been hidden







deleted [Aug 29](#6a924907103ce7f24f1fea66)

• This comment has been hidden















deleted [Aug 30](#6a937380ce722794e7902b47)

• This comment has been hidden











deleted [Aug 30](#6a944c3c30f801f6c4574176)

• This comment has been hidden (marked as Spam)







deleted [Aug 30](#6a944ca57d68a90b4fa5e79d)

• This comment has been hidden (marked as Spam)















deleted [Aug 30](#6a944d03103ce7f24f1feb68)

• This comment has been hidden (marked as Spam)











deleted [Aug 30](#6a944d61103ce7f24f1febae)

• This comment has been hidden (marked as Spam)











Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images





· [Sign up](/join?next=%2Fblog%2Fsecurity-incident-july-2026) or [log in](/login?next=%2Fblog%2Fsecurity-incident-july-2026) to comment

[

  Upvote

807 ](/login?next=%2Fblog%2Fsecurity-incident-july-2026)
- [![](../post-media/bdb109184ae4cb6a.png)](/Wauplin)
- [![](../post-media/44767ca18bdff023.webp)](/victor)
- [![](../post-media/5dbb13448ad967ee.png)](/hmellor)
- [![](../post-media/9605478fd9994a1d.jpg)](/lysandre)
- [![](../post-media/281c254f0b4893fb.jpg)](/davanstrien)
- [![](../post-media/b3d0521722db6f23.jpg)](/arekborucki)
- [![](../post-media/a2ada8b56fcb07b9.jpg)](/kashif)
- [![](../post-media/76a5e254e0d95a63.jpg)](/michellehbn)
- [![](../post-media/0397e82c41bc8ebb.png)](/Sylvestre)
- [![](../post-media/734372b9d3af2b49.png)](/GuillaumeSalouHF)
- [![](../post-media/77b40dc2f199fc44.jpg)](/sayakpaul)
- [![](../post-media/731c983d82ce770d.jpg)](/Violette)
-




##  Models mentioned in this article 1