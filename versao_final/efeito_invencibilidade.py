from efeito import Efeito
from estado import Estado


class EfeitoInvencibilidade(Efeito):
    def __init__(self):
        super().__init__("lightgreen")
        self.set_nome("INVENCIBILIDADE")

    def efeito(self, estado: Estado) -> Estado:
        estado._invencibilidade = True
        return estado
