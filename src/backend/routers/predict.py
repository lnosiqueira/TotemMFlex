from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.backend.services.model import load_model, predict_value
from src.backend.services.database import save_interaction

router = APIRouter(prefix="/predict", tags=["Predição"])


class SensorInput(BaseModel):
    valor: float = Field(..., description="Valor do sensor (0.0 a 1.0)")


_model = None


def _get_model():
    global _model
    if _model is None:
        _model = load_model()
    return _model


@router.post("")
def make_prediction(data: SensorInput):
    """
    Recebe um valor (float) e retorna a classificação prevista:
    - toque_curto
    - toque_longo

    Também salva a interação no banco SQLite.
    """
    try:
        model = _get_model()
        resultado = predict_value(model, data.valor)

        # salva no banco para rastreabilidade
        save_interaction(valor=data.valor, pred=resultado, sensor_type="sensor_simulado")

        return {
            "valor_sensor": data.valor,
            "classificacao": resultado,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {e}")