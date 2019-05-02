from database import Base, db_sess
from sqlalchemy import Column, Integer, String

class StoreModel(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': self.items}

class storeDAO(object):

    @staticmethod
    def save():
