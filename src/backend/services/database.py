import sqlite3

DB_PATH = "database/totemflex.db"

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
    print("✅ Banco pronto")

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