from json import load
from urllib2 import urlopen
from pprint import pprint

class WeatherAPI:
    weatherAPIUrl = 'http://openweathermap.org/data/2.1/find/name?q=%s'
    descriptions = { 'Sky is Clear': 1, 
                     'few clouds': 2, 
                     'scattered clouds': 3, 
                     'broken clouds': 4,
                     'shower rain': 5,
                     'Rain': 6,
                     'Thunderstorm': 7,
                     'snow': 8,
                     'mist': 9 }

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

    def getWeatherCode(self):
        if hasattr(self, 'city'):
            return self.descriptions[self.city['weather'][0]['description']]
        return 0
        
    def getWeather(self):
        if hasattr(self, 'city'):
            return self.city['weather'][0]['description']
        return ''
