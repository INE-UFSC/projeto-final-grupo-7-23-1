from pygame import Vector2

from controlador import Controlador
from jogador import Jogador
from obstaculo import Obstaculo
import pygame

from efeito_gravidade_invertida import EfeitoGravidadeInvertida
from efeito_gravidade_baixa import EfeitoGravidadeBaixa
from efeito_diminuir_velocidade import EfeitoDiminuirVelocidade
from efeito_aumentar_velocidade import EfeitoAumentarVelocidade
from efeito_invencibilidade import EfeitoInvencibilidade

from background import Background
from constantes import *

# obstaculos terrestres

t_fino_baixo = Obstaculo(1, Vector2(1280, 516), Vector2(45, 60),"red",pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"))
t_fino_alto = Obstaculo(2, Vector2(1280, 466), Vector2(45, 110),"red",pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"))
t_largo_baixo = Obstaculo(3, Vector2(1280, 516), Vector2(90, 60),"red",pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"))
t_largo_alto = Obstaculo(4, Vector2(1280, 476), Vector2(90, 100),"red",pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"))

#obstaculos aereos
a_voo_baixo = Obstaculo(5, Vector2(1280, 476), Vector2(35, 40),"white",pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"))
a_voo_alto = Obstaculo(6, Vector2(1280, 426), Vector2(35, 40),"white",pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"))

#caixas efeitos
efeito_1 = EfeitoGravidadeInvertida(7, Vector2(1280, 400),Vector2(40,40),"blue",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
efeito_2 = EfeitoGravidadeBaixa(7, Vector2(1280, 400),Vector2(40,40),"lightblue",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
efeito_3 = EfeitoDiminuirVelocidade(7, Vector2(1280, 400),Vector2(40,40),"purple",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
efeito_4 = EfeitoAumentarVelocidade(7, Vector2(1280, 400),Vector2(40,40),"pink",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
efeito_5 = EfeitoInvencibilidade(7, Vector2(1280, 400),Vector2(40,40),"pink",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))

#backgrounds
background1= Background(1,Vector2(0,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',pygame.image.load(CAMINHO_ASSETS+"amazonia1.jpg"))
background2= Background(1,Vector2(0,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',pygame.image.load(CAMINHO_ASSETS+"amazonia2.jpg"))


if __name__ == '__main__':
    controlador = Controlador()
    controlador.add_background(background1)
    controlador.add_background(background2)

    controlador.add_obstaculo(t_fino_baixo)
    controlador.add_obstaculo(t_fino_alto)
    controlador.add_obstaculo(t_largo_baixo)
    controlador.add_obstaculo(t_largo_alto)
    controlador.add_obstaculo(a_voo_baixo)
    controlador.add_obstaculo(a_voo_alto)

    controlador.add_efeito(efeito_1)
    controlador.add_efeito(efeito_2)
    controlador.add_efeito(efeito_3)
    controlador.add_efeito(efeito_4)
    controlador.add_efeito(efeito_5)


    controlador.menu_inicial()
