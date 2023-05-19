from pygame import Vector2

from controlador import Controlador
from jogador import Jogador

if __name__ == '__main__':
    controlador = Controlador()
    controlador.add_entity(Jogador(0, Vector2(50, 50), Vector2(30, 30)))
    controlador.run()
