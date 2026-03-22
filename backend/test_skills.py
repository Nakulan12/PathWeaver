import pytest
from skills import extract_skills

def test_extract_skills_direct_match():
    text = "I am proficient in Python and SQL."
    skills = extract_skills(text)
    assert "python" in skills
    assert "sql" in skills

def test_extract_skills_semantic_match():
    text = "I have extensive experience building cloud-native applications on Amazon Web Services."
    skills = extract_skills(text)
    # AWS should be matched semantically or via keyword
    assert "aws" in skills or "cloud" in skills

def test_extract_skills_empty():
    assert extract_skills("") == []

def test_extract_skills_no_match():
    assert extract_skills("I like cooking and hiking.") == []
