from efeito import Efeito
from estado import Estado


class EfeitoGravidade(Efeito):
    def __init__(self, id, posicao, tamanho,cor):
        super().__init__(id, posicao, tamanho,cor)

    def efeito(self, estado: Estado) -> Estado:
        estado._gravidade *= -1
        return estado