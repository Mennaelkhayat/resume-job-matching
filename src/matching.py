"""Similarity scoring between a resume and a job description.

Combines two signals:
- TF-IDF cosine similarity over the full texts (scikit-learn)
- Skill overlap: extracted-skill recall against the job's required skills
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocessing import normalize
from src.skill_extraction import extract_skills


def tfidf_similarity(resume_text, job_text):
    """Cosine similarity between TF-IDF vectors of the two documents."""
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    vectors = vectorizer.fit_transform([normalize(resume_text), normalize(job_text)])
    return float(cosine_similarity(vectors[0], vectors[1])[0, 0])


def skill_overlap(resume_text, job_text):
    """Skill recall: which job-required skills the resume covers."""
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    recall = len(matched) / len(job_skills) if job_skills else 0.0
    return recall, matched, missing


def match_score(resume_text, job_text, tfidf_weight=0.5):
    """Weighted blend of TF-IDF similarity and skill recall, in [0, 1]."""
    tfidf = tfidf_similarity(resume_text, job_text)
    recall, matched, missing = skill_overlap(resume_text, job_text)
    score = tfidf_weight * tfidf + (1 - tfidf_weight) * recall
    return {
        "score": round(score, 3),
        "tfidf_similarity": round(tfidf, 3),
        "skill_recall": round(recall, 3),
        "matched_skills": matched,
        "missing_skills": missing,
    }
