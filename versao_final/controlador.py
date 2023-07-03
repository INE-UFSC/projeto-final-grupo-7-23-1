import pygame
import random
import copy
import math

from estado import Estado
from entidade import Entidade

from jogador import Jogador
from obstaculo import Obstaculo
from efeito import Efeito
from background import Background
from inicializador import inicializador

from menus.controlador_menus import *

from constantes import *

class Controlador:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.__estado = Estado(GRAVIDADE, VELOCIDADE, 1, False)
        self.__estado_inical = Estado(GRAVIDADE, VELOCIDADE, 1, False)
        self.__jogador = Jogador()
        self.__obstaculos = []
        self.__obstaculos_ativos = []
        self.__tempo_efeito = 0
        self.__tempo_pontuacao = 0
        self.__efeitos = []
        self.__efeitos_ativos = []
        self.__efeito_desenhar = None
        self.__background = []
        self.__controlador_menus = ControladorMenus()
        inicializador(self, self.__estado._mapa)

    def add_obstaculo(self, obstaculo):
        self.__obstaculos.append(obstaculo)
    
    def add_efeito(self, efeito):
        self.__efeitos.append(efeito)
    
    def add_background(self, background):
        self.__background.append(background)

    def menu_run(self):
        self.__controlador_menus.menu_loop(self.__estado)
        self.__nome = self.__controlador_menus.get_menu_principal().get_nome()
        self.__jogador.set_imagens_levantado(self.__controlador_menus.get_menu_personagem().get_personagem()[0])
        self.__jogador.set_imagens_agachado(self.__controlador_menus.get_menu_personagem().get_personagem()[1])
        self.__jogador.set_imagens(self.__controlador_menus.get_menu_personagem().get_personagem()[0])
        self.run()

    def run(self):
        self.__estado._pontuacao = 0
        screen = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))
        clock = pygame.time.Clock()
        font = pygame.font.Font(CAMINHO_ASSETS + "font.ttf", 20)
        #mapa=1
        running = True
        dt = 0
        speed_mul = 1
        enable_switch = True
        self.__tempo_pontuacao = pygame.time.get_ticks()
        for imagem in self.__jogador.get_imagens():
            imagem.convert_alpha()

        while running:
            running = self.__update(screen, dt, font, self.__estado._velocidade*speed_mul)
            dt = clock.tick(FPS) / 1000
            if speed_mul < MAX_SPEED:
                speed_mul += ACELERACAO
            testepont=int(self.__estado._pontuacao)
            if testepont % 100 == 0 and testepont != 0 and enable_switch:
                enable_switch = False
                mapa = self.__estado._mapa + 1 if self.__estado._mapa < 3 else 1
                self.__estado.set_mapa(mapa)
                self.__estado_inical._mapa = self.__estado._mapa
                self.__obstaculos = []
                self.__efeitos = []
                self.__background = []
                inicializador(self, self.__estado._mapa)
            elif testepont % 105 == 0 and not enable_switch:
                enable_switch = True

        self.__estado.save_highscore(self.__nome)
        p = self.__estado._pontuacao
        self.reset()
        self.__estado._pontuacao = p
        self.__controlador_menus.set_menu_atual(self.__controlador_menus.get_menu_gameover())
        self.menu_run()

    def reset(self):
        self.__estado = copy.deepcopy(self.__estado_inical)
        self.__estado._mapa = 1
        self.__jogador = Jogador()
        self.__obstaculos = []
        self.__obstaculos_ativos = []
        self.__tempo_efeito = 0
        self.__efeitos = []
        self.__efeitos_ativos = []
        self.__efeito_desenhar = None
        self.__background = []
        inicializador(self, self.__estado._mapa)

    def __update(self, screen: pygame.Surface, dt: float, font: pygame.font.Font, game_speed: int) -> bool:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.__jogador.jump()
        elif keys[pygame.K_DOWN]:
            self.__jogador.pular_pra_baixo(self.__estado._gravidade)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_DOWN:
                    self.__jogador.agachar()
                elif event.key == pygame.K_DOWN:
                    self.__jogador.pular_pra_baixo(self.__estado._gravidade)
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                    self.__jogador.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__jogador.levantar()

        screen.fill("black")

        for background in self.__background:
            background.draw(screen)
            background.update(0, dt, game_speed)
            if background.checkOver():
                background.set_posicao_x(TELA_WIDTH)

        self.__jogador.draw(screen)
        for imagem in self.__jogador.get_imagens():
            imagem.set_alpha(255)

        if self.__estado._invencibilidade:
            for imagem in self.__jogador.get_imagens():
                imagem.set_alpha(123)
            self.__jogador.draw(screen)
        self.__jogador.update(self.__estado._gravidade, dt)

        if (len(self.__obstaculos_ativos) == 0 or
                (len(self.__obstaculos_ativos) == 1 and
                 self.__obstaculos_ativos[0].get_posicao().x <=
                 self.__obstaculos_ativos[0].get_random_x())
                and len(self.__obstaculos)) > 0:
            self.__obstaculos_ativos.append(random.choice(self.__obstaculos))

        if pygame.time.get_ticks() - self.__tempo_efeito >= 5000:
            p = self.__estado._pontuacao
            self.__estado = copy.deepcopy(self.__estado_inical)
            self.__estado._pontuacao = p
            self.__efeito_desenhar = None

        for obstaculo in self.__obstaculos_ativos:
            obstaculo.draw(screen)
            obstaculo.update(0, dt, game_speed)
            if obstaculo.checkOver():
                obstaculo.set_posicao_x(TELA_WIDTH)
                self.__obstaculos_ativos.pop(0)
                obstaculo.randomize_x()
            if self.__jogador.get_rect().colliderect(obstaculo.get_rect()):
                    obstaculo.set_posicao_x(TELA_WIDTH)
                    self.__obstaculos_ativos.pop(0)
                    if not self.__estado._invencibilidade :
                        screen.fill("red")
                        return False

        if len(self.__efeitos_ativos) == 0 and len(self.__efeitos) > 0:
            self.__efeitos_ativos.append(random.choice(self.__efeitos))

        for efeito in self.__efeitos_ativos:
            efeito.draw(screen)
            efeito.update(0, dt, game_speed)
            random_x = random.randint(TELA_WIDTH*3, TELA_WIDTH*8)
            random_y = int(random.choice([TELA_HEIGHT-CHAO-efeito.get_tamanho().y,
                                      TELA_HEIGHT-CHAO-efeito.get_tamanho().y*1.5,
                                      TELA_HEIGHT-CHAO-efeito.get_tamanho().y*2,
                                      TELA_HEIGHT-CHAO-efeito.get_tamanho().y*2.5,
                                      TELA_HEIGHT-CHAO-efeito.get_tamanho().y*3]))
            if efeito.checkOver():
                efeito.set_posicao_x(random_x)
                efeito.set_posicao_y(random_y)
                self.__efeitos_ativos.pop()
            if self.__jogador.get_rect().colliderect(efeito.get_rect()):
                efeito.set_posicao_x(random_x)
                efeito.set_posicao_y(random_y)
                self.__tempo_efeito = pygame.time.get_ticks()
                p = self.__estado._pontuacao
                self.__estado = copy.deepcopy(self.__estado_inical)
                self.__estado._pontuacao = p
                self.__estado = efeito.efeito(self.__estado)
                self.__efeito_desenhar = efeito
                self.__efeitos_ativos.pop()
                screen.fill("blue")

        if self.__efeito_desenhar is not None:
            nome_efeito = self.__efeito_desenhar.get_nome()
            tempo_restante = (5000 - (pygame.time.get_ticks() - self.__tempo_efeito)) / 1000
            text = "{}    {:.2f}s" .format(nome_efeito, tempo_restante)
            text_surface = font.render(text, True, "yellow")
            text_rect = text_surface.get_rect()
            text_rect.center = (520, 40)
            screen.blit(text_surface, text_rect)

        print(f'1: {self.__estado._pontuacao}')
        self.__estado.gerar_pontuacao(self.__tempo_pontuacao)
        print(f'2: {self.__estado._pontuacao}')
        score_text = font.render(f"PONTUAÇÃO {int(self.__estado._pontuacao)}", True, "yellow")
        screen.blit(score_text, (TELA_WIDTH-380, 30))

        pygame.display.flip()

        return True
