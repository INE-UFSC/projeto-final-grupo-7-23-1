from efeito import Efeito
from estado import Estado


class EfeitoDiminuirVelocidade(Efeito):
    def __init__(self):
        super().__init__("purple")
        self.set_nome("0.75X VELOCIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._velocidade *= 0.75
        return estado
