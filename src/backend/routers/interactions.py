from fastapi import APIRouter
from src.backend.services.database import SessionLocal
from src.backend.services.model import Interaction

router = APIRouter()

@router.post("/interactions/")
def criar_interacao(payload: dict):
    db = SessionLocal()

    try:
        nova_interacao = Interaction(
            sensor_type=payload.get("sensor_type"),
            valor=payload.get("valor")
        )

        db.add(nova_interacao)
        db.commit()
        db.refresh(nova_interacao)  # 🔥 ESSENCIAL

        return {"msg": "Interação salva com sucesso"}

    except Exception as e:
        db.rollback()
        return {"erro": str(e)}

    finally:
        db.close()