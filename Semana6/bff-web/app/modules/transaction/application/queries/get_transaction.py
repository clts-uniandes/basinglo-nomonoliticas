from fastapi import Request, HTTPException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.transaction.infrastructure.repositories import TransactionRepository


class GetTransactions:
    def __init__(self, transaction_repository: "TransactionRepository"):
        self.transaction_repository = transaction_repository

    async def get_transactions(self, request: Request):
        return {"msg":"Operation not available"}
        #try:
        #    return await self.transaction_repository.get_transactions(request)
        #except HTTPException as e:
        #    print("Http exception: ", e.detail)
        #    raise e
        #except Exception as e:
        #    print("Internal server error: ", e)
        #    raise HTTPException(500, "Internal server error")
