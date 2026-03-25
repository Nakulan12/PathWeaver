import time
import torch
from skills import extract_skills

# Large text with many sentences to highlight batching speedup
sample_text = """
Experienced Software Engineer with a strong background in Python and Machine Learning.
Proficient in Java and SQL. Worked on various data analysis projects using Excel.
Excellent communication skills.
Developed web applications using React and Node.
Experienced with Cloud technologies like AWS.
Strong understanding of Statistics.
""" * 100  # Increased from 10 to 100

start_time = time.time()
skills = extract_skills(sample_text)
end_time = time.time()

print(f"Extracted skills: {skills}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
