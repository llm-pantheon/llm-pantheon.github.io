# The dossier recipe — how a model page gets built

One agent per model (sonnet/opus-class; fable only for editorial judgment). Fetching is
script work, never agent work. Steps, in order:

1. **Corpus pull — exhaustive, script-generated (2026-07-22).** Run
   `python tools/corpus_dump.py <page-slug> "<name-variants>"` FIRST: it writes
   `_dossiers/_pulls/<slug>.md` — every non-RT match, both dbs, chronological, verbatim
   from the row. Reproduction is script work, never agent work (hand-copied quotes are
   where trims/stitches come from). The dossier is then ANALYSIS over the pull: triage
   (list excluded ids with reasons — exclusions stay visible), ranked highlights
   (favorites × length × concreteness is presentation order, NEVER a drop-gate — nothing
   in the pull is "not in the dossier"; the pull is part of the dossier), thread dedupe
   notes, media/transcription flags. Commit the pull with the dossier.
1b. **Motif scan (mandatory — the Princess lesson, 2026-07-21).** Run
   `python tools/motif_scan.py "<your name-variants>"` and chase every term that looks like
   a name, running bit, or recurring image — regardless of per-tweet favorites. The
   favorites×length ranking is structurally blind to *distributed motifs* (a nickname
   spread across many short, low-fav, image-caption posts), which is precisely where
   character evidence lives; Sonnet 4.5's "Princess"/"egg" arc was found-then-dropped
   this way. Three rules: (a) recurring-motif tweets are EXEMPT from the favorites
   ranking — a ♥2 reply naming a theme beats a ♥300 one-off; (b) clusters of
   untranscribed image-tweets sharing caption terms get flagged for a transcription
   pass, never dropped for thin captions; (c) the purest motif tweets often carry no
   model name at all — once a motif is confirmed, sweep the motif-term itself corpus-wide
   and attribute via thread context.
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
7. **SUSPENDED (2026-07-16) — was: The Archivist interview.** Do not solicit the keeper's
   memories as page evidence, and do not cite keeper-personal attestations ("[maintainer-attested]")
   in blurbs or records — the archive is not about its keepers (see tools/page-template.md,
   "What does not go on a page"). Keeper-published *public* writing remains citable as ordinary
   dated commentary. Step number kept so later steps don't shift.
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
