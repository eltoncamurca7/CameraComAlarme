import pygame
from time import sleep

class Alarm:
    
    def som():
        pygame.init()
        pygame.mixer.music.load('alarm.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        sleep(60)
        