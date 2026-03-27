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

    # 🔹 Step 2: Semantic matching (controlled ML) - Optimized with Batching
    # Filtering sentences beforehand to avoid processing noise
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if sentences:
        # Batch encode all sentences at once for significantly better
        # throughput (GPU/CPU parallelism)
        sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

        # Vectorized similarity calculation:
        # (num_sentences, embedding_dim) x (num_skills, embedding_dim)^T
        # Result shape: (num_sentences, num_skills)
        similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

        # Find any skill that matches at least one sentence above threshold
        # Taking max across sentences (dim 0) gives (num_skills,)
        max_similarities = similarities.max(dim=0).values

        for i, score in enumerate(max_similarities):
            if score > 0.6:   # 🔥 Balanced threshold
                found_skills.add(SKILLS_DB[i])

    return list(found_skills)
