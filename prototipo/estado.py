import pygame

class Estado:
    def __init__(self,gravidade,velocidade,mapa,pontuacao=0):
        self._gravidade = gravidade
        self._velocidade = velocidade
        self._mapa = mapa
        self.__pontuacao = pontuacao
    def gerar_pontuacao(self):
        self.__pontuacao = pygame.time.get_ticks()/100