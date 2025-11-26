import sqlite3
from datetime import datetime

DB_PATH = "src/database/totem.db"

def save_interaction(sensor_type, value, prediction):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_type TEXT,
            value REAL,
            prediction TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO interactions (sensor_type, value, prediction, created_at)
        VALUES (?, ?, ?, ?)
    """, (sensor_type, value, prediction, datetime.now().isoformat()))

    conn.commit()
    conn.close()


