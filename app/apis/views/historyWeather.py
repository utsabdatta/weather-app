import logging
from app.extensions import csrf
from app.models.users import User
from app.models.weather import Weather
from app.schemas.weather import WeatherSchema
from flask import request, jsonify, make_response
from app.apis.views import token_required as jwt_token

# Initialize Logger  here
logger = logging.getLogger(__name__)


@csrf.exempt
@jwt_token
def history_weather():
    """
    It will show all the Past search result of the particular User. It reuired Valid JWT Token
    :return: List of all Past Search Result done by he User
    """
    if request.method == "GET" or request.method == "POST":
        data = request.form

        if not data or not data.get('email'):
            # returns 401 if any email or / and password is missing
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
            )

        user = User.query \
            .filter_by(email=data.get('email')) \
            .first()

        if not user:
            # returns 401 if user does not exist
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
            )

        try:
            weather_report = Weather.get_by_email(data.get('email'))

            weather_schema = WeatherSchema(many=True)

            logger.debug(f"weather_report_schema: {weather_schema.dump(weather_report)}")

            return jsonify(weather_schema.dump(weather_report))
        except:
            return jsonify({"Status Code": 404})
