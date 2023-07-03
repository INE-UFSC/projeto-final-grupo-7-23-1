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
from obstaculo_carrovermelho import CarroVermelho
from obstaculo_carroazul import CarroAzul
from obstaculo_caranguejo import Caranguejo
from obstaculo_gaivota import Gaivota
from obstaculo_capivara import Capivara

class inicializador:

#fazes
    def __init__(self,controlador,mapa):
        self.jacare = Jacare()
        self.arara = Arara()
        self.carro_vermelho = CarroVermelho()
        self.carro_azul = CarroAzul()
        self.caranguejo = Caranguejo()
        self.gaivota = Gaivota()
        self.capivara = Capivara()
        self.__dictBackgrounds = {
            1 : [pygame.image.load(CAMINHO_ASSETS+"floresta.png")],
            2 : [pygame.image.load(CAMINHO_ASSETS+"praia.png")],
            3 : [pygame.image.load(CAMINHO_ASSETS+"rj.png")]
            }
        self.__dictInimigo ={
            1: [self.jacare, self.arara, self.capivara],
            2: [self.caranguejo, self.gaivota],
            3: [self.carro_vermelho, self.carro_azul]
        }
        self.add_controlador(controlador,mapa)

    def sel_imagens(self,mapa):

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
        self.background2= Background(Vector2(TELA_WIDTH,TELA_HEIGHT-CHAO),Vector2(TELA_WIDTH,TELA_HEIGHT),'black',[self.__dictBackgrounds[mapa][0]])


    def add_controlador(self,controlador,mapa):
        self.sel_imagens(mapa)
        controlador.add_background(self.background1)
        controlador.add_background(self.background2)

        for obstaculo in self.__dictInimigo[mapa]:
            controlador.add_obstaculo(obstaculo)

        for efeito in self.efeitos:
            controlador.add_efeito(efeito)
