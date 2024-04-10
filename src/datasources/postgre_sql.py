from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_URL
from src.models import DeclarativeBaseModel

engine = create_engine(DATABASE_URL)
PostgreSQLDatasource = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DeclarativeBaseModel.metadata.create_all(engine)


def get_datasource():
    datasource = PostgreSQLDatasource()
    try:
        yield datasource
    finally:
        datasource.close()
