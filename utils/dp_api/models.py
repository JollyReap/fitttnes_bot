from sqlalchemy import (
    Column,
    VARCHAR,
    String,
    Integer
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    tg_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    email = Column(VARCHAR(100), nullable=True, unique=True)
    nickname = Column(String(100), nullable=False, unique=True)


