import fitz  # PyMuPDF

async def extract_text(file):
    # Performance Optimization: Process file in memory to avoid slow disk I/O
    content = await file.read()

    # Open document directly from byte stream
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text
