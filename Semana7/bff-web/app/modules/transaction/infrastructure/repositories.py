import httpx
import os
import uuid
from datetime import datetime
from fastapi import HTTPException, Request, BackgroundTasks

from app.seedwork.infrastructure import utils
from app.config.settings import settings
from .producers import Producer

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

TRANSACTION_COMMAND_TOPIC = "TRANSACTION_COMMAND_TOPIC"


class TransactionRepository:
    async def get_transactions(self, request: Request):
        async with httpx.AsyncClient() as client:
            uri = utils.build_request_uri(settings.transactions_ms, "transactions")
            # uri = utils.build_request_uri("localhost:8000", "transactions")
            print(f"Sending {request.query_params} to {uri}")
            response = await client.get(uri, params=request.query_params, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()

    async def create_transaction(
        self, request: Request, background_tasks: BackgroundTasks
    ):
        payload = dict(
            dni_landlord=str(request.seller_id),
            dni_tenant=str(request.buyer_id),
            id_property=str(request.property_id),
            monetary_value=str(request.amount),
            type_lease="SELL",
            contract_initial_date="",
            contract_final_date=datetime.now().isoformat(),
        )
        print("Payload received: " + str(request))
        command = dict(
            # id = str(uuid.uuid4()),
            # time=utils.time_millis(),
            # specversion = "v1",
            # type = "NewTransactionCommand",
            # ingestion=utils.time_millis(),
            # datacontenttype="AVRO",
            # service_name = "PDA BFF Web edition",
            data=payload
        )
        print("To-be sent command: " + str(command))
        pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
        pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")
        transaction_command_topic = os.getenv(TRANSACTION_COMMAND_TOPIC, default="")
        producer = Producer()
        # producer.produce_message(command, "transaction-event", "public/default/transaction-event")
        background_tasks.add_task(
            producer.produce_message,
            pulsar_tenant + "/" + pulsar_namespace + "/" + transaction_command_topic,
            command,
        )
        return {"msg": "Registering transaction..."}
