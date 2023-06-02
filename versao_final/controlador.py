import pygame
import random

from estado import Estado
from entidade import Entidade

from jogador import Jogador
from obstaculo import Obstaculo
from efeito import Efeito

from constantes import *

class Controlador:
    def __init__(self):
        self.__estado = Estado(GRAVIDADE, VELOCIDADE, 1)
        self.__jogador = Jogador(0, pygame.Vector2(50, 476), pygame.Vector2(50, 100), "white")
        self.__obstaculos = []
        self.__obstaculos_ativos = []

    def add_obstaculo(self, obstaculo):
        self.__obstaculos.append(obstaculo)

    def run(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))
        clock = pygame.time.Clock()

        running = True
        dt = 0

        while running:
            running = self.__update(screen, dt)
            dt = clock.tick(FPS) / 1000

        pygame.quit()

    def __update(self, screen: pygame.Surface, dt: float) -> bool:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.__jogador.jump()
        elif keys[pygame.K_DOWN]:
            self.__jogador.pular_pra_baixo(self.__estado._gravidade)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

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

        self.__jogador.draw(screen)
        self.__jogador.update(self.__estado._gravidade, dt)

        if len(self.__obstaculos_ativos) == 0:
            self.__obstaculos_ativos.append(random.choice(self.__obstaculos))

        for obstaculo in self.__obstaculos_ativos:
            obstaculo.draw(screen)
            obstaculo.update(0, dt)
            if obstaculo.checkOver():
                obstaculo.set_posicao_x(TELA_WIDTH)
                self.__obstaculos_ativos.pop()
            if self.__jogador.get_rect().colliderect(obstaculo.get_rect()):
                if isinstance(obstaculo, Obstaculo):
                    obstaculo.set_posicao_x(TELA_WIDTH)
                    self.__obstaculos_ativos.pop()
                    screen.fill("red")
                elif isinstance(obstaculo,Efeito):
                    obstaculo.set_posicao_x(TELA_WIDTH)
                    self.__estado = obstaculo.efeito(self.__estado)
                    self.__obstaculos_ativos.pop()
                    screen.fill("blue")

        pygame.draw.rect(screen,"white",[0,TELA_HEIGHT-CHAO,TELA_WIDTH,CHAO])

        font = pygame.font.Font(None, 30)
        self.__estado.gerar_pontuacao()
        score_text = font.render(f"Pontuação: {int(self.__estado._pontuacao)}", True, "yellow")
        screen.blit(score_text, (TELA_WIDTH-TELA_WIDTH/7, 10))

        pygame.display.flip()

        return True
