## 2025-05-15 - [Vectorized Skill Extraction]
**Learning:** Batching `model.encode` operations and using vectorized `cos_sim` operations (via `numpy` or `torch`) provides a 3-5x speedup in NLP-based keyword extraction compared to sequential processing in Python loops.
**Action:** Always batch NLP encoding operations and use vectorized matrix operations for similarity calculations to maximize throughput.

## 2025-05-15 - [Direct Buffer PDF Extraction]
**Learning:** PyMuPDF (`fitz`) can open PDFs directly from memory buffers (`stream=content`), which is faster and cleaner than writing to temporary files on disk.
**Action:** Avoid temporary file I/O; process uploaded file contents directly from memory buffers whenever possible.
