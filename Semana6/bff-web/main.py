import asyncio
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from typing import Any

from initializer import Initializer
from app.config.config import BaseConfig
from app.modules.transaction.infrastructure.consumers import topic_subscribe

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
    #taskTransactions = asyncio.ensure_future(topic_subscribe("transaction-event","web-bff","public/default/transaction-event", events=events))
    taskTransactions = asyncio.ensure_future(topic_subscribe("transaction-event","web-bff-sub","public/default/transaction-event", events=events))
    tasks.append(taskTransactions)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get('/event-stream')
async def stream_events(request: Request):
    def new_event():
        global events
        return {'data': events.pop(), 'event': 'NewEvent'}
    async def get_events():
        global events
        while True:
            if await request.is_disconnected():
                break
            if len(events) > 0:
                yield new_event()
            await asyncio.sleep(0.1)
    return EventSourceResponse(get_events())