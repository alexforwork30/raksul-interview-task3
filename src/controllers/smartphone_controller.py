from fastapi import APIRouter, Depends

from src.dtos import CreateSmartphoneRQ, CreateSmartphoneRP
from src.services import SmartphoneService

smartphone_router = APIRouter(prefix="/smartphones")


@smartphone_router.post(
    "/", response_model=CreateSmartphoneRP, response_model_by_alias=True
)
def create(
    payload: CreateSmartphoneRQ,
    smartphone_service: SmartphoneService = Depends(SmartphoneService),
):
    return smartphone_service.create(payload)
