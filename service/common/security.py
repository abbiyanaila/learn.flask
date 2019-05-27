from werkzeug.security import safe_str_cmp
from service.models.user_model import UserModel, UserDAO


def authenticate(username, password):
    usr = UserDAO.find_by_username(username)
    if usr and safe_str_cmp(usr.password, password):
        return usr


def identity(payload):
    user_id = payload['identity']
    return UserDAO.find_by_id(user_id)