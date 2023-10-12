from pygame import mixer
import pygame
pygame.init()
mixer.init()
mixer.music.load('Áudio do WhatsApp de 2023-10-11 à(s) 17.55.25_d61817fe.mp3')
mixer.music.play()
mixer.music.set_volume(0.6)
import time
time.sleep(360)