from fastapi import FastAPI
from src.backend.routers.predict import router as predict_router

app = FastAPI(
    title="TotemMFlex API",
    version="2.0",
    description="API do MVP Sprint 2 - TotemMFlex"
)

app.include_router(predict_router)

@app.get("/status")
def status():
    return {"status": "online", "message": "API TotemMFlex funcionando!"}




