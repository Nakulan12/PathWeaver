## 2025-05-15 - [Batching NLP encoding and Vectorizing Similarity]
**Learning:** In pipelines using `sentence-transformers`, unbatched `model.encode` calls in a loop are a massive bottleneck. Batching sentences into a single `model.encode` call allows for significantly higher throughput by leveraging vectorized operations and internal batch processing. Additionally, using `util.cos_sim` on the entire batch of embeddings at once is more efficient than individual similarity checks.
**Action:** Always collect candidates for encoding and perform a single batch `model.encode` call. Use matrix-based similarity calculations to process all comparisons in one go.

## 2025-05-15 - [In-memory PDF Processing with PyMuPDF]
**Learning:** Writing uploaded files to a temporary disk location (`temp.pdf`) introduces unnecessary I/O overhead and creates potential race conditions or concurrency issues in a web environment. PyMuPDF (`fitz`) supports opening PDF documents directly from a memory stream (`stream=content`).
**Action:** Prefer `fitz.open(stream=content, filetype="pdf")` over writing to temporary files when processing uploaded PDFs.
