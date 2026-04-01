import fitz  # PyMuPDF

async def extract_text(file):
    # ⚡ DIRECT BUFFER PROCESSING (Removes slow Disk I/O)
    content = await file.read()

    # Open the PDF directly from the memory buffer stream
    doc = fitz.open(stream=content, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    doc.close() # Good practice to close the document
    return text
