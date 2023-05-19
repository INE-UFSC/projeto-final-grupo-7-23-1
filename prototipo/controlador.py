import pygame

from estado import Estado
from entidade import Entidade

from constantes import *

class Controlador:
    def __init__(self):
        self.__estado = Estado(GRAVIDADE, VELOCIDADE, 1)
        self.__entidades = []

    def add_entity(self, entity: Entidade):
        self.__entidades.append(entity)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))
        clock = pygame.time.Clock()

        running = True
        dt = 0

        while running:
            self.__update(screen, dt)
            dt = clock.tick(FPS) / 1000

        pygame.quit()

    def __update(self, screen: pygame.Surface, dt: float) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__entidades[0].jump()


        for entity in self.__entidades:
            entity.update(self.__estado._gravidade, dt)

        screen.fill("black")

        for entity in self.__entidades:
            entity.draw(screen)

        pygame.draw.rect(screen,"white",[0,TELA_HEIGHT-CHAO,TELA_WIDTH,CHAO])

        pygame.display.flip()

        return True
