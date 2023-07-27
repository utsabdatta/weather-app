from app.extensions import db


class Weather(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), db.ForeignKey('users.email'))
    placeName = db.Column(db.String(100))
    weatherText = db.Column(db.String(100))
    weatherIcon = db.Column(db.String(100))
    observationDateTime = db.Column(db.String(100))
    temperature = db.Column(db.String(100))
    realFeelTemperature = db.Column(db.String(100))
    realFeelTemperatureShade = db.Column(db.String(100))
    relativeHumidity = db.Column(db.String(100))
    indoorRelativeHumidity = db.Column(db.String(100))
    dewPoint = db.Column(db.String(100))
    wind = db.Column(db.String(100))
    windGust = db.Column(db.String(100))
    uvIndex = db.Column(db.String(100))
    visibility = db.Column(db.String(100))
    cloudCover = db.Column(db.String(100))
    ceiling = db.Column(db.String(100))
    pressure = db.Column(db.String(100))

    def __init__(self, email, place_name, weather_text, weather_icon, observation_date_time, temperature,
                 real_feel_temperature, real_feel_temperature_shade, relative_humidity, indoor_relative_humidity,
                 dew_point, wind, wind_gust, uv_index, visibility, cloud_cover, ceiling, pressure):
        self.email = email
        self.placeName = place_name
        self.weatherText = weather_text
        self.weatherIcon = weather_icon
        self.observationDateTime = observation_date_time
        self.temperature = temperature
        self.realFeelTemperature = real_feel_temperature
        self.realFeelTemperatureShade = real_feel_temperature_shade
        self.relativeHumidity = relative_humidity
        self.indoorRelativeHumidity = indoor_relative_humidity
        self.dewPoint = dew_point
        self.wind = wind
        self.windGust = wind_gust
        self.uvIndex = uv_index
        self.visibility = visibility
        self.cloudCover = cloud_cover
        self.ceiling = ceiling
        self.pressure = pressure

    def __repr__(self):
        return self.email

    @classmethod
    def get_by_email(cls, email):
        return db.session.query(cls.placeName, cls.weatherText,
                                cls.temperature, cls.realFeelTemperatureShade,
                                cls.indoorRelativeHumidity, cls.dewPoint, cls.wind,
                                cls.windGust, cls.uvIndex, cls.visibility, cls.cloudCover, cls.ceiling,
                                cls.pressure).filter(cls.email == email).all()

    def save(self):
        db.session.add(self)
        db.session.commit()
