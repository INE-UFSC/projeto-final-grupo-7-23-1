from pygame import Rect
from menus.menu import Menu
from constantes import *

class MenuGameOver(Menu):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__state = "Jogar"
        self.__jogarx, self.__jogary = 280, TELA_HEIGHT - 100
        self.__voltarx, self.__voltary = TELA_WIDTH / 2 + 100, TELA_HEIGHT - 100
        self.__sairx, self.__sairy = TELA_WIDTH - 180, TELA_HEIGHT - 100
        self.__rankingleft, self.__rankingtop = 295, 520
        self.__offset_jogar = -210
        self.__offset_voltar = -210
        self.__offset_sair = -110
        self.get_image_bg().set_alpha(40)
        self.get_cursor_rect().midtop = (self.__jogarx + self.__offset_jogar, self.__jogary)
    
    def display_menu(self):
        self.set_run_display(True)
        while self.get_run_display():
            self.get_controlador().check_events()
            self.get_controlador().update_mouse()
            self.get_controlador().get_display().fill("black")
            self.get_controlador().draw_image(self.get_image_bg(), TELA_WIDTH / 2, TELA_HEIGHT / 2)
            self.get_controlador().draw_text("FIM DO JOGO", 60, TELA_WIDTH / 2, 100, "red")
            self.get_controlador().draw_text(f"Sua pontuação foi de {100000}.", 30, TELA_WIDTH / 2, 200, "white")
            self.get_controlador().draw_text(f"Você ficou entre os cinco melhores locais!", 30, TELA_WIDTH / 2, 250, "white")
            self.get_controlador().draw_ranking(30, self.__rankingleft, self.__rankingtop)
            rect_jogar1 = self.get_controlador().draw_text("JOGAR", 40, self.__jogarx, self.__jogary - 25)
            rect_jogar2 = self.get_controlador().draw_text("NOVAMENTE", 40, self.__jogarx, self.__jogary + 25)
            self.__botao_jogar = Rect(rect_jogar2.left, rect_jogar1.top, rect_jogar2.width, rect_jogar1.height * 2 + 10)
            rect_voltar1 = self.get_controlador().draw_text("MENU", 40, self.__voltarx, self.__voltary - 25)
            rect_voltar2 = self.get_controlador().draw_text("PRINCIPAL", 40, self.__voltarx, self.__voltary + 25)
            self.__botao_voltar = Rect(rect_voltar2.left, rect_voltar1.top, rect_voltar2.width, rect_voltar1.height * 2 + 10)
            self.__botao_sair = self.get_controlador().draw_text("SAIR", 40, self.__sairx, self.__sairy)
            if self.check_input():
                return True
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.get_controlador().RIGHT_KEY:
            if self.__state == "Jogar":
                self.get_cursor_rect().midtop = (self.__voltarx + self.__offset_voltar, self.__voltary)
                self.__state = "Voltar"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__sairx + self.__offset_sair, self.__sairy)
                self.__state = "Sair"
            elif self.__state == "Sair":
                self.get_cursor_rect().midtop = (self.__jogarx + self.__offset_jogar, self.__jogary)
                self.__state = "Jogar"
        if self.get_controlador().LEFT_KEY:
            if self.__state == "Jogar":
                self.get_cursor_rect().midtop = (self.__sairx + self.__offset_sair, self.__sairy)
                self.__state = "Sair"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__jogarx + self.__offset_jogar, self.__jogary)
                self.__state = "Jogar"
            elif self.__state == "Sair":
                self.get_cursor_rect().midtop = (self.__voltarx + self.__offset_voltar, self.__voltary)
                self.__state = "Voltar"
        if self.get_controlador().MOUSE:
            if self.__botao_jogar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__jogarx + self.__offset_jogar, self.__jogary)
                self.__state = "Jogar"
            elif self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__voltarx + self.__offset_voltar, self.__voltary)
                self.__state = "Voltar"
            elif self.__botao_sair.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__sairx + self.__offset_sair, self.__sairy)
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
