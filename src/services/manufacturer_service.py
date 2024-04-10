from fastapi import Depends

from src.dtos import CreateManufacturerRQ, CreateManufacturerRP
from src.repositories import ManufacturerRepository


class ManufacturerService:
    def __init__(
        self,
        manufacturer_repository: ManufacturerRepository = Depends(
            ManufacturerRepository
        ),
    ):
        self.manufacturer_repository = manufacturer_repository

    def create(self, payload: CreateManufacturerRQ) -> CreateManufacturerRP:
        try:
            manufacturer = self.manufacturer_repository.create(payload)
            return manufacturer
        except Exception as exception:
            raise exception
