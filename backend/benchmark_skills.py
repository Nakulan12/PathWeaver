import time
import torch
from skills import extract_skills

# Mock text that resembles a resume/JD
sample_text = """
Experienced Software Engineer with a strong background in Python and Java.
Proficient in SQL and data analysis using Excel.
Worked on machine learning projects and developed web applications with React and Node.
Excellent communication skills and experience with cloud platforms like AWS.
Strong understanding of statistics and its application in data science.
Experience with Docker and Kubernetes for containerization.
Familiar with Agile methodologies and Scrum.
Deep learning and neural networks experience.
Natural Language Processing and Computer Vision.
Big Data technologies like Spark and Hadoop.
""" * 5  # Make it larger to see the difference

def benchmark():
    start_time = time.time()
    skills = extract_skills(sample_text)
    end_time = time.time()
    print(f"Extracted skills: {skills}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
