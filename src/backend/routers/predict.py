from fastapi import APIRouter
from datetime import datetime
import time

from src.backend.services.database import insert_interaction

router = APIRouter()

@router.post("/predict")
def predict(data: dict):

    pergunta = data.get("pergunta", "")

    start = time.time()

    # Simulação básica de resposta (depois plugamos IA real)
    resposta = f"Resposta para: {pergunta}"

    end = time.time()
    tempo_resposta = round(end - start, 2)

    # Score baseado no tamanho da pergunta (simples, mas REAL)
    valor = round(min(len(pergunta) / 100, 1), 2)

    classificacao = "toque_curto" if valor < 0.4 else "toque_longo"

    data_registro = datetime.now().isoformat()

    # 🔥 SALVA NO BANCO
    insert_interaction({
        "sensor_type": "api",
        "pergunta": pergunta,
        "resposta": resposta,
        "tempo_resposta": tempo_resposta,
        "valor": valor,
        "classificacao": classificacao,
        "data": data_registro
    })

    return {
        "status": "ok",
        "resposta": resposta,
        "classificacao": classificacao,
        "valor": valor,
        "tempo_resposta": tempo_resposta
    }

    return {
    "status": "ok",
    "versao": "TOTEM_V2_DEPLOY_TESTE",
}