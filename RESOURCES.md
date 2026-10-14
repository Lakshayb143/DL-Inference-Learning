# Resources

Use the resource needed for the current implementation. This is a reference list across the whole roadmap, not a reading queue to finish before writing code.

## Current study: PyTorch foundations

- [Deep Learning with PyTorch, Second Edition](https://www.manning.com/books/deep-learning-with-pytorch-second-edition), by Howard Huang, Eli Stevens, Luca Antiga, and Thomas Viehmann, published by Manning. My current book; Chapter 3 on tensors is complete.
- [The authors' source code](https://github.com/deep-learning-with-pytorch/dlwpt-code-2e). Reference examples are separate from the scripts I write in this repository.
- [PyTorch tutorials](https://pytorch.org/tutorials/).
- [Tensor Views](https://docs.pytorch.org/docs/stable/tensor_view.html).
- [torch.Tensor.view](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.view.html).
- [Channels Last Memory Format](https://docs.pytorch.org/tutorials/intermediate/memory_format_tutorial.html).
- [NumPy internal organization](https://numpy.org/doc/stable/dev/internals.html).

The book supports the Phase 1 implementation list. I will use the chapters that support that work rather than make finishing the book the goal.

## Foundations and computer vision

- [Dive into Deep Learning](https://d2l.ai/).
- [Deep Learning](https://www.deeplearningbook.org/), by Goodfellow, Bengio, and Courville: Chapters 8 and 9 as references in the roadmap.
- [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html).

## Transformers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).
- [Build a Large Language Model (From Scratch): code](https://github.com/rasbt/LLMs-from-scratch), by Sebastian Raschka.
- [nanoGPT](https://github.com/karpathy/nanoGPT), to inspect after my first implementation attempt.
- [FlashAttention](https://github.com/Dao-AILab/flash-attention), for the memory and I/O perspective.

## Real-time CV deployment

- [GStreamer documentation](https://gstreamer.freedesktop.org/documentation/).
- [ONNX Runtime performance documentation](https://onnxruntime.ai/docs/performance/).
- [TensorRT documentation](https://docs.nvidia.com/deeplearning/tensorrt/latest/).
- [DeepStream SDK documentation](https://docs.nvidia.com/metropolis/deepstream/dev-guide/).
- [Jetson developer documentation](https://developer.nvidia.com/embedded/develop/documentation).

## C++, CUDA, Triton, and GPU systems

- *C++ Primer*: the C++ book used alongside the roadmap.
- *Programming Massively Parallel Processors*: a reference for the GPU phase.
- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/).
- [Nsight Systems documentation](https://docs.nvidia.com/nsight-systems/).
- [Nsight Compute documentation](https://docs.nvidia.com/nsight-compute/).
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html).
- [GPU MODE lectures](https://github.com/gpu-mode/lectures).
- [PyTorch compiler documentation](https://docs.pytorch.org/docs/stable/torch.compiler.html).
- [FlashInfer](https://github.com/flashinfer-ai/flashinfer).

## LLM inference and serving

- [vLLM documentation](https://docs.vllm.ai/). The first engine I plan to study in depth.
- [SGLang documentation](https://docs.sglang.ai/). A comparison after the vLLM work.
- [PagedAttention / vLLM paper](https://arxiv.org/abs/2309.06180).
- [AWQ](https://github.com/mit-han-lab/llm-awq).
- [GPTQ](https://github.com/IST-DASLab/gptq).
- [NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/).

Modern architecture reports belong in Phase 8, when there is a specific cache, memory, or serving question to investigate.

## Reading and writing

I use the official documentation and experiments to check technical claims. Other people's posts on the same topic come after my own draft, so they do not decide the explanation for me.

[Back to the README](README.md) · [The roadmap](ROADMAP.md)
