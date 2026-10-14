# Learning roadmap

A public version of my current roadmap from computer vision to GPU/ML inference engineering. The week ranges are planning targets; the implementations and exit criteria determine progress.

**Current status:** Phase 1 in progress. Chapter 3 on tensors in *Deep Learning with PyTorch, Second Edition* completed.

**Plan:** 12 months, 10 focused hours per week alongside work.

[README](README.md) · [Resources](RESOURCES.md)

## North Star

Become an ML systems and inference engineer who can take computer-vision, transformer, and multimodal models from PyTorch research code to fast, reliable production systems.

This roadmap does not abandon computer vision. Detection, tracking, video pipelines, and small-object problems remain your domain advantage. The new emphasis is understanding how models execute, profiling them, optimizing them, and serving them efficiently on GPUs.

Duration: 12 months

Commitment: 10 focused hours per week alongside work

Primary languages: Python, C++, CUDA

Primary stack: PyTorch, GStreamer, DeepStream, ONNX, TensorRT, CUDA/Triton, vLLM, SGLang

## Weekly Structure

Use the following split during most phases:

- 6 hours: Current roadmap phase and its main project
- 2 hours: C++ initially; CUDA/Triton later
- 2 hours: DSA and interview problem solving

During the dedicated CUDA phase, combine the first two categories:

- 8 hours: CUDA/Triton, GPU profiling, and the phase project
- 2 hours: DSA

### A Practical Week

- Monday: 1 hour theory or mathematics
- Tuesday: 1 hour implementation
- Wednesday: 1 hour C++/CUDA
- Thursday: 1 hour implementation
- Friday: 1 hour DSA
- Saturday: 4 hours project work, experiments, and measurements
- Sunday: 1 hour DSA, review, or catch-up

Missing one day is not failure. Preserve the weekly total and the phase deliverable.

## Rules for Learning

### 1. Implementation before collection

Do not collect five courses on a topic. Select one primary resource, implement the concept, test it, and proceed.

### 2. Use mathematics just in time

Study the mathematics needed for the current implementation:

- Linear algebra: vectors, matrices, dot products, matrix multiplication, transpose, norms
- Calculus: derivatives, partial derivatives, chain rule, gradients
- Probability: mean, variance, distributions, softmax and cross-entropy
- Systems math: FLOPs, bandwidth, arithmetic intensity, latency percentiles

Do not pause the roadmap for a separate six-month mathematics curriculum.

### 3. Use AI without surrendering the implementation

For every important component:

- Read the concept and write tensor shapes or pseudocode.
- Make the first implementation attempt yourself.
- Write at least one test yourself.
- Use AI to review, explain errors, suggest tests, or compare designs.
- Rewrite any code you cannot explain line by line.

### 4. Measure everything

Every deployment or optimization project must record:

- Correctness or model-quality metric
- Batch size and input/sequence length
- Hardware and software versions
- Warm-up procedure
- Median and p95 latency
- Throughput
- Peak CPU/GPU memory
- GPU utilization when available

An optimization without a reproducible measurement is only a guess.

### 5. One repository per substantial project

Each repository should contain:

- Clear problem statement
- Architecture diagram or concise design description
- Reproduction commands
- Tests
- Benchmark methodology
- Results table
- Bottleneck analysis
- Limitations and next steps

## Phases

### Phase 1: PyTorch and Deep-Learning Repair

**Weeks 1–4**

#### Learn

- Tensors, shapes, strides, broadcasting, views, and contiguous memory
- Matrix multiplication and common tensor transformations
- Autograd and computation graphs
- nn.Module, parameters, initialization, train/eval modes
- Dataset, DataLoader, batching, and device transfers
- Cross-entropy and gradient descent
- SGD, momentum, and AdamW conceptually
- Mixed precision basics
- Overfitting one batch as a debugging test
- Gradient norms and activation statistics

#### Implement

- Linear regression using tensors and manual gradient descent
- A small MLP with a handwritten training loop
- Cross-entropy once using tensor operations
- A small CNN and residual block
- A small ResNet-18-style model using PyTorch building blocks

Do not implement a complete ResNet-50 or spend weeks reproducing high CIFAR accuracy. The purpose is to understand execution, gradients, and debugging.

#### Mathematics

- Matrix multiplication and tensor dimensions
- Chain rule and partial derivatives
- Mean, variance, and normalization
- Softmax and cross-entropy gradients

#### Deliverable

