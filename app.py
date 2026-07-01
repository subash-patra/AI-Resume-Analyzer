print("AI Resume Analyzer")
from src.matcher import calculate_similarity

resume = """
Python
SQL
Pandas
Machine Learning
"""

job_description = """
Python
SQL
TensorFlow
Machine Learning
"""

score = calculate_similarity(resume, job_description)

print(f"Resume Match Score: {score:.2%}")