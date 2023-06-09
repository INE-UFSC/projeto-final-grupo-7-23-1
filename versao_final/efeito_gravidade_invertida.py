from efeito import Efeito
from estado import Estado


class EfeitoGravidadeInvertida(Efeito):
    def __init__(self):
        super().__init__("blue")
        self.set_nome("GRAVIDADE INVERTIDA")

    def efeito(self, estado: Estado) -> Estado:
        estado._gravidade *= -1
        return estado
