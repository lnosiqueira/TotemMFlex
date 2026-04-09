from fastapi import APIRouter
from src.backend.services.database import SessionLocal
from src.backend.services.model import Interaction

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    db = SessionLocal()

    dados = db.query(Interaction).all()

    total = len(dados)

    media = 0
    if total > 0:
        media = sum(d.valor for d in dados) / total

    db.close()

    return {
        "total_interacoes": total,
        "media_valor": round(media, 2)
    }