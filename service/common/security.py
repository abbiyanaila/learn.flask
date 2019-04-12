from werkzeug.security import safe_str_cmp
from service.resources import user


def authenticate(username, password):
    usr = user.User.find_by_username(username)
    if user and safe_str_cmp(usr.password, password):
        return usr


def identity(payload):
    user_id = payload['identity']
    return user.User.find_by_id(user_id)