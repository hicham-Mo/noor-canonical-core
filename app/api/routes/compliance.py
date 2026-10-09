from fastapi import APIRouter

from app.core.compliance import cloud_configuration_summary, islamic_compliance, moroccan_law_42_25

router = APIRouter()


@router.get("/law-42-25")
def law_42_25() -> dict:
    return moroccan_law_42_25()


@router.get("/islamic")
def islamic() -> dict:
    return islamic_compliance()


@router.get("/cloud")
def cloud() -> dict:
    return cloud_configuration_summary()
