from fastapi import APIRouter
from src.backend.services.database import get_interactions

router = APIRouter(prefix="/interactions", tags=["Interactions"])

@router.get("/")
def listar_interacoes():
    return get_interactions()