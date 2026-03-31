import asyncio
import io
import fitz
from parser import extract_text
from skills import extract_skills

# Mock UploadFile-like object
class MockUploadFile:
    def __init__(self, content):
        self.content = content
    async def read(self):
        return self.content

async def test_extract_text():
    print("Testing extract_text (PDF parsing)...")
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 50), "Hello, this is a test PDF with python and machine learning skills.")
    pdf_bytes = doc.write()
    doc.close()

    mock_file = MockUploadFile(pdf_bytes)
    text = await extract_text(mock_file)
    print(f"Extracted text: {text.strip()}")
    assert "python" in text.lower()
    print("✓ extract_text passed")

def test_extract_skills():
    print("\nTesting extract_skills...")
    text = "Experienced in Python and Java. Also familiar with statistics."
    skills = extract_skills(text)
    print(f"Extracted skills: {skills}")
    assert "python" in [s.lower() for s in skills]
    assert "java" in [s.lower() for s in skills]
    assert "statistics" in [s.lower() for s in skills]
    print("✓ extract_skills passed")

if __name__ == "__main__":
    asyncio.run(test_extract_text())
    test_extract_skills()
