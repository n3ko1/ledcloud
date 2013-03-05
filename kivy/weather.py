from json import load
from urllib2 import urlopen
from pprint import pprint
import math

class WeatherAPI:
    CODE_RAIN = 1
    CODE_LIGHTNING = 2
    CODE_SUN = 3

    API_CODES = { 'API_THUNDER': 2.0,
                  'API_RAIN_1': 3.0,
                  'API_RAIN_2': 5.0,
                  'API_SNOW': 6.0,
                  'API_CLEAR': 8.0 }
    
    weatherAPIUrl = 'http://openweathermap.org/data/2.1/find/name?q=%s'

    def __init__(self, cityName):
        data = urlopen(self.weatherAPIUrl % (cityName))
        cities = load(data)
        if cities['cod'] != '404' and cities['cod'] != '404.5':
            if cities['count'] > 0:
                self.city = cities['list'][0]
        else:
            return None

    def getTemperature(self):
        if hasattr(self, 'city'):
            return float(self.city['main']['temp']) - 273.15
        return 0

    def getWeatherCategory(self):
        if hasattr(self, 'city'):
            if math.floor(self.city['weather'][0]['id'] / 100) == self.API_CODES['API_THUNDER']:
                return self.CODE_LIGHTNING
            if (math.floor(self.city['weather'][0]['id'] / 100) == self.API_CODES['API_RAIN_1'] or 
                math.floor(self.city['weather'][0]['id'] / 100) == self.API_CODES['API_RAIN_2'] or 
                math.floor(self.city['weather'][0]['id'] / 100) == self.API_CODES['API_SNOW']):
                return self.CODE_RAIN
            if math.floor(self.city['weather'][0]['id'] / 100) == self.API_CODES['API_CLEAR']:
                return self.CODE_SUN
        return self.CODE_SUN

    def getWeatherCode(self):
        if hasattr(self, 'city'):
            return self.city['weather'][0]['id']
        return 0
        
    def getWeather(self):
        if hasattr(self, 'city'):
            return self.city['weather'][0]['description']
        return ''
