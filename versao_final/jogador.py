from pygame import Vector2

from entidade import *
from constantes import *

class Jogador(Entidade):
    def __init__(self):
        self.__altura_inicial = 100
        super().__init__(pygame.Vector2(50, 476), pygame.Vector2(50, self.__altura_inicial), "white", [])

    def jump(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_velocidade(Vector2(0, JUMP_FORCE))
        elif self.get_posicao().y <= 0:
            self.set_velocidade(Vector2(0, -JUMP_FORCE))

    def agachar(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_height(self.__altura_inicial/2)
            self.set_posicao_y(self.get_posicao().y + self.__altura_inicial/2)
        elif self.get_posicao().y <= 0:
            self.set_height(self.__altura_inicial/2)

    def pular_pra_baixo(self, gravidade):
        if self.get_posicao().y < TELA_HEIGHT-CHAO-self.get_tamanho().y and gravidade > 0:
            self.set_velocidade(Vector2(0, -JUMP_FORCE))
        elif self.get_posicao().y > 0 and gravidade < 0:
            self.set_velocidade(Vector2(0, JUMP_FORCE))

    def levantar(self):
        if self.get_tamanho().y < self.__altura_inicial:
            self.set_height(self.__altura_inicial)
            self.set_posicao_y(self.get_posicao().y - self.__altura_inicial/2)