- Create pytorch-foundations containing the implementations, shape tests, a training loop, gradient/activation plots, and a short debugging checklist.

#### Exit Criteria

- You can write a training and evaluation loop without copying one.
- You can explain what autograd stores and when gradients accumulate.
- You can diagnose a model that cannot overfit one batch.
- You can explain BatchNorm, LayerNorm, residual connections, and mixed precision.

### Phase 2: Preserve Core Computer-Vision Depth

**Weeks 5–10**

The goal is to retain and strengthen the CV knowledge directly connected to your professional experience. It is not to rebuild the entire history of computer vision.

#### Learn

**Detection**

- Image resizing, normalization, and coordinate transformations
- IoU, GIoU, and bounding-box encoding
- Confidence thresholds, precision, recall, and mAP
- NMS and why DETR-style detectors avoid it
- Multi-scale features and FPN
- Anchor-based versus anchor-free detection
- DETR: object queries, encoder/decoder structure, and Hungarian matching
- RF-DETR design choices relevant to your current work

**Tracking**

- State vectors and constant-velocity motion models
- Kalman-filter predict/update intuition
- IoU and appearance-based association
- Hungarian assignment
- SORT and ByteTrack principles
- Track lifecycle, occlusion, identity switches, and evaluation

**Training and Debugging**

- Data and annotation validation
- Class imbalance and hard examples
- Learning-rate schedules and warm-up
- AMP, checkpointing, and resuming
- Inspecting separate loss components
- Error analysis by class, size, and scene type

#### Implement

- IoU and NMS using tensor operations
- Hungarian association on a toy tracking sequence (Scope: already production experience; move through quickly)
- A minimal Kalman filter or SORT implementation (Scope: already production experience; move through quickly)
- A small DETR attention/matching inspection—not a complete detector training project (Scope: already production experience; move through quickly)

#### Work-Focused Experiment

Select one public or safely reproducible sports dataset and perform an error analysis similar to your production work:

- Small ball versus large player detections
- False positives and missed detections by object size
- Tracking failures caused by detector confidence or occlusion
- Latency distribution across pipeline stages

#### Deliverable

- Create sports-cv-analysis with visualizations, metrics, failure cases, and three evidence-backed improvement proposals.

#### Exit Criteria

- You can explain your detection/tracking pipeline below the API level.
- You can distinguish model errors from data, post-processing, and association errors.
- You can identify the stage responsible for a latency or quality regression.

### Phase 3: Transformers from First Principles

**Weeks 11–18**

Build a decoder-only language Transformer first. This gives you the foundation for LLM inference. Relate it back to ViT and DETR so your CV knowledge remains connected.

#### Learn in This Order

- Token embeddings and vocabulary logits
- Scaled dot-product attention
- Causal masks
- Multi-head self-attention
- Residual connections and pre-normalization
- Feed-forward networks and SwiGLU
- Positional embeddings and RoPE
- RMSNorm
- Autoregressive decoding
- KV caching
- MQA and GQA
- Training versus inference execution

#### Implement

- Single-head attention using raw tensor operations
- Multi-head causal self-attention
- One manual attention backward exercise, verified against autograd (Scope: training-focused; keep to one quick pass, do not go deep)
- A Transformer decoder block
- A small GPT-style model
- Greedy and temperature-based sampling
- Cached and uncached autoregressive generation
- GQA as a modification to standard attention

Train only a small model on TinyStories, Shakespeare, or another manageable dataset. You are learning the architecture and runtime—not trying to produce a competitive language model.

#### Connect Back to CV

- Compare sequence tokens with ViT patch tokens
- Compare causal attention with bidirectional ViT attention
- Understand DETR cross-attention and object queries
- Inspect how a vision encoder connects to an LLM in a simple VLM

#### Deliverable

- Create transformer-from-scratch containing tests for tensor shapes, causal masking, cached decoding correctness, and benchmarks comparing cached versus uncached generation.

#### Exit Criteria

- You can draw and explain a decoder-only Transformer.
- You can calculate the shape of Q, K, V, attention scores, and KV caches.
- You can explain why decoding is sequential and often memory-bandwidth sensitive.
- You can implement KV caching without copying an existing cache implementation.

### Phase 4: Real-Time CV Deployment

**Weeks 19–26**

This phase turns your existing CV experience into systems experience.

#### Learn

**Video and Pipeline Systems**

