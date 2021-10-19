from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    id = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    nickname = Column(String(100), nullable=False, unique=True)

