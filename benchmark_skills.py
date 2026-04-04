import time
import torch
from backend.skills import extract_skills

test_text = """
Experienced software engineer with 5 years of experience in Python and Java.
Strong background in machine learning and data analysis.
Familiar with cloud technologies like AWS and Azure.
Excellent communication skills and experience with React and Node.js.
I have worked on several projects involving statistics and excel.
""" * 10  # Make it larger to see the difference

start_time = time.time()
skills = extract_skills(test_text)
end_time = time.time()

print(f"Extracted skills: {skills}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
