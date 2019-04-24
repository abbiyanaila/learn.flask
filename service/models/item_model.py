from database import Base, db_sess
from sqlalchemy import Column, Integer, String, Float

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    def __repr__(self):
        return '<Item %r>' % (self.name)


class ItemDAO(object):

    @staticmethod
    def save(item):
        db_sess.add(item)
        db_sess.commit()

    @staticmethod
    def find_by_name(name):
        query = db_sess.query(ItemModel).filter_by(name=name)
        res = list(query)
        if len(res)==0:
            return False
        else:
            return res