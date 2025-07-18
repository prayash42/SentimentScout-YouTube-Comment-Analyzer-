# sentiment_analysis.py
from transformers import pipeline

# Load once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiments(comments):
    results = sentiment_pipeline(comments, truncation=True)
    sentiments = [{"comment": c, "label": r["label"], "score": round(r["score"], 3)} 
                  for c, r in zip(comments, results)]
    return sentiments
