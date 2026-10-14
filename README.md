# Deep Learning to GPU/ML Inference Engineering

This is where I keep the code and experiments from my learning roadmap. I work in computer vision, and I am building a deeper understanding of how models execute, how to find their bottlenecks, and how to deploy them efficiently.

The roadmap runs for 12 months alongside my job, with a target of 10 focused hours a week. It moves from PyTorch fundamentals and computer vision to Transformers, real-time video pipelines, GPU programming, and LLM serving.

I am sharing the work so other engineers can follow along, use the roadmap to plan their own study, and compare what they learn with working examples.

## Start here

- [The roadmap](ROADMAP.md): phases, implementations, deliverables, and exit criteria.
- [Resources](RESOURCES.md): the books and documentation used for each part of the roadmap.
- [My current code](1.Pytorch/My-code/ch3-tensors/): small experiments from Chapter 3 on tensors.
- [My website](https://www.lakshaybhatia.com/): the home of my writing and portfolio.

## Current progress

Updated **14 October 2026**.

| Item | Status |
|---|---|
| Current phase | Phase 1: PyTorch and Deep-Learning Repair |
| Current book | *Deep Learning with PyTorch, Second Edition*, Manning |
| Latest chapter completed | Chapter 3: tensors |
| Code available | Small scripts exploring indexing, shapes, storage, broadcasting, and channel dimensions |
| Phase 1 deliverable | In progress |

Completing a chapter is one step toward the phase deliverable. The training loop, tests, and debugging evidence described in the roadmap will be added as I build them.

## The route

| Phase | Weeks | Focus | Planned deliverable |
|---|---|---|---|
| 1 | 1–4 | PyTorch foundations | `pytorch-foundations` |
| 2 | 5–10 | Detection, tracking, and CV error analysis | `sports-cv-analysis` |
| 3 | 11–18 | Transformers and KV caching | `transformer-from-scratch` |
| 4 | 19–26 | Real-time CV deployment and runtime comparisons | `realtime-cv-inference` |
| 5 | 27–34 | C++, CUDA, Triton, and GPU profiling | `gpu-kernel-lab` |
| 6 | 35–42 | Batching, caches, and LLM inference | `mini-llm-runtime` |
| 7 | 43–48 | vLLM, with an SGLang comparison | `llm-serving-benchmarks` |
| 8 | 49–52 | Architecture case studies and an integrated capstone | GPU inference portfolio and technical report |

These are planned deliverables, not completed projects. The existing code stays in its current location; later implementations will be linked here as they are added.

## Repository layout

```text
DL-Inference-learning/
├── README.md
├── ROADMAP.md
├── RESOURCES.md
├── requirements.txt
└── 1.Pytorch/
    └── My-code/
        └── ch3-tensors/
            ├── tensors.py
            ├── tensor-storage.py
            ├── broadcasting.py
            └── named-tensors.py
```

`My-code` contains the scripts I write while studying. Some follow examples from the book, which is credited in [Resources](RESOURCES.md). The downloaded book source is kept locally and excluded from this repository; the authors' original code is [available here](https://github.com/deep-learning-with-pytorch/dlwpt-code-2e).

## Run the current scripts

The current local environment uses Python 3.12 and PyTorch 2.14.0. From the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python 1.Pytorch/My-code/ch3-tensors/tensors.py
```

The other Chapter 3 files can be run the same way. They are exploratory scripts; some expressions are intended to be inspected in a REPL and do not print a result when run as a script.

For an installation suited to a particular GPU, use the [official PyTorch installation selector](https://pytorch.org/get-started/locally/). Environments, datasets, and generated model files are excluded from Git.

## How I am learning

- Read a small section, then recall it in my own words before reopening the book.
- Predict what the code will do before running it.
- Keep the questions and unexpected results that come out of those experiments.
- Make the first implementation attempt myself, and use AI for review and help when needed.
- For performance work, record correctness, hardware, software versions, warm-up, latency, throughput, and memory.

If you are following along, choose the phase relevant to you, make your own implementation attempt, and keep your own measurements. The exit criteria in [ROADMAP.md](ROADMAP.md) are a better progress check than the number of chapters read.

## Follow the work

- [Portfolio and blog](https://www.lakshaybhatia.com/)
- [Substack](https://loopbreaker143.substack.com/)
- [X](https://x.com/lakshayb143)
- [LinkedIn](https://www.linkedin.com/in/lakshaybhatia/)

You can watch the repository for updates or open an issue with a correction or a reproducible problem in one of the examples.
