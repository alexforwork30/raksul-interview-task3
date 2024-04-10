from typing import Type, Optional, List

from sqlalchemy.orm import Session

from src.types.base import TBaseModel, TBaseRQ, TBaseRP


class BaseRepository:
    def __init__(self, model: Type[TBaseModel], datasource: Session):
        self.model = model
        self.datasource = datasource

    def create(self, payload: TBaseRQ) -> TBaseRP:
        new_row = self.model(**payload.dict())
        self.datasource.add(new_row)
        self.datasource.commit()
        self.datasource.refresh(new_row)
        return new_row

    def find_all(self) -> List[TBaseRP]:
        return self.datasource.query(self.model).all()

    def find_by_id(self, model_id: int) -> Optional[TBaseRP]:
        return self.datasource.query(self.model).get(model_id)

    def find_by(self, **kwargs) -> List[TBaseRP]:
        return self.datasource.query(self.model).filter_by(**kwargs).all()

    def update_by_id(self, model_id: int, payload: TBaseRQ) -> Optional[TBaseRP]:
        row_to_update = self.find_by_id(model_id)
        if row_to_update:
            for key, value in payload.dict().items():
                if getattr(row_to_update, key) != value:
                    setattr(row_to_update, key, value)
            self.datasource.add(row_to_update)
            self.datasource.commit()
            self.datasource.refresh(row_to_update)
        return row_to_update

    def delete_by_id(self, model_id: int) -> None:
        row_to_delete = self.find_by_id(model_id)
        if row_to_delete:
            self.datasource.delete(row_to_delete)
            self.datasource.commit()
