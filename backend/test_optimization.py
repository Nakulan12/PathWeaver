import pytest
from fastapi.testclient import TestClient
from main import app
from io import BytesIO

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "PathForge AI Running"}

def test_extract_skills():
    from skills import extract_skills
    text = "I have experience with Python and Machine Learning."
    skills = extract_skills(text)
    assert "python" in skills
    assert "machine learning" in skills

def test_roadmap_endpoint():
    # Mock files
    resume_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 12 Tf 100 700 Td (Python and SQL) Tj ET\nendstream\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"
    jd_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 50 >>\nstream\nBT /F1 12 Tf 100 700 Td (Python, SQL and React) Tj ET\nendstream\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"

    files = {
        "resume": ("resume.pdf", resume_content, "application/pdf"),
        "jd": ("jd.pdf", jd_content, "application/pdf")
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
