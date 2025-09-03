import pymysql

conn = pymysql.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4ALQsV1JXs7TTLr.root",
    password="ZNDGQQiArl4qcGGx",
    database="test",
    ssl={'ca': '/etc/ssl/cert.pem'}
)

cursor = conn.cursor()

# Create table for symptom + ECG embeddings
cursor.execute("""
CREATE TABLE IF NOT EXISTS health_cases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    case_name VARCHAR(255),
    symptoms TEXT,
    ecg_vector JSON
)
""")

print("Table 'health_cases' created or already exists.")

conn.commit()
conn.close()
