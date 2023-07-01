from efeito import Efeito
from estado import Estado


class EfeitoGravidadeBaixa(Efeito):
    def __init__(self, posicao, tamanho,cor,imagem):
        super().__init__(posicao, tamanho,cor,imagem)

    def efeito(self, estado: Estado) -> Estado:
        estado._gravidade *= 0.5
        return estado
