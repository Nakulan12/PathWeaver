from sentence_transformers import SentenceTransformer, util
import torch

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

    # 🔹 Step 2: Semantic matching (optimized batch ML)
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if sentences:
        # ⚡ Batch encode all sentences at once for significant speedup
        sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

        # ⚡ Vectorized similarity matrix calculation
        cos_sims = util.cos_sim(sentence_embeddings, skill_embeddings)

        # ⚡ Find skills that have at least one sentence with similarity > 0.6
        matched_indices = (cos_sims > 0.6).any(dim=0).nonzero(as_tuple=True)[0]
        for idx in matched_indices:
            found_skills.add(SKILLS_DB[idx])

    return list(found_skills)