from efeito import Efeito
from estado import Estado


class EfeitoGravidadeBaixa(Efeito):
    def __init__(self, posicao, tamanho,cor,imagem):
        super().__init__(posicao, tamanho,cor,imagem)
        self.set_nome("0.5X GRAVIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._gravidade *= 0.5
        return estado
