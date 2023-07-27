from app.apis.views.getAllUsers import get_all_users
from app.apis.views.generateToken import generate_token
from app.apis.views.historyWeather import history_weather
from app.apis.views.currentWeather import current_weather
from app.apis.views.customWeather import custom_weather
from app.apis import api_generate_token_bp, api_get_all_users_bp, api_current_weather_bp, api_history_weather_bp,\
api_custom_weather_bp

"""
Initiaizing Route for the APIs
"""

api_generate_token_bp.route("/generate_token", methods=['GET', 'POST'])(generate_token)
api_get_all_users_bp.route("/get/all_users", methods=['GET', 'POST'])(get_all_users)
api_current_weather_bp.route("/currentWeather",  methods=['GET', 'POST'])(current_weather)
api_custom_weather_bp.route("/customWeather",  methods=['GET', 'POST'])(custom_weather)
api_history_weather_bp.route("/historyWeather",  methods=['GET', 'POST'])(history_weather)
