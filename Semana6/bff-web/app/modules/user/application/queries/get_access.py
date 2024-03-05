from fastapi import HTTPException, Request
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.user.infrastructure.repositories import (
        UserRepository,
    )

class GetAccess:
    def __init__(self, user_repository: "UserRepository"):
        self.user_repository = user_repository

    async def get_access(self, request: Request):
        try:
            return await self.user_repository.login(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")
