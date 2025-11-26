from fastapi import APIRouter
from pydantic import BaseModel
from src.backend.services.model import load_model, predict_value
from src.backend.services.database import save_interaction

router = APIRouter(prefix="/predict", tags=["Predição"])

class SensorInput(BaseModel):
    value: float

model = load_model()

@router.post("/")
def predict_route(data: SensorInput):
    pred = predict_value(model, data.value)
    save_interaction(sensor_type="simulado", value=data.value, prediction=pred)
    return {"value": data.value, "prediction": pred}


