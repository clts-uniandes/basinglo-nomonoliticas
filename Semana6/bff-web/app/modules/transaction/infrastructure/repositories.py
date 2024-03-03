import httpx
import uuid
from fastapi import HTTPException, Request

from .producers import Producer
from . import utils

#from config import settings


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
    
    async def create_transaction(self, request: Request):
        payload = dict(
            buyer_id = request.buyer_id,
            seller_id = request.seller_id,
            amount = request.amount,
            realization_date = request.realization_date,
            notes = request.notes,
            fecha_creacion = utils.time_millis()
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
        #producer.publish_message(command, "command-create-transaction, "public/default/new-transaction-command")
        producer.publish_message(command, "transaction-event", "public/default/new-transaction-command")
        
