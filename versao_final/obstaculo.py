import pygame
import random
from entidade import *

class Obstaculo(Entidade):
    def __init__(self, posicao, tamanho, imagem):
        super().__init__(posicao, tamanho,"red",imagem)
        self.set_velocidade(pygame.Vector2(-300, 0))
        self.__random_x = random.randint(0, 780)

    def checkOver(self):
        return self.get_rect().right < 0

    def randomize_x(self):
        self.__random_x = random.randint(0, 780)

    def get_random_x(self):
        return self.__random_x
