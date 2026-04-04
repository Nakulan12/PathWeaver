import fitz  # PyMuPDF

async def extract_text(file):
    # ⚡ Read file content directly into memory to avoid slow disk I/O
    content = await file.read()

    # ⚡ Open PDF from memory stream for better performance
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text