from pygame import Vector2

from entidade import *
from constantes import *

class Jogador(Entidade):
    def __init__(self):
        self.__altura_inicial = 100
        super().__init__(pygame.Vector2(50, 476), pygame.Vector2(50, self.__altura_inicial), "white", [])
        self.__imagens_levantado = []
        self.__imagens_agachado = []

    def jump(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_velocidade(Vector2(0, JUMP_FORCE))
        elif self.get_posicao().y <= 0:
            self.set_velocidade(Vector2(0, -JUMP_FORCE))

    def agachar(self):
        if self.get_posicao().y >= TELA_HEIGHT-CHAO-self.get_tamanho().y:
            self.set_height(self.__altura_inicial/2)
            self.set_posicao_y(self.get_posicao().y + self.__altura_inicial/2)
            if self.get_imagens() != self.__imagens_agachado:
                self.set_imagens(self.__imagens_agachado)
        elif self.get_posicao().y <= 0:
            self.set_height(self.__altura_inicial/2)
            if self.get_imagens() != self.__imagens_agachado:
                self.set_imagens(self.__imagens_agachado)

    def pular_pra_baixo(self, gravidade):
        if self.get_posicao().y < TELA_HEIGHT-CHAO-self.get_tamanho().y and gravidade > 0:
            self.set_velocidade(Vector2(0, -JUMP_FORCE))
        elif self.get_posicao().y > 0 and gravidade < 0:
            self.set_velocidade(Vector2(0, JUMP_FORCE))

    def levantar(self):
        if self.get_tamanho().y < self.__altura_inicial:
            self.set_height(self.__altura_inicial)
            self.set_posicao_y(self.get_posicao().y - self.__altura_inicial/2)
            if self.get_imagens() != self.__imagens_levantado:
                self.set_imagens(self.__imagens_levantado)

    def set_imagens_levantado(self, imagens_levantado):
        self.__imagens_levantado = imagens_levantado

    def set_imagens_agachado(self, imagens_agachado):
        self.__imagens_agachado = imagens_agachado
