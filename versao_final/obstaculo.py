import pygame
from entidade import *

class Obstaculo(Entidade):
    def __init__(self, id, posicao, tamanho, imagem):
        super().__init__(id, posicao, tamanho,"red",imagem)
        self.set_velocidade(pygame.Vector2(-300, 0))
    
    def checkOver(self):
        return self.get_rect().right < 0