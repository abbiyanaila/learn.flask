from flask_restful import Resource, reqparse
from service.common import connector
from service.models.user_model import UserModel


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

        if UserModel.find_by_username(data['username']):
            return {"massage": "A user witth hat usernamse already exist"}, 400

        connection = connector.get_connection()
        cursor = connector.get_cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"massage": "User Created Successfully."}, 201


