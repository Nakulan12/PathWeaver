import fitz  # PyMuPDF

async def extract_text(file):
    """
    Extracts text from an uploaded PDF file without disk I/O.
    Performance: Eliminates disk writes/reads by using in-memory byte streams.
    """
    content = await file.read()

    # ⚡ PERFORMANCE BOOST: Open from memory stream (buffer)
    # instead of writing to a temporary file first.
    doc = fitz.open(stream=content, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    doc.close()
    return text