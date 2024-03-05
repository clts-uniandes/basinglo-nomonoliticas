import httpx
from fastapi import HTTPException, Request

from .utils import build_request_uri
#from config import settings


class UserRepository:
    async def login(self, request: Request):
        async with httpx.AsyncClient() as client:
            body = await request.json()
            #uri = build_request_uri(settings.auth_ms, ""/auth/signin")
            uri = build_request_uri("localhost:8000", "/auth/signin")
            print(f"Sending {body} to {uri}")
            response = await client.post(uri, json=body, timeout=60)

            if 400 <= response.status_code < 600: 
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()