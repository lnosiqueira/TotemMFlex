from fastapi import APIRouter
from src.backend.services.database import get_interactions

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    data = get_interactions()

    if not data:
        return {"msg": "Sem dados ainda"}

    total = len(data)

    media_valor = round(sum(d["valor"] for d in data) / total, 2)
    media_tempo = round(sum(d["tempo_resposta"] for d in data) / total, 3)

    toques_curto = sum(1 for d in data if d["classificacao"] == "toque_curto")
    toques_longo = sum(1 for d in data if d["classificacao"] == "toque_longo")

    return {
        "total_interacoes": total,
        "media_valor": media_valor,
        "media_tempo": media_tempo,
        "toque_curto": toques_curto,
        "toque_longo": toques_longo
    }