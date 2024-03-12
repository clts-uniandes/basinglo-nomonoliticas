from fastapi import BackgroundTasks, Request, HTTPException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.record.infrastructure.repositories import RecordRepository

class RecordSellTransaction:
    def __init__(self, record_repository: "RecordRepository"):
        self.record_repository = record_repository

    async def record_sell_transaction(self, request: Request, background_tasks: BackgroundTasks):
        try:
            return await self.record_repository.call_record_saga(request, background_tasks)
        except HTTPException as e:
            print("Pulsar exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

