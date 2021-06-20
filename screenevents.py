import pygame
from pygame import mixer
from random import randint

def screening(num):
    amongus = mixer.Sound('assets/amongus drip.mp3')

    if num == 0:
        amongus.play(loops=-1, fade_ms=2500)
        amongus.set_volume(1.0)

    if num == 1:
        pygame.mixer.pause()
        amongus.set_volume(0.0)