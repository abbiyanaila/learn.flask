from database import Base, db_sess
from sqlalchemy import Column, Integer, String

class StoreModel(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    items = db_sess.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        # return {'name': self.name, 'items': self.items}
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

class storeDAO(object):

    @staticmethod
    def save(store: StoreModel):
        db_sess.add(store)
        db_sess.commit()

    @staticmethod
    def find_by_name(name):
        query = db_sess.query(StoreModel).filter_by(name=name)
        res = list(query)
        if len(res)==0:
            return False
        else:
            return res

    @staticmethod
    def delete(name):
        res = storeDAO.find_by_name(name=name)
        if res:
            db_sess.delete(res[0])


