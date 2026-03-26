import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔥 cria uma pasta garantida
DB_FOLDER = os.path.join(BASE_DIR, "db")

# 🔥 garante que a pasta existe (ESSA LINHA É O OURO)
os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, "totemflex.db")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    print("🔥 Inicializando banco...")

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

    print("✅ Banco criado com sucesso")


def insert_interaction(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interactions (sensor_type, valor, classificacao, data)
        VALUES (?, ?, ?, ?)
    """, (
        data["sensor_type"],
        data["valor"],
        data["classificacao"],
        data["data"]
    ))

    conn.commit()
    conn.close()


def get_interactions():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interactions")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]