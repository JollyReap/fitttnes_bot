
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models
from .models import Users
from sqlalchemy import select, delete


class Database:
    def __init__(self, db_url):
        engine = create_engine(db_url, pool_pre_ping=True)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)
        self.connection = engine.connect()

    def get_or_create(self, session, model, filter_field, data):
        instance = session.query(model).filter_by(**{filter_field: data[filter_field]}).first()
        if not instance:
            instance = model(**data)
        return instance

    def add_registration_info(self, data, model, filter_field):
        session = self.maker()
        info = self.get_or_create(session, model, filter_field, data)
        session.add(info)
        try:
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
        finally:
            session.close()

    def select_user(self, user_id):
        session = self.maker()
        usr = session.execute(select(Users.tg_id).where(Users.tg_id == user_id)
                              ).first()
        return usr

    def delete_usr(self, user_id):
        session = self.maker()
        obj = session.query(Users).filter_by(tg_id=user_id).one()
        session.delete(obj)
        try:
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
        finally:
            session.close()




