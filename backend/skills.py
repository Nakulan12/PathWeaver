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
    # Split by newlines and filter out short or empty sentences
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    # Only process unique sentences to avoid redundant computations
    unique_sentences = list(set(sentences))

    if unique_sentences:
        # ⚡ Optimization: Batch encode all sentences at once
        sentence_embeddings = model.encode(
            unique_sentences, convert_to_tensor=True
        )

        # ⚡ Optimization: Calculate all similarities in one matrix operation
        # similarities shape: (len(unique_sentences), len(SKILLS_DB))
        all_similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

        for sentence_idx in range(len(unique_sentences)):
            similarities = all_similarities[sentence_idx]
            for skill_idx, score in enumerate(similarities):
                if score > 0.6:   # 🔥 Balanced threshold
                    found_skills.add(SKILLS_DB[skill_idx])

    return list(found_skills)
