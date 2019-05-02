from flask_restful import Resource
from service.models.store_model import StoreModel, StoreDAO

class Store(Resource):
    def get(self, name):
        store = StoreDAO.find_by_name(name)
        if store:
            return store[0].json()
        return {'massage': "Store Not Found"}

    def post(self, name):
        res = StoreDAO.find_by_name(name)
        if res:
            return {'massage': "Store with Name '{}' already Exist.".format(name)}

        store = StoreModel(name)
        StoreDAO.save(store)
        return store.json()