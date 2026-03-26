import fitz  # PyMuPDF

async def extract_text(file):
    # Optimization: Read file content directly from memory buffer
    # instead of writing to a temporary file on disk.
    content = await file.read()

    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text
