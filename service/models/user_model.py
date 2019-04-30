from database import Base, db_sess
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))

    def __repr__(self):
        return '<User %r>' % (self.username)

class UserDAO(object):

    @staticmethod
    def save(user: UserModel):
        db_sess.add(user)
        db_sess.commit()

    @staticmethod
    def find_by_username(username):
        query = db_sess.query(UserModel).filter_by(username=username)
        res = list(query)
        if len(res)==0:
            return False
        else:
            return res

    @staticmethod
    def find_by_id(id):
        query = db_sess.query(UserModel).filter_by(id=id)
        res = list(query)
        if len(res)==0:
            return False
        else:
            return res

