## 2025-05-15 - [Batch NLP Encoding and In-memory PDF Extraction]
**Learning:** Batching sentences for `sentence-transformers` encoding is significantly faster (~6x in local benchmarks) than individual encoding calls due to reduced overhead and optimized internal processing. Additionally, using `fitz.open(stream=content)` avoids unnecessary disk I/O and temporary file management.
**Action:** Always batch NLP encoding operations and prefer in-memory file processing when working with PyMuPDF.
