from fastapi import APIRouter

from app.api.routes.health import health as health_route

router = APIRouter()
router.include_router(health_route, tags=["system"])
