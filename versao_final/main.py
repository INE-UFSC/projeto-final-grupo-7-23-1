from pygame import Vector2

from controlador import Controlador
from jogador import Jogador
from obstaculo import Obstaculo
from efeito import Efeito

# obstaculos terrestres
t_fino_baixo = Obstaculo(1, Vector2(1280, 516), Vector2(45, 60),"red")
t_fino_alto = Obstaculo(2, Vector2(1280, 466), Vector2(45, 110),"red")
t_largo_baixo = Obstaculo(3, Vector2(1280, 516), Vector2(90, 60),"red")
t_largo_alto = Obstaculo(4, Vector2(1280, 476), Vector2(90, 100),"red")

#obstaculos aereos
a_voo_baixo = Obstaculo(5, Vector2(1280, 476), Vector2(35, 40),"white")
a_voo_alto = Obstaculo(6, Vector2(1280, 426), Vector2(35, 40),"white")

#caixas efeitos
efeito_1 = Efeito(7, Vector2(1280, 400),Vector2(40,40),"blue")


if __name__ == '__main__':
    controlador = Controlador()
    controlador.add_obstaculo(t_fino_baixo)
    controlador.add_obstaculo(t_fino_alto)
    controlador.add_obstaculo(t_largo_baixo)
    controlador.add_obstaculo(t_largo_alto)
    controlador.add_obstaculo(a_voo_baixo)
    controlador.add_obstaculo(a_voo_alto)
    controlador.add_obstaculo(efeito_1)
    controlador.run()
