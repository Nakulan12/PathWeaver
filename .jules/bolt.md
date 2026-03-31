## 2025-05-15 - [Batching and In-Memory Processing]
**Learning:** Batching NLP encoding operations (`model.encode`) and using vectorized matrix operations for similarity calculations provides a significant throughput boost (approx. 3.7x in this case). Additionally, processing file uploads directly from memory using `fitz.open(stream=content, ...)` avoids slow disk I/O and potential race conditions in concurrent environments.
**Action:** Always prefer batching for ML inference and memory-resident processing for file uploads to maximize performance and reliability.
