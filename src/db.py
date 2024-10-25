import os
import psycopg2

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME", "agenda"),
    user=os.getenv("DB_USER", "username"),
    password=os.getenv("DB_PASSWORD", "password")
)
cursor = conn.cursor()
