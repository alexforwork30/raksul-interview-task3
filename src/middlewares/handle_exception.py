from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.config import ENV
from src.enums import EEnvironment


class HandleExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={
                    "error": "Http error",
                    "message": str(http_exception.detail),
                },
            )
        except Exception as exception:
            if ENV != EEnvironment.PRODUCTION.value:
                return JSONResponse(
                    status_code=500,
                    content={
                        "error": exception.__class__.__name__,
                        "messages": exception.args,
                    },
                )
            return JSONResponse(status_code=500, content={})
