import fitz  # PyMuPDF

async def extract_text(file):
    # Performance Optimization: Process file in memory to avoid slow Disk I/O
    content = await file.read()

    # Open PDF from memory stream directly using PyMuPDF
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""

    # Use a list to collect text chunks and join once for better performance
    text_chunks = [page.get_text() for page in doc]
    text = "".join(text_chunks)

    return text