import pygame
from pygame import Vector2

from obstaculo import Obstaculo
from constantes import *

class CarroVermelho(Obstaculo):
    def __init__(self):
        super().__init__(Vector2(1280, 496), Vector2(120, 80), [pygame.image.load(CAMINHO_ASSETS+"carrovermelho.png")])
