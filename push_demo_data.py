import pandas as pd
import numpy as np
import pymysql
from sentence_transformers import SentenceTransformer
import json

# Load demo symptom data
df = pd.read_csv("data/Training.csv")  # your Training.csv from demo_data_generator

# We'll use a small subset for demo
demo_df = df.sample(5, random_state=42)

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to TiDB
conn = pymysql.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4ALQsV1JXs7TTLr.root",
    password="ZNDGQQiArl4qcGGx",
    database="test",
    ssl={'ca': '/etc/ssl/cert.pem'}
)
cursor = conn.cursor()

for idx, row in demo_df.iterrows():
    # Combine symptoms into a string
    symptoms_text = ", ".join([col for col in df.columns[:-1] if row[col] == 1])
    
    # Generate embedding for symptoms
    ecg_vector = model.encode(symptoms_text).tolist()
    
    # Insert into TiDB
    cursor.execute("""
        INSERT INTO health_cases (case_name, symptoms, ecg_vector)
        VALUES (%s, %s, %s)
    """, (f"demo_case_{idx}", symptoms_text, json.dumps(ecg_vector)))

conn.commit()
conn.close()
print("Inserted demo cases into TiDB successfully ✅")
