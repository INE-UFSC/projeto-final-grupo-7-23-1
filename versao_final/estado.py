import os
import json

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
    
    def set_mapa(self,mapa):
        self._mapa = mapa

    def save_highscore(self, nome) -> bool:
        print(f'Saving current score: {self._pontuacao}')
        nome = nome.strip()
        try:
            #if self._pontuacao <= self.load_highscore(): return False
            scores = self.load_highscores()
            if nome in scores and self._pontuacao <= scores[nome]: return False
            scores[nome] = self._pontuacao

            os.makedirs(os.path.dirname(CAMINHO_SCORES), exist_ok=True)
            with open(CAMINHO_SCORES,"w") as f:
                json.dump(json.dumps(scores), f)
                return True
        except Exception:
            return False

    def load_highscores(self) -> dict:
        try:
            with open(CAMINHO_SCORES,"r") as f:
                return json.loads(json.load(f))
        except Exception:
            return {}