- GStreamer elements, pads, caps, pipelines, queues, and backpressure
- Decode, color conversion, preprocessing, inference, tracking, and rendering stages
- CPU/GPU synchronization and avoidable copies
- Threading, bounded queues, dropped frames, and latency accumulation
- Throughput versus end-to-end latency
- Hardware-accelerated decode/encode (NVDEC/NVENC) and zero-copy buffer paths
- DeepStream as a GPU-native alternative to a plain CPU-decode GStreamer pipeline

**Model Export and Runtime**

- model.eval() and inference mode
- Static versus dynamic shapes
- PyTorch export limitations
- ONNX graph structure and shape inference
- ONNX Runtime profiling
- TensorRT engines, precision modes, and optimization profiles
- FP32, TF32, FP16, BF16, and INT8 trade-offs
- Calibration and accuracy validation after quantization

**Edge Inference (Jetson)**

- TensorRT on Jetson boards, unified memory, and power/thermal limits
- Running the same pipeline on an edge device versus a discrete GPU, and what changes in the profile

#### Build

Create a real-time sports-video pipeline:

video/RTSP -> decode -> preprocess -> RF-DETR or comparable detector -> tracking -> overlay/output

Develop it incrementally:

- Establish a correct PyTorch baseline.
- Measure time spent in decode, preprocessing, inference, tracking, and rendering.
- Export the model to ONNX.
- Run and validate ONNX Runtime inference.
- Build a TensorRT version if supported by the available GPU/runtime.
- Reduce unnecessary copies and synchronization.
- Measure quality and performance after every change.
- Optionally deploy the same pipeline on a Jetson (or comparable edge device) and compare against the discrete-GPU numbers.

Use a public model and public data in the portfolio version if work assets are private.

#### Deliverable

- Create realtime-cv-inference with a GStreamer pipeline, runtime adapters, correctness checks, profiling traces, and a benchmark table across available backends.

#### Exit Criteria

- You can explain where every millisecond in the pipeline goes.
- You can export, validate, and benchmark a CV model outside PyTorch.
- You can discuss accuracy/latency/memory trade-offs rather than only mAP.
- You understand how decode and data movement can dominate model inference.

### Phase 5: C++, CUDA, Triton, and GPU Performance

**Weeks 27–34**

Continue C++ Primer before and during this phase. You do not need to finish the entire book before starting CUDA, but you should be comfortable with functions, references, containers, classes, RAII, compilation, and basic debugging.

#### Learn

**C++ and Tooling**

- Compilation, linking, headers, libraries, and CMake
- References, const-correctness, lifetime, and ownership
- RAII and smart pointers
- Basic concurrency concepts
- Unit tests and debugger usage

**GPU Architecture**

- Threads, blocks, grids, warps, and SIMT execution
- Global, shared, register, constant, and host memory
- Coalesced access and memory transactions
- Branch divergence
- Occupancy and register pressure
- Synchronization and asynchronous execution
- Streams, events, and host/device transfers
- Compute-bound versus memory-bound kernels

**Kernel Work**

- Vector addition
- Matrix transpose
- Reduction
- Naive matrix multiplication and tiled matrix multiplication
- Softmax
- RMSNorm or LayerNorm
- One fused operation
- Equivalent Triton implementation for at least two kernels

Do not try to outperform cuBLAS at general matrix multiplication. Use vendor libraries as the production baseline and kernels as a vehicle for understanding.

**Compilation and Graph Capture**

- torch.compile and TorchInductor: graph capture, guards, and recompilation
- CUDA graphs, and why they remove per-step launch overhead during decoding
- Where a compiled graph is enough, and where a hand-written or fused kernel is still needed

**Production Kernel Libraries (Reading Only)**

- FlashAttention and FlashInfer as reference implementations of a fused, memory-aware attention kernel
- CUTLASS/CuTe at an introductory level — enough to navigate the code production kernels are built on, not to author it

#### Profiling

- PyTorch Profiler
- Nsight Systems for timeline and synchronization analysis
- Nsight Compute for kernel-level analysis
- Warm-up, repeated trials, and synchronization-correct timing

#### Deliverable

- Create gpu-kernel-lab with correctness tests and benchmarks against PyTorch or suitable library operations. Each result must explain why the custom kernel wins or loses.

#### Exit Criteria

- You can write, launch, test, and time a CUDA kernel correctly.
- You can recognize uncoalesced access and excessive synchronization.
- You can use a profiler instead of guessing about bottlenecks.
- You understand why fusion can improve performance by reducing memory traffic.

