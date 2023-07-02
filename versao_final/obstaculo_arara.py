import pygame
from pygame import Vector2

from obstaculo import Obstaculo
from constantes import *

class Arara(Obstaculo):
    def __init__(self):
        super().__init__(Vector2(1280, 476), Vector2(35, 40), [pygame.image.load(CAMINHO_ASSETS+"arara1.png"),pygame.image.load(CAMINHO_ASSETS+"arara2.png")])
