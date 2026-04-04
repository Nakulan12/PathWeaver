## 2025-05-22 - [Vectorized Skill Extraction]
**Learning:** Batching NLP encoding operations (`model.encode`) and using vectorized matrix operations for similarity calculations provides a significant performance boost (~3.6x speedup) compared to processing individual sentences in a loop.
**Action:** Always prefer batched operations for Transformer-based models and utilize PyTorch's vectorized functions for similarity checks instead of Python-level loops.

## 2025-05-22 - [In-Memory PDF Processing]
**Learning:** Reading file contents directly from a memory buffer (`stream=content`) using PyMuPDF instead of writing to a temporary file on disk reduces latency and avoids potential race conditions in concurrent environments.
**Action:** Avoid temporary file I/O for uploaded files when the library supports in-memory streams.
