from src.pdf_reader import extract_text_from_pdf
from src.matcher import calculate_similarity

resume = extract_text_from_pdf("data/resume.pdf")

job_description = """
Python
SQL
TensorFlow
Machine Learning
"""

score = calculate_similarity(resume, job_description)

print("Extracted Resume:\n")
print(resume)

print("\n--------------------------")

print(f"\nResume Match Score: {score:.2%}")