import pygame
from pygame import Vector2

from abc import abstractmethod
from entidade import *
from estado import Estado

class Efeito(Entidade):
    IMAGENS = [
        pygame.image.load(CAMINHO_ASSETS+"box1.png"),
        pygame.image.load(CAMINHO_ASSETS+"box2.png"),
        pygame.image.load(CAMINHO_ASSETS+"box3.png"),
        pygame.image.load(CAMINHO_ASSETS+"box4.png")
    ]

    def __init__(self, cor):
        super().__init__(Vector2(TELA_WIDTH * 2, 400),Vector2(40,40), cor, Efeito.IMAGENS)
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
