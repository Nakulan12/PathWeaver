import time
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Mocking parts of the backend to benchmark extract_skills
SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "excel", "communication",
    "react", "node", "cloud", "aws", "statistics"
]

model = SentenceTransformer('all-MiniLM-L6-v2')
skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)

def extract_skills_original(text):
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

def extract_skills_optimized(text):
    text = text.lower()
    found_skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]
    if not sentences:
        return list(found_skills)

    # Vectorized batch encoding
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
    # Batch similarity calculation
    # cos_sim returns a tensor or numpy array based on input
    similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Use numpy/tensor operations to find where similarity > 0.6
    # Converting to numpy for safe indexing if torch is not available or preferred
    sim_np = similarities.cpu().numpy() if hasattr(similarities, 'cpu') else similarities

    matched_indices = np.where(sim_np > 0.6)
    for skill_idx in matched_indices[1]:
        found_skills.add(SKILLS_DB[skill_idx])

    return list(found_skills)

# Benchmark
sample_text = """
I am a software engineer with 5 years of experience.
I have worked extensively with Python and Java.
I am also familiar with Machine Learning and Data Analysis.
My communication skills are excellent.
I have used React and Node.js for frontend and backend development.
I am experienced with Cloud services like AWS.
I also have a strong background in Statistics and SQL.
I use Excel for data reporting.
""" * 5 # Total 45 sentences (5 empty if split by \n and text is exactly like this)

start_time = time.time()
res_orig = extract_skills_original(sample_text)
original_duration = time.time() - start_time
print(f"Original duration: {original_duration:.4f}s")

start_time = time.time()
res_opt = extract_skills_optimized(sample_text)
optimized_duration = time.time() - start_time
print(f"Optimized duration: {optimized_duration:.4f}s")

print(f"Speedup: {original_duration / optimized_duration:.2f}x")

# Verification
print(f"Results match: {sorted(res_orig) == sorted(res_opt)}")
