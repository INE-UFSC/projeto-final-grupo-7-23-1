import pygame
from abc import ABC, abstractmethod
from entidade import *
from estado import Estado

class Efeito(Entidade):
    def __init__(self, id, posicao, tamanho,cor,imagem):
        super().__init__(id, posicao, tamanho,cor,imagem)
        self.set_velocidade(pygame.Vector2(-300, 0))

    @abstractmethod
    def efeito(self, estado: Estado) -> Estado:
        pass
    
    def checkOver(self):
        return self.get_rect().right<0