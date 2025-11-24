from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(
    title="ToteMFlex API",
    description="Backend da plataforma ToteMFlex - Global Solution FIAP 2025.2",
    version="1.0.0"
)

class CheckinRequest(BaseModel):
    colaborador_id: int
    humor: int           # 1-5
    nivel_estresse: int  # 1-5
    horas_sono: float
    observacoes: Optional[str] = None

@app.get("/")
def root():
    return {
        "message": "ToteMFlex API online na Azure!",
        "status": "ok",
        "versao": "1.0.0"
    }

@app.post("/checkin")
def checkin(payload: CheckinRequest):
    score = payload.nivel_estresse - payload.humor

    if score <= 0:
        risco = "baixo"
        recomendacao = "Continue assim! Mantenha pausas e hidratação."
    elif score <= 2:
        risco = "moderado"
        recomendacao = "Atenção! Faça uma pausa de 5 minutos."
    else:
        risco = "alto"
        recomendacao = "Risco elevado. Procure apoio da liderança."

    return {
        "mensagem": "Check-in processado",
        "risco": risco,
        "recomendacao": recomendacao,
        "timestamp": datetime.utcnow()
    }
