import pytest
from fastapi.testclient import TestClient
from main import app
import io
import fitz

client = TestClient(app)

def create_pdf(text):
    pdf_buffer = io.BytesIO()
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 50), text)
    doc.save(pdf_buffer)
    doc.close()
    pdf_buffer.seek(0)
    return pdf_buffer

def test_roadmap_endpoint():
    resume_pdf = create_pdf("I am a software engineer with Python and SQL experience.")
    jd_pdf = create_pdf("Looking for a developer with Python, SQL, and React experience.")

    files = {
        "resume": ("resume.pdf", resume_pdf, "application/pdf"),
        "jd": ("jd.pdf", jd_pdf, "application/pdf")
    }

    response = client.post("/roadmap/", files=files)

    assert response.status_code == 200
    data = response.json()
    assert "resume_skills" in data
    assert "jd_skills" in data
    assert "matched" in data
    assert "missing" in data
    assert "readiness_score" in data
    assert "learning_path" in data

    # Check if skills were correctly extracted
    assert "python" in [s.lower() for s in data["resume_skills"]]
    assert "sql" in [s.lower() for s in data["resume_skills"]]
    assert "react" in [s.lower() for s in data["jd_skills"]]
    assert "react" in [s.lower() for s in data["missing"]]
