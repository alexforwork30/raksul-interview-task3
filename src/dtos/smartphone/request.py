from src.types.base import BaseRQ


class CreateSmartphoneRQ(BaseRQ):
    manufacturer_id: int
    smartphone_model: str
    data_memory: str
    year_of_manufacture: int
    os_version: str
    body_color: str
    price: float
    stock_quantity: int
