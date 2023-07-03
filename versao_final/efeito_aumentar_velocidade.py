from efeito import Efeito
from estado import Estado


class EfeitoAumentarVelocidade(Efeito):
    def __init__(self):
        super().__init__("pink")
        self.set_nome("1.5X VELOCIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._velocidade *= 1.5
        return estado
