from werkzeug.security import safe_str_cmp
from service.models.user_model import UserModel, UserDAO


def authenticate(username, password):
    list_usr = UserDAO.find_by_username(username)
    if list_usr and safe_str_cmp(list_usr[0].password, password):
        return list_usr[0]


def identity(payload):
    user_id = payload['identity']
    return UserDAO.find_by_id(user_id)