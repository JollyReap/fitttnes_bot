from sqlalchemy import (
    Column,
    VARCHAR,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    id = Column(String(100), nullable=False, unique=True)
    email = Column(VARCHAR(100), nullable=True, unique=True)
    nickname = Column(String(100), nullable=False, unique=True)


class HealthDiet(Base):
    __tablename__ = 'HealthDiet'
    product_name = Column(String(100), nullable=False, unique=False)
    calories = Column(VARCHAR(100), nullable=True, unique=False)
    proteins = Column(VARCHAR(100), nullable=True, unique=False)
    fats = Column(VARCHAR(100), nullable=True, unique=False)
    carboh = Column(VARCHAR(100), nullable=True, unique=False)

