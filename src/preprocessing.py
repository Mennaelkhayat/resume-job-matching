"""Text preprocessing for resume and job-description matching."""

import re

# Compact English stopword list (the usual suspects, no external downloads).
STOPWORDS = frozenset(
    "a an the and or but if then else when at by for with about into through "
    "during before after above below to from up down in out on off over under "
    "again further once here there all any both each few more most other some "
    "such no nor not only own same so than too very can will just should now "
    "i me my we our you your he him his she her it its they them their this "
    "that these those am is are was were be been being have has had having do "
    "does did doing would could ought as of us".split()
)


def normalize(text):
    """Lowercase, strip punctuation, collapse whitespace."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)  # keep c++, c#, .net readable
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text):
    """Normalize, then split into content tokens (stopwords removed)."""
    return [tok for tok in normalize(text).split() if tok not in STOPWORDS and len(tok) > 1]
