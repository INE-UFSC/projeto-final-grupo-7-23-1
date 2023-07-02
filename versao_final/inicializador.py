from pygame import Vector2

import pygame

from efeito_gravidade_invertida import EfeitoGravidadeInvertida
from efeito_gravidade_baixa import EfeitoGravidadeBaixa
from efeito_diminuir_velocidade import EfeitoDiminuirVelocidade
from efeito_aumentar_velocidade import EfeitoAumentarVelocidade
from efeito_invencibilidade import EfeitoInvencibilidade

from background import Background
from constantes import *
from obstaculo_arara import Arara
from obstaculo_jacare import Jacare

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
        self.jacare = Jacare()

        #obstaculos aereos
        self.arara = Arara()

        #caixas efeitos
        self.efeitos = [
            EfeitoGravidadeInvertida(),
            EfeitoGravidadeBaixa(),
            EfeitoDiminuirVelocidade(),
            EfeitoAumentarVelocidade(),
            EfeitoInvencibilidade()
        ]

        #backgrounds
        self.background1= Background(Vector2(0,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',[self.__dictBackgrounds[mapa][0]])
        self.background2= Background(Vector2(TELA_WIDTH,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',[self.__dictBackgrounds[mapa][1]])


    def add_controlador(self,controlador,mapa):
        self.sel_imagens(mapa)
        controlador.add_background(self.background1)
        controlador.add_background(self.background2)

        controlador.add_obstaculo(self.arara)
        controlador.add_obstaculo(self.jacare)

        for efeito in self.efeitos:
            controlador.add_efeito(efeito)
