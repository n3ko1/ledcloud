import kivy
kivy.require('1.4.1')

from kivy.properties import NumericProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.clock import Clock
from weather import WeatherAPI

ip = '192.168.0.123'

class RemoteLayout(FloatLayout):
    city = 'stuttgart'

    def weather_forecast(self, element):
        weather = WeatherAPI(self.city)
        if weather != None:
            print(weather.getWeatherCode())
            print(weather.getTemperature())
        else:
            self.city = 'stuttgart'
            weather = WeatherAPI(self.city)
            print(weather.getWeatherCode())
            print(weather.getTemperature())
        #r = requests.post(ip, params={'weatherCode':stuttgart.getWeatherCode()})

    def change_city(self, element, value):
        self.city = value

    def show_popup(self):
        btnclose = Button(text='Abort', size_hint_y=None, height='50dp')
        btngo = Button(text='Forecast', size_hint_y=None, height='50dp')
        ti = TextInput(
                text='',
                size_hint_y=None,
                height='30dp')
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Enter a city'))
        content.add_widget(ti)
        content.add_widget(btngo)
        content.add_widget(btnclose)
        popup = Popup(content=content, title='Weather forecast',
                      size_hint=(None, None), size=('300dp', '300dp'))
        btnclose.bind(on_release=popup.dismiss)
        btngo.bind(on_press=self.weather_forecast)
        ti.bind(text=self.change_city)
        popup.open()

    def sunshine(self):
        print "sunshine"
    
    def rain(self):
        print "rain"
    
    def lightning(self):
        print "lightning"
    
    def random(self):
        print "random"

    def shutdown(self):
        print "shutdown"

    def setRSl(self, value):
        print value
    
    def setYSl(self, value):
        print value

    def setGSl(self, value):
        print value

    def setBSl(self, value):
        print value

    def setRSw(self, value):
        print value

    def setWSw(self, value):
        print value

    def setYSw(self, value):
        print value

    def setRgbSw(self, value):
        print value

class RemoteApp(App):

    def build(self):
        return RemoteLayout()

if __name__ == '__main__':
    RemoteApp().run()
