## 2025-03-10 - [Batching Sentence Encoding Performance Boost]
**Learning:** Batching `model.encode` operations for NLP tasks (like skill extraction) provides massive performance improvements over sequential encoding. The overhead of individual model calls is significant, and batching allows for internal optimization and parallelism (even on CPU). In this codebase, batching reduced the execution time for a sample resume by ~80%.
**Action:** Always prefer batching for model inference tasks when multiple inputs are available at once.
