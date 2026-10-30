<a href="https://mmdpy.github.io/">
  <img src="./assets/terminal.svg" alt="mmdpy — Staff AI Engineer @ Proofpoint. Sub-second speech-to-speech agent, 20M+ messages/day, 10–122× cheaper inference." width="100%" />
</a>

<p align="center">
  <a href="https://mmdpy.github.io/"><img src="./assets/btn-website.svg" alt="mmdpy.github.io" /></a>
  <a href="https://mmdpy.github.io/assets/resume/MohammadKarimi_Resume.pdf"><img src="./assets/btn-resume.svg" alt="resume.pdf" /></a>
  <a href="https://www.linkedin.com/in/mohammad-karimi-abdolmaleki/"><img src="./assets/btn-linkedin.svg" alt="LinkedIn" /></a>
  <a href="mailto:mmdkarimi96@gmail.com"><img src="./assets/btn-email.svg" alt="email" /></a>
  <a href="https://doi.org/10.1007/s40593-025-00468-8"><img src="./assets/btn-paper.svg" alt="paper · IJAIED 2025" /></a>
</p>

```console
mmdpy ~ ❯ cat about.txt
Staff AI Engineer @ Proofpoint. I architect and ship multi-agent, RAG, and
document-intelligence systems end to end — from research prototype to Kubernetes
services handling 20M+ messages/day — with LLM inference that runs 10–122×
cheaper than managed AWS services.
```

### `❯ ls ~/systems` <sub>— in production at Proofpoint (descriptions only; code is proprietary)</sub>

| system | what it does | number |
|:--|:--|--:|
| **`voice-investigator`** | Speech-to-speech multi-agent system for Compliance Investigator: unified context layer over knowledge graphs, entity resolution, and parallel LLM subagents | **< 1 s** |
| **`automate-inference`** | Proofpoint Automate's LLM inference platform: 20+ open-weight models on Kubernetes · vLLM · AWQ · prefix/KV caching · continuous batching, 10–15× cheaper than Bedrock | **20M+ msgs/day** |
| **`agentic-decisioning`** | Cascade for Supervision: classical ML filters → tool-calling LLMs → human-in-the-loop active learning | **−45% false positives** |
| **`hybrid-rag`** | Petabyte-scale search over millions of archived emails: dense embeddings + BM25 + cross-encoder re-ranker, −65% query latency | **94% recall@5** |
| **`distilled-compliance-llm`** | Frontier-model reasoning distilled into a QLoRA-tuned open-weight LLM; +40% AWS Nova F1 via function calling + DSPy/GEPA | **beats commercial baselines** |
| **`redaction-api`** | Hybrid BERT PII redaction, alongside Longformer classification (90%+ F1) with Integrated Gradients | **122× cheaper** |

### `❯ ls ~/oss`

| repo | |
|:--|:--|
| [**Commonsense-Validation-and-Explanation**](https://github.com/MMDPY/Commonsense-Validation-and-Explanation) | SemEval 2020 Task 4. Can a model tell sense from nonsense, and explain why? |
| [**bert_fine_tuning_review_analysis**](https://github.com/MMDPY/bert_fine_tuning_review_analysis) | Fine-tuning BERT for review analysis |
| [**booking_probability_prediction**](https://github.com/MMDPY/booking_probability_prediction) | End-to-end: will this hotel get booked, given the search session? |
| [**Neural-Representation-of-Words-within-Phrases**](https://github.com/MMDPY/Neural-Representation-of-Words-within-Phrases) | Decoding adjective–noun composition from MEG brain signals |
| [**Relation-Extraction-and-Classification**](https://github.com/MMDPY/Relation-Extraction-and-Classification) | Naive Bayes relation extraction, from scratch |
| [**Language-Identification**](https://github.com/MMDPY/Language-Identification) | Character-level n-gram language models |

### `❯ cat stack.json`

```json
{
  "llm":       ["multi-agent", "LangGraph", "LangChain", "tool calling", "hybrid RAG", "DSPy", "GEPA"],
  "inference": ["vLLM", "AWQ", "prefix/KV caching", "continuous batching"],
  "ml":        ["PyTorch", "Hugging Face", "QLoRA", "Unsloth", "Longformer", "BERT", "XGBoost"],
  "infra":     ["Kubernetes", "Docker", "Airflow", "AWS Bedrock", "GCP Vertex AI", "Azure"],
  "certs":     ["GCP Professional ML Engineer", "Azure AI Engineer", "+20 more"]
}
```

```console
mmdpy ~ ❯ git log --oneline --reverse
a1f3e09  robotics: imagery pipeline + Faster R-CNN        — Iranian National Robotics Team
b72c4d1  research: neural LMs, 97% grammar detection     — University of Alberta (M.Sc.)
c9e0a5f  prod: GPT-3.5 bias classifier, 2.6B geo points   — AltaML
d4b8e21  prod: agentic LLMs + RAG on GCP                  — KPMG Lighthouse
e5f1c7a  prod: multi-agent speech, 20M+ msgs/day          — Proofpoint  (HEAD -> main)
```

<p align="center"><sub>❯ the interactive version lives at <a href="https://mmdpy.github.io/">mmdpy.github.io</a>. try <code>sudo hire-me</code></sub></p>
