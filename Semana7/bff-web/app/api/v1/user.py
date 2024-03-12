from fastapi import APIRouter, BackgroundTasks, Request
from typing import TYPE_CHECKING
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
    async def signup(request: NewUser, background_tasks: BackgroundTasks):
        return await register_user.create_transaction(request, background_tasks)

    return {"signin": signin, "signup": signup}
