import pygame
from entidade import *
from constantes import TELA_WIDTH

class Background(Entidade):
    def __init__(self, id, posicao, tamanho,cor, imagem):
        super().__init__(id, posicao, tamanho,cor,imagem)
        self.set_velocidade(pygame.Vector2(-100, 0))
    
    def checkLeft(self):
        return self.get_rect().left <= 0
    def checkOver(self):
        return self.get_rect().right < 0
