from fastapi import APIRouter
from datetime import datetime
import time

from src.backend.services.database import insert_interaction

router = APIRouter()

@router.post("/predict")
def predict(data: dict):

    pergunta = data.get("pergunta", "").strip()

    start = time.time()

    # 🧠 LÓGICA DE RESPOSTA (simples, mas inteligente)
    if not pergunta:
        resposta = "Você não enviou nenhuma pergunta."
    elif "ia" in pergunta.lower():
        resposta = "IA é a simulação da inteligência humana por máquinas."
    elif "totem" in pergunta.lower():
        resposta = "O TotemMFlex é um assistente inteligente interativo."
    else:
        resposta = f"Interessante pergunta! Você disse: '{pergunta}'"

    end = time.time()
    tempo_resposta = round(end - start, 3)

    # 📊 SCORE INTELIGENTE
    tamanho = len(pergunta)

    if tamanho == 0:
        valor = 0.0
    elif tamanho < 20:
        valor = 0.3
    elif tamanho < 50:
        valor = 0.6
    else:
        valor = 0.9

    # 🎯 CLASSIFICAÇÃO
    classificacao = "toque_curto" if valor < 0.5 else "toque_longo"

    data_registro = datetime.now().isoformat()

    # 💾 SALVA NO BANCO
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