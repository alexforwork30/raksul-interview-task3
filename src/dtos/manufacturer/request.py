from src.types.base import BaseRQ


class CreateManufacturerRQ(BaseRQ):
    manufacturer_name: str
