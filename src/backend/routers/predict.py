from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3
from datetime import datetime

router = APIRouter()

# =========================
# MODELO DE ENTRADA
# =========================
class InputData(BaseModel):
    valor: float


# =========================
# FUNÇÃO PARA SALVAR NO BANCO
# =========================
def salvar_interacao(valor, classificacao):
    conn = sqlite3.connect("src/database/totem.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interactions (sensor_type, valor, classificacao, data)
        VALUES (?, ?, ?, ?)
    """, ("sensor_simulado", valor, classificacao, datetime.now()))

    conn.commit()
    conn.close()


# =========================
# ENDPOINT PRINCIPAL
# =========================
@router.post("/predict")
def predict(data: InputData):
    valor = data.valor

    # =========================
    # CLASSIFICAÇÃO
    # =========================
    if valor < 30:
        classificacao = "toque_curto"
    elif valor < 70:
        classificacao = "toque_medio"
    else:
        classificacao = "toque_longo"

    # =========================
    # SALVAR NO BANCO 🔥
    # =========================
    salvar_interacao(valor, classificacao)

    # =========================
    # RETORNO
    # =========================
    return {
        "valor_sensor": valor,
        "classificacao": classificacao
    }