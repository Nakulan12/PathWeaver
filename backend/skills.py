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
    # ⚡ OPTIMIZATION: Batch process sentences to reduce model overhead
    # and use vectorized operations for similarity calculations.
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if sentences:
        # Batch encode all sentences at once
        sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
        # Vectorized similarity calculation:
        # (N_sentences, 384) x (384, N_skills) -> (N_sentences, N_skills)
        similarity_matrix = util.cos_sim(sentence_embeddings, skill_embeddings)

        # Identify skills that meet the threshold
        # threshold = 0.6
        for i in range(len(sentences)):
            similarities = similarity_matrix[i]
            for j, score in enumerate(similarities):
                if score > 0.6:   # 🔥 Balanced threshold
                    found_skills.add(SKILLS_DB[j])

    return list(found_skills)
