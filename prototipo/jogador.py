from pygame import Vector2

from entidade import *
from constantes import *

class Jogador(Entidade):
    def __init__(self, id, posicao, tamanho):
        super().__init__(id, posicao, tamanho)

    def jump(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_velocidade(Vector2(0, JUMP_FORCE))
