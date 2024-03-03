from fastapi import Request, HTTPException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.transaction.infrastructure.repositories import TransactionRepository

class CreateTransaction:
    def __init__(self, transaction_repository: "TransactionRepository"):
        self.transaction_repository = transaction_repository

    async def create_transaction(self, request: Request):
        try:
            await self.transaction_repository.create_transaction(request)
            return {"msg" : "Registering transaction..."}
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

