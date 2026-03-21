import pytest
from skills import extract_skills
from logic import skill_gap, calculate_readiness

def test_extract_skills():
    text = "I have experience with Python and Java."
    skills = extract_skills(text)
    assert "python" in skills
    assert "java" in skills

def test_skill_gap():
    resume_skills = ["python", "sql"]
    jd_skills = ["python", "java", "sql"]
    matched, missing = skill_gap(resume_skills, jd_skills)
    assert matched == ["python", "sql"] or matched == ["sql", "python"]
    assert missing == ["java"]

def test_calculate_readiness():
    matched = ["python"]
    jd_skills = ["python", "java"]
    score = calculate_readiness(matched, jd_skills)
    assert score == 50.0
