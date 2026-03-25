from fastapi import APIRouter
from src.backend.services.database import get_db_connection

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    conn = get_db_connection()
    cursor = conn.cursor()

    # total de interações
    cursor.execute("SELECT COUNT(*) FROM interactions")
    total = cursor.fetchone()[0]

    # média dos valores
    cursor.execute("SELECT AVG(value) FROM interactions")
    media = cursor.fetchone()[0] or 0

    # classificação mais comum (CORRIGIDO AQUI 👇)
    cursor.execute("""
        SELECT prediction, COUNT(*) as count
        FROM interactions
        GROUP BY prediction
        ORDER BY count DESC
        LIMIT 1
    """)

    result = cursor.fetchone()
    mais_comum = result[0] if result else "N/A"

    conn.close()

    return {
        "total_interacoes": total,
        "media_valor": round(media, 2),
        "mais_comum": mais_comum
    }