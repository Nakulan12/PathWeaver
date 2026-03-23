import time
from backend.skills import extract_skills

def benchmark():
    text = """
    I have extensive experience with Python and Java.
    I am also proficient in SQL and machine learning.
    Data analysis and Excel are my strong suits.
    I have great communication skills.
    I worked with React and Node.
    Cloud and AWS are also areas of my expertise.
    Statistics is also something I am good at.
    """ * 10  # Make it larger to see the difference

    start_time = time.time()
    skills = extract_skills(text)
    end_time = time.time()

    print(f"Extracted skills: {skills}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
