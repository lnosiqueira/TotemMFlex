from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class InputData(BaseModel):
    valor: int

@router.post("/predict")
def predict(data: InputData):
    valor = data.valor

    if valor < 30:
        classificacao = "toque_curto"
    elif valor < 70:
        classificacao = "toque_medio"
    else:
        classificacao = "toque_longo"

    return {
        "valor_sensor": valor,
        "classificacao": classificacao
    }