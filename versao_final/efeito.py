import pygame
from abc import abstractmethod
from entidade import *
from estado import Estado

class Efeito(Entidade):
    def __init__(self, posicao, tamanho,cor,imagens):
        super().__init__(posicao, tamanho,cor,imagens)
        self.__nome = ""
        self.set_velocidade(pygame.Vector2(-300, 0))

    @abstractmethod
    def efeito(self, estado: Estado) -> Estado:
        pass

    def checkOver(self):
        return self.get_rect().right<0
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
