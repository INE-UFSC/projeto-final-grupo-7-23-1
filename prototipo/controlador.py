import pygame

from estado import Estado

FPS = 60

class Controlador:
    def __init__(self):
        self._estado = Estado(500,200,1)
        self.__entidades = []

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()

        running = True
        dt = 0

        while running:
            self.__update(screen, dt);
            dt = clock.tick(FPS) / 1000

        pygame.quit()

    def __update(self, screen: pygame.Surface, dt: float) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill("black")
        pygame.display.flip()

        return True
