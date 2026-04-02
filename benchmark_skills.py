import time
import numpy as np
from skills import extract_skills

# Mock a large-ish resume/JD text
large_text = """
Experienced Software Engineer with a strong background in Python and Java.
Expertise in SQL and Machine Learning.
Worked on various data analysis projects using Excel.
Excellent communication skills.
Developed web applications using React and Node.
Experienced with Cloud technologies, specifically AWS.
Strong foundation in Statistics and Mathematics.
""" * 50 # 50 times to make it significant

def benchmark():
    start_time = time.time()
    skills = extract_skills(large_text)
    end_time = time.time()

    print(f"Extracted skills: {skills}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
