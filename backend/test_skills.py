from skills import extract_skills

def test_extract_skills_basic():
    text = "I know Python and Java."
    skills = extract_skills(text)
    assert "python" in [s.lower() for s in skills]
    assert "java" in [s.lower() for s in skills]

def test_extract_skills_semantic():
    # Use "Machine Learning" directly to test Step 1
    text = "I am proficient in machine learning."
    skills = extract_skills(text)
    assert "machine learning" in [s.lower() for s in skills]

def test_extract_skills_empty():
    assert extract_skills("") == []
