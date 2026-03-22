import fitz  # PyMuPDF


async def extract_text(file):
    content = await file.read()

    # ⚡ OPTIMIZATION: Process file from memory directly
    # Reduces disk I/O latency and avoids managing temp files
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text
