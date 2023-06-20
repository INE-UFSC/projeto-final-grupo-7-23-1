import pygame

class Estado:
    def __init__(self,gravidade,velocidade,mapa,invencibilidade: bool,pontuacao=0):
        self._gravidade = gravidade
        self._velocidade = velocidade
        self._mapa = mapa
        self._invencibilidade = invencibilidade
        self._pontuacao = pontuacao
    def gerar_pontuacao(self, tempo_inicial):
        self._pontuacao = (pygame.time.get_ticks()-tempo_inicial)/100