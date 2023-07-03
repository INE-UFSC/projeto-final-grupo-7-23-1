import pygame
from pygame import Vector2

from obstaculo import Obstaculo
from constantes import *

class Gaivota(Obstaculo):
    def __init__(self):
        super().__init__(Vector2(1280, 476), Vector2(45, 45), [pygame.image.load(CAMINHO_ASSETS+"gaivota1.png"),
                                                               pygame.image.load(CAMINHO_ASSETS+"gaivota2.png"),
                                                               pygame.image.load(CAMINHO_ASSETS+"gaivota3.png"),
                                                               pygame.image.load(CAMINHO_ASSETS+"gaivota4.png")])
