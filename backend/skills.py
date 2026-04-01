import numpy as np
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "excel", "communication",
    "react", "node", "cloud", "aws", "statistics"
]

skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)


def extract_skills(text):
    text = text.lower()
    found_skills = set()

    # 🔹 Step 1: Direct keyword match (strong baseline)
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # 🔹 Step 2: Semantic matching (optimized batch processing)
    # Filter out empty or very short sentences to save processing time
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # ⚡ Batch encode sentences for significant speedup
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # ⚡ Vectorized similarity calculation (replaces O(n*m) Python loop)
    similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Convert to numpy for efficient thresholding and indexing
    # (Checking if it's a tensor and moving to CPU if needed)
    sim_np = similarities.cpu().numpy() if hasattr(similarities, 'cpu') else similarities

    # Find all (sentence_idx, skill_idx) pairs where similarity > 0.6
    matched_indices = np.where(sim_np > 0.6)

    for skill_idx in matched_indices[1]:
        found_skills.add(SKILLS_DB[skill_idx])

    return list(found_skills)
