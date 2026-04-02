## 2025-05-15 - [Batching Sentence Embeddings]
**Learning:** Batching `model.encode` calls in `sentence-transformers` is significantly faster than individual calls per sentence due to reduced model invocation overhead and optimized vectorized operations.
**Action:** Always filter and collect sentences before calling `model.encode` to ensure high throughput in NLP tasks.

## 2025-05-15 - [In-memory PDF Processing]
**Learning:** Writing uploaded file content to disk (`temp.pdf`) before processing with PyMuPDF is a major bottleneck and potential race condition.
**Action:** Use `fitz.open(stream=content, filetype="pdf")` to process PDF files directly from memory buffers.
