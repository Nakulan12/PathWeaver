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

# Generate some dummy sentences
dummy_sentences = [
    "I am a software engineer with 5 years of experience in python and java.",
    "Experienced in data analysis and statistics using excel.",
    "Worked on cloud technologies like aws and azure.",
    "Familiar with react and node for web development.",
    "Strong communication skills and team player.",
    "Interested in machine learning and artificial intelligence.",
    "Learning about SQL and database management.",
    "Applying for a role that requires python and cloud skills."
] * 10  # 80 sentences total

def original_method(sentences):
    found_skills = set()
    for sentence in sentences:
        if len(sentence.strip()) < 5:
            continue
        sentence_embedding = model.encode(sentence, convert_to_tensor=True)
        similarities = util.cos_sim(sentence_embedding, skill_embeddings)[0]
        for i, score in enumerate(similarities):
            if score > 0.6:
                found_skills.add(SKILLS_DB[i])
    return found_skills

def optimized_method(sentences):
    found_skills = set()
    valid_sentences = [s.strip() for s in sentences if len(s.strip()) >= 5]
    if not valid_sentences:
        return found_skills

    sentence_embeddings = model.encode(valid_sentences, convert_to_tensor=True)
    cosine_scores = util.cos_sim(sentence_embeddings, skill_embeddings)

    for i in range(len(valid_sentences)):
        similarities = cosine_scores[i]
        for j, score in enumerate(similarities):
            if score > 0.6:
                found_skills.add(SKILLS_DB[j])
    return found_skills

# Warmup
original_method(dummy_sentences[:5])
optimized_method(dummy_sentences[:5])

# Benchmark Original
start_time = time.time()
for _ in range(5):
    original_method(dummy_sentences)
original_duration = (time.time() - start_time) / 5
print(f"Original Method: {original_duration:.4f} seconds per call")

# Benchmark Optimized
start_time = time.time()
for _ in range(5):
    optimized_method(dummy_sentences)
optimized_duration = (time.time() - start_time) / 5
print(f"Optimized Method: {optimized_duration:.4f} seconds per call")

print(f"Speedup: {original_duration / optimized_duration:.2f}x")
