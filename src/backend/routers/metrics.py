from fastapi import APIRouter
import sqlite3

router = APIRouter()

DB_PATH = "totem.db"


@router.get("/metrics")
def get_metrics():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # total
        cursor.execute("SELECT COUNT(*) FROM interactions")
        total = cursor.fetchone()[0]

        # agrupado
        cursor.execute("""
            SELECT classificacao, COUNT(*) 
            FROM interactions 
            GROUP BY classificacao
        """)
        rows = cursor.fetchall()

        conn.close()

        classificacoes = {
            "toque_curto": 0,
            "toque_longo": 0
        }

        for row in rows:
            classificacoes[row[0]] = row[1]

        return {
            "total_interacoes": total,
            "toque_curto": classificacoes["toque_curto"],
            "toque_longo": classificacoes["toque_longo"]
        }

    except Exception as e:
        # 🔥 NUNCA MAIS QUEBRA
        return {
            "total_interacoes": 0,
            "toque_curto": 0,
            "toque_longo": 0,
            "error": str(e)
        }