from entidade import *

class Obstaculo(Entidade):
    def __init__(self, id, posicao, tamanho):
        super.__init__(id, posicao, tamanho)
    
    def checkOver(self):
        if self.__posicao.x < 0:
            return True
        else:
            return False