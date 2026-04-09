from fastapi import APIRouter
from src.backend.services.database import SessionLocal
from src.backend.services.model import Interaction

router = APIRouter()

# =========================
# 📥 CRIAR INTERAÇÃO (POST)
# =========================
@router.post("/interactions/")
def criar_interacao(payload: dict):
    db = SessionLocal()

    nova_interacao = Interaction(
        sensor_type=payload.get("sensor_type"),
        valor=payload.get("valor")
    )

    db.add(nova_interacao)
    db.commit()
    db.close()

    return {"msg": "Interação salva com sucesso"}

# =========================
# 📤 LISTAR INTERAÇÕES (GET)
# =========================
@router.get("/interactions/")
def listar_interacoes():
    db = SessionLocal()
    dados = db.query(Interaction).all()
    db.close()

    return [
        {
            "sensor_type": d.sensor_type,
            "valor": d.valor,
            "data": str(d.data)
        }
        for d in dados
    ]