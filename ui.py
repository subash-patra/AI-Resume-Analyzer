import streamlit as st
from src.pdf_reader import extract_text_from_pdf
from src.matcher import calculate_similarity
from src.skills import extract_skills


st.title("📄 AI Resume Analyzer")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job Description
jd = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and jd:

        # Save uploaded file temporarily
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())

        # Extract resume text
        resume_text = extract_text_from_pdf("temp_resume.pdf")

        # Match score (we assume you already have this function)
        score = calculate_similarity(resume_text, jd)

        # Extract skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd)

        matched = resume_skills.intersection(jd_skills)
        missing = jd_skills - resume_skills

        st.subheader("📊 Analysis Result")

        # Score display
        st.markdown(f"### 🎯 Match Score: {score:.2f}%")

        # Progress bar (0–100)
        st.progress(int(score))

        # Layout split
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## ✅ Matched Skills")
            for skill in matched:
                st.success(skill)

        with col2:
            st.markdown("## ❌ Missing Skills")
            for skill in missing:
                st.error(skill)

    else:
        st.warning("Please upload resume and job description")