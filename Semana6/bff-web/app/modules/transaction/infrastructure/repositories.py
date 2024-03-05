import httpx
import uuid
from fastapi import HTTPException, Request, BackgroundTasks

from .producers import Producer
from . import utils

class TransactionRepository:
    async def get_transactions(self, request: Request):
        async with httpx.AsyncClient() as client:
            #uri = build_request_uri(settings.transactions_ms, "transactions")
            uri = utils.build_request_uri("localhost:8000", "transactions")
            print(f"Sending {request.query_params} to {uri}")
            response = await client.get(uri, params=request.query_params, timeout=60)
 
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
    
    async def create_transaction(self, request: Request, background_tasks: BackgroundTasks):
        payload = dict(
            buyer_id = str(request.buyer_id),
            seller_id = str(request.seller_id),
            amount = int(request.amount),
            realization_date = str(request.realization_date),
            notes = str(request.notes)
        )
        print("Payload received: "+str(payload))
        command = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "NewTransactionCommand",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "PDA BFF Web edition",
            data = payload
        )
        print("To-be sent command: "+str(command))
        producer = Producer()
        #producer.produce_message(command, "transaction-event", "public/default/transaction-event")
        background_tasks.add_task(producer.produce_message, command, "transaction-event", "public/default/transaction-event")
        return {"msg" : "Registering transaction..."}
        
