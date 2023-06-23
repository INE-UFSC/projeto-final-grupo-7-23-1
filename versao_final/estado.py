import os

import pygame

from constantes import *

class Estado:
    def __init__(self,gravidade,velocidade,mapa,invencibilidade: bool,pontuacao=0):
        self._gravidade = gravidade
        self._velocidade = velocidade
        self._mapa = mapa
        self._invencibilidade = invencibilidade
        self._pontuacao = pontuacao
    def gerar_pontuacao(self, tempo_inicial):
        self._pontuacao = (pygame.time.get_ticks()-tempo_inicial)/100

    def save_highscore(self) -> bool:
        if self._pontuacao <= self.load_highscore(): return False

        os.makedirs(os.path.dirname(CAMINHO_SCORES), exist_ok=True)
        with open(CAMINHO_SCORES,"w") as f:
            f.write(f'{self._pontuacao}')
            return True

    def load_highscore(self) -> float:
        try:
            with open(CAMINHO_SCORES,"r") as f:
                return float(f.readline())
        except (FileNotFoundError, ValueError) as _:
            return 0.0
