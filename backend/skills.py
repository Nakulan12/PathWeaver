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
    sentences = text.split("\n")

    for sentence in sentences:
        if len(sentence.strip()) < 5:
            continue

        sentence_embedding = model.encode(sentence, convert_to_tensor=True)
        similarities = util.cos_sim(sentence_embedding, skill_embeddings)[0]

        for i, score in enumerate(similarities):
            if score > 0.6:   # 🔥 Balanced threshold
                found_skills.add(SKILLS_DB[i])

    return list(found_skills)