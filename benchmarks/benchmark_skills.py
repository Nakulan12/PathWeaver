import sys
import os
import time
import torch

# Add backend to path
sys.path.append(os.path.abspath('backend'))

from skills import extract_skills, model, SKILLS_DB, skill_embeddings
from sentence_transformers import util

def benchmark_current():
    test_text = "I am a python developer with experience in machine learning and data analysis. I also know react and node."
    # Simulate a larger text to see the impact
    large_text = (test_text + "\n") * 50

    start_time = time.time()
    skills = extract_skills(large_text)
    end_time = time.time()

    print(f"Current implementation took: {end_time - start_time:.4f} seconds")
    print(f"Found skills: {skills}")

def benchmark_optimized():
    test_text = "I am a python developer with experience in machine learning and data analysis. I also know react and node."
    large_text = (test_text + "\n") * 50

    start_time = time.time()

    text = large_text.lower()
    found_skills = set()

    # Step 1: Direct keyword match
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # Step 2: Batched Semantic matching
    sentences = [s.strip() for s in text.split("\n") if len(s.strip()) >= 5]

    if sentences:
        sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
        # cosine_similarity between (N, D) and (M, D) -> (N, M)
        similarities = util.cos_sim(sentence_embeddings, skill_embeddings)

        # Check if any sentence matches any skill above threshold
        # similarities shape is (num_sentences, num_skills)
        matched_indices = (similarities > 0.6).any(dim=0).nonzero(as_tuple=True)[0]
        for idx in matched_indices:
            found_skills.add(SKILLS_DB[idx])

    end_time = time.time()

    print(f"Optimized implementation took: {end_time - start_time:.4f} seconds")
    print(f"Found skills: {list(found_skills)}")

if __name__ == "__main__":
    print("Running Benchmark...")
    benchmark_current()
    benchmark_optimized()
