import time
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from skills import extract_skills

sample_text = """
John Doe
Software Engineer
Experience with python and java.
Worked on machine learning projects using statistics and data analysis.
Skilled in react and node for frontend and backend development.
Familiar with cloud technologies like aws and azure.
Excellent communication skills.
""" * 10 # Make it a bit larger to measure

start_time = time.time()
skills = extract_skills(sample_text)
end_time = time.time()

print(f"Extracted skills: {skills}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
