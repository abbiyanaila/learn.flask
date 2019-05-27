from flask  import Flask
from flask_restful import Api
from service.common import security
from flask_jwt import JWT
# from service.resources.item import Item
from service.resources.item import Item, ItemList
from service.resources.user import UserRegister
from flask_sqlalchemy import SQLAlchemy
from service.resources.store import Store, StoreList
import os

app = Flask(__name__) #special python variable, unique name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'qwerty'
db = SQLAlchemy(app)
api = Api(app)

jwt = JWT(app, security.authenticate, security.identity)
# /aut   h , we send username and password, and JWT extension gets that username
# and password

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #pengganti route pada class Item
api.add_resource(ItemList, '/items') #pengganti route pada class ItemList
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register' )

