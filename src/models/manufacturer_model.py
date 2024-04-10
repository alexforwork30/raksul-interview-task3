from sqlalchemy import Column, Integer, Identity, String

from .base_model import BaseModel


class ManufacturerModel(BaseModel):
    __tablename__ = "manufacturers"

    manufacturer_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)

    manufacturer_name = Column(String(100), nullable=False)
