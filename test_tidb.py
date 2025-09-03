import pymysql

# Connect to your TiDB Serverless cluster
conn = pymysql.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4ALQsV1JXs7TTLr.root",
    password="ZNDGQQiArl4qcGGx",
    database="test",
    ssl={'ca': '/etc/ssl/cert.pem'}
)

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print("Connected to TiDB version:", version)
conn.close()
