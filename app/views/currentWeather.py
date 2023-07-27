import logging
import requests
from app.models.users import User
from app.models.weather import Weather
from app.schemas.weather import WeatherSchema
from flask import request, render_template, session, url_for

# Initialize Logger  here
logger = logging.getLogger(__name__)


class CurrentWeather:
    """
    To get the Current Weather Report based on the search City and then store it into DB. It uses 3rd Party API
    and API Key is of trial version per day it will give 50 limits.
    """
    api_key = "5t3AW5j7siNP2h2TuBG2QqPUVlGRBr99"
    # api_key = "cY9n3uHKf706BvJG4nIU0JuDf1uGg1Dn"
    base_url = "http://dataservice.accuweather.com/"
    location_api = "locations/v1/cities/search"
    current_condition_api = "currentconditions/v1/"

    def __init__(self, city_name):
        self.city_name = city_name
        self.city_key = None

    @staticmethod
    def get_data(complete_url):
        data = {
            "Accept-Encoding": "gzip"
        }

        logger.info(f"complete_url: {complete_url}")

        response = requests.get(complete_url, json=data)
        return response.json()

    @staticmethod
    def get_weather_report(api_response, place_name):
        """
        It is to take the required data from the API Response

        :param api_response: reponse of the 3rd party api
        :param place_name: valid place if not found by default it will take "Tamluk"
        :return: Serialized Data
        """
        response = api_response[0]
        weather_text = response['WeatherText']
        weather_icon = response['WeatherIcon']
        observation_date_time = response['LocalObservationDateTime']
        temperature_metric = response['Temperature']['Metric']
        temperature_imperial = response['Temperature']['Imperial']
        temperature = str(temperature_metric['Value']) + temperature_metric['Unit'] + ' / ' \
                      + str(temperature_imperial['Value']) + temperature_imperial['Unit']
        real_feel_temperature_metric = response['RealFeelTemperature']['Metric']
        real_feel_temperature_imperial = response['RealFeelTemperature']['Imperial']
        real_feel_temperature = str(real_feel_temperature_metric['Value']) + real_feel_temperature_metric['Unit'] + \
                                ' / ' + str(real_feel_temperature_imperial['Value']) \
                                + real_feel_temperature_imperial['Unit']
        real_feel_temperature_shade_metric = response['RealFeelTemperatureShade']['Metric']
        real_feel_temperature_shade_imperial = response['RealFeelTemperatureShade']['Imperial']
        real_feel_temperature_shade = str(real_feel_temperature_shade_metric['Value']) + \
                                      real_feel_temperature_shade_metric['Unit'] + ' / ' + \
                                      str(real_feel_temperature_shade_imperial['Value']) + \
                                      real_feel_temperature_shade_imperial['Unit']
        relative_humidity = str(response['RelativeHumidity']) + '%'
        indoor_relative_humidity = str(response['IndoorRelativeHumidity']) + '%'
        dew_point_metric = response['DewPoint']['Metric']
        dew_point_imperial = response['DewPoint']['Imperial']
        dew_point = str(dew_point_metric['Value']) + dew_point_metric['Unit'] + ' / ' + \
                    str(dew_point_imperial['Value']) + dew_point_imperial['Unit']
        wind_direction = response['Wind']['Direction']['Localized']
        wind_metric = response['Wind']['Speed']['Metric']
        wind_imperial = response['Wind']['Speed']['Imperial']
        wind = wind_direction + ' ' + str(wind_metric['Value']) + wind_metric['Unit'] + ' / ' + \
               str(wind_imperial['Value']) + wind_imperial['Unit']
        wind_gust_metric = response['WindGust']['Speed']['Metric']
        wind_gust_imperial = response['WindGust']['Speed']['Imperial']
        wind_gust = str(wind_gust_metric['Value']) + wind_gust_metric['Unit'] + ' / ' + \
                    str(wind_gust_imperial['Value']) + wind_gust_imperial['Unit']
        uv_index = str(response['UVIndex']) + ' ' + response['UVIndexText']
        visibility_metric = response['Visibility']['Metric']
        visibility_imperial = response['Visibility']['Imperial']
        visibility = str(visibility_metric['Value']) + visibility_metric['Unit'] + ' / ' + \
                     str(visibility_imperial['Value']) + visibility_imperial['Unit']
        cloud_cover = str(response['CloudCover'])
        ceiling_metric = response['Ceiling']['Metric']
        ceiling_imperial = response['Ceiling']['Imperial']
        ceiling = str(ceiling_metric['Value']) + ceiling_metric['Unit'] + ' / ' + \
                  str(ceiling_imperial['Value']) + ceiling_imperial['Unit']
        pressure_metric = response['Pressure']['Metric']
        pressure_imperial = response['Pressure']['Imperial']
        pressure = str(pressure_metric['Value']) + pressure_metric['Unit'] + ' / ' + \
                   str(pressure_imperial['Value']) + pressure_imperial['Unit']
        email = session['email']

        weather = Weather(email, place_name, weather_text, weather_icon, observation_date_time, temperature,
                          real_feel_temperature, real_feel_temperature_shade, relative_humidity,
                          indoor_relative_humidity, dew_point, wind, wind_gust, uv_index,
                          visibility, cloud_cover, ceiling, pressure)

        weather.save()

        serializer = WeatherSchema()

        data = serializer.dump(weather)
        logger.debug(f"Weather Schema: {data}")
        return data, weather_icon

    def access_api(self):
        """
        Using 3rd Party APi Fetching the Weather Report
        :return: API Response if API Key is Valid
        """
        try:
            complete_url = self.base_url + self.location_api + "?apikey=" + self.api_key + "&q=" + self.city_name

            location_api_response = CurrentWeather.get_data(complete_url)

            logger.debug(f"location_api_response: {location_api_response}")

            try:
                self.city_key = location_api_response[0]['Key']
            except Exception as e:
                self.city_key = "191648"
                self.city_name = "Tamluk"

            complete_url = self.base_url + self.current_condition_api + self.city_key + "?apikey=" + self.api_key + "&details=true"

            current_condition_api_response = CurrentWeather.get_data(complete_url)

            logger.debug(f"current_condition_api_response: {current_condition_api_response}")

            get_weather_report, weather_icon =  CurrentWeather.get_weather_report(current_condition_api_response, self.city_name)
            logger.debug(f"get_weather_report: {get_weather_report}")
            return get_weather_report, weather_icon
        except:
            return False, False


def current_weather():
    if request.method == "POST":
        try:
            city_name = request.form['city_name']
            print(f"city_name: {city_name}")
            weather = CurrentWeather(city_name)
            weather_report, weather_icon = weather.access_api()
            logger.debug(f"weather_report: {weather_report} weather_icon: {weather_icon}")
            user = User.query.filter_by(email=session['email']).first()
            icon = "icons/"+str(weather_icon)+".png"
            if weather_report is not False:
                return render_template("currentWeather.html", weather=weather_report, user=user, icon=url_for('static', filename=icon))
            else:
                return render_template("dashboard.html", user=user, message="API Key is not Valid")
            if weather_report is None:
                return render_template("index.html", message="You must loggedIn to Access the Page")
        except:
            return render_template("index.html", message="You must loggedIn to Access the Page")
    else:
        try:
            user = User.query.filter_by(email=session['email']).first()
            return render_template("dashboard.html", user=user, message="You can't access it directly")
        except Exception as error:
            print(error)
            return render_template("index.html", message="You must loggedIn to Access the Page")
