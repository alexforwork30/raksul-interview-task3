from fastapi import APIRouter, Depends

from src.dtos import CreateManufacturerRQ, CreateManufacturerRP
from src.services import ManufacturerService

manufacturer_router = APIRouter(prefix="/manufacturers")


@manufacturer_router.post(
    "/", response_model=CreateManufacturerRP, response_model_by_alias=True
)
def create(
    payload: CreateManufacturerRQ,
    manufacturer_service: ManufacturerService = Depends(ManufacturerService),
):
    return manufacturer_service.create(payload)
