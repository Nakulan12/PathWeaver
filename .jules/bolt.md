## 2025-05-15 - [Batch Encoding & Memory Buffers]
**Learning:** Batching `model.encode` calls and using `fitz.open(stream=...)` for PDF parsing significantly reduces overhead and I/O wait times in document processing pipelines.
**Action:** Always batch NLP encoding operations and avoid temporary disk I/O when processing uploaded files.
