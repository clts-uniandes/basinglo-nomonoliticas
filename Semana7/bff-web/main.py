import asyncio
import json
import os
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from typing import Any

from initializer import Initializer
from app.config.config import BaseConfig
from app.modules.transaction.infrastructure.consumers import topic_subscribe

PULSAR_TENANT = "PULSAR_TENANT"
PULSAR_NAMESPACE = "PULSAR_NAMESPACE"

USERS_EVENT_TOPIC = "USERS_EVENT_TOPIC"
RECORD_EVENT_TOPIC = "RECORD_EVENT_TOPIC"

# success events
NOTIFICATION_EVENT_TOPIC = "NOTIFICATION_EVENT_TOPIC"
TRANSACTION_EVENT_TOPIC = "TRANSACTION_EVENT_TOPIC"
PROPERTIES_EVENT_TOPIC = "PROPERTIES_EVENT_TOPIC"

# failure
NOTIFICATION_FAIL_EVENT_TOPIC = "NOTIFICATION_FAIL_EVENT_TOPIC"
TRANSACTIONS_FAIL_EVENT_TOPIC = "TRANSACTIONS_FAIL_EVENT_TOPIC"
PROPERTIES_FAIL_EVENT_TOPIC = "PROPERTIES_FAIL_EVENT_TOPIC"


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


    users_event_topic=os.getenv(USERS_EVENT_TOPIC, default="unset")
    record_event_topic=os.getenv(RECORD_EVENT_TOPIC, default="unset")

    # remove comments for debugging
    #notification_event_topic=os.getenv(NOTIFICATION_EVENT_TOPIC, default="unset")
    #transaction_event_topic=os.getenv(TRANSACTION_EVENT_TOPIC, default="unset")
    #properties_event_topic=os.getenv(PROPERTIES_EVENT_TOPIC, default="unset")

    #notification_fail_event_topic=os.getenv(NOTIFICATION_FAIL_EVENT_TOPIC, default="unset")
    #transaction_fail_event_topic=os.getenv(TRANSACTIONS_FAIL_EVENT_TOPIC, default="unset")
    #properties_fail_event_topic=os.getenv(PROPERTIES_FAIL_EVENT_TOPIC = "PROPERTIES_FAIL_EVENT_TOPIC", default="unset")
    
    subscription_name = os.getenv(BFF_SUB_NAME, default="")
    print("adding futures")
    # taskNotification = ... outdated
    taskUsers = asyncio.ensure_future(
        topic_subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + users_event_topic,
            subscription_name,
            events=events,
        )
    )
    taskRecord = asyncio.ensure_future(
        topic_subscribe(
            pulsar_tenant + "/" + pulsar_namespace + "/" + record_event_topic,
            subscription_name,
            events=events,
        )
    )
    #othertasks as wished
    tasks.append(taskRecord)
    tasks.append(taskUsers)


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

@app.get("/event-stream-users")
async def stream_users_events(request: Request):
    def new_event():
        global events
        new_event = events.pop()
        if "PersonalInfoCreated" in new_event:
            return {"data": new_event, "event": "PersonalInfoCreated"}
        else:
            events.append(new_event)

    async def get_events():
        global events
        while True:
            if await request.is_disconnected():
                break
            if len(events) > 0:
                yield new_event()
            await asyncio.sleep(0.1)

    return EventSourceResponse(get_events())

@app.get("/event-stream-saga")
async def stream_saga_events(request: Request):
    def new_event():
        global events
        new_event = events.pop()
        if "Saga" in new_event:
            return {"data": new_event, "event": "Saga"}
        else:
            events.append(new_event)

    async def get_events():
        global events
        while True:
            if await request.is_disconnected():
                break
            if len(events) > 0:
                yield new_event()
            await asyncio.sleep(0.1)

    return EventSourceResponse(get_events())
