import fitz  # PyMuPDF


async def extract_text(file):
    # ⚡ OPTIMIZATION: Avoid temporary file I/O and process
    # directly from memory buffer
    content = await file.read()

    # PyMuPDF can open directly from a bytes stream
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text
