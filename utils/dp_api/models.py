from sqlalchemy import (
    Column,
    VARCHAR,
    String,
    Integer,
    Float
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    tg_id = Column(String(100), nullable=False, unique=True)
    email = Column(VARCHAR(100), nullable=True, unique=True)
    nickname = Column(String(100), nullable=False, unique=True)


class Products(Base):
    __tablename__ = 'Products'
    product_id = Column(Integer, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    call = Column(Float, nullable=True)
    proteins = Column(Float, nullable=True)
    fats = Column(Float, nullable=True)
    carboh = Column(Float, nullable=True)

