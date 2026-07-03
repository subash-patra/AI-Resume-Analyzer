SKILLS = {
    "python",
    "sql",
    "tensorflow",
    "pandas",
    "numpy",
    "machine learning",
    "deep learning",
    "scikit-learn",
    "streamlit",
    "git",
    "github",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "nlp",
    "data analysis",
    "matplotlib"
}

def extract_skills(text):
    """
    Extract known skills from text.
    """

    text = text.lower()

    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return found_skills