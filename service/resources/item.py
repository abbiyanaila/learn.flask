from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from service.common import connector

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
        item = self.find_by_name()
        if item:
            return item
        return {'massage': 'Item not found'}, 404


    def find_by_name(self):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}


    def post(self, name):
        if self.find_by_name()
            return {'massage': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        try:
            item.insert(item)
        except:
            return {'massage': "An error inserting the item"}

        return item, 201 #information for data was create or not


    @classmethod
    def insert(cls, item):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, item['name'], item['price'])


    def delete(self, name):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        return {'massage': 'Item delete'}


    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name()
        update_item = {'name':name, 'price': data['price']}
        if item is None:
            try:
                Item.insert(update_item)
            except:
                return {'massage': 'An error insert item'}
        else:
            try:
                Item.update(update_item)
            except:
                raise
                return {'massage': 'An error update item'}
        return update_item

    @classmethod
    def update(cls, item):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['price'], item['name']))

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