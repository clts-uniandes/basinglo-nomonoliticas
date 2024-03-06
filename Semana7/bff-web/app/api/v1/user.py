from typing import TYPE_CHECKING
from fastapi import APIRouter
from .schemas.schemas import LoginResponse, Login, NewUser


if TYPE_CHECKING:
    from app.modules.user.application.queries.get_access import GetAccess
    from app.modules.user.application.commands.register_user import RegisterUser


router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)


def initialize(get_access: "GetAccess", register_user: "RegisterUser"):
    @router.post("/signin")
    async def signin(request: Login) -> LoginResponse:
        return await get_access.get_access(request)

    @router.post("/signup")
    async def signup(request: NewUser):
        return await register_user.register_user(request)

    return {"signin": signin, "signup": signup}
