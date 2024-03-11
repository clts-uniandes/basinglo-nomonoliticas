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

USERS_COMMAND_TOPIC = "USERS_COMMAND_TOPIC"
class UsersRepository:
    async def login(self, request: Request):
        async with httpx.AsyncClient() as client:
            body = {
                "username" : str(request.username),
                "password" :str(request.password)
            }
            uri = utils.build_request_uri(settings.users_ms, "auth/signin")
            #uri = build_request_uri("localhost:8000", "/auth/signin")
            print(f"Sending {body} to {uri}")
            response = await client.post(uri, json=body, timeout=60)

            if response.status_code == 500:
                return response.json()
            elif 400 <= response.status_code < 600: 
                print(response.json())
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
    
    async def register_user(
        self, request: Request, background_tasks: BackgroundTasks
    ):
        payload = dict(
            username=str(request.username),
            password=str(request.password),
            email=str(request.email),
            dni=str(request.dni),
            fullName=str(request.fullName),
            phoneNumber=str(request.phoneNumber),
        )
        print("Payload received: " + str(request))
        command = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "RegisterCredential",
            #ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "PDA BFF Web edition",
            data=payload
        )
        print("To-be sent command: " + str(command))
        pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
        pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")
        users_command_topic = os.getenv(USERS_COMMAND_TOPIC, default="unset")
        producer = Producer()
        # producer.produce_message(command, "transaction-event", "public/default/transaction-event")
        background_tasks.add_task(
            producer.produce_message,
            pulsar_tenant + "/" + pulsar_namespace + "/" + users_command_topic,
            command,
        )
        return {"msg": "Registering user..."}