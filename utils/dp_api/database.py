

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models
from .models import Users, HealthDiet
from sqlalchemy import update


class Database:
    def __init__(self, db_url='sqlite:///database.sqlite'):
        engine = create_engine(db_url, pool_pre_ping=True)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)
        self.connection = engine.connect()