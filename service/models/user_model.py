from service.common import connector
from database import Base, db_sess
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapper

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<UserRegister %r>' % (self.username)

class UserDAO(object):

    @staticmethod
    def save(item):
        db_sess.add(item)
        db_sess.commit()

    @staticmethod
    def find_by_username(cls, username):
        query = db_sess.query(UserModel).filter_by(name=username)
        res = list(query)
        if len(res)==0:
            return pass
        else:
            return res
        # connection = connector.get_connection()
        # cursor = connector.get_cursor()
        #
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        connection = connector.get_connection()
        cursor = connector.get_cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
