from fastapi import Depends

from src.dtos import CreateSmartphoneRQ, CreateSmartphoneRP
from src.repositories import SmartphoneRepository


class SmartphoneService:
    def __init__(
        self,
        smartphone_repository: SmartphoneRepository = Depends(SmartphoneRepository),
    ):
        self.smartphone_repository = smartphone_repository

    def create(self, payload: CreateSmartphoneRQ) -> CreateSmartphoneRP:
        try:
            smartphone = self.smartphone_repository.create(payload)
            return smartphone
        except Exception as exception:
            raise exception
