from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from service.common import connector
from service.models.item_model import ItemModel

class Item(Resource): #every resource has to be a class
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank !"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'massage': 'Item not found'}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'massage': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {'massage': "An error inserting the item"}

        return item.json() #information for data was create or not


    @jwt_required()
    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'massage': 'Item Delete'}
        # connection = connector.get_connection()
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        # cursor.execute(query, (name,))
        #
        # return {'massage': 'Item delete'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        # updated_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, data['price'])
            # try:
            #     updated_item.insert()
            # except:
            #     return {"message": "An error occurred inserting the item."}
        else:
            item.price = data['price']

        item.save_to_db()
            # try:
            #     updated_item.update()
            # except:
            #     raise
            #     return {"message": "An error occurred updating the item."}
        return item.json()

class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        return {'items': items}