from fastapi import APIRouter
from src.backend.services.database import get_interactions

router = APIRouter(prefix="/interactions", tags=["Interações"])


@router.get("")
def list_interactions():
    return get_interactions()