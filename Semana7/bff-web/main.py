import asyncio
import os
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from typing import Any

from initializer import Initializer
from app.config.config import BaseConfig
from app.modules.transaction.infrastructure.consumers import topic_subscribe

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

USER_EVENT_TOPIC = "USER_EVENT_TOPIC"
TRANSACTION_EVENT_TOPIC = "TRANSACTION_EVENT_TOPIC"
BFF_SUB_NAME = "BFF_SUB_NAME"

settings = BaseConfig()
app_configs: dict[str, Any] = {"title": "PDA BFF for Web"}

app = FastAPI(**app_configs)
tasks = list()
events = list()

Initializer(app).setup()


@app.on_event("startup")
async def startup():
    global tasks
    global events

    pulsar_tenant = os.getenv(PULSAR_TENANT, default="public")
    pulsar_namespace = os.getenv(PULSAR_NAMESPACE, default="default")
    # user_event_topic=os.getenv(USER_EVENT_TOPIC, default="")
    transaction_event_topic = os.getenv(TRANSACTION_EVENT_TOPIC, default="")
    subscription_name = os.getenv(BFF_SUB_NAME, default="")
    print("adding futures")
    # taskUser = asyncio.ensure_future(topic_subscribe(pulsar_tenant+"/"+pulsar_namespace+"/"+transaction_event_topic,subscription_name, events=events))
    taskTransaction = asyncio.ensure_future(
        topic_subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + transaction_event_topic,
            subscription_name,
            events=events,
        )
    )
    # tasks.append(taskUser)
    tasks.append(taskTransaction)


@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/event-stream")
async def stream_events(request: Request):
    def new_event():
        global events
        return {"data": events.pop(), "event": "NewEvent"}

    async def get_events():
        global events
        while True:
            if await request.is_disconnected():
                break
            if len(events) > 0:
                yield new_event()
            await asyncio.sleep(0.1)

    return EventSourceResponse(get_events())