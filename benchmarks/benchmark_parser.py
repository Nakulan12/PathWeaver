import time
import fitz
import io
import os

async def original_extract_text(content):
    with open("temp.pdf", "wb") as f:
        f.write(content)

    doc = fitz.open("temp.pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    doc.close()
    if os.path.exists("temp.pdf"):
        os.remove("temp.pdf")
    return text

async def optimized_extract_text(content):
    # Use memory stream instead of disk file
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

if __name__ == "__main__":
    import asyncio

    # Create a dummy PDF in memory
    pdf_buffer = io.BytesIO()
    doc = fitz.open()
    page = doc.new_page()
    for i in range(100):
        page.insert_text((50, 50 + i*10), f"This is line {i} of the dummy PDF for benchmarking.")
    doc.save(pdf_buffer)
    content = pdf_buffer.getvalue()
    doc.close()

    async def run_benchmark():
        print(f"PDF Size: {len(content) / 1024:.2f} KB")

        # Warm up
        await original_extract_text(content)
        await optimized_extract_text(content)

        start_time = time.time()
        for _ in range(100):
            await original_extract_text(content)
        original_duration = (time.time() - start_time) / 100
        print(f"Original average duration: {original_duration:.6f}s")

        start_time = time.time()
        for _ in range(100):
            await optimized_extract_text(content)
        optimized_duration = (time.time() - start_time) / 100
        print(f"Optimized average duration: {optimized_duration:.6f}s")

        improvement = (original_duration - optimized_duration) / original_duration * 100
        print(f"Improvement: {improvement:.2f}%")

    asyncio.run(run_benchmark())
