from fastapi import Depends
from sqlalchemy.orm import Session

from src.datasources.postgre_sql import get_datasource
from src.models import SmartphoneModel
from .base_repository import BaseRepository


class SmartphoneRepository(BaseRepository):
    def __init__(self, datasource: Session = Depends(get_datasource)):
        super().__init__(model=SmartphoneModel, datasource=datasource)
