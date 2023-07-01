from menus.menu import Menu
from constantes import *

class MenuRanking(Menu):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__state = "Voltar"
        self.__voltarx, self.__voltary = TELA_WIDTH / 2, TELA_HEIGHT - 100
        self.__rankingleft, self.__rankingtop = 180, 500
        self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
    
    def display_menu(self):
        self.set_run_display(True)
        while self.get_run_display():
            self.get_controlador().check_events()
            self.get_controlador().update_mouse()
            self.get_controlador().get_display().fill("black")
            self.get_controlador().draw_text("CLASSIFICAÇÃO", 60, TELA_WIDTH / 2, 100)
            self.get_controlador().draw_ranking(40, self.__rankingleft, self.__rankingtop)
            self.__botao_voltar = self.get_controlador().draw_text("VOLTAR", 40, self.__voltarx, self.__voltary)
            self.check_input()
            self.draw_cursor()
            self.blit_screen()
    
    def check_input(self):
        if (self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS)
                and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY
                or self.get_controlador().BACK_KEY):
            self.set_run_display(False)
            self.get_controlador().set_menu_atual(self.get_controlador().get_menu_principal())
