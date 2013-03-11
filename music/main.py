import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar

import os

from music import ArduinoMusic
from ard_socket import ArduinoSocket

#ip = '192.168.1.177'
ip = '141.31.74.21'

class MusicLayout(FloatLayout):
    loadfile = ObjectProperty(None)
    ardSocket = ArduinoSocket(ip, 5000);

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def show_warning(self):
        popup = Popup(title='Warning',
                      content=Label(text='No track loaded'),
                      size_hint=(0.2, 0.2))
        popup.open()
        
    def load(self, path, filename):
        try:
            print path
            print filename
            pb = ProgressBar(max=1000)
            self.ardMusic = ArduinoMusic(os.path.join(path, filename[0]), self.ardSocket)
        except:
            pass
        self.dismiss_popup()

    def startMusic(self):
        if hasattr(self,'ardMusic'):
            self.ardMusic.start()
        else:
            self.show_warning()

    def stopMusic(self):
        if hasattr(self,'ardMusic'):
            self.ardMusic.stop()
        else:
            self.show_warning()

    def pauseMusic(self):
        if hasattr(self,'ardMusic'):
            self.ardMusic.pause()
        else:
            self.show_warning()

    def unpauseMusic(self):
        if hasattr(self,'ardMusic'):
            self.ardMusic.play()
        else:
            self.show_warning()

    def shutdown(self):
        print "shutdown"
        self.ardSocket.sendPackage(self.ardSocket.SHUTDOWN, 0)

    def reconnect(self):
        self.ardSocket.close()
        self.ardSocket = ArduinoSocket(ip, 5000);

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MusicApp(App):
    def build(self):
        return MusicLayout()

if __name__ == '__main__':
    MusicApp().run()
