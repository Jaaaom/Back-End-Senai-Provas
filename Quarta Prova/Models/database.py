from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models.base import Base
import Models.herois
import Models.missao

engine = create_engine("sqlite:///Associacao_Herois.db", echo=False)

SessionLocal = sessionmaker(bind=engine)


def criar_tabelas():
    Base.metadata.create_all(engine)


def get_session():
    return SessionLocal()