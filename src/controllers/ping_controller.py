from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.datasources.postgre_sql import get_datasource

ping_router = APIRouter(prefix="/ping")


# *INFO: This api is used to check if the server is running and the connection to the database is working.
@ping_router.get("/")
def ping(session: Session = Depends(get_datasource)):
    print(session)
    return {"ping": "pong!"}
