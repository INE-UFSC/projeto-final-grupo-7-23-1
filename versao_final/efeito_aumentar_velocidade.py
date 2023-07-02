from efeito import Efeito
from estado import Estado


class EfeitoAumentarVelocidade(Efeito):
    def __init__(self, posicao, tamanho,cor,imagem):
        super().__init__(posicao, tamanho,cor,imagem)
        self.set_nome("1.5X VELOCIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._velocidade *= 2
        return estado
