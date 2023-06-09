from pygame import Vector2

from entidade import *
from constantes import *

class Jogador(Entidade):
    def __init__(self, id, posicao, tamanho):
        super().__init__(id, posicao, tamanho)
        self.__altura_inicial = tamanho.y

    def jump(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_velocidade(Vector2(0, JUMP_FORCE))

    def agachar(self):
        self.set_height(self.__altura_inicial/2)
        self.set_posicao_y(self.get_posicao().y + self.__altura_inicial/2)

    def levantar(self):
        self.set_height(self.__altura_inicial)
        self.set_posicao_y(self.get_posicao().y - self.__altura_inicial/2)
