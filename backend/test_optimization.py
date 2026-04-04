import pytest
from fastapi.testclient import TestClient
from main import app
from skills import extract_skills
import torch

client = TestClient(app)

def test_extract_skills_functional():
    text = "I know Python and Machine Learning. I also have experience with SQL and AWS."
    skills = extract_skills(text)
    assert "python" in skills
    assert "machine learning" in skills
    assert "sql" in skills
    assert "aws" in skills

def test_extract_skills_empty():
    assert extract_skills("") == []

def test_extract_skills_no_match():
    assert extract_skills("Nothing related here.") == []

def test_readiness_calculation():
    from logic import calculate_readiness
    assert calculate_readiness(["python"], ["python", "sql"]) == 50.0
    assert calculate_readiness([], ["python"]) == 0.0
    assert calculate_readiness(["python"], []) == 0.0

# Add more as needed
