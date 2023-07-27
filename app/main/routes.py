from app.views.login import login
from app.views.logout import logout
from app.views.index import index
from app.views.dashboard import dashboard
from app.views.register import register
from app.views.currentWeather import current_weather
from app.views.historyWeather import history_weather
from app.main import login_bp, logout_bp,  index_bp, dashboard_bp, register_bp, current_weather_bp, history_weather_bp

"""
Initiaizing Route for the Sites
"""

login_bp.route("/login", methods=['GET', 'POST'])(login)
logout_bp.route("/logout", methods=['GET', 'POST'])(logout)
index_bp.route("/")(index)
dashboard_bp.route("/dashboard")(dashboard)
register_bp.route("/register",  methods=['GET', 'POST'])(register)
current_weather_bp.route("/currentWeather",  methods=['GET', 'POST'])(current_weather)
history_weather_bp.route("/historyWeather",  methods=['GET', 'POST'])(history_weather)
