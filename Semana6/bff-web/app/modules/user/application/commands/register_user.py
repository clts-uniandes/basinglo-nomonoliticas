from fastapi import BackgroundTasks, Request, HTTPException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.user.infrastructure.repositories import UserRepository

class RegisterUser:
    def __init__(self, user_repository: "UserRepository"):
        self.user_repository = user_repository

    async def register_user(self, request: Request, background_tasks: BackgroundTasks):
        return {"msg": "Not Available"}
        #try:
        #    return await self.transaction_repository.create_transaction(request, background_tasks)
        #except HTTPException as e:
        #    print("Http exception: ", e.detail)
        #    raise e
        #except Exception as e:
        #    print("Internal server error: ", e)
        #    raise HTTPException(500, "Internal server error")

