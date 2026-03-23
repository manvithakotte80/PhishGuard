import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("dataset.csv")

X = data[["url_length", "dots", "has_at", "https", "http", "hyphen"]]
y = data["label"]

model = RandomForestClassifier(n_estimators=150)
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model upgraded and trained!")