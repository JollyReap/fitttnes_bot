from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    id = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    nickname = Column(String(100), nullable=False, unique=True)


class HealthDiet(Base):
    __tablename__ = 'HealthDiet'
    product_name = Column(String(100), nullable=False, unique=False)
    calories = Column(String(100), nullable=True, unique=False)
    proteins = Column(String(100), nullable=True, unique=False)
    fats = Column(String(100), nullable=True, unique=False)
    carboh = Column(String(100), nullable=True, unique=False)

