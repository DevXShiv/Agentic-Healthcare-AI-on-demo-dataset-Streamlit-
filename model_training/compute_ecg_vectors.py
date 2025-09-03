import pandas as pd
import numpy as np
import json
from sentence_transformers import SentenceTransformer
import os

# Load demo ECG
df = pd.read_csv("data/demo_ecg.csv")

# Create folder if doesn't exist
os.makedirs("backend/models", exist_ok=True)

# Load embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert each ECG row to a “text” string for embedding
ecg_vectors = []
for idx, row in df.iterrows():
    # Convert numeric row to comma-separated string
    row_str = ",".join(map(str, row.values))
    vec = embed_model.encode(row_str)
    ecg_vectors.append(vec.tolist())

# Save vectors as JSON
df["ecg_vector"] = [json.dumps(vec) for vec in ecg_vectors]
df.to_csv("data/demo_ecg_with_vectors.csv", index=False)

print("ECG vectors computed and saved to data/demo_ecg_with_vectors.csv")
