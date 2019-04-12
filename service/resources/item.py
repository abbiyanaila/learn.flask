from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items = []

class Item(Resource): #every resource has to be a class
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank !"
                        )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #The function filter(function, list) offers an
        # elegant way to filter out all the elements of a list, for which the function function returns True.

        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': item}, 200 if item else 404 #information for data was create or not

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