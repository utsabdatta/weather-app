from flask import Blueprint

"""
Initializing Blue Print so that it can be use to route 
"""

login_bp = Blueprint("login", __name__)
logout_bp = Blueprint("logout", __name__)
index_bp = Blueprint("index", __name__)
dashboard_bp = Blueprint("dashboard", __name__)
register_bp = Blueprint("register", __name__)
current_weather_bp = Blueprint("current_weather", __name__)
history_weather_bp = Blueprint("history_weather", __name__)

from app.main import routes

