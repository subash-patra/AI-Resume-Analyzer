from src.pdf_reader import extract_text_from_pdf
from src.matcher import calculate_similarity
from src.skills import extract_skills, SKILLS

resume = extract_text_from_pdf("data/resume.pdf")

job_description = """
Python
SQL
TensorFlow
Machine Learning
"""

score = calculate_similarity(resume, job_description)
resume_skills = extract_skills(resume,SKILLS)
job_skills = extract_skills(job_description,SKILLS)
matched_skills = resume_skills & job_skills
missing_skills = job_skills - resume_skills


print("Extracted Resume:\n")
print(resume)

print("\n--------------------------")

print(f"\nResume Match Score: {score:.2%}")

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)