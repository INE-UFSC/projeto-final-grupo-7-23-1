import pygame
from pygame import Vector2

from obstaculo import Obstaculo
from constantes import *

class Jacare(Obstaculo):
    def __init__(self):
        super().__init__(Vector2(1280, 516), Vector2(90, 60), [pygame.image.load(CAMINHO_ASSETS+"jacare1.png"),pygame.image.load(CAMINHO_ASSETS+"jacare2.png")])
