from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from service.common import connector

class Item(Resource): #every resource has to be a class
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank !"
                        )

    @jwt_required()
    def get(self, name):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'massage': 'Item not found'}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'massage': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        # data = request.get_json() #request data with json file
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #information for data was create or not

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'massage': 'Item delete'}
    #
    def put(self, name):
        # data = request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}