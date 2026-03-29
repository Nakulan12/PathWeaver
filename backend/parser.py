import fitz  # PyMuPDF

async def extract_text(file):
    # Process file directly from memory to avoid disk I/O overhead
    content = await file.read()

    # Open PDF from stream (in-memory bytes)
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text
