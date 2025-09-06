from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_sentiment_pipeline():
    pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return pipe

def analyze_text(text: str):
    pipe = get_sentiment_pipeline()
    result = pipe(text, truncation=True)[0]
    return {
        "label": result.get("label"),
        "score": float(result.get("score", 0.0))
    }
