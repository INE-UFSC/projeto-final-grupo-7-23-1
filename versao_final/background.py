import pygame
from entidade import *
from constantes import TELA_WIDTH

class Background(Entidade):
    def __init__(self, id, posicao, tamanho,cor, imagem):
        super().__init__(id, posicao, tamanho,cor,imagem)
        self.set_velocidade(pygame.Vector2(-100, 0))
        self.__random_x = TELA_WIDTH
    
    def checkLeft(self):
        return self.get_rect().left <= 0
    def checkOver(self):
        return self.get_rect().right < 0
    def randomize_x(self):
        self.__random_x = TELA_WIDTH
    
    def get_random_x(self):
        return self.__random_x