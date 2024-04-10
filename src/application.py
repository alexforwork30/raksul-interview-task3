from fastapi import FastAPI

from src.controllers import ping_router, smartphone_router, manufacturer_router
from src.middlewares import HandleExceptionMiddleware


def create_app() -> FastAPI:
    application = FastAPI()

    application.include_router(ping_router)
    application.include_router(smartphone_router)
    application.include_router(manufacturer_router)

    application.add_middleware(HandleExceptionMiddleware)

    return application
