## 2025-05-15 - [Batch Inference for Skill Extraction]
**Learning:** Sequential processing of sentences using a Transformer model (one `model.encode` call per sentence) is a major bottleneck in NLP pipelines. Batching multiple sentences into a single inference call significantly reduces overhead and allows for efficient parallelization.
**Action:** Always batch NLP encoding operations and use vectorized matrix operations (e.g., `util.cos_sim` on tensors) instead of nested loops for similarity calculations.

## 2025-05-15 - [In-Memory PDF Processing]
**Learning:** Writing uploaded file contents to disk as temporary files for processing (e.g., PDF extraction) adds unnecessary I/O latency and requires manual cleanup of temporary files.
**Action:** Use memory streams (e.g., `fitz.open(stream=content, filetype="pdf")`) to process file contents directly from memory whenever possible.
