import sqlite3
from datetime import datetime

DB_PATH = "totem.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_type TEXT,
            valor REAL,
            classificacao TEXT,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()


# 🔥 ESSA FUNÇÃO ESTAVA FALTANDO
def get_interactions():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interactions ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


# 🔥 OPCIONAL MAS IMPORTANTE
def insert_interaction(sensor_type, valor, classificacao):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interactions (sensor_type, valor, classificacao, data)
        VALUES (?, ?, ?, ?)
    """, (sensor_type, valor, classificacao, datetime.now().isoformat()))

    conn.commit()
    conn.close()