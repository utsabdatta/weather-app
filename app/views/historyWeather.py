import logging
from app.models.users import User
from app.models.weather import Weather
from app.schemas.weather import WeatherSchema
from flask import request, render_template, session
from flask_paginate import Pagination, get_page_parameter

# Initialize Logger  here
logger = logging.getLogger(__name__)


def history_weather():
    """
    It will show all the Past search result of the particular User.
    :return: List of all Past Search Result done by he User
    """
    if request.method == "GET":
        try:
            email = session['email']
            try:
                weather_report = Weather.get_by_email(email)
                weather_report_columns = ["Place", "Weather", "Temperature", "Temperature Shade",
                                         "Humidity", "Dew Point", "Wind", "Wind Gust", "UV Index", "Visibility", "Cloud Cover",
                                         "Ceiling", "Pressure"]
                user = User.query.filter_by(email=email).first()

                weatherSchema = WeatherSchema(many=True)

                logger.debug(f"weather_report_schema: {weatherSchema.dump(weather_report)}")

                page = request.args.get(get_page_parameter(), type=int, default=1)
                pagination = Pagination(page=page, per_page=10, total=len(weather_report), search=False, record_name='weather_report')


                return render_template("historyWeather.html", weather_report=weatherSchema.dump(weather_report)[(page-1)*10:page*10],
                                       weather_report_columns=weather_report_columns, user=user, pagination=pagination)
            except Exception as error:
                user = User.query.filter_by(email=email).first()
                return render_template("dashboard.html", user=user, message="Nothing to Show")
        except:
            return render_template("index.html", message="You must loggedIn to Access the Page")
