from sqlalchemy import Column, Integer, Identity, String, Float, ForeignKey

from .base_model import BaseModel


class SmartphoneModel(BaseModel):
    __tablename__ = "smartphones"

    smartphone_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)

    manufacturer_id = Column(
        Integer, ForeignKey("manufacturers.manufacturer_id"), nullable=False
    )

    smartphone_model = Column(String(100), nullable=False)
    data_memory = Column(String(100), nullable=False)
    year_of_manufacture = Column(Integer, nullable=False)
    os_version = Column(String(100), nullable=False)
    body_color = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
