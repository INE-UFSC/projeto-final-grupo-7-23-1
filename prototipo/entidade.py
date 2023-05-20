import pygame
from abc import ABC, abstractmethod

from constantes import *

class Entidade(ABC):
    def __init__(self, id: int, posicao: pygame.Vector2, tamanho: pygame.Vector2):
        self.__id = id
        self.__posicao = posicao
        self.__tamanho = tamanho
        self.__velocidade = pygame.Vector2(0, 0)

    def update(self, gravidade, dt):
        self.__velocidade.y += gravidade
        self.__posicao += self.__velocidade * dt
        if self.__posicao.y > TELA_HEIGHT-CHAO-self.__tamanho.y:
            self.__posicao.y = TELA_HEIGHT-CHAO-self.__tamanho.y
            self.__velocidade.y = 0
        self.__rect = pygame.Rect(self.__posicao.x, self.__posicao.y, self.__tamanho.x, self.__tamanho.y)

    def draw(self, surface):
        pygame.draw.rect(surface, "white", [self.__posicao.x, self.__posicao.y, self.__tamanho.x, self.__tamanho.y])

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade
    def set_posicao_x(self, posicao_x):
        self.__posicao.x = posicao_x
    
    def get_posicao(self):
        return self.__posicao
    def get_tamanho(self):
        return self.__tamanho
    def get_rect(self):
        return self.__rect