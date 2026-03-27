import time
import asyncio
from unittest.mock import MagicMock
from backend.parser import extract_text

async def benchmark():
    # Create a dummy PDF content (not a real PDF, but enough to trigger the write/open)
    # Actually, to be fair, I should use a real small PDF or just mock the file object
    content = b"%PDF-1.4\n1 0 obj\n<< /Title (Test) >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"

    mock_file = MagicMock()
    mock_file.read.return_value = content

    start_time = time.time()
    try:
        # This will likely fail with invalid PDF but we can measure the I/O part
        await extract_text(mock_file)
    except Exception:
        pass
    end_time = time.time()

    print(f"Time taken for parser (with I/O): {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(benchmark())
