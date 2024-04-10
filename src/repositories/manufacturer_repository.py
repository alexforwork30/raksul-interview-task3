from fastapi import Depends
from sqlalchemy.orm import Session

from src.datasources.postgre_sql import get_datasource
from src.models import ManufacturerModel
from .base_repository import BaseRepository


class ManufacturerRepository(BaseRepository):
    def __init__(self, datasource: Session = Depends(get_datasource)):
        super().__init__(model=ManufacturerModel, datasource=datasource)
