import pygame
from entidade import *

class Efeito(Entidade):
    def __init__(self, id, posicao, tamanho,cor):
        super().__init__(id, posicao, tamanho,cor)
        self.set_velocidade(pygame.Vector2(-300, 0))
    
    def checkOver(self):
        if self.get_posicao().x < 0:
            return True
        else:
            return False