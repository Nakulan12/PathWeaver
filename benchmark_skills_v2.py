import time
from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "excel", "communication",
    "react", "node", "cloud", "aws", "statistics"
]

skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)

def extract_skills_original(text):
    text = text.lower()
    found_skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)
    sentences = [s for s in text.split("\n") if len(s.strip()) >= 5]
    for sentence in sentences:
        sentence_embedding = model.encode(sentence, convert_to_tensor=True)
        similarities = util.cos_sim(sentence_embedding, skill_embeddings)[0]
        for i, score in enumerate(similarities):
            if score > 0.6:
                found_skills.add(SKILLS_DB[i])
    return list(found_skills)

def extract_skills_optimized(text):
    text = text.lower()
    found_skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)
    sentences = [s for s in text.split("\n") if len(s.strip()) >= 5]
    if not sentences:
        return list(found_skills)

    # Batch encoding
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # Vectorized similarity calculation
    # sentence_embeddings: [num_sentences, embedding_dim]
    # skill_embeddings: [num_skills, embedding_dim]
    # cos_sim: [num_sentences, num_skills]
    similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Find indices where similarity > 0.6
    matched_indices = (similarities > 0.6).nonzero(as_tuple=False)
    for _, skill_idx in matched_indices:
        found_skills.add(SKILLS_DB[skill_idx])

    return list(found_skills)

sample_text = """
John Doe
Software Engineer
Experience with python and java.
Worked on machine learning projects using statistics and data analysis.
Skilled in react and node for frontend and backend development.
Familiar with cloud technologies like aws and azure.
Excellent communication skills.
""" * 20 # Increased size

print(f"Text length: {len(sample_text)} characters")
print(f"Number of lines: {len(sample_text.splitlines())}")

start_time = time.time()
skills1 = extract_skills_original(sample_text)
time_orig = time.time() - start_time
print(f"Original: {time_orig:.4f}s, Skills: {len(skills1)}")

start_time = time.time()
skills2 = extract_skills_optimized(sample_text)
time_opt = time.time() - start_time
print(f"Optimized: {time_opt:.4f}s, Skills: {len(skills2)}")

print(f"Speedup: {time_orig / time_opt:.2f}x")
assert set(skills1) == set(skills2)
