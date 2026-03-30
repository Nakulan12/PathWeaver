from fastapi.testclient import TestClient
from main import app
import fitz

client = TestClient(app)


def create_pdf(text):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 50), text)
    return doc.write()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "PathForge AI Running"}


def test_roadmap_endpoint():
    resume_pdf = create_pdf("Experience with python and machine learning. "
                            "John Doe.")
    jd_pdf = create_pdf("Requires python, sql, and machine learning skills.")

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

    # Check if some skills were extracted (both direct and semantic)
    assert "python" in data["resume_skills"]
    assert "machine learning" in data["resume_skills"]
    assert "sql" in data["jd_skills"]


def test_extract_skills_edge_cases():
    from skills import extract_skills

    # Empty text
    assert extract_skills("") == []

    # Short sentences (should be ignored by semantic but caught by direct)
    assert set(extract_skills("python")) == {"python"}

    # Text with no skills
    assert extract_skills("This text has no mention of any known "
                          "technical skills whatsoever.") == []
