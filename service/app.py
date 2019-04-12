from flask  import Flask
from flask_restful import Api
from service.common import security
from flask_jwt import JWT
from service.resources import item, user


app = Flask(__name__) #special python variable, unique name
app.secret_key = 'qwerty'
api = Api(app)

jwt = JWT(app, security.authenticate, security.identity)
# /aut   h , we send username and password, and JWT extension gets that username
# and password

api.add_resource(item.Item, '/item/<string:name>') #pengganti route pada class Item
api.add_resource(item.ItemList, '/items') #pengganti route pada class ItemList

