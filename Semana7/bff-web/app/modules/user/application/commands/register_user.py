from fastapi import BackgroundTasks, Request, HTTPException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.user.infrastructure.repositories import UsersRepository

class RegisterUser:
    def __init__(self, user_repository: "UsersRepository"):
        self.user_repository = user_repository

    async def create_transaction(self, request: Request, background_tasks: BackgroundTasks):
        try:
            return await self.user_repository.register_user(request, background_tasks)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

