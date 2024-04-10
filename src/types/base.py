from datetime import datetime
from typing import TypeVar, Optional

from humps import camelize
from pydantic import BaseModel as PydanticBaseModel

from src.models import BaseModel


def to_camel(string: str) -> str:
    return camelize(string)


class BasePydantic(PydanticBaseModel):
    pass


# *INFO: RQ = Request
class BaseRQ(BasePydantic):
    class Config:
        populate_by_name = True
        alias_generator = to_camel


# *INFO: RP = Response
class BaseRP(BasePydantic):
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
        populate_by_name = True
        alias_generator = to_camel


TBaseModel = TypeVar("TBaseModel", bound=BaseModel)
TBaseRQ = TypeVar("TBaseRQ", bound=BaseRQ)
TBaseRP = TypeVar("TBaseRP", bound=BaseRP)
