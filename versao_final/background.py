import pygame
from entidade import *

class Background(Entidade):
    def __init__(self, id, posicao, tamanho,cor, imagem):
        super().__init__(id, posicao, tamanho,cor,imagem)
        self.set_velocidade(pygame.Vector2(-100, 0))
    
    def checkOver(self):
        return self.get_rect().right < 0