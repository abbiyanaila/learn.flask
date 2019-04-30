from flask_restful import Resource, reqparse
from service.models.user_model import UserModel, UserDAO

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field can't be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field can't be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserDAO.find_by_username(data['username']):
            return {"massage": "A user with usernamse already exist"}

        user = UserModel()
        user.username = data['username']
        user.password = data['password']
        UserDAO.save(user)

        return {"massage": "User Created Successfully."}


