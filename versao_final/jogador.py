from pygame import Vector2

from entidade import *
from constantes import *

class Jogador(Entidade):
    def __init__(self, id, posicao, tamanho,cor):
        super().__init__(id, posicao, tamanho, cor)
        self.__altura_inicial = tamanho.y

    def jump(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_velocidade(Vector2(0, JUMP_FORCE))

    def agachar(self):
        self.set_height(self.__altura_inicial/2)
        self.set_posicao_y(self.get_posicao().y + self.__altura_inicial/2)

    def pular_pra_baixo(self):
        if self.get_posicao().y < TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_velocidade(Vector2(0, -JUMP_FORCE))

    def levantar(self):
        if self.get_tamanho().y < self.__altura_inicial:
            self.set_height(self.__altura_inicial)
            self.set_posicao_y(self.get_posicao().y - self.__altura_inicial/2)
