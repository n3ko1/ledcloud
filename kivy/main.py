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
from ard_socket import ArduinoSocket

ip = '192.168.1.177'

class RemoteLayout(FloatLayout):
    city = 'stuttgart'
    ardSocket = ArduinoSocket(ip, 5000);

    def weather_forecast(self, element):
        weather = WeatherAPI(self.city)
        self.print_weather(weather)
        print(weather.getWeather())
        print(weather.getWeatherCode())
        print(weather.getTemperature())
        print(weather.getWeatherCategory())
        category = weather.getWeatherCategory();
        if category == weather.CODE_SUN:
            self.ardSocket.sendPackage(self.ardSocket.SUNSHINE, 0)
        if category == weather.CODE_RAIN:
            self.ardSocket.sendPackage(self.ardSocket.RAIN, 0)
        if category == weather.CODE_LIGHTNING:
            self.ardSocket.sendPackage(self.ardSocket.LIGHTNING, 0)
            

    def change_city(self, element, value):
        self.city = value

    def print_weather(self, weather):
        data = '%s at %s degrees' % ( weather.getWeather(), str(weather.getTemperature()) )
        content = BoxLayout(orientation='vertical')
        btnclose = Button(text='Done', size_hint_y=.4)
        content.add_widget(Label(text=data))
        content.add_widget(btnclose)
        popup = Popup(content=content, title='Weather forecast',
                      size_hint=(.4, .4))
        btnclose.bind(on_release=popup.dismiss)
        popup.open()

    def show_popup(self):
        btnclose = Button(text='Abort', size_hint_y=.4)
        btngo = Button(text='Forecast', size_hint_y=.4)
        ti = TextInput(
                text='',
                size_hint_y=.4)
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Enter a city'))
        content.add_widget(ti)
        content.add_widget(btngo)
        content.add_widget(btnclose)
        popup = Popup(content=content, title='Weather forecast',
                      size_hint=(.5, .5))
        btnclose.bind(on_release=popup.dismiss)
        btngo.bind(on_press=self.weather_forecast)
        ti.bind(text=self.change_city)
        popup.open()

    def sunshine(self):
        print "sunshine"
        self.ardSocket.sendPackage(self.ardSocket.SUNSHINE, 0)
    
    def rain(self):
        print "rain"
        self.ardSocket.sendPackage(self.ardSocket.RAIN, 0)
    
    def lightning(self):
        print "lightning"
        self.ardSocket.sendPackage(self.ardSocket.LIGHTNING, 0)
    
    def random(self):
        print "random"
        self.ardSocket.sendPackage(self.ardSocket.RANDOM, 0)

    def shutdown(self):
        print "shutdown"
        self.ardSocket.sendPackage(self.ardSocket.SHUTDOWN, 0)

    def reconnect(self):
        self.ardSocket.close()
        self.ardSocket = ArduinoSocket(ip, 5000);

    def setRSl(self, value):
        print value
        if int(value) % 5 == 0:
            self.ardSocket.sendPackage(self.ardSocket.RED_PWM, value)
    
    def setYSl(self, value):
        print value
        if int(value) % 5 == 0:
            self.ardSocket.sendPackage(self.ardSocket.YELLOW_PWM, value)

    def setGSl(self, value):
        print value
        if int(value) % 5 == 0:
            self.ardSocket.sendPackage(self.ardSocket.GREEN_PWM, value)

    def setBSl(self, value):
        print value
        if int(value) % 5 == 0:
            self.ardSocket.sendPackage(self.ardSocket.BLUE_PWM, value)

    def setRSw(self, value):
        print value
        if value:
            self.ardSocket.sendPackage(self.ardSocket.RED, 100)
        else:
            self.ardSocket.sendPackage(self.ardSocket.RED, 0)

    def setWSw(self, value):
        print value
        if value:
            self.ardSocket.sendPackage(self.ardSocket.WHITE, 100)
        else:
            self.ardSocket.sendPackage(self.ardSocket.WHITE, 0)

    def setYSw(self, value):
        print value
        if value:
            self.ardSocket.sendPackage(self.ardSocket.YELLOW, 100)
        else:
            self.ardSocket.sendPackage(self.ardSocket.YELLOW, 0)

    def setRgbSw(self, value):
        print value
        if value:
            self.ardSocket.sendPackage(self.ardSocket.RGB, 100)
        else:
            self.ardSocket.sendPackage(self.ardSocket.RGB, 0)

class RemoteApp(App):

    def build(self):
        return RemoteLayout()

if __name__ == '__main__':
    RemoteApp().run()
