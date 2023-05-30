from pygame import Vector2

from controlador import Controlador
from jogador import Jogador
from obstaculo import Obstaculo

# obstaculos terrestres
t_fino_baixo = Obstaculo(1, Vector2(1280, 516), Vector2(45, 60))
t_fino_alto = Obstaculo(2, Vector2(1280, 466), Vector2(45, 110))
t_largo_baixo = Obstaculo(3, Vector2(1280, 516), Vector2(90, 60))
t_largo_alto = Obstaculo(4, Vector2(1280, 476), Vector2(90, 100))

#obstaculos aereos
a_voo_baixo = Obstaculo(5, Vector2(1280, 476), Vector2(35, 40))
a_voo_alto = Obstaculo(6, Vector2(1280, 426), Vector2(35, 40))


if __name__ == '__main__':
    controlador = Controlador()
    controlador.add_obstaculo(t_fino_baixo)
    controlador.add_obstaculo(t_fino_alto)
    controlador.add_obstaculo(t_largo_baixo)
    controlador.add_obstaculo(t_largo_alto)
    controlador.add_obstaculo(a_voo_baixo)
    controlador.add_obstaculo(a_voo_alto)
    controlador.run()
