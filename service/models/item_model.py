from database import Base, db_sess
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class ItemModel(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))

    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

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

    @staticmethod
    def delete(name):
        res = ItemDAO.find_by_name(name=name)
        if res:
            db_sess.delete(res[0])

    @staticmethod
    def update(name, price):
        res = ItemDAO.find_by_name(name=name, price=price)
        if res:
            item = res[0]
            item.name = name
            item.price = price
            db_sess.update(item)