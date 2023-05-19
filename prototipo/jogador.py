from entidade import *

class Jogador(Entidade):
    def __init__(self, id, posicao, tamanho):
        super.__init__(id, posicao, tamanho)
        self.__velocidade = pygame.Vector2(0, 0)

    def jump(self):
        if self.__posicao.y == 0:
            self.__velocidade.y = 300