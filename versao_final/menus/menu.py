import pygame
from abc import ABC, abstractmethod
from constantes import *

class Menu(ABC):
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__run_display = True
        self.__cursor_rect = pygame.Rect(0, 0, 30, 30)
        self.__font = CAMINHO_ASSETS + "font.ttf"

    def draw_cursor(self):
        self.__controlador.draw_text('>>', 30, self.__cursor_rect.x, self.__cursor_rect.y, "green")

    def blit_screen(self):
        self.__controlador.get_screen().blit(self.__controlador.get_display(), (0, 0))
        pygame.display.update()
        self.__controlador.reset_keys()

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def check_input(self):
        pass

    def get_controlador(self):
        return self.__controlador
    def get_run_display(self):
        return self.__run_display
    def get_cursor_rect(self):
        return self.__cursor_rect
    def get_font(self):
        return self.__font
    
    def set_run_display(self, boolean: bool):
        self.__run_display = boolean
