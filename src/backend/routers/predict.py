from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import random

router = APIRouter()

# ==============================
# 📦 Modelo de entrada
# ==============================
class PredictRequest(BaseModel):
    sensor_type: str = "api"


# ==============================
# 🔌 Conexão com banco
# ==============================
def get_connection():
    # Render usa /tmp para escrita
    return sqlite3.connect("/tmp/totemflex.db")


# ==============================
# 🧠 Lógica de predição (AGORA REAL)
# ==============================
def gerar_interacao(sensor_type: str):
    # Simula comportamento real
    valor = round(random.uniform(0.1, 1.0), 2)

    # Classificação baseada no valor
    if valor < 0.4:
        classificacao = "toque_curto"
    else:
        classificacao = "toque_longo"

    data = datetime.now().isoformat()

    return {
        "sensor_type": sensor_type,
        "valor": valor,
        "classificacao": classificacao,
        "data": data
    }


# ==============================
# 🚀 Endpoint de previsão
# ==============================
@router.post("/predict/")
def predict(request: PredictRequest):
    conn = get_connection()
    cursor = conn.cursor()

    # Gera interação dinâmica
    interacao = gerar_interacao(request.sensor_type)

    # Garante que a tabela existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_type TEXT,
            valor REAL,
            classificacao TEXT,
            data TEXT
        )
    """)

    # Salva no banco
    cursor.execute("""
        INSERT INTO interactions (sensor_type, valor, classificacao, data)
        VALUES (?, ?, ?, ?)
    """, (
        interacao["sensor_type"],
        interacao["valor"],
        interacao["classificacao"],
        interacao["data"]
    ))

    conn.commit()
    conn.close()

    return {
        "status": "ok",
        "classificacao": interacao["classificacao"],
        "valor": interacao["valor"]
    }