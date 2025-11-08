#!/usr/bin/env python3
import time, os, json
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from tinydb import TinyDB

# Paths
BASE = Path(__file__).parent.resolve()
TRAIN_CSV = BASE / "data" / "train_data.csv"
LOGFILE = BASE / "events.log"
DBFILE = BASE / "profiles.json"

# Train model
def train_model():
    df = pd.read_csv(TRAIN_CSV)
    X, y = df['text'], df['label']
    model = make_pipeline(
        TfidfVectorizer(ngram_range=(1,2), max_features=2000),
        LogisticRegression(max_iter=1000)
    )
    model.fit(X, y)
    return model

# Simple explain function
def explain(model, text):
    return f"Prediction based on token and context analysis of: '{text[:60]}...'"

# Real-time log classifier
def classify_stream(model):
    db = TinyDB(DBFILE)
    last_size = 0
    LOGFILE.touch(exist_ok=True)
    print(f"🧠 Monitoring {LOGFILE} for new events...")
    while True:
        size = LOGFILE.stat().st_size
        if size > last_size:
            with open(LOGFILE, 'r') as f:
                f.seek(last_size)
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    pred = model.predict([line])[0]
                    prob = max(model.predict_proba([line])[0])
                    score = round(prob * 10, 2)
                    record = {
                        "time": time.strftime('%Y-%m-%d %H:%M:%S'),
                        "text": line,
                        "prediction": pred,
                        "score": score,
                        "explain": explain(model, line)
                    }
                    db.insert(record)
                    print(f"[+] {record['prediction']} | {record['score']}/10 | {record['text']}")
            last_size = size
        time.sleep(1)

if __name__ == "__main__":
    model = train_model()
    classify_stream(model)
