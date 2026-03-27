import fitz  # PyMuPDF


async def extract_text(file):
    # Optimized: Read from memory stream instead of writing to disk (I/O)
    content = await file.read()

    # Passing stream directly to fitz avoids temporary file overhead
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text
