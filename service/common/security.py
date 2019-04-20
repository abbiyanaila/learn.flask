from werkzeug.security import safe_str_cmp
from service.models.user_model import UserModel


def authenticate(username, password):
    usr = UserModel.find_by_username(username)
    if user and safe_str_cmp(usr.password, password):
        return usr


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)