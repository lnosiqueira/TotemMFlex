from fastapi import APIRouter
from pydantic import BaseModel
import random
from datetime import datetime
from src.backend.services.database import insert_interaction

router = APIRouter(prefix="/predict", tags=["Predict"])

class InputData(BaseModel):
    valor: float

@router.post("/")
def predict(data: InputData):

    valor = data.valor

    if valor < 0.5:
        classificacao = "toque_curto"
    else:
        classificacao = "toque_longo"

    nova_interacao = {
        "sensor_type": "api",
        "valor": valor,
        "classificacao": classificacao,
        "data": datetime.now().isoformat()
    }

    insert_interaction(nova_interacao)

    return {
        "status": "ok",
        "classificacao": classificacao,
        "valor": valor
    }