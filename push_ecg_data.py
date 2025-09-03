import pymysql
import pandas as pd
import json
from tqdm import tqdm
import math

# Load ECG data with vectors
df = pd.read_csv("data/demo_ecg_with_vectors.csv")

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

# Prepare data for insertion
insert_data = []
for idx, row in df.iterrows():
    case_name = f"demo_case_{idx+1}"
    symptoms = row["symptoms"] if "symptoms" in row else ""
    ecg_vector = row["ecg_vector"]
    insert_data.append((case_name, symptoms, ecg_vector))

# Batch insert to TiDB
batch_size = 100
num_batches = math.ceil(len(insert_data) / batch_size)

for i in tqdm(range(num_batches), desc="Pushing ECG data"):
    batch = insert_data[i*batch_size : (i+1)*batch_size]
    cursor.executemany("""
        INSERT INTO health_cases (case_name, symptoms, ecg_vector)
        VALUES (%s, %s, %s)
    """, batch)
    conn.commit()

print(f"Inserted {len(insert_data)} ECG cases into TiDB successfully ✅")
conn.close()
