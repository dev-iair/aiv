from sqlmodel import Session, create_engine
from core.config import settings
from database.model import *

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session