from fastapi import APIRouter, Request
from typing import TYPE_CHECKING
from .schemas.schemas import Transaction, GenericResponse, TransactionsResponse

if TYPE_CHECKING:
    from app.modules.transaction.application.queries.get_transaction import GetTransactions
    from app.modules.transaction.application.commands.create_transaction import CreateTransaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)


def initialize(get_transactions: "GetTransactions", create_transaction: "CreateTransaction"):
    @router.get("")
    async def get_all_transactions(request: Request) -> GenericResponse: # -> TransactionsResponse
        return await get_transactions.get_transactions(request)

    @router.post("", status_code=202)
    async def create_new_transaction(request: Transaction):
        return await create_transaction.create_transaction(request)
    