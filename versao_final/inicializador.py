from pygame import Vector2

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

class inicializador:

#fazes
    def __init__(self,controlador,mapa):
        self.__dictBackgrounds = {
            1 : [pygame.image.load(CAMINHO_ASSETS+"amazonia1.jpg"),pygame.image.load(CAMINHO_ASSETS+"amazonia2.jpg")],
            2 : [pygame.image.load(CAMINHO_ASSETS+"testetransbg.jpg"),pygame.image.load(CAMINHO_ASSETS+"testetransbg.jpg")]
            }
        self.__dictInimigo ={
            1: (pygame.image.load(CAMINHO_ASSETS+"crocodilo.jpg"),),
            2: (pygame.image.load(CAMINHO_ASSETS+"testetransbg.jpg"),)
        }
        self.add_controlador(controlador,mapa)
    # obstaculos terrestres

    def sel_imagens(self,mapa):
        self.t_fino_baixo = Obstaculo(1, Vector2(1280, 516), Vector2(45, 60),self.__dictInimigo[mapa][0])
        self.t_fino_alto = Obstaculo(2, Vector2(1280, 466), Vector2(45, 110),self.__dictInimigo[mapa][0])
        self.t_largo_baixo = Obstaculo(3, Vector2(1280, 516), Vector2(90, 60),self.__dictInimigo[mapa][0])
        self.t_largo_alto = Obstaculo(4, Vector2(1280, 476), Vector2(90, 100),self.__dictInimigo[mapa][0])

        #obstaculos aereos
        self.a_voo_baixo = Obstaculo(5, Vector2(1280, 476), Vector2(35, 40),self.__dictInimigo[mapa][0])
        self.a_voo_alto = Obstaculo(6, Vector2(1280, 426), Vector2(35, 40),self.__dictInimigo[mapa][0])

        #caixas efeitos
        self.efeito_1 = EfeitoGravidadeInvertida(7, Vector2(1280, 400),Vector2(40,40),"blue",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
        self.efeito_2 = EfeitoGravidadeBaixa(7, Vector2(1280, 400),Vector2(40,40),"lightblue",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
        self.efeito_3 = EfeitoDiminuirVelocidade(7, Vector2(1280, 400),Vector2(40,40),"purple",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
        self.efeito_4 = EfeitoAumentarVelocidade(7, Vector2(1280, 400),Vector2(40,40),"pink",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))
        self.efeito_5 = EfeitoInvencibilidade(7, Vector2(1280, 400),Vector2(40,40),"pink",pygame.image.load(CAMINHO_ASSETS+"powerup.png"))

        #backgrounds
        self.background1= Background(1,Vector2(0,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',self.__dictBackgrounds[mapa][0])
        self.background2= Background(1,Vector2(0,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',self.__dictBackgrounds[mapa][1])


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

        controlador.add_efeito(self.efeito_1)
        controlador.add_efeito(self.efeito_2)
        controlador.add_efeito(self.efeito_3)
        controlador.add_efeito(self.efeito_4)
        controlador.add_efeito(self.efeito_5)