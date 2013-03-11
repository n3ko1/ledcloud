from ard_socket import ArduinoSocket
import echonest.remix.audio as audio
import pygame
import subprocess

from pyechonest import config
config.ECHO_NEST_API_KEY="7F6SMSDFUDAQE3QAJ"

class ArduinoMusic:
    def __init__(self, mp3, sock):
        self.sock = sock
        self.mp3 = mp3
        self.convertToOgg()
        self.calcBpm()
        self.toogg.wait()
        pygame.init()
        pygame.mixer.music.load("temp.ogg")

    def convertToOgg(self):
        self.frommp3 = subprocess.Popen(['mpg123', '-w', '-', self.mp3], stdout=subprocess.PIPE)
        self.toogg = subprocess.Popen(['oggenc', '-'], stdin=self.frommp3.stdout, stdout=open('temp.ogg', 'wb'))

    def calcBpm(self):
        audio_file = audio.LocalAudioFile(self.mp3)
        self.bpm = round(audio_file.analysis.tempo['value'])
        print "track has %d bpm." % (self.bpm)

    def start(self):
        pygame.mixer.music.play()
        self.sock.sendPackage(self.sock.MUSIC, self.bpm)

    def stop(self):
        pygame.mixer.music.stop()
        self.sock.sendPackage(sock.RANDOM, 0)

    def play(self):
        pygame.mixer.music.unpause()
        self.sock.sendPackage(sock.MUSIC, bpm)

    def pause(self):
        pygame.mixer.music.pause()
        self.sock.sendPackage(sock.RANDOM, 0)
