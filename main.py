"""Screen a resume against a job description.

Usage:
    python main.py --resume data/sample_resume.txt --job data/sample_job_description.txt
"""

import argparse

from src.matching import match_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", default="data/sample_resume.txt")
    parser.add_argument("--job", default="data/sample_job_description.txt")
    args = parser.parse_args()

    resume_text = open(args.resume, encoding="utf-8").read()
    job_text = open(args.job, encoding="utf-8").read()

    result = match_score(resume_text, job_text)
    print(f"Match score:        {result['score']:.1%}")
    print(f"TF-IDF similarity:  {result['tfidf_similarity']:.3f}")
    print(f"Skill recall:       {result['skill_recall']:.1%}")
    print(f"Matched skills:     {', '.join(result['matched_skills']) or '-'}")
    print(f"Missing skills:     {', '.join(result['missing_skills']) or '-'}")


if __name__ == "__main__":
    main()
