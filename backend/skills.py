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
    # Filter out empty or too short sentences before encoding
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # Batch encode all sentences at once for better throughput
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # Vectorized similarity calculation: (num_sentences, embedding_dim) x (num_skills, embedding_dim)^T
    # This results in a (num_sentences, num_skills) matrix of similarity scores
    cosine_scores = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Efficiently find all skills that exceed the threshold in any sentence
    # We take the max similarity score for each skill across all sentences
    max_scores, _ = cosine_scores.max(dim=0)

    for i, score in enumerate(max_scores):
        if score > 0.6:  # 🔥 Balanced threshold
            found_skills.add(SKILLS_DB[i])

    return list(found_skills)