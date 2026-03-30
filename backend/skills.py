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

    # 🔹 Step 2: Semantic matching (controlled ML)
    # Optimized: Batch process sentences to reduce overhead
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if sentences:
        # Batch encode all sentences at once
        sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
        # Vectorized similarity calculation
        # (returns matrix [num_sentences, num_skills])
        similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

        # Efficiently find indices where similarity exceeds threshold
        matched_indices = (similarities > 0.6).nonzero(as_tuple=False)
        for _, skill_idx in matched_indices:
            found_skills.add(SKILLS_DB[skill_idx])

    return list(found_skills)
