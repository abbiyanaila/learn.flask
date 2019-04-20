from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from service.common import connector
from service.models.item_model import ItemModel

class Item(Resource): #every resource has to be a class
    TABLE_NAME = 'items'

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
            return item
        return {'massage': 'Item not found'}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'massage': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        try:
            ItemModel.insert(item)
        except:
            return {'massage': "An error inserting the item"}

        return item #information for data was create or not


    @jwt_required()
    def delete(self, name):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        return {'massage': 'Item delete'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                ItemModel.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                ItemModel.update(updated_item)
            except:
                raise
                return {"message": "An error occurred updating the item."}
        return updated_item

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