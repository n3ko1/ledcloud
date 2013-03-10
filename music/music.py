from ard_socket import ArduinoSocket
import echonest.remix.audio as audio
import pygame
import subprocess
import time, threading
import random
import sys

from pyechonest import config
config.ECHO_NEST_API_KEY="7F6SMSDFUDAQE3QAJ"

mp3 = sys.argv[1]
frommp3 = subprocess.Popen(['mpg123', '-w', '-', mp3], stdout=subprocess.PIPE)
toogg = subprocess.call(['oggenc', '-'], stdin=frommp3.stdout, stdout=open('temp.ogg', 'wb'))

ip = '192.168.0.177'
    
audio_file = audio.LocalAudioFile("temp.ogg")
bpm = audio_file.analysis.tempo
print bpm
print "track has %d bpm." % (bpm['value'])

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 30
y = 30

sock = ArduinoSocket(ip, 5000)

clock = pygame.time.Clock()
pygame.mixer.music.load("temp.ogg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            pygame.mixer.music.play()
            sock.sendPackage(sock.MUSIC, bpm['value'])
        if pressed[pygame.K_DOWN]: 
            pygame.mixer.music.stop()
            sock.sendPackage(sock.RANDOM, 0)
        if pressed[pygame.K_LEFT]:
            pygame.mixer.music.pause()
            sock.sendPackage(sock.RANDOM, 0)
        if pressed[pygame.K_RIGHT]:
            pygame.mixer.music.unpause()
            sock.sendPackage(sock.MUSIC, bpm['value'])
        
        screen.fill((255, 255, 255))
        # Display some text
	font = pygame.font.Font(None, 36)
	text = font.render(mp3, 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)
        
        pygame.display.flip()
        clock.tick(60)
