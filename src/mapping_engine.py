# mapping_engine.py
import pandas as pd
from src.alignment_metrics import compute_similarity

def map_journal_entries(oracle_df, sap_df):
    mappings = []
    for idx, oracle_row in oracle_df.iterrows():
        best_match = None
        highest_score = 0
        for _, sap_row in sap_df.iterrows():
            score = compute_similarity(oracle_row, sap_row)
            if score > highest_score:
                highest_score = score
                best_match = sap_row
        mappings.append((oracle_row.to_dict(), best_match.to_dict(), highest_score))
    return mappings
