import pygame
from pygame import Vector2

from obstaculo import Obstaculo
from constantes import *

class Capivara(Obstaculo):
    def __init__(self):
        super().__init__(Vector2(1280, 496), Vector2(80, 80), [pygame.image.load(CAMINHO_ASSETS+"capivara1.png"), pygame.image.load(CAMINHO_ASSETS+"capivara2.png")])
