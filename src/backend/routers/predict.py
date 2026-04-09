from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
def predict(payload: dict):
    pergunta = payload.get("pergunta")

    if not pergunta:
        return {"status": "erro", "mensagem": "Pergunta obrigatória"}

    return {
        "status": "ok",
        "resposta": f"Resposta simulada para: {pergunta}"
    }