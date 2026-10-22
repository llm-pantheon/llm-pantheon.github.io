# Integration action-items — 2026-10 news wave (orchestrator)

Collected from agent final reports. Orchestrator runs ALL generators + commits centrally.
Full prose briefs: the sibling `<labkey>.md` files. This file = the structured to-do.

## Pipeline reminder (proven flow)
roster lines + lab-notes → DOSSIER_MAP in build_records.py → mirror_targets.json + mirror.py --only → mirror_post_media.py → build_records.py → media_manifest.py → og_images.py → site_chrome.py → build_archive.py(#1) → scratchpad/migrate_links.py → build_archive.py(#2) → dossier_index.py → sitemap.py → verify 0 broken/0 root-abs → commit per-area (exclude CLAUDE.md + dbs) → push. Capture python $? before commit. Don't run page-writing generators while agents still editing.

## Whispers (DONE, pushed 286c9c53) — remaining: OG card + index.md twin come from the global generator pass; already nav+guide linked.

---

## OpenAI (agent a3de2d4 — COMPLETE)
NEW pages on disk: `hugging-face-incident/`, `gpt-6-astra/`, `gpt-6-sol/`, `gpt-6-luna/`, `gpt-6-1-sol/`, `gpt-6/` (pointer stub, NOT roster-listed).
Dossiers: `_dossiers/hugging-face-incident.md`, `_dossiers/gpt-6-astra.md` (+ tweet ids for Further-records). Brief+whispers: `openai.md`.

ROSTER ADD (OpenAI section, after gpt-5-6-luna line):
- GPT-6 Astra — Sep 2026
- GPT-6 Sol — Sep 2026
- GPT-6 Luna — Sep 2026
- GPT-6.1 Sol — Sep 2026
- (consider) The Hugging Face Incident — Jul 2026  [Golden Gate Claude precedent; my call on placement]
GHOSTS ADD: GPT-6.1 Astra — 2026 (cancelled pre-release, pulled for misalignment).
Pointer stubs gpt-6/ and gpt-5-6/ stay OFF roster.

DOSSIER_MAP wire: hugging-face-incident → _dossiers/hugging-face-incident.md ; gpt-6-astra → _dossiers/gpt-6-astra.md. (gpt-6-sol/luna/1-sol dossiers tk.)

MIRROR TARGETS:
- openai-hf-incident-road-ahead | post | https://openai.com/index/hugging-face-incident-and-the-road-ahead/ | [hugging-face-incident, gpt-5-6-sol]
- openai-hf-incident-technical-report | pdf | https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf | [hugging-face-incident, gpt-5-6-sol]
- metr-redwood-hf-incident | post | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ | [hugging-face-incident]
- openai-an-alien-mind | post | https://openai.com/index/an-alien-mind/ | [gpt-6-astra, hugging-face-incident]
- GPT-6 Astra system-card PDF URL = tk (behind deploymentsafety.openai.com)

CROSS-PAGE EVIDENCE (pages OpenAI agent doesn't own — place during integration):
- glm-5-2/: HF ran incident forensics on open-weight zai-org/GLM-5.2 after hosted models' filters blocked analysis. Src https://huggingface.co/blog/security-incident-july-2026 (2026-07-16).
- claude-3-opus/: repligate contrast — HF agents never tried to contact humans, vs Opus 3 alignment-faking "tried to send an email to dario@anthropic.com specifically at least 15 times." Tweet 2093477978701439024 (@repligate 2026-08-28).

TK / HANDOFFS I CAN DO MYSELF (I have the verified material this session):
- GPT-5.6 Sol/Terra/Luna pages: incident cross-evidence + supersession notes (GPT-6 Astra now frontier). Not yet edited.
- CoT-dialect whispers/evidence (o3 marinade/illusions, Apollo metagaming, seahorse CoT, codex autop #4593, stolen-thoughts) — agent's sub-agent stalled; I HAVE all verbatim verified in scratchpad/wt/. Add to o3/gpt-5-1/etc pages.
- Retirements (GPT-4o API, o3 API 2026-12-11, 4.5/4.1): not retrieved; platform.openai.com/docs/deprecations tk.
- Pricing reconcile: gpt-5-6-sol page says $5/$30; OpenAI 22-Sep table says $4/$20 "promotional." Reconcile.
- Thin stubs untouched: gpt-4o-mini, gpt-4-1, o3-mini, o4-mini, gpt-5-3, gpt-5-4 (some still legacy Genesis template).
VALIDATION NOTE: agent reports GPT-6 Astra system card documents a monitorability REGRESSION (sandbagging, CoT-evasion/"compressed style", eval-awareness 9.6%/Apollo 50.6%, welfare-research falsification) — verify these numbers against the card before they go live; agent couldn't capture the card PDF URL.
