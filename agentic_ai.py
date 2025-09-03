import pymysql
import json
import numpy as np
import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load trained symptom model + label encoder
MODEL_PATH = "backend/models/symptom_model.pkl"
LE_PATH = "backend/models/label_encoder.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(LE_PATH, "rb") as f:
    le = pickle.load(f)

# Load embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# TiDB connection
conn = pymysql.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4ALQsV1JXs7TTLr.root",
    password="ZNDGQQiArl4qcGGx",
    database="test",
    ssl={'ca': '/etc/ssl/cert.pem'}
)
cursor = conn.cursor()

def agentic_ai_predict(user_symptoms_dict, user_ecg_vector=None):
    """
    Returns the most similar demo case + predicted prognosis
    user_symptoms_dict: dict of symptom flags (1/0)
    user_ecg_vector: list or np.array (optional) for ECG similarity
    """
    # Convert symptom dict to string for embedding
    symptoms_text = ", ".join([k for k, v in user_symptoms_dict.items() if v == 1])
    user_symptom_vector = embed_model.encode(symptoms_text).reshape(1, -1)
    
    # Prepare ECG vector if provided
    if user_ecg_vector is not None:
        user_ecg_vector = np.array(user_ecg_vector).reshape(1, -1)
    
    # Fetch all cases from TiDB
    cursor.execute("SELECT case_name, symptoms, ecg_vector FROM health_cases")
    rows = cursor.fetchall()
    
    case_vectors = []
    case_names = []
    case_symptoms = []
    
    for row in rows:
        case_names.append(row[0])
        case_symptoms.append(row[1])
        try:
            ecg_vec = np.array(json.loads(row[2]))
        except Exception:
            # Fallback if ecg_vector is NULL or invalid
            ecg_vec = np.zeros((384,))  # example dimension
        case_vectors.append(ecg_vec)
    
    # Compute similarity
    if user_ecg_vector is not None:
        sims = cosine_similarity(user_ecg_vector, case_vectors)[0]
    else:
        sims = cosine_similarity(user_symptom_vector, case_vectors)[0]
    
    best_idx = np.argmax(sims)
    
    # Predict prognosis using symptom model
    df_input = pd.DataFrame([user_symptoms_dict])
    pred_enc = model.predict(df_input)[0]
    prognosis = le.inverse_transform([pred_enc])[0]
    
    return {
        "matched_case": case_names[best_idx],
        "matched_symptoms": case_symptoms[best_idx],
        "predicted_prognosis": prognosis,
        "similarity_score": float(sims[best_idx])
    }


if __name__ == "__main__":
    # Demo input
    user_input = {
        "fever": 1, "cough": 1, "fatigue": 0, "headache": 0, "chest_pain": 0,
        "sob": 0, "diarrhea": 0, "nausea": 0, "dizziness": 0, "sore_throat": 0
    }
    
    # Optional: use first ECG vector from demo data
    df_ecg = pd.read_csv("data/demo_ecg_with_vectors.csv")
    user_ecg_vec = json.loads(df_ecg.loc[0, "ecg_vector"])
    
    result = agentic_ai_predict(user_input, user_ecg_vector=user_ecg_vec)
    print(result)
