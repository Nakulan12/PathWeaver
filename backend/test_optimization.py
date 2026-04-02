import pytest
from skills import extract_skills
from logic import skill_gap, calculate_readiness, generate_reasoned_path

def test_extract_skills_functional():
    text = "Experienced Software Engineer with Python and Java."
    skills = extract_skills(text)
    assert "python" in [s.lower() for s in skills]
    assert "java" in [s.lower() for s in skills]

def test_extract_skills_semantic():
    text = "Expert in building machine learning models for prediction."
    skills = extract_skills(text)
    assert "machine learning" in [s.lower() for s in skills]

def test_logic_consistency():
    resume_skills = ["python", "java"]
    jd_skills = ["python", "sql", "machine learning"]

    matched, missing = skill_gap(resume_skills, jd_skills)
    assert "python" in matched
    assert "sql" in missing
    assert "machine learning" in missing

    readiness = calculate_readiness(matched, jd_skills)
    assert readiness == 33.33

    path = generate_reasoned_path(missing, resume_skills)
    # Machine learning requires python and statistics
    # Python is in resume_skills, so only statistics should be a prerequisite for ML
    skills_in_path = [item["skill"] for item in path]
    assert "statistics" in skills_in_path
    assert "sql" in skills_in_path
    assert "machine learning" in skills_in_path
