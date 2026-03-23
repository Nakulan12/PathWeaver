from sentence_transformers import SentenceTransformer, util

# ⚡ Bolt: Using all-MiniLM-L6-v2 which is optimized for speed/accuracy trade-off
model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "excel", "communication",
    "react", "node", "cloud", "aws", "statistics"
]

# ⚡ Bolt: Pre-calculate skill embeddings once at startup
skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)


def extract_skills(text):
    text = text.lower()
    found_skills = set()

    # 🔹 Step 1: Direct keyword match (strong baseline)
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # 🔹 Step 2: Semantic matching (controlled ML)
    # ⚡ Bolt: Batching NLP encoding operations to maximize throughput
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # ⚡ Bolt: Perform a single batch encoding instead of multiple individual calls
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # ⚡ Bolt: Use vectorized matrix operations for similarity calculations
    # cos_sim will return a matrix of size (len(sentences), len(SKILLS_DB))
    similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # ⚡ Bolt: Efficiently find skills that exceed the threshold
    # Using a list comprehension or any/where to avoid deep nested loops if possible
    # but for clarity and correctness in this small scale, a single pass over similarities is fine.
    for row in similarities:
        for i, score in enumerate(row):
            if score > 0.6:   # 🔥 Balanced threshold
                found_skills.add(SKILLS_DB[i])

    return list(found_skills)
