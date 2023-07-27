import jwt
from app.config import Config
from functools import wraps
from flask import request, jsonify


def token_required(f):
    """
    It validate JWT Token
    :param f: token
    :return: It returns error that means the token is not valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            print(f"Token: {token}")
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        except Exception as error:
            print(error)
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return f(*args, **kwargs)

    return decorated
