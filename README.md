<a href="https://mmdpy.github.io/">
  <img src="./assets/terminal.svg" alt="mohammad@toronto — Staff AI Engineer @ Proofpoint. Sub-second speech-to-speech agent, 20M+ messages/day, 10–122× cheaper inference." width="100%" />
</a>

<p align="center">
  <a href="https://mmdpy.github.io/"><img src="https://img.shields.io/badge/❯_mmdpy.github.io-07090c?style=for-the-badge&labelColor=07090c&color=3ddc97" alt="website" /></a>
  <a href="https://www.linkedin.com/in/mohammad-karimi-abdolmaleki/"><img src="https://img.shields.io/badge/linkedin-07090c?style=for-the-badge&logo=linkedin&logoColor=3ddc97" alt="LinkedIn" /></a>
  <a href="mailto:mmdkarimi96@gmail.com"><img src="https://img.shields.io/badge/email-07090c?style=for-the-badge&logo=gmail&logoColor=3ddc97" alt="email" /></a>
  <a href="https://doi.org/10.1007/s40593-025-00468-8"><img src="https://img.shields.io/badge/paper_·_IJAIED_2025-07090c?style=for-the-badge&logo=springer&logoColor=3ddc97" alt="paper" /></a>
</p>

```console
mohammad@toronto ~ ❯ cat about.txt
Staff AI Engineer @ Proofpoint. I build AI systems that hold up in production:
agents that reason and use tools, a speech agent that answers in under a second,
RAG over millions of messages, and inference stacks that run 10–122× cheaper
than managed cloud services.
```

### `❯ ls ~/systems` <sub>— in production at Proofpoint (descriptions only; code is proprietary)</sub>

| system | what it does | number |
|:--|:--|--:|
| **`voice-investigator`** | Speech-to-speech compliance agent. Context layer over messages, docs, entities, context graphs, classifier outputs, and LLM subagents | **< 1 s** |
| **`automate-models`** | ML + LLM models I develop, deploy, and maintain for enterprise customers | **20M+ msgs/day** |
| **`agentic-decisioning`** | LLM reasoning + classical models + tools + human feedback for supervision decisions | **~15× cheaper** |
| **`archive-rag`** | Plain-English search over millions of archived emails; semantic chunking + LLM re-ranker | **94% recall@5** |
| **`llm-serving`** | 20+ open-weight models on Kubernetes · vLLM · KV cache · quantization · CPU offload | **10× cheaper** |
| **`redaction-api`** | Hybrid BERT + rules PII masking vs. AWS Guardrail | **122× cheaper** |

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
  "llm":       ["agents", "subagents", "tool use", "RAG", "DSPy", "GEPA", "LangChain"],
  "inference": ["vLLM", "KV cache", "continuous batching", "quantization"],
  "ml":        ["PyTorch", "Transformers", "Unsloth", "Longformer", "BERT", "XGBoost"],
  "infra":     ["Kubernetes", "Docker", "Airflow", "AWS Bedrock", "GCP Vertex AI", "Azure"],
  "certs":     ["GCP Professional ML Engineer", "Azure AI Engineer", "+20 more"]
}
```

```console
mohammad@toronto ~ ❯ git log --oneline --reverse
a1f3e09  robotics: Faster R-CNN on ROS                    — Iranian National Robotics Team
b72c4d1  research: neural LMs, 97% grammar detection     — University of Alberta (M.Sc.)
c9e0a5f  prod: GPT-3.5 bias classifier, 2.6B geo points   — AltaML
d4b8e21  prod: agentic LLM + RAG on GCP                   — KPMG Lighthouse
e5f1c7a  prod: speech agents, 20M+ msgs/day               — Proofpoint  (HEAD -> main)
```

<p align="center"><sub>❯ the interactive version lives at <a href="https://mmdpy.github.io/">mmdpy.github.io</a>. try <code>sudo hire-me</code></sub></p>
