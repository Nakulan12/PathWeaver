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
    # ⚡ BOLT OPTIMIZATION: Collected all valid sentences for batched encoding
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # ⚡ BOLT OPTIMIZATION: Batching NLP encoding operations
    # Encoding all sentences at once is much faster than one-by-one in a loop
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # ⚡ BOLT OPTIMIZATION: Vectorized similarity calculation
    # util.cos_sim handles matrix-matrix similarity efficiently
    similarity_matrix = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Find which skills have at least one sentence with similarity > 0.6
    # This vectorized approach avoids nested loops and takes advantage of GPU
    matched_skill_indices = (
        (similarity_matrix > 0.6).any(dim=0).nonzero().flatten()
    )
    for idx in matched_skill_indices:
        found_skills.add(SKILLS_DB[idx.item()])

    return list(found_skills)