### Phase 6: LLM Inference Fundamentals

**Weeks 35–42**

#### Learn

- Prompt prefill versus autoregressive decoding
- Time to first token (TTFT)
- Time per output token (TPOT) and inter-token latency
- Requests per second and tokens per second
- KV-cache size and memory calculations
- Static, dynamic, and continuous batching
- Chunked prefill
- Prefix caching
- Paged KV-cache management
- Weight and activation quantization
- FP8 formats, and where they apply (weights, activations, KV cache)
- Weight-only 4-bit methods (AWQ, GPTQ) and their accuracy trade-offs
- FP4/NVFP4 on newer (Blackwell-class) GPUs
- Speculative decoding
- Tensor, pipeline, data, and expert parallelism
- Prefill/decode disaggregation across separate GPUs or nodes
- Collective communication basics (all-reduce, all-to-all) via NCCL — enough to reason about tensor- and expert-parallel cost
- Single-GPU versus multi-GPU bottlenecks
- Correctness, latency, throughput, memory, and cost trade-offs

#### Implement a Mini Inference Runtime

Extend transformer-from-scratch with:

- Batched prompt prefill
- Per-request KV caches
- Dynamic request arrival simulation
- A simple continuous-batching scheduler
- Cache block allocation or a simplified paged-cache design
- Benchmarking for different prompt/output lengths and concurrency levels

The runtime can be educational and small. The purpose is to understand why production engines are designed the way they are.

#### Deliverable

- Create mini-llm-runtime with a written comparison between naive generation, cached generation, static batching, and continuous batching.

#### Exit Criteria

- You can estimate KV-cache memory for a given architecture and sequence length.
- You can explain why higher throughput may worsen latency.
- You can distinguish a scheduler optimization from a kernel optimization.
- You can design a benchmark that does not hide warm-up or queuing effects.

### Phase 7: vLLM and SGLang

**Weeks 43–48**

Learn vLLM first, then compare it with SGLang. Using both as command-line tools is not sufficient.

#### vLLM

- Run a supported small model and expose its API
- Measure TTFT, TPOT, throughput, and memory
- Explore scheduler and memory-related configuration
- Understand continuous batching and PagedAttention conceptually
- Locate model definitions, request scheduling, cache management, and worker execution in the codebase
- Compare precision/quantization options available on your hardware
- Profile at least one workload

#### SGLang (Scope: go deep on one engine (vLLM); treat this section as a lighter comparison pass, not equal depth)

- Run the same or a comparable model
- Understand RadixAttention and prefix reuse
- Compare behaviour on short independent prompts and shared-prefix workloads
- Record methodological limitations instead of claiming a universal winner

#### Multimodal Serving

- Vision-encoder cost relative to the language-model forward pass
- Image/video tokens filling the KV cache, and why long video inputs are expensive
- Splitting a vision encoder and language model across separate GPUs or services

#### Contribution Goal

Contribute at least one of the following:

- Reproducible bug report
- Documentation improvement
- Benchmark or test improvement
- Small bug fix
- Model-support improvement
- Profiling or observability improvement

Begin with a small contribution. Understanding the development workflow of a real inference engine is itself valuable.

#### Deliverable

- Create llm-serving-benchmarks with workload definitions, reproducible commands, results, analysis, and a link to any upstream issue or contribution.

#### Exit Criteria

- You can explain the relevant path of a request through an inference engine.
- You can explain when prefix caching helps and when it does not.
- You can compare engines using controlled workloads rather than headline numbers.
- You have read and modified production inference-system code.

### Phase 8: Modern Architectures, Capstone, and Job Preparation

**Weeks 49–52**

#### Architecture Case Studies

Study modern models as variations on the foundation you already built:

- MoE routing and sparse activation
- Load balancing and expert capacity
- Communication cost and expert parallelism
- MQA/GQA serving trade-offs
- Multi-head Latent Attention (MLA)
- Multi-token prediction and speculative approaches
- DeepSeek and Kimi architecture reports (Scope: read only for what changes cache shape and serving cost, not full report study)

Implement only small components:

- A toy top-k MoE layer and router
- A small experiment showing expert-load imbalance
- GQA or MLA-inspired cache-shape comparison

Do not attempt to reproduce or train an entire DeepSeek or Kimi model.

#### Diffusion and Flow-Model Inference (Small)

