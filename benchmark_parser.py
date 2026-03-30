import time
import os
import fitz

async def extract_text_original(content):
    with open("temp_bench.pdf", "wb") as f:
        f.write(content)

    doc = fitz.open("temp_bench.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    if os.path.exists("temp_bench.pdf"):
        os.remove("temp_bench.pdf")
    return text

async def extract_text_optimized(content):
    # Use memory stream instead of file on disk
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# Create a dummy PDF for benchmarking
import io
def create_dummy_pdf():
    doc = fitz.open()
    for i in range(10):
        page = doc.new_page()
        page.insert_text((50, 50), f"This is page {i} of a dummy PDF for benchmarking. It contains some text for extraction.")
    return doc.write()

pdf_content = create_dummy_pdf()

import asyncio

async def main():
    # Warm up
    await extract_text_original(pdf_content)
    await extract_text_optimized(pdf_content)

    start_time = time.time()
    for _ in range(100):
        await extract_text_original(pdf_content)
    time_orig = time.time() - start_time
    print(f"Original: {time_orig:.4f}s")

    start_time = time.time()
    for _ in range(100):
        await extract_text_optimized(pdf_content)
    time_opt = time.time() - start_time
    print(f"Optimized: {time_opt:.4f}s")

    print(f"Speedup: {time_orig / time_opt:.2f}x")

asyncio.run(main())
