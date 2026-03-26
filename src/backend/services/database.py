import sqlite3

DB_PATH = "src/database/totem.db"


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