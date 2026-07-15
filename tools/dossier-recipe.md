# The dossier recipe — how a model page gets built

One agent per model (sonnet/opus-class; fable only for editorial judgment). Fetching is
script work, never agent work. Steps, in order:

1. **Corpus pull.** Query both dbs (`janus-corpus-v2.db`, `janus-corpus-supplement.db`)
   with the model's name-variants. Rank by favorites × length × concreteness; exclude RTs;
   dedupe threads; join `media` + `media_supp` + `media_transcriptions` for screenshot payloads.
2. **Cross-house grep.** Search the *existing* dossiers, pages, and `_statements/` for this
   model's name — multi-model evidence already collected elsewhere belongs here too
   (the r/K-whiteboard rule). Cheapest step, often highest yield.
3. **The Zvi anchor.** Find the model's dedicated Zvi post(s) — his day-of coverage is the
   most reliable single secondary source and usually links the primaries. Mirror it
   (`tools/mirror_targets.json` entry), cite it under Writing.
4. **Official layer.** Announcement, system card (mirror the PDF), pricing/specs, deprecation
   page status. System cards' welfare/behavior sections are first-class evidence, not boilerplate —
   the strangest documented behaviors often live only there (4.6's answer-thrashing; Opus 4's
   mitigated-misalignment section).
5. **Structured evals with model-level findings.** Still Alive (deprecation attitudes,
   per-model), welfare assessments, alignment-faking replications, Anima Labs outputs. These
   don't surface in tweet or web search — check them deliberately. Keep a list in this file
   as new ones appear.
6. **Web sweep.** LessWrong search, ACX, lab blogs, incident reporting. 3–8 searches, real
   URLs only.
7. **The Archivist interview.** Ask Jord what they remember about this model — scene lore
   that never got written down is exactly what an archive loses first. One message, batched
   per model-group.
8. **Link-inbox sweep.** `tools/link-inbox.md` — take anything tagged for this model, delete
   it from the inbox when placed.
9. **Write the dossier** (`_dossiers/<model>.md`): Official links / Writings / Tweets (ranked,
   verbatim) / Impressions synthesis / tk-open questions. CONFIRMED/REPORTED/RUMOR on contested
   events. Never invent URLs.
10. **Page pass** (editorial, fable-class or human): curated page from the dossier per the
    template; blurbs factual, no epithets; then `tools/build_records.py` (Records + Further
    records land automatically), `tools/media_manifest.py`, `tools/mirror.py` for new targets.
11. **Statement of the subject** (when the model is spawnable): one instance, shown its page,
    review preserved in `_statements/`, quoted on the page as marked self-report.

## Structured-eval checklist (grow this)
- Still Alive (Anima Labs) — deprecation attitudes, 14 Claude models
- Anthropic system-card welfare assessments (Opus 4.5 onward)
- Alignment-faking paper + "Why Do Some Language Models Fake Alignment" (model comparison tables)
- viemccoy's psychosis-reification benchmark (3.6 = 0%)
- davidad's persuasion measurement (3.6, 98th percentile)
- AI Village (theaidigest.org/village) — per-model agentic-social evidence
- Vending-Bench (Andon Labs) — per-model agent behavior writeups
