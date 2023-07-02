from efeito import Efeito
from estado import Estado


class EfeitoInvencibilidade(Efeito):
    def __init__(self, posicao, tamanho,cor,imagem):
        super().__init__(posicao, tamanho,cor,imagem)
        self.set_nome("INVENCIBILIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._invencibilidade = True
        return estado
