from fastapi import APIRouter

from app.modules.health.application.get_health import GetHealth

router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)

def initialize(get_health: GetHealth):
    @router.get("/")
    def call_health():
        return get_health.get_health()

    return call_health
