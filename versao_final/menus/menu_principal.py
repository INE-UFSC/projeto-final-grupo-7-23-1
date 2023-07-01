import pygame_textinput
from pygame import Rect
from menus.menu import Menu
from constantes import *

class MenuPrincipal(Menu):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__state = "Jogar"
        self.__textinputx, self.__textinputy = TELA_WIDTH / 2 + 100, TELA_HEIGHT - 380
        self.__jogarx, self.__jogary = TELA_WIDTH / 2, TELA_HEIGHT - 310
        self.__personagemx, self.__personagemy = TELA_WIDTH / 2, TELA_HEIGHT - 240
        self.__rankingx, self.__rankingy = TELA_WIDTH / 2, TELA_HEIGHT - 170
        self.__sairx, self.__sairy = TELA_WIDTH / 2, TELA_HEIGHT - 100
        self.__nome = "Jogador1"
        self.__manager = pygame_textinput.TextInputManager(self.__nome, lambda input: len(input) <= 10)
        self.__textinput = pygame_textinput.TextInputVisualizer(self.__manager, self.get_controlador().get_font_object(40),
                                               True, "white", cursor_color="white")
        self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)

    def display_menu(self):
        self.set_run_display(True)
        while self.get_run_display():
            self.get_controlador().check_events()
            self.get_controlador().update_mouse()
            self.get_controlador().get_display().fill("black")
            self.get_controlador().draw_text("FUGA PELO", 100, TELA_WIDTH / 2, 100)
            self.get_controlador().draw_text("BRASIL", 100, TELA_WIDTH / 2, 220)
            rect_textinput1 = self.get_controlador().draw_text("NOME:", 40, TELA_WIDTH / 2 - 250, self.__textinputy)
            rect_textinput2 = self.get_controlador().draw_textinput(self.__textinput, self.__textinputx, self.__textinputy)
            self.__textinput_rect = Rect(rect_textinput1.left, rect_textinput1.top,
                                         rect_textinput2.right - rect_textinput1.left - 40, rect_textinput1.height)
            self.__botao_jogar = self.get_controlador().draw_text("JOGAR", 40, self.__jogarx, self.__jogary)
            self.__botao_personagem = self.get_controlador().draw_text("ESCOLHER PERSONAGEM", 40, self.__personagemx, self.__personagemy)
            self.__botao_ranking = self.get_controlador().draw_text("CLASSIFICAÇÃO", 40, self.__rankingx, self.__rankingy)
            self.__botao_sair = self.get_controlador().draw_text("SAIR", 40, self.__sairx, self.__sairy)
            if self.check_input():
                return True
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.get_controlador().DOWN_KEY:
            if self.__state == "Jogar":
                self.get_cursor_rect().midtop = (self.__personagemx + self.get_offset(), self.__personagemy)
                self.__state = "Personagem"
            elif self.__state == "Personagem":
                self.get_cursor_rect().midtop = (self.__rankingx + self.get_offset(), self.__rankingy)
                self.__state = "Ranking"
            elif self.__state == "Ranking":
                self.get_cursor_rect().midtop = (self.__sairx + self.get_offset(), self.__sairy)
                self.__state = "Sair"
            elif self.__state == "Sair":
                self.get_cursor_rect().midtop = (self.__textinputx + self.get_offset(), self.__textinputy)
                self.__state = "Nome"
            elif self.__state == "Nome":
                self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)
                self.__state = "Jogar"
        if self.get_controlador().UP_KEY:
            if self.__state == "Jogar":
                self.get_cursor_rect().midtop = (self.__textinputx + self.get_offset(), self.__textinputy)
                self.__state = "Nome"
            elif self.__state == "Personagem":
                self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)
                self.__state = "Jogar"
            elif self.__state == "Ranking":
                self.get_cursor_rect().midtop = (self.__personagemx + self.get_offset(), self.__personagemy)
                self.__state = "Personagem"
            elif self.__state == "Sair":
                self.get_cursor_rect().midtop = (self.__rankingx + self.get_offset(), self.__rankingy)
                self.__state = "Ranking"
            elif self.__state == "Nome":
                self.get_cursor_rect().midtop = (self.__sairx + self.get_offset(), self.__sairy)
                self.__state = "Sair"
        if self.get_controlador().MOUSE:
            if self.__botao_jogar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)
                self.__state = "Jogar"
            elif self.__botao_personagem.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__personagemx + self.get_offset(), self.__personagemy)
                self.__state = "Personagem"
            elif self.__botao_ranking.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__rankingx + self.get_offset(), self.__rankingy)
                self.__state = "Ranking"
            elif self.__botao_sair.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__sairx + self.get_offset(), self.__sairy)
                self.__state = "Sair"
            elif self.__textinput_rect.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__textinputx + self.get_offset(), self.__textinputy)
                self.__state = "Nome"

    def check_input(self):
        self.move_cursor()
        if self.__state != "Nome":
            self.__textinput.cursor_visible = False
        if self.__state == "Jogar":
            if (self.__botao_jogar.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.__nome = self.__textinput.manager.value
                self.set_run_display(False)
                return True
        elif self.__state == "Personagem":
            if (self.__botao_personagem.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                self.get_controlador().set_menu_atual(self.get_controlador().get_menu_personagem())
        elif self.__state == "Ranking":
            if (self.__botao_ranking.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                self.get_controlador().set_menu_atual(self.get_controlador().get_menu_ranking())
        elif self.__state == "Sair":
            if (self.__botao_sair.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.get_controlador().quit()
        elif self.__state == "Nome":
            self.get_controlador().update_textinput(self.__textinput)

    def get_nome(self):
        return self.__nome
