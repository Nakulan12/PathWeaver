import time
import statistics
from skills import extract_skills

SAMPLE_TEXT = """
I am a senior software engineer with 10 years of experience.
I have strong expertise in python and machine learning.
I also work with react and node for frontend and backend development.
My cloud experience includes aws and networking.
I have good communication skills and I am familiar with sql and data analysis.
I have used excel and statistics in my previous roles.
"""

def benchmark():
    print("Starting benchmark...")
    times = []
    for i in range(10):
        start_time = time.time()
        skills = extract_skills(SAMPLE_TEXT)
        end_time = time.time()
        duration = end_time - start_time
        times.append(duration)
        print(f"Run {i+1}: {duration:.4f}s")

    avg_time = statistics.mean(times)
    print(f"\nAverage time: {avg_time:.4f}s")
    print(f"Skills found: {skills}")

if __name__ == "__main__":
    benchmark()
