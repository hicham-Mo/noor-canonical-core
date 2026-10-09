from fastapi import FastAPI
from app.api.routes import compliance, health

app = FastAPI(
    title="Noor Canonical Core",
    description="Integrated knowledge, production, and legal investment system",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(compliance.router, prefix="/compliance", tags=["compliance"])


@app.get("/")
def root() -> dict:
    return {
        "app": "Noor Canonical Core",
        "status": "ok",
        "message": "نور الاستخلاف is running",
    }
