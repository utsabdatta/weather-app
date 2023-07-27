from marshmallow import Schema, fields


class WeatherSchema(Schema):
    placeName = fields.String()
    weatherText = fields.String()
    observationDateTime = fields.String()
    temperature = fields.String()
    realFeelTemperature = fields.String()
    realFeelTemperatureShade = fields.String()
    relativeHumidity = fields.String()
    indoorRelativeHumidity = fields.String()
    dewPoint = fields.String()
    wind = fields.String()
    windGust = fields.String()
    uvIndex = fields.String()
    visibility = fields.String()
    cloudCover = fields.String()
    ceiling = fields.String()
    pressure = fields.String()