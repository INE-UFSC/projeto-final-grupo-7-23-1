from efeito import Efeito
from estado import Estado


class EfeitoGravidadeBaixa(Efeito):
    def __init__(self):
        super().__init__("lightblue")
        self.set_nome("0.5X GRAVIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._gravidade *= 0.5
        return estado
