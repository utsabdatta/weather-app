from flask import Blueprint

"""
Initializing Blue Print so that it can be use to route 
"""

api_generate_token_bp = Blueprint("api_generate_token", __name__)
api_get_all_users_bp = Blueprint("api_get_all_users", __name__)
api_current_weather_bp = Blueprint("api_current_weather", __name__)
api_custom_weather_bp = Blueprint("api_custom_weather", __name__)
api_history_weather_bp = Blueprint("api_history_weather", __name__)

from app.apis import routes