import time
import sys
import os

# Mocking SentenceTransformer and util since we might not have them installed or want to load the full model for a simple logic check
# However, for a real benchmark we need the actual model.
# Let's assume they are installed as per requirements.txt

from sentence_transformers import SentenceTransformer, util
import torch

def original_extract_skills(text, model, skill_embeddings, SKILLS_DB):
    text = text.lower()
    found_skills = set()

    # Step 1: Direct keyword match
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # Step 2: Semantic matching
    sentences = [s for s in text.split("\n") if len(s.strip()) >= 5]

    for sentence in sentences:
        sentence_embedding = model.encode(sentence, convert_to_tensor=True)
        similarities = util.cos_sim(sentence_embedding, skill_embeddings)[0]

        for i, score in enumerate(similarities):
            if score > 0.6:
                found_skills.add(SKILLS_DB[i])

    return list(found_skills)

def optimized_extract_skills(text, model, skill_embeddings, SKILLS_DB):
    text = text.lower()
    found_skills = set()

    # Step 1: Direct keyword match
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # Step 2: Semantic matching (Batched)
    sentences = [s for s in text.split("\n") if len(s.strip()) >= 5]

    if not sentences:
        return list(found_skills)

    # Batch encode all sentences at once
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # Vectorized similarity calculation
    # sentence_embeddings: [num_sentences, embedding_dim]
    # skill_embeddings: [num_skills, embedding_dim]
    # cos_sim returns [num_sentences, num_skills]
    similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

    # Find where similarity > 0.6
    matched_indices = (similarities > 0.6).nonzero(as_tuple=False)
    for _, skill_idx in matched_indices:
        found_skills.add(SKILLS_DB[skill_idx.item()])

    return list(found_skills)

if __name__ == "__main__":
    SKILLS_DB = [
        "python", "java", "sql", "machine learning",
        "data analysis", "excel", "communication",
        "react", "node", "cloud", "aws", "statistics"
    ]

    print("Loading model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    skill_embeddings = model.encode(SKILLS_DB, convert_to_tensor=True)

    test_text = """
    I am a software engineer with experience in building web applications.
    I have used Python for various data science projects.
    My background includes working with SQL databases and performing data analysis.
    I am familiar with cloud technologies like AWS.
    I have also worked with React and Node for frontend and backend development.
    Excellent communication skills and ability to work in a team.
    Deep understanding of machine learning algorithms and statistics.
    I can also use Excel for basic reporting.
    """ * 10 # Increase size for better measurement

    print(f"Text length: {len(test_text)} characters")

    # Warm up
    original_extract_skills("warm up text", model, skill_embeddings, SKILLS_DB)
    optimized_extract_skills("warm up text", model, skill_embeddings, SKILLS_DB)

    start_time = time.time()
    for _ in range(5):
        original_extract_skills(test_text, model, skill_embeddings, SKILLS_DB)
    original_duration = (time.time() - start_time) / 5
    print(f"Original average duration: {original_duration:.4f}s")

    start_time = time.time()
    for _ in range(5):
        optimized_extract_skills(test_text, model, skill_embeddings, SKILLS_DB)
    optimized_duration = (time.time() - start_time) / 5
    print(f"Optimized average duration: {optimized_duration:.4f}s")

    improvement = (original_duration - optimized_duration) / original_duration * 100
    print(f"Improvement: {improvement:.2f}%")
