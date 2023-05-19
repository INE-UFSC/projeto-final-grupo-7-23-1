import pygame
from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, id: int, posicao: pygame.Vector2, tamanho: pygame.Vector2):
        self.__id = id
        self.__posicao = posicao
        self.__tamanho = tamanho
        self.__velocidade = pygame.Vector2(0, 0)

    def update(self, gravidade, dt):
        self.__velocidade.y += gravidade
        self.__posicao += self.__velocidade * dt

    def draw(self, surface):
        pygame.draw.rect(surface, "white", [self.__posicao.x, self.__posicao.y, self.__tamanho.x, self.__tamanho.y])
