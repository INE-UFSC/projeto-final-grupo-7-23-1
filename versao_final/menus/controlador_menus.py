import pygame
import sys
from constantes import *
from menus.menu import Menu
from menus.menu_principal import MenuPrincipal
from menus.menu_personagem import MenuPersonagem
from menus.menu_ranking import MenuRanking
from menus.menu_gameover import MenuGameOver

class ControladorMenus:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.__running = True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY = False, False, False
        self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False
        self.MOUSE, self.MOUSE_CLICK = False, False
        self.MOUSE_POS = pygame.mouse.get_pos()
        self.__display = pygame.Surface((TELA_WIDTH, TELA_HEIGHT))
        self.__screen = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))
        self.__font = CAMINHO_ASSETS + "font.ttf"
        self.__menu_principal = MenuPrincipal(self)
        self.__menu_personagem = MenuPersonagem(self)
        self.__menu_ranking = MenuRanking(self)
        self.__menu_gameover = MenuGameOver(self)
        self.__menu_atual = self.__menu_principal

    def menu_loop(self):
        self.__running = True
        pygame.key.set_repeat(250, 40)
        while self.__running:
            self.check_events()
            self.update_mouse()
            if self.__menu_atual.display_menu():
                pygame.key.set_repeat(0, 40)
                self.__running = False
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.MOUSEMOTION:
                self.MOUSE = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.MOUSE_CLICK = True


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY = False, False, False
        self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False
        self.MOUSE, self.MOUSE_CLICK = False, False
    
    def draw_text(self, text, size, x, y, color= "white"):
        font = pygame.font.Font(self.__font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__display.blit(text_surface, text_rect)
        return text_rect

    def draw_textinput(self, text_input, x, y):
        text_input_rect = text_input.surface.get_rect()
        text_input_rect.center = (x, y)
        self.__display.blit(text_input.surface, text_input_rect)
        return text_input_rect

    def update_textinput(self, text_input):
        text_input.update(pygame.event.get())

    def update_mouse(self):
        self.MOUSE_POS = pygame.mouse.get_pos()

    def quit(self):
        self.__menu_atual.set_run_display(False)
        self.__running = False
        pygame.quit()
        sys.exit()


    def get_running(self):
        return self.__running
    def get_display(self):
        return self.__display
    def get_screen(self):
        return self.__screen
    def get_font_object(self, size):
        return pygame.font.Font(self.__font, size)
    def get_menu_principal(self):
        return self.__menu_principal
    def get_menu_personagem(self):
        return self.__menu_personagem
    def get_menu_ranking(self):
        return self.__menu_ranking
    def get_menu_gameover(self):
        return self.__menu_gameover

    def set_running(self, boolean: bool):
        self.__running = boolean
    def set_menu_atual(self, menu: Menu):
        self.__menu_atual = menu
