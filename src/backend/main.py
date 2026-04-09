from fastapi import FastAPI
from src.backend.routers.predict import router as predict_router
from src.backend.routers.interactions import router as interactions_router
from src.backend.routers.metrics import router as metrics_router
from src.backend.services.database import init_db

app = FastAPI(
    title="TotemMFlex API",
    version="3.0"
)

# =========================
# 🚀 STARTUP
# =========================
@app.on_event("startup")
def startup():
    print("🚀 Inicializando aplicação...")
    print("🔥 Inicializando banco...")
    init_db()
    print("✅ Banco pronto")

# =========================
# 🌐 ROTAS BÁSICAS
# =========================
@app.get("/")
def root():
    return {"message": "TotemMFlex API is running 🚀"}

@app.get("/status")
def status():
    return {
        "status": "ok",
        "service": "TotemMFlex API",
        "version": "3.0"
    }

# =========================
# 📡 ROUTERS
# =========================
app.include_router(predict_router, tags=["Predict"])
app.include_router(interactions_router, tags=["Interactions"])
app.include_router(metrics_router, tags=["Metrics"])




