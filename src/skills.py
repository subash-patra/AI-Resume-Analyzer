import re

SKILLS = {
    "python",
    "sql",
    "tensorflow",
    "pandas",
    "numpy",
    "machine learning",
    "deep learning",
    "git",
    "github",
    "c",
    "c++"
}

SYNONYMS = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing"
}
def clean_text(text):
    """
    Improved text cleaning for better NLP matching
    """

    text = text.lower()

    # important special cases like c++,c#,and more
    text = text.replace("c++","cplusplus")
    text = text.replace("c#","csharp")

    # replace hyphens with space (machine-learning → machine learning)
    text = re.sub(r"[-/]", " ", text)

    # remove everything except letters and spaces
    text = re.sub(r"[^a-z\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def extract_skills(text, SKILLS):
    """
    Improved skill extraction using cleaned text
    """

    text = clean_text(text)

    for short_form,full_form in SYNONYMS.items():
        text = text.replace(short_form,full_form)
    
    word_set = set(text.split())

    found_skills = set()

    for skill in SKILLS:
        skill_clean = clean_text(skill)

        # multi-word skills
        if " " in skill_clean:
            if skill_clean in text:
                found_skills.add(skill_clean)

        # single-word skills
        else:
            if skill_clean in word_set:
                found_skills.add(skill_clean)

    return found_skills