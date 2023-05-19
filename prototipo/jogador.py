from pygame import Vector2

from entidade import *

JUMP_FORCE = -300

class Jogador(Entidade):
    def __init__(self, id, posicao, tamanho):
        super().__init__(id, posicao, tamanho)

    def jump(self):
        self.set_velocidade(Vector2(0, JUMP_FORCE))
