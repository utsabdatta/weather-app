import jwt
import logging
from app.config import Config
from app.extensions import csrf
from app.models.users import User
from datetime import datetime, timedelta
from flask import request, jsonify, make_response

# Initialize Logger  here
logger = logging.getLogger(__name__)


@csrf.exempt
def generate_token():
    """
    If email and password are correct then it will return a valid JWT Token using which we will be able to access other APIs.
    :return: Valid JWT Token
    """
    # creates dictionary of form data
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

    user = User.query \
        .filter_by(email=auth.get('email')) \
        .first()

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        )

    if user.check_password(auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, Config.SECRET_KEY)

        logger.debug(f"Token got greated for {auth.get('email')}")
        return make_response(jsonify({'token': token}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
    )
