# Muse Spark Open

    
Meta (Meta Superintelligence Labs) · weights released 15 Oct 2026 · current (Muse Model License)
    
Released 15 October 2026 with downloadable weights — 816 billion parameters, 42 billion active, 1M-token context — under Meta’s Muse Model License, which Meta says has “limited commercial terms”. Meta calls it “The open-weight version of Muse Spark”, given “additional safety post-training” for use without system guardrails, and released it two months after the 30B [Muse Glimmer](../muse-glimmer/) and three days after [Muse Wonder](../muse-wonder/), following weeks of users asking when Muse Spark weights would appear.
    
Thin — one week old. The record is Meta’s release post, the model card (rendered on the gated Hugging Face page) and an evaluation-methodology note. No corpus matches yet (supplement db through 2026-10-21). Sourcing skew, named: entirely official so far.

    
## Sources

    
### Official

    

      
- 2026-10-15 [Introducing Muse Spark Open, The Most Capable US Open‑Weight Model to Date](https://research.meta.ai/blog/muse-spark-open) (Meta) — “Today, we’re releasing the weights for Muse Spark Open, the most capable US open-weight model to date. Muse Spark Open is a natively multimodal model with 816B total parameters (42B active) and a 1M-token context window.” On running it locally: “Muse Spark Open is the first model in its class to run on your desktop using two Apple M5 Ultra Mac Studios with the latest MLX framework.” On safety: “Open weights also carry their own considerations, and Muse Spark Open has additional safety post-training for that reason.” On license: “We’re releasing the weights under the Muse Model License with limited commercial terms, which allow many developers to use the model for free.”
      
- 2026-10-15 [Muse Spark Open model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) (Hugging Face, gated download; card text rendered on the page) — “This open weights version has additional safety post-training to make it more robust against misuse as a standalone model without system guardrails.” Mixture-of-Experts transformer with a perception encoder; 256 experts, 8 active per token; input text, image, video and audio, output text. Collection: [meta-models/muse-spark-open](https://huggingface.co/collections/meta-models/muse-spark-open).
      
- 2026-10-15 [Muse Spark Open Evaluation Methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) (PDF) — comparison settings against other open-weight models (including [Inkling](../inkling/), [Kimi K3](../kimi-k3/), GLM 5.3 and Qwen3.8).
      
- 2026-10-02 [Developing capable models responsibly](https://research.meta.ai/blog/developing-capable-models-responsibly) (Meta) — the framework revision covering open releases: “Someone holding the weights can resample to get around a refusal, prefill outputs, or fine-tune refusal behavior away.”
      
- tk — the full evaluation report (promised “soon”); the Muse Model License text; independent benchmarks.
    
    
### Writing & commentary

    
tk — no independent coverage retrieved in this pass.
    
### Tweets

    
No corpus matches on muse spark open / muse-spark-open / spark open through 2026-10-21. The weights-release requests that preceded it are recorded on the [Muse Spark](../muse-spark/) page (@jmbollenbacher, 2026-09-06 and 10-12).

    
## Official record

    

      
- Weights released 15 October 2026 on Hugging Face (gated), Amazon SageMaker AI, Google Cloud Model Garden and Microsoft Foundry Models, in BF16 and NVFP4; hosted inference through Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter and Together AI. License: Muse Model License. CONFIRMED
      
- Model card: 816B total / 42B active parameters; 62 layers; 256 experts with 8 active per token; a 1.8B-parameter perception encoder; context “1M at inference”; vocabulary 202,048; “Multilingual, trained on data from more than 100 languages”; self-hosting needs “a GPU with at least 700GB of VRAM for NVFP4 and 2TB for BF16.” The published chat template defaults cutoff_date to 2026-01-04. CONFIRMED
      
- Headline numbers as published (Meta’s table, xhigh effort): Artificial Analysis Intelligence Index 39 (GLM 5.3 45, Kimi K3 44, Qwen3.8 40, Inkling 26); MCP-Atlas 89.2. CONFIRMED (as published)
      
- Jailbreak robustness (model card, Safety rows): on StrongREJECT v2 (adaptive), lower is better, Muse Spark Open 0.5 against Inkling 86.4, Nemotron 3 Ultra 80.7, Kimi K3 66.6, Qwen3.8 65.6, GLM 5.3 62.9. On cyber misuse with adaptive attackers and no system safeguards: “The model refused 99.2% of jailbreaks on our internal benchmark and 94.8% when aggregating across PolyGuard (cyber subset), RedCode, and CyberBench 2024.” CONFIRMED (as published)
      
- Loss of control (model card): “On our misalignment evaluations, the model showed low propensity for deceptive or unilateral harmful behavior, with a 98.1% honesty rate on the MASK benchmark and a 0% misbehavior rate on the Agentic Misalignment benchmark.” The card adds: “Downstream modifications could degrade safety, and results for the released checkpoint should not be assumed to apply to modified models.” CONFIRMED
      
- Deployment guidance (model card): “For user-facing applications, developers should avoid exposing raw chain-of-thought and apply appropriate safety checks to any reasoning summaries.” A noted quirk: with very short or low-resolution videos, “the model may sometimes reply that it can't view the video.” CONFIRMED
    

    
## History

    

      
- 2026-04-08 → 09-02 Closed first: [Muse Spark](../muse-spark/) and its point releases ship without weights; Meta’s only open-weight Muse model is the 30B [Muse Glimmer](../muse-glimmer/) (10 Aug, Apache 2.0).
      
- 2026-09-06 → 10-12 The asking: users press Meta on Muse Spark weights (“'Soon' and a month later theres no update”; “So, Meta is definitely not open sourcing their models anymore, are they?” — @jmbollenbacher).
      
- 2026-10-02 Framework: Meta revises its Superintelligence Scaling Framework, adding open-weight considerations, after White House commitments.
      
- 2026-10-15 Release: three days after [Muse Wonder](../muse-wonder/), the weights go out under the Muse Model License, with Mac Studio (MLX) support and custom Helion GPU kernels for SGLang.
    

    
## Impressions

    

      
- tk — too new: no corpus record or independent reports yet. Watch for: whether the extra safety post-training reads as refusal-heavy in use (its StrongREJECT figure is far below the other open models listed); fine-tuned derivatives; how it compares in character with the served Muse Spark versions.
    

    
[← back to the Pantheon](../)
