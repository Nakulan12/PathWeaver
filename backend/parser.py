import fitz


async def extract_text(file):
    # ⚡ Optimization: Read content directly from memory
    # instead of writing to a temporary file.
    # PyMuPDF (fitz) is faster than pdfplumber.
    content = await file.read()

    text = ""
    # Open from memory buffer
    with fitz.open(stream=content, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    return text
