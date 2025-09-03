# demo_data_generator.py
import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

symptoms = ["fever","cough","fatigue","headache","chest_pain","sob","diarrhea","nausea","dizziness","sore_throat"]

diseases = {
    "Common Cold": ["cough","sore_throat","headache"],
    "Flu": ["fever","cough","fatigue","headache"],
    "COVID-19": ["fever","cough","fatigue","sob"],
    "Gastritis": ["nausea","diarrhea","dizziness"],
    "Heart Attack": ["chest_pain","sob","dizziness"]
}

rows = []
np.random.seed(42)
for i in range(300):
    disease = np.random.choice(list(diseases.keys()), p=[0.25,0.25,0.2,0.15,0.15])
    row = {}
    for s in symptoms:
        val = 1 if s in diseases[disease] and np.random.rand() < 0.9 else (1 if np.random.rand()<0.05 else 0)
        row[s] = val
    row["prognosis"] = disease
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("data/Training.csv", index=False)
print("Wrote data/Training.csv with columns:", df.columns.tolist())

# create a tiny demo ECG CSV (single-lead synthetic signal)
t = np.linspace(0, 10, 3000)  # 10 seconds, 300 Hz
signal = 0.1*np.random.randn(len(t)) + 0.8*np.sin(2*np.pi*1.2*t) * (np.exp(-((t%1)-0.0)**2 / 0.02))
pd.DataFrame({"signal": signal}).to_csv("data/demo_ecg.csv", index=False)
print("Wrote data/demo_ecg.csv")
