from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TIMESTAMP

from .declarative_base_model import DeclarativeBaseModel


class BaseModel(DeclarativeBaseModel):
    __abstract__ = True

    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True
    )
