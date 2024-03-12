from fastapi import APIRouter, BackgroundTasks
from typing import TYPE_CHECKING
from .schemas.schemas import NewSellTransaction, RecordResponse


if TYPE_CHECKING:
    from app.modules.record.application.commands.record_sell_transaction import RecordSellTransaction


router = APIRouter(
    prefix="/record",
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)


def initialize(record_sell_transaction: "RecordSellTransaction"):
    @router.post("/transaction")
    async def record_new_sell_transaction(request: NewSellTransaction, background_tasks: BackgroundTasks):
        return await record_sell_transaction.record_sell_transaction(request, background_tasks)

    return {"record_new_sell_transaction": record_new_sell_transaction}
