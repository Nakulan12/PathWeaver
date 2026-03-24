import pytest
from skills import extract_skills

def test_extract_skills_functional():
    text = """
    I have skills in Python and Machine Learning.
    I also know React and SQL.
    """
    expected_skills = ["python", "machine learning", "react", "sql"]
    found_skills = extract_skills(text)

    for skill in expected_skills:
        assert skill in found_skills

def test_extract_skills_empty():
    assert extract_skills("") == []

def test_extract_skills_no_match():
    assert extract_skills("I am a space explorer.") == []

def test_extract_skills_mixed_case():
    text = "PYTHON and JAVA"
    found_skills = extract_skills(text)
    assert "python" in found_skills
    assert "java" in found_skills
