import time
from backend.skills import extract_skills

def benchmark():
    sample_text = """
    Experienced Software Engineer with a strong background in Python and Java.
    Proficient in SQL and data analysis using Excel.
    Excellent communication skills and experience with React and Node.
    Knowledge of cloud technologies like AWS and statistics for machine learning.

    Work Experience:
    - Developed web applications using React and Node.
    - Managed databases with SQL.
    - Performed data analysis to drive business decisions.
    - Used AWS for cloud infrastructure.
    - Applied machine learning techniques for predictive modeling.
    - Communicated complex technical concepts to non-technical stakeholders.
    """

    # Warm up
    extract_skills(sample_text)

    start_time = time.time()
    for _ in range(10):
        extract_skills(sample_text)
    end_time = time.time()

    print(f"Average time per extraction: {(end_time - start_time) / 10:.4f} seconds")

if __name__ == "__main__":
    benchmark()
