import pygame
from pygame import Vector2

from obstaculo import Obstaculo
from constantes import *

class Caranguejo(Obstaculo):
    def __init__(self):
        super().__init__(Vector2(1280, 516), Vector2(60, 60), [pygame.image.load(CAMINHO_ASSETS+"caranguejo.png")])
