import logging
import requests
from app.extensions import csrf
from bs4 import BeautifulSoup as bs
from flask import request, jsonify, make_response
from app.apis.views import token_required as jwt_token

# Initialize Logger  here
logger = logging.getLogger(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


@csrf.exempt
@jwt_token
def custom_weather():
    """
    It is made using BeautifulSoup, It simply sracp data from google search and show the result. It don't store it in the DB.
    :return:
            {
            "dayhour": "Thursday, 1:00 am",
            "humidity": "86%",
            "place": "bangalore",
            "precipitation": "6%",
            "region": "Weather",
            "temp_now": "21",
            "weather_now": "Drizzle",
            "wind": "21 km/h"
        }
    """
    if request.method == "GET" or request.method == "POST":
        data = request.form

        if not data or not data.get('city_name'):
            return make_response(
                'City Name Required',
                401,
                {'WWW-Authenticate': 'Basic realm ="City Name Required!!"'}
            )
    city = data.get('city_name')
    city = city.replace(" ", "+")

    url = f"https://www.google.com/search?q=weather+{city}"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"

    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['place'] = city
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

    logger.debug(f"result: {result}")

    return jsonify(result)
