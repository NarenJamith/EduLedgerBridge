# alignment_metrics.py
from difflib import SequenceMatcher

def compute_similarity(row1, row2):
    total_score = 0
    fields = ['GL Account', 'Amount', 'Cost Center']
    for field in fields:
        a = str(row1[field])
        b = str(row2[field])
        score = SequenceMatcher(None, a, b).ratio()
        total_score += score
    return total_score / len(fields)
