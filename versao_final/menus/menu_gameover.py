from menus.menu import Menu
from constantes import *

class MenuGameOver(Menu):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__state = "Jogar"
        self.__jogarx, self.__jogary = 380, TELA_HEIGHT - 100
        self.__voltarx, self.__voltary = TELA_WIDTH / 2 + 220, TELA_HEIGHT - 100
        self.__sairx, self.__sairy = TELA_WIDTH / 2 + 470, TELA_HEIGHT - 100
        self.set_cursor_pos(self.__jogarx + self.get_offset(), self.__jogary)
    
    def display_menu(self):
        self.set_run_display(True)
        while self.get_run_display():
            self.get_controlador().check_events()
            self.get_controlador().update_mouse()
            self.get_controlador().get_display().fill("black")
            self.get_controlador().draw_text("FIM DO JOGO", 80, TELA_WIDTH/ 2, 100)
            self.get_controlador().draw_text("RANKING", 150, TELA_WIDTH/ 2, TELA_HEIGHT / 2 + 50, "blue")
            self.__botao_jogar = self.get_controlador().draw_text("JOGAR NOVAMENTE", 40, self.__jogarx, self.__jogary)
            self.__botao_voltar = self.get_controlador().draw_text("MENU", 40, self.__voltarx, self.__voltary)
            self.__botao_sair = self.get_controlador().draw_text("SAIR", 40, self.__sairx, self.__sairy)
            if self.check_input():
                return True
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.get_controlador().RIGHT_KEY:
            if self.__state == "Jogar":
                self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
                self.__state = "Voltar"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__sairx + self.get_offset(), self.__sairy)
                self.__state = "Sair"
            elif self.__state == "Sair":
                self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)
                self.__state = "Jogar"
        if self.get_controlador().LEFT_KEY:
            if self.__state == "Jogar":
                self.get_cursor_rect().midtop = (self.__sairx + self.get_offset(), self.__sairy)
                self.__state = "Sair"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)
                self.__state = "Jogar"
            elif self.__state == "Sair":
                self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
                self.__state = "Voltar"
        if self.get_controlador().MOUSE:
            if self.__botao_jogar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__jogarx + self.get_offset(), self.__jogary)
                self.__state = "Jogar"
            elif self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
                self.__state = "Voltar"
            elif self.__botao_sair.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__sairx + self.get_offset(), self.__sairy)
                self.__state = "Sair"
    
    def check_input(self):
        self.move_cursor()
        if self.__state == "Jogar":
            if (self.__botao_jogar.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                return True
        if self.__state == "Voltar":
            if (self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                self.get_controlador().set_menu_atual(self.get_controlador().get_menu_principal())
        if self.__state == "Sair":
            if (self.__botao_sair.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                self.get_controlador().quit()
