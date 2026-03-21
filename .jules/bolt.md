## 2025-05-15 - [Batch Encoding & Vectorized Similarity]
**Learning:** Sequential encoding of sentences in a NLP pipeline is a massive bottleneck. Grouping sentences and processing them in a single `model.encode()` call allows the underlying deep learning framework (like PyTorch) to utilize parallel processing. Furthermore, using `util.cos_sim` on the entire batch at once (matrix multiplication) is significantly faster than looping through individual vectors.
**Action:** Always look for opportunities to batch NLP operations and use vectorized library functions instead of loops for similarity calculations.

## 2025-05-15 - [In-Memory I/O with PyMuPDF]
**Learning:** Writing uploaded files to disk before processing them adds unnecessary I/O overhead. PyMuPDF (`fitz`) supports opening PDF documents directly from memory buffers (`fitz.open(stream=content, filetype="pdf")`), which is significantly faster than writing to a temporary file and also faster than using libraries like `pdfplumber`.
**Action:** Use PyMuPDF's memory buffer support for PDF parsing to maximize speed and minimize I/O.
