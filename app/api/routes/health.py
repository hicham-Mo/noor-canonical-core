from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "Noor Canonical Core",
        "version": "0.1.0",
    }


@router.get("/ready")
def ready() -> dict:
    return {
        "status": "ready",
        "checks": {
            "app": "ok",
            "environment": "configured",
        },
    }
