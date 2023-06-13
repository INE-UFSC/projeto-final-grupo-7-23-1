import pygame
from abc import ABC, abstractmethod

from constantes import *

class Entidade(ABC):
    def __init__(self, id: int, posicao: pygame.Vector2, tamanho: pygame.Vector2, cor: str, imagem = None):
        self.__id = id
        self.__velocidade = pygame.Vector2(0, 0)
        self.__rect = pygame.Rect(posicao.x, posicao.y, tamanho.x, tamanho.y)
        self.__cor = cor
        self.__imagem = imagem
    
    def get_cor(self):
        return self.__cor

    def update(self, gravidade, dt, game_speed = 0):
        self.__velocidade.y += gravidade
        self.__rect.x += (self.__velocidade.x * dt) - game_speed
        self.__rect.y += self.__velocidade.y * dt
        if self.__rect.y > TELA_HEIGHT-CHAO-self.__rect.height:
            self.__rect.y = TELA_HEIGHT-CHAO-self.__rect.height
            self.__velocidade.y = 0
        if self.__rect.y < 0:
            self.__rect.y = 0
            self.__velocidade.y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.__cor, self.__rect)
        if self.__imagem is not None:
            surface.blit(self.__imagem, self.__rect)

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade
    def set_posicao_x(self, posicao_x):
        self.__rect.x = posicao_x
    def set_posicao_y(self, posicao_y):
        self.__rect.y = posicao_y
    def set_height(self, height):
        self.__rect.height = height
    
    def get_posicao(self):
        return pygame.Vector2(self.__rect.x, self.__rect.y)
    def get_tamanho(self):
        return pygame.Vector2(self.__rect.width, self.__rect.height)
    def get_rect(self):
        return self.__rect
