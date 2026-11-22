# Resume Screening and Job Matching Prototype

A prototype applicant-tracking-style screener: given a resume and a job
description, it scores how well they match and explains the score with the
skills it found, matched, and missed.

## How it works

1. **Text preprocessing** (`src/preprocessing.py`) - lowercasing, punctuation
   stripping (keeping `c++`, `c#`, `.net` intact), tokenization and stopword
   removal, with no external data downloads.
2. **Skill extraction** (`src/skill_extraction.py`) - phrase matching against a
   curated lexicon of programming languages, ML/NLP frameworks, software tools,
   and soft skills.
3. **Similarity scoring** (`src/matching.py`) - two complementary signals,
   blended 50/50 by default:
   - TF-IDF vectors + cosine similarity over the full texts (scikit-learn)
   - Skill recall: the share of the job's required skills the resume covers

The output is a single match score plus the matched and missing skills, so the
result is explainable rather than a black-box number.

## Example

```bash
pip install -r requirements.txt
python main.py --resume data/sample_resume.txt --job data/sample_job_description.txt
```

```
Match score:        48.6%
TF-IDF similarity:  0.207
Skill recall:       76.5%
Matched skills:     python, pytorch, tensorflow, transformers, hugging face,
                    natural language processing, pandas, numpy, git, linux, ...
Missing skills:     aws, classification, docker, rest api
```

(Numbers are from the bundled sample documents.)

## Project structure

```
├── main.py                        # CLI: score one resume against one job post
├── data/
│   ├── sample_resume.txt          # example resume
│   └── sample_job_description.txt # example job post
├── src/
│   ├── preprocessing.py           # normalization, tokenization, stopwords
│   ├── skill_extraction.py        # lexicon-based skill matching
│   └── matching.py                # TF-IDF cosine similarity + skill recall
└── requirements.txt
```

## Notes and extensions

- The scorer is deterministic and transparent by design; the skill lexicon is a
  plain Python list in `src/skill_extraction.py` and easy to extend per domain.
- Natural next steps: batch screening of many resumes against one post, a small
  classifier learned on labeled hiring decisions, and embedding-based
  (semantic) similarity alongside TF-IDF.
