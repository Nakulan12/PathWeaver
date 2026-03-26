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
    # Optimization: Batch encode sentences and use vectorized similarity calculation
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # Batch encode all sentences at once
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # Calculate similarities for all sentences against all skills in one operation
    all_similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Identify matches where similarity score > 0.6
    matches = (all_similarities > 0.6).nonzero(as_tuple=False)
    for match in matches:
        skill_idx = match[1].item()
        found_skills.add(SKILLS_DB[skill_idx])

    return list(found_skills)