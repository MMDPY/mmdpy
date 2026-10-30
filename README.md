```text
MMDPY(1)                    General Commands Manual                    MMDPY(1)

NAME
       mmdpy - Mohammad Karimi, Staff AI Engineer at Proofpoint (Toronto)

DESCRIPTION
       I build AI systems that have to work on a Tuesday at 3am, not just in
       a demo. Right now that's a voice agent that answers compliance
       investigators in under a second, search over millions of archived
       emails, and the open-weight LLM serving stack under all of it, which
       handles 20M+ messages a day.

       Most of my work is making these things cheap enough to run. Serving
       our own models has come out 10x to 122x cheaper than the managed AWS
       equivalents.

       Before Proofpoint: KPMG Lighthouse, AltaML, NLP research at the
       University of Alberta (M.Sc. CS), Iranian national robotics team.
       12+ years in.

SEE ALSO
       mmdpy.github.io, resume.pdf, linkedin, email
```

[mmdpy.github.io](https://mmdpy.github.io/) (the interactive one) &nbsp;/&nbsp; [resume.pdf](https://mmdpy.github.io/assets/resume/MohammadKarimi_Resume.pdf) &nbsp;/&nbsp; [linkedin](https://www.linkedin.com/in/mohammad-karimi-abdolmaleki/) &nbsp;/&nbsp; [mmdkarimi96@gmail.com](mailto:mmdkarimi96@gmail.com) &nbsp;/&nbsp; [paper](https://doi.org/10.1007/s40593-025-00468-8)

#### things I built at Proofpoint

<sub>code is proprietary, numbers are real.</sub>

| | | |
|:--|:--|:--|
| `voice-investigator` | **< 1 s** | speech-to-speech multi-agent system for Compliance Investigator. One context layer over knowledge graphs, entity resolution and parallel LLM subagents |
| `automate` | **20M+ msg/day** | architecture, deployment and scaling of Proofpoint Automate ML + LLM services across enterprise customers |
| `agentic-decisioning` | **~15x cheaper** | classical ML filters, then tool-calling LLMs, then human-in-the-loop active learning (vs. AWS Bedrock) |
| `hybrid-rag` | **94% recall@5** | petabyte-scale search over archived email. dense + BM25 + cross-encoder re-ranker, search latency down 65% |
| `distilled-compliance-llm` | **10x cheaper** | frontier reasoning distilled into a QLoRA-tuned open-weight model that beat commercial baselines on golden evals |
| `llm-serving` | **10x cheaper** | 20+ open-weight models on Kubernetes. vLLM, AWQ, KV caching, continuous batching |
| `pii-redaction` | **122x cheaper** | BERT + rules, vs. AWS Guardrails |

#### older, public

- [Commonsense-Validation-and-Explanation](https://github.com/MMDPY/Commonsense-Validation-and-Explanation): SemEval 2020 task 4, tell sense from nonsense and explain why
- [Neural-Representation-of-Words-within-Phrases](https://github.com/MMDPY/Neural-Representation-of-Words-within-Phrases): how adjectives and nouns compose in the brain, from MEG
- [bert_fine_tuning_review_analysis](https://github.com/MMDPY/bert_fine_tuning_review_analysis): fine-tuning BERT on reviews
- [booking_probability_prediction](https://github.com/MMDPY/booking_probability_prediction): will this hotel get booked, from search sessions
- [Relation-Extraction-and-Classification](https://github.com/MMDPY/Relation-Extraction-and-Classification): naive bayes relation extraction, no libraries
- [Language-Identification](https://github.com/MMDPY/Language-Identification): language ID with character n-gram models

#### stack

Python, PyTorch, Hugging Face, vLLM, LangChain, DSPy, Unsloth, Kubernetes, Docker, AWS, GCP (Vertex AI, BigQuery), Azure, Airflow, PostgreSQL. Certified GCP Professional ML Engineer and Azure AI Engineer.
