import sys
import os
import time
import io
import asyncio
from unittest.mock import MagicMock

# Add backend to path
sys.path.append(os.path.abspath('backend'))

from parser import extract_text

class MockUploadFile:
    def __init__(self, content):
        self.content = content

    async def read(self):
        return self.content

async def benchmark_parser():
    # Create a small valid PDF content or simulate it
    # Since fitz is used, we need a real-ish PDF or just mock the file object
    # For a real test, let's create a simple PDF if possible, or just measure the I/O overhead

    # Let's create a dummy PDF file for testing
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 72), "This is a test PDF content for benchmarking.")
    pdf_bytes = doc.tobytes()
    doc.close()

    mock_file = MockUploadFile(pdf_bytes)

    print("Benchmarking current (with temp file)...")
    start_time = time.time()
    text = await extract_text(mock_file)
    end_time = time.time()
    print(f"Current took: {end_time - start_time:.4f} seconds")

    print("\nBenchmarking optimized (in-memory)...")
    start_time = time.time()
    # Manual implementation of optimized version
    content = await mock_file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    text_opt = ""
    for page in doc:
        text_opt += page.get_text()
    doc.close()
    end_time = time.time()
    print(f"Optimized took: {end_time - start_time:.4f} seconds")

    assert text == text_opt

if __name__ == "__main__":
    asyncio.run(benchmark_parser())
