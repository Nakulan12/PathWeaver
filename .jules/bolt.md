## 2024-05-20 - [Optimized NLP Batching and I/O]
**Learning:** Sequential processing of sentences in transformer models is a major bottleneck (1.5s vs 0.3s). Batched encoding allows the model to utilize vectorized operations, drastically reducing latency. Additionally, disk-based temporary files for PDF processing create unnecessary I/O overhead and potential race conditions in a web environment.
**Action:** Always batch `model.encode` calls and prefer `fitz.open(stream=content)` over temporary file creation.
