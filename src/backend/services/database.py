import sqlite3
from datetime import datetime


def get_db_connection():
    conn = sqlite3.connect("totemflex.db")
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
            pergunta TEXT,
            resposta TEXT,
            tempo_resposta REAL,
            valor REAL,
            classificacao TEXT,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("✅ Banco criado com sucesso")


def insert_interaction(data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO interactions (
                sensor_type,
                pergunta,
                resposta,
                tempo_resposta,
                valor,
                classificacao,
                data
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("sensor_type"),
            data.get("pergunta"),
            data.get("resposta"),
            data.get("tempo_resposta"),
            data.get("valor"),
            data.get("classificacao"),
            data.get("data", datetime.now().isoformat())
        ))

        conn.commit()
        conn.close()

        print("✅ Interação salva com sucesso")

    except Exception as e:
        print("❌ Erro ao salvar interação:", str(e))


def get_interactions():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM interactions")
        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    except Exception as e:
        print("❌ Erro ao buscar interações:", str(e))
        return []