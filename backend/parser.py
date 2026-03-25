import fitz  # PyMuPDF


async def extract_text(file):
    # ⚡ BOLT OPTIMIZATION: Avoid temporary file I/O
    # Processing uploaded file contents directly from memory buffers
    content = await file.read()

    # ⚡ BOLT OPTIMIZATION: Use fitz.open(stream=content, filetype="pdf")
    # This avoids writing to disk and then reading back
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text
