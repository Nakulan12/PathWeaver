import time
import pytest
from fastapi.testclient import TestClient
from main import app
from skills import extract_skills, SKILLS_DB
import numpy as np

client = TestClient(app)

def test_extract_skills_performance():
    sample_text = """
    I am a software engineer with 5 years of experience.
    I have worked extensively with Python and Java.
    I am also familiar with Machine Learning and Data Analysis.
    My communication skills are excellent.
    I have used React and Node.js for frontend and backend development.
    I am experienced with Cloud services like AWS.
    I also have a strong background in Statistics and SQL.
    I use Excel for data reporting.
    """ * 10 # Increase size for better measurement

    start_time = time.time()
    skills = extract_skills(sample_text)
    duration = time.time() - start_time

    print(f"\nSkill extraction duration: {duration:.4f}s")
    assert len(skills) > 0
    # Ensure some core skills are found
    assert "python" in skills
    assert "machine learning" in skills

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "PathForge AI Running"}

if __name__ == "__main__":
    # If run directly, just run the performance test and print result
    sample_text = "I know python and machine learning." * 50
    start_time = time.time()
    extract_skills(sample_text)
    duration = time.time() - start_time
    print(f"Extraction took {duration:.4f} seconds for {len(sample_text)} characters.")
