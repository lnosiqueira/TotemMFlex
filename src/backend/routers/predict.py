from fastapi import APIRouter
from datetime import datetime
import random

from src.backend.database import insert_interaction

router = APIRouter()

@router.post("/predict")
def predict():

    # simulação de valor
    valor = round(random.uniform(0.1, 1.0), 2)

    classificacao = "toque_curto" if valor < 0.4 else "toque_longo"

    data = datetime.now().isoformat()

    # 🔥 SALVA NO BANCO
    insert_interaction({
        "sensor_type": "api",
        "valor": valor,
        "classificacao": classificacao,
        "data": data
    })

    return {
        "status": "ok",
        "classificacao": classificacao,
        "valor": valor
    }