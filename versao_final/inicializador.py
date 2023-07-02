from pygame import Vector2

from obstaculo import Obstaculo
import pygame

from efeito_gravidade_invertida import EfeitoGravidadeInvertida
from efeito_gravidade_baixa import EfeitoGravidadeBaixa
from efeito_diminuir_velocidade import EfeitoDiminuirVelocidade
from efeito_aumentar_velocidade import EfeitoAumentarVelocidade
from efeito_invencibilidade import EfeitoInvencibilidade

from background import Background
from constantes import *
from obstaculo_arara import Arara

class inicializador:

#fazes
    def __init__(self,controlador,mapa):
        self.__dictBackgrounds = {
            1 : [pygame.image.load(CAMINHO_ASSETS+"amazonia1.jpg"),pygame.image.load(CAMINHO_ASSETS+"amazonia2.jpg")],
            2 : [pygame.image.load(CAMINHO_ASSETS+"testetransbg.jpg"),pygame.image.load(CAMINHO_ASSETS+"testetransbg.jpg")],
            3 : [pygame.image.load(CAMINHO_ASSETS+"foresttest.png"), pygame.image.load(CAMINHO_ASSETS+"foresttest.png")]
            }
        self.__dictInimigo ={
            1: [pygame.image.load(CAMINHO_ASSETS+"jacare1.png"), pygame.image.load(CAMINHO_ASSETS+"jacare2.png")],
            2: [pygame.image.load(CAMINHO_ASSETS+"testetransbg.jpg")],
            3: [pygame.image.load(CAMINHO_ASSETS+"foresttest.png")]
        }
        self.add_controlador(controlador,mapa)
    # obstaculos terrestres

    def sel_imagens(self,mapa):
        self.t_fino_baixo = Obstaculo(Vector2(1280, 516), Vector2(45, 60),self.__dictInimigo[mapa])
        self.t_fino_alto = Obstaculo(Vector2(1280, 466), Vector2(45, 110),self.__dictInimigo[mapa])
        self.t_largo_baixo = Obstaculo(Vector2(1280, 516), Vector2(90, 60),self.__dictInimigo[mapa])
        self.t_largo_alto = Obstaculo(Vector2(1280, 476), Vector2(90, 100),self.__dictInimigo[mapa])

        #obstaculos aereos
        self.a_voo_baixo = Obstaculo(Vector2(1280, 476), Vector2(35, 40),self.__dictInimigo[mapa])
        self.arara = Arara()
        self.a_voo_alto = Obstaculo(Vector2(1280, 426), Vector2(35, 40),self.__dictInimigo[mapa])

        #caixas efeitos
        imagens_efeitos = [
            pygame.image.load(CAMINHO_ASSETS+"box1.png"),
            pygame.image.load(CAMINHO_ASSETS+"box2.png"),
            pygame.image.load(CAMINHO_ASSETS+"box3.png"),
            pygame.image.load(CAMINHO_ASSETS+"box4.png")
        ]
        self.efeito_1 = EfeitoGravidadeInvertida(Vector2(1280, 400),Vector2(40,40),"blue",imagens_efeitos)
        self.efeito_2 = EfeitoGravidadeBaixa(Vector2(1280, 400),Vector2(40,40),"lightblue",imagens_efeitos)
        self.efeito_3 = EfeitoDiminuirVelocidade(Vector2(1280, 400),Vector2(40,40),"purple",imagens_efeitos)
        self.efeito_4 = EfeitoAumentarVelocidade(Vector2(1280, 400),Vector2(40,40),"pink",imagens_efeitos)
        self.efeito_5 = EfeitoInvencibilidade(Vector2(1280, 400),Vector2(40,40),"pink",imagens_efeitos)

        #backgrounds
        self.background1= Background(Vector2(0,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',[self.__dictBackgrounds[mapa][0]])
        self.background2= Background(Vector2(TELA_WIDTH,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',[self.__dictBackgrounds[mapa][1]])


    def add_controlador(self,controlador,mapa):
        self.sel_imagens(mapa)
        controlador.add_background(self.background1)
        controlador.add_background(self.background2)

        controlador.add_obstaculo(self.t_fino_baixo)
        controlador.add_obstaculo(self.t_fino_alto)
        controlador.add_obstaculo(self.t_largo_baixo)
        controlador.add_obstaculo(self.t_largo_alto)
        controlador.add_obstaculo(self.a_voo_baixo)
        controlador.add_obstaculo(self.a_voo_alto)
        controlador.add_obstaculo(self.arara)

        controlador.add_efeito(self.efeito_1)
        controlador.add_efeito(self.efeito_2)
        controlador.add_efeito(self.efeito_3)
        controlador.add_efeito(self.efeito_4)
        controlador.add_efeito(self.efeito_5)
