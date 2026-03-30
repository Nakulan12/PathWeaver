import fitz  # PyMuPDF


async def extract_text(file):
    # Optimized: Directly process file content from memory stream
    # This avoids writing a temporary file to disk, reducing I/O overhead.
    content = await file.read()

    # Open PDF document from memory buffer
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text
