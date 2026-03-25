import sqlite3
from datetime import datetime
import os

# Caminho absoluto do banco (funciona local e no Render)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "totem.db")


def get_db_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_type TEXT NOT NULL,
        value REAL NOT NULL,
        prediction TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_interaction(valor: float, pred: str, sensor_type: str = "sensor_simulado"):
    conn = get_db_connection()
    cursor = conn.cursor()

    created_at = datetime.now().replace(microsecond=0).isoformat()

    cursor.execute("""
    INSERT INTO interactions (sensor_type, value, prediction, created_at)
    VALUES (?, ?, ?, ?)
    """, (sensor_type, float(valor), str(pred), created_at))

    conn.commit()
    conn.close()


def get_interactions():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, sensor_type, value, prediction, created_at
    FROM interactions
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    interactions = []
    for row in rows:
        interactions.append({
            "id": row[0],
            "sensor_type": row[1],
            "valor": row[2],
            "classificacao": row[3],
            "data": row[4]
        })

    conn.close()

    return interactions