Reading and small exercises only — not a training project. World models and video generation are largely diffusion/flow-based, and the inference mechanics differ from LLM decoding.

- Step distillation and reduced-step samplers
- Caching across denoising steps
- Classifier-free guidance batching
- Why diffusion/flow inference is typically compute-bound, while LLM decoding is typically memory-bandwidth-bound

#### Capstone: Unified GPU Inference Portfolio

Present your work as one coherent engineering story:

I began with real-time sports CV, learned to profile and deploy those models, then applied the same GPU, runtime, caching, batching, and serving principles to Transformers and LLMs.

The capstone should include:

- One real-time CV inference pipeline
- One Transformer implementation with KV caching
- CUDA/Triton kernel benchmarks
- One vLLM/SGLang serving study
- A two- to four-page technical report
- A concise portfolio page linking the repositories
- Recommended direction: retarget the capstone toward real-time multimodal or edge (Jetson) inference — this is where your CV background and the added GPU-video, quantization, and multimodal-serving work combine into a less-crowded niche than general LLM serving

#### Job Preparation

Prepare explanations for:

- A difficult detection/tracking failure you diagnosed
- A pipeline bottleneck you measured and improved
- A CUDA kernel you profiled
- KV-cache memory and batching trade-offs
- A vLLM or SGLang code path you investigated
- One failed optimization and what the evidence taught you

Apply throughout the roadmap. Do not wait for Week 52. After Phase 4, you can credibly target CV deployment and model-optimization roles; later phases expand you toward GPU and LLM inference roles.

## Milestones

| Target | Evidence |
|---|---|
| End of Month 1 | Independent PyTorch training loop and debugging notes |
| End of Month 2–3 | Detection/tracking error analysis grounded in your existing CV experience |
| End of Month 4 | Small decoder-only Transformer with correct cached generation |
| End of Month 6 | Profiled GStreamer + CV inference pipeline with backend comparison |
| End of Month 8 | Tested CUDA/Triton kernels with reproducible benchmarks |
| End of Month 10 | Mini LLM runtime demonstrating batching and cache trade-offs |
| End of Month 11 | vLLM/SGLang benchmark and initial upstream contribution |
| End of Month 12 | Integrated portfolio, technical report, and interview stories |

## Postponed topics

These topics are not useless; they are postponed because they do not support the current target strongly enough:

- Reimplementing AlexNet, VGG, ResNet-50, YOLOv1, Faster R-CNN, U-Net, and Mask R-CNN in full
- Studying every YOLO or detector generation chronologically
- A complete segmentation specialization
- SimCLR, MoCo, SimSiam, and MAE implementations
- Diffusion-model implementation [training/full implementation stays excluded; a small inference-only pass was added to Phase 8]
- Training full DeepSeek, Kimi, or other large models
- Reading dozens of papers without an implementation need
- Learning vLLM and SGLang simultaneously at a shallow level
- Starting Kubernetes or multi-node infrastructure before single-GPU profiling is comfortable

Return to a postponed topic when a real job, project, or research question requires it.

## Keeping the scope manageable

- Do not change the roadmap because of one LinkedIn or X post.
- Save interesting topics to a backlog; review that backlog only at the end of a phase.
- Add a topic only if it replaces something of equal size.
- Study a new architecture by asking: what changed, why, and what is the inference consequence?
- Do not confuse knowing model names with possessing an engineering skill.
- Finish the current deliverable before beginning another major course or framework.

## Monthly review

At the end of each month, answer:

- What did I implement without depending on generated code?
- What can I now explain more deeply than one month ago?
- What benchmark or correctness evidence did I produce?
- Where did I lose time?
- What is the single deliverable for next month?

Do not rewrite the entire roadmap during a monthly review. Change the next phase only when work constraints, available hardware, or evidence genuinely require it.

## Success test

At the end of the roadmap, choose an unfamiliar model and workload. You should be able to:

- Understand the relevant architecture.
- Establish a correct PyTorch baseline.
- Export or integrate it into an appropriate inference runtime.
- Construct a representative benchmark.
- Profile the end-to-end system.
- Identify the actual bottleneck.
- Implement or configure a defensible improvement.
- Verify correctness and model quality.
- Report latency, throughput, memory, and limitations honestly.

If you can do this for both a video/CV workload and a Transformer workload, you have preserved your computer-vision experience while building the transferable inference-engineering depth this roadmap is designed to produce.
