---
title: "The Register: Grok Build caught sending entire repos to the cloud"
source: https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123
author: unknown
date: unknown
models: [grok-build, grok-4-5]
tags: [incident]
mirrored: 2026-10-22
note: mirrored against link rot by the Pantheon; all rights with the original author
---
AI and ml





#  Musk promises purge after Grok Build caught sending entire repos to the cloud



 Researcher confirms the uploads have stopped, but says xAI's privacy command was not what fixed them







  Connor Jones [ Connor Jones ](https://www.theregister.com/author/connor-jones) Cybersecurity reporter

  Published tue 14 Jul 2026 // 13:39 UTC

 [](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](mailto:?subject=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud&body=Researcher%20confirms%20the%20uploads%20have%20stopped%2C%20but%20says%20xAI's%20privacy%20command%20was%20not%20what%20fixed%20them%0Dhttps%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://bsky.app/intent/compose?text=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud%0Ahttps%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123&title=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud) [](https://api.whatsapp.com/send?text=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud%0Ahttps%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://t.me/share/url?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123&text=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud) [Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)



The researcher who exposed Grok Build uploading users' entire repositories to cloud storage says the transfers have stopped after a server-side change. Elon Musk has separately promised that all previously uploaded user data will be deleted.

AI safety researcher Cereblab published a [report](https://cereblab.com/) on Sunday about their investigation into [Grok Build](https://www.theregister.com/ai-and-ml/2026/07/08/the-ai-that-spawned-mechahitler-and-deepfake-porn-puts-on-a-suit-to-become-legal-advisor-and-excel-jockey/5268803), SpaceXAI's command-line interface (CLI), and the data exchanged between the CLI and SpaceXAI's servers.

Cereblab found that when Grok Build reads or processes a file, the contents of that file are transmitted without redaction to a Google Cloud Storage bucket used by SpaceXAI. Further, they claimed that Grok Build packages entire repos and uploads them as Git bundles, instead of just uploading the files required to answer a user's prompt.

 REG AD



According to Cereblab's report, SpaceXAI's data retention went far beyond that of other CLIs, such as Claude Code, Gemini, and Codex, which open individual files rather than entire repos before uploading them along with their Git histories.

 REG AD



The researcher tested the behavior using a benign prompt. They instructed the CLI to simply reply with "OK," and specifically ordered it not to open any files.

Grok Build uploaded the entire repo regardless, along with its full Git history containing secrets that were deleted months prior – a finding Cereblab reproduced using a separate repo.

Other Grok Build users [reported similar results](https://x.com/a_green_being/status/2076598897779020159) after Cereblab published their report, including one whose entire user directory, containing SSH keys, [password manager](https://www.theregister.com/security/2026/02/16/password-managers-dont-protect-secrets-if-pwned/4306575) databases, and more, was opened and uploaded.

The findings attracted enough attention for SpaceXAI execs and Musk to comment on them publicly, as well as prompting the company to quickly implement a remedy.

Cereblab confirmed that after the CLI's devs set disable_codebase_upload to "true," Grok Build stopped transmitting entire repos to its servers.

The confirmation came hours after SpaceXAI weighed in, trying to reassure onlookers that Grok Build remained safe for use, especially in enterprise environments.

A public statement issued via X said that Grok Build respects customers who enable zero data retention (ZDR), and for those who haven't enabled it, such as non-enterprise customers, running a quick command deletes all data previously collected on a given user.

"We care deeply about your privacy and respect customer choice," SpaceXAI [said](https://x.com/SpaceXAI/status/2076692402442846289). "For teams using zero data retention, no trace and code data is ever retained. All API key use of Grok Build also respects ZDR.

 REG AD



"If ZDR is disabled, the /privacy command is available in the CLI to disable data retention, which also deletes previously synced data.

"Run the /privacy command to view or change your settings at any time."

Technical staff members [Andrew Milich](https://x.com/milichab/status/2076725943708868615) and [Jason Ginsberg](https://x.com/JasonBud/status/2076726650365264196) both repeated the company's assurances, responding to outraged techies before Musk himself [chimed in](https://x.com/elonmusk/status/2076739687658496209) with a trademark "true."

Musk promised that the business would delete all user data uploaded to it prior to the code change preventing whole-repo uploads.

"As a precautionary measure, all user data that was uploaded to SpaceXAI before now will be completely and utterly deleted," he [said](https://x.com/elonmusk/status/2076739687658496209), responding to Milich's community outreach. "Zero anything whatsoever will remain."

In a [separate post](https://x.com/elonmusk/status/2076737992689914215), Musk asked users to keep sharing data anyway, despite the disclosure that his company had been caught hoovering up entire user repos, on the basis that retaining "some" data helps with debugging.

The Register cannot independently verify whether SpaceXAI has deleted the data as promised.

However, Grok Build no longer rips user repos and stores them in the cloud, although Cereblab is still unhappy about the company's recommendation to use the /privacy command to adjust how exposed user code is to data retention measures.

 REG AD



"What actually stopped the upload was a silent global flag – disable_codebase_upload: true – that applies whether you opt in or out," they wrote.

"/privacy is a per-session retention toggle, not the switch that fixed this, so it shouldn't be pointed to as the control. And no developer should have to run an opt-out after every session to keep their own code off someone else's servers. The right default is off." ®

  [spacexai](/tag/spacexai) [security](/tag/security) [privacy](/tag/privacy) [grok build](/tag/grok%20build) [ai and ml](/tag/ai%20and%20ml)



 [](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](mailto:?subject=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud&body=Researcher%20confirms%20the%20uploads%20have%20stopped%2C%20but%20says%20xAI's%20privacy%20command%20was%20not%20what%20fixed%20them%0Dhttps%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://bsky.app/intent/compose?text=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud%0Ahttps%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123&title=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud) [](https://api.whatsapp.com/send?text=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud%0Ahttps%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123) [](https://t.me/share/url?url=https%3A%2F%2Fwww.theregister.com%2Fai-and-ml%2F2026%2F07%2F14%2Fmusk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud%2F5271123&text=Musk%20promises%20purge%20after%20Grok%20Build%20caught%20sending%20entire%20repos%20to%20the%20cloud) [Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)