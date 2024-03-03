from typing import TYPE_CHECKING
from fastapi import APIRouter, Request
from .schemas.schemas import LoginResponse


if TYPE_CHECKING:
    from app.modules.auth.application.queries.get_access import GetAccess


router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)


def initialize(get_access: "GetAccess"):
    @router.post("/signin")
    async def signin(request: Request) -> LoginResponse:
        return await get_access.get_access(request)
        # return LoginResponse(token="token")

    return {"signin": signin}
