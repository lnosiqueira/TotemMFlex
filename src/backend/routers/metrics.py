from fastapi import APIRouter
from src.backend.services.database import get_interactions

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    data = get_interactions()

    if not data:
        return {"msg": "Sem dados ainda"}

    total = len(data)

    media_valor = round(sum(d.get("valor", 0) for d in data) / total, 2)
    media_tempo = round(sum(d.get("tempo_resposta", 0) for d in data) / total, 3)

    toques_curto = sum(1 for d in data if d.get("classificacao") == "toque_curto")
    toques_longo = sum(1 for d in data if d.get("classificacao") == "toque_longo")

    # 🧠 INSIGHT AUTOMÁTICO
    if toques_longo > toques_curto:
        insight = "Usuários estão engajando com perguntas mais longas"
    elif toques_curto > toques_longo:
        insight = "Usuários estão realizando interações rápidas, indicando uso direto e objetivo do sistema"
    else:
        insight = "Comportamento equilibrado entre curto e longo"

    {
   "total_interacoes": 20,
   "media_valor": 0.5,
   "toque_curto": 15,
   "toque_longo": 5
}