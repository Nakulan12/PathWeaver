from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS_DB = [
    "python", "java", "sql", "machine learning",
    "data analysis", "excel", "communication",
    "react", "node", "cloud", "aws", "statistics"
]

skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)


def extract_skills(text):
    """
    Extracts skills from text using a hybrid approach of keyword matching
    and batched semantic similarity.
    """
    text = text.lower()
    found_skills = set()

    # 🔹 Step 1: Direct keyword match (strong baseline - O(N))
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # 🔹 Step 2: Semantic matching (Optimized Batched ML)
    # Filter valid sentences once to avoid redundant checks
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # ⚡ PERFORMANCE BOOST: Batch encode all sentences at once.
    # This is significantly faster than encoding one by one as it allows
    # the model to utilize vectorized operations across the entire batch.
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # ⚡ PERFORMANCE BOOST: Vectorized similarity calculation.
    # Instead of nested loops, we compute a similarity matrix [num_sentences x num_skills]
    # in a single operation using util.cos_sim.
    similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # ⚡ PERFORMANCE BOOST: Matrix thresholding.
    # Use torch operations to find matching indices directly, avoiding manual iteration.
    matched_indices = (similarities > 0.6).nonzero(as_tuple=False)
    for _, skill_idx in matched_indices:
        found_skills.add(SKILLS_DB[skill_idx.item()])

    return list(found_skills)