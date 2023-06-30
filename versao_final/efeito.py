import pygame
from abc import abstractmethod
from entidade import *
from estado import Estado

class Efeito(Entidade):
    def __init__(self, id, posicao, tamanho,cor,imagens):
        super().__init__(id, posicao, tamanho,cor,imagens)
        self.set_velocidade(pygame.Vector2(-300, 0))

    @abstractmethod
    def efeito(self, estado: Estado) -> Estado:
        pass

    def checkOver(self):
        return self.get_rect().right<0
