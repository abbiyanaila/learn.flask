from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from service.common import connector
from service.models.item_model import ItemModel, ItemDAO

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank !"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="every item need store id."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemDAO.find_by_name(name)
        if item:
            return item[0].json()
        return {'massage': 'Item not found'}

    def post(self, name):
        res = ItemDAO.find_by_name(name)
        # if len(res)!=0:
        if res:
            return {'massage': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])
        ItemDAO.save(item)

        return item.json()

    def delete(self, name):
        item = ItemDAO.find_by_name(name)
        if item:
            ItemDAO.delete(name)

        return {'massage': 'Item Delete'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemDAO.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item[0].json()

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