"""Skill extraction via lexicon phrase matching.

Matches a curated lexicon of technical and soft skills against normalized text.
Multi-word skills ("machine learning") are matched as phrases; single tokens as
whole words.
"""

import re

from src.preprocessing import normalize

SKILL_LEXICON = [
    # Programming languages
    "python", "java", "javascript", "typescript", "c++", "c#", "c", "r", "go",
    "rust", "sql", "php", "swift", "kotlin", "matlab", "scala",
    # ML / NLP
    "machine learning", "deep learning", "natural language processing", "nlp",
    "computer vision", "transformers", "bert", "gpt", "llm", "pytorch",
    "tensorflow", "keras", "scikit-learn", "hugging face", "spacy", "nltk",
    "pandas", "numpy", "data analysis", "data science", "feature engineering",
    "model evaluation", "fine-tuning", "prompt engineering", "reinforcement learning",
    "statistics", "classification", "regression", "clustering",
    # Web / software
    "react", "angular", "vue", "node.js", "django", "flask", "fastapi",
    "rest api", "graphql", "html", "css", "git", "github", "docker",
    "kubernetes", "aws", "azure", "gcp", "linux", "ci/cd", "agile", "scrum",
    "unit testing", "mongodb", "postgresql", "mysql", "redis",
    # Soft skills
    "communication", "teamwork", "problem solving", "leadership",
    "time management", "mentoring", "collaboration", "presentation",
]


def extract_skills(text, lexicon=SKILL_LEXICON):
    """Return the sorted set of lexicon skills present in text."""
    normalized = normalize(text)
    found = set()
    for skill in lexicon:
        # Whole-phrase match with escaped special chars (c++, c#, node.js)
        pattern = r"(?<![a-z0-9+#.])" + re.escape(skill) + r"(?![a-z0-9+#.])"
        if re.search(pattern, normalized):
            found.add(skill)
    return sorted(found)
