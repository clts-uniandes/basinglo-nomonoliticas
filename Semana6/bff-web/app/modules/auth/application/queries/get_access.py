from fastapi import HTTPException, Request
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.auth.infrastructure.rest_repository import (
        AuthenticationRepository,
    )

class GetAccess:
    def __init__(self, authentication_repository: "AuthenticationRepository"):
        self.authentication_repository = authentication_repository

    async def get_access(self, request: Request):
        try:
            return await self.authentication_repository.login(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")
