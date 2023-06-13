import pygame
import random
import copy

from estado import Estado
from entidade import Entidade

from jogador import Jogador
from obstaculo import Obstaculo
from efeito import Efeito

from constantes import *

class Controlador:
    def __init__(self):
        self.__estado = Estado(GRAVIDADE, VELOCIDADE, 1)
        self.__estado_inical = Estado(GRAVIDADE, VELOCIDADE, 1)
        self.__jogador = Jogador(0, pygame.Vector2(50, 476), pygame.Vector2(50, 100), "white",pygame.image.load("versao_final/Assets/crocodilo.jpg"))
        self.__obstaculos = []
        self.__obstaculos_ativos = []
        self.__tempo_efeito = 0
        self.__tempo_pontuação = 0
        self.__efeitos = []
        self.__efeitos_ativos = []

    def add_obstaculo(self, obstaculo):
        self.__obstaculos.append(obstaculo)
    
    def add_efeito(self, efeito):
        self.__efeitos.append(efeito)

    def run(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 30)
        sair= False
        running = True
        dt = 0
        speed_mul = 1

        while running:
            running = self.__update(screen, dt, font, self.__estado._velocidade*speed_mul)
            dt = clock.tick(FPS) / 1000
            if speed_mul < MAX_SPEED: #velocidade maxima de 13 é atingida por volta de 2100 pontos
                speed_mul += ACELERACAO
        self.show_go_screen()
        
    def show_go_screen(self):
            font = pygame.font.Font(None, 30)
            screen = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))
            text_surface = font.render("Pressione espaço para jogar novamente", True, "white")
            screen.blit(text_surface, (TELA_WIDTH / 2, TELA_HEIGHT * 7 / 8))
            pygame.display.flip()
            self.__tempo_pontuação = pygame.time.get_ticks()
            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        return False
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                done = True
                                self.run()
                                self.__estado = self.__estado_inical
                                self.__jogador = Jogador(0, pygame.Vector2(50, 476), pygame.Vector2(50, 100), "white",pygame.image.load("versao_final/Assets/crocodilo.jpg"))

    def __update(self, screen: pygame.Surface, dt: float, font: pygame.font.Font, game_speed: int) -> bool:
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

        if len(self.__obstaculos_ativos) == 0 and len(self.__obstaculos) >0:
            self.__obstaculos_ativos.append(random.choice(self.__obstaculos))

        if pygame.time.get_ticks() - self.__tempo_efeito >= 5000:
            self.__estado = copy.deepcopy(self.__estado_inical)

        for obstaculo in self.__obstaculos_ativos:
            obstaculo.draw(screen)
            obstaculo.update(0, dt, game_speed)
            if obstaculo.checkOver():
                obstaculo.set_posicao_x(TELA_WIDTH)
                self.__obstaculos_ativos.pop()
            if self.__jogador.get_rect().colliderect(obstaculo.get_rect()):

                obstaculo.set_posicao_x(TELA_WIDTH)
                self.__obstaculos_ativos.pop()
                screen.fill("red")
                return False
                
        
        if len(self.__efeitos_ativos) == 0 and len(self.__efeitos) >0:
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
                self.__estado_inical = copy.deepcopy(self.__estado)
                efeito.set_posicao_x(random_x)
                efeito.set_posicao_y(random_y)
                self.__tempo_efeito = pygame.time.get_ticks()
                self.__estado = efeito.efeito(self.__estado)
                self.__efeitos_ativos.pop()
                screen.fill("blue")

        pygame.draw.rect(screen,"white",[0,TELA_HEIGHT-CHAO,TELA_WIDTH,CHAO])

        self.__estado.gerar_pontuacao(self.__tempo_pontuação)
        score_text = font.render(f"Pontuação: {int(self.__estado._pontuacao)}", True, "yellow")
        screen.blit(score_text, (TELA_WIDTH-TELA_WIDTH/7, 10))

        pygame.display.flip()

        return True
