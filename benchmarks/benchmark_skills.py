import time
from backend.skills import extract_skills

sample_text = """
I am a highly motivated software engineer with experience in Python and Java.
I have worked on several machine learning projects using Scikit-Learn and TensorFlow.
My data analysis skills are top-notch, and I am proficient in Excel.
I also have experience with React and Node.js for web development.
I have a good understanding of cloud computing and AWS.
I am also familiar with statistics and mathematical modeling.
Communication is one of my strong suits.
I am looking for a role where I can apply my technical skills to solve complex problems.
""" * 100 # Make it even longer to see the impact

# First run to ensure everything is loaded
extract_skills("warmup text")

start_time = time.time()
skills = extract_skills(sample_text)
end_time = time.time()

print(f"Extracted skills: {skills}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
