import time
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "excel", "communication",
    "react", "node", "cloud", "aws", "statistics"
]

skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)

test_text = """
Experienced software engineer with 5 years of experience in Python and Java.
Strong background in machine learning and data analysis.
Familiar with cloud technologies like AWS and Azure.
Excellent communication skills and experience with React and Node.js.
I have worked on several projects involving statistics and excel.
""" * 50  # 300 lines

def original_extract(text):
    text = text.lower()
    found_skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)
    sentences = text.split("\n")
    for sentence in sentences:
        if len(sentence.strip()) < 5:
            continue
        sentence_embedding = model.encode(sentence, convert_to_tensor=True)
        similarities = util.cos_sim(sentence_embedding, skill_embeddings)[0]
        for i, score in enumerate(similarities):
            if score > 0.6:
                found_skills.add(SKILLS_DB[i])
    return list(found_skills)

def optimized_extract(text):
    text = text.lower()
    found_skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]
    if not sentences:
        return list(found_skills)

    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
    cos_sims = util.cos_sim(sentence_embeddings, skill_embeddings)

    matched_indices = (cos_sims > 0.6).any(dim=0).nonzero(as_tuple=True)[0]
    for idx in matched_indices:
        found_skills.add(SKILLS_DB[idx])

    return list(found_skills)

start = time.time()
original_extract(test_text)
mid = time.time()
optimized_extract(test_text)
end = time.time()

print(f"Original time: {mid - start:.4f}s")
print(f"Optimized time: {end - mid:.4f}s")
print(f"Speedup: {(mid - start) / (end - mid):.2f}x")
