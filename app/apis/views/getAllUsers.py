from app.models.users import User
from flask import jsonify, request
from app.schemas.users import UserSchema
from app.apis.views import token_required as jwt_token


@jwt_token
def get_all_users():
    """
    It will return all valid users registered for the App if Token is Valid
    :return: All Valid Users
    """
    if request.method == "GET" or request.method == "POST":
        users = User.query.all()
        users_schema = UserSchema(many=True)
        return jsonify(users_schema.dump(users))
