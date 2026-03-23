import fitz  # PyMuPDF

async def extract_text(file):
    # ⚡ Bolt: Read file content directly into memory
    content = await file.read()

    # ⚡ Bolt: Avoid temporary file I/O by opening PDF directly from memory buffer
    # This reduces overhead and is faster than disk operations
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text
