import os
import uuid
from fastapi import Request, BackgroundTasks

from app.seedwork.infrastructure import utils
from .producers import Producer

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

RECORD_SAGA_COMMAND_TOPIC = "RECORD_SAGA_COMMAND_TOPIC"

class RecordRepository:
    async def call_record_saga(
        self, request: Request, background_tasks: BackgroundTasks
    ):
        payload = dict(
            dni_landlord=str(request.dni_landlord),
            dni_tenant=str(request.dni_tenant),
            id_property=str(request.id_property),
            monetary_value=str(request.monetary_value),
            contract_initial_date=str(request.contract_initial_date),
            contract_final_date=str(request.contract_final_date),
        )
        print("Payload received: " + str(request))
        command = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "CommandStartTransaction",
            #ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "PDA BFF Web edition",
            data=payload
        )
        print("To-be sent command: " + str(command))
        pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
        pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")
        records_saga_command_topic = os.getenv(RECORD_SAGA_COMMAND_TOPIC, default="unset")
        producer = Producer()
        # producer.produce_message(command, "transaction-event", "public/default/transaction-event")
        background_tasks.add_task(
            producer.produce_message,
            pulsar_tenant + "/" + pulsar_namespace + "/" + records_saga_command_topic,
            command,
        )
        return {"msg": "Registering data record..."}