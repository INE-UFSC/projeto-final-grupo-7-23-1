from menus.menu import Menu
from constantes import *

class MenuPersonagem(Menu):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__state = "Teste"
        self.__testex, self.__testey = TELA_WIDTH / 2, TELA_HEIGHT / 2
        self.__voltarx, self.__voltary = TELA_WIDTH / 2, TELA_HEIGHT - 100
        self.get_cursor_rect().midtop = (self.__testex + self.get_offset(), self.__testey)
    
    def display_menu(self):
        self.set_run_display(True)
        while self.get_run_display():
            self.get_controlador().check_events()
            self.get_controlador().update_mouse()
            self.get_controlador().get_display().fill("black")
            self.get_controlador().draw_text("ESCOLHA SEU", 80, TELA_WIDTH/ 2, 100)
            self.get_controlador().draw_text("PERSONAGEM", 80, TELA_WIDTH/ 2, 200)
            self.__botao_teste = self.get_controlador().draw_text("TESTE", 40, self.__testex, self.__testey, "blue")
            self.__botao_voltar = self.get_controlador().draw_text("VOLTAR", 40, self.__voltarx, self.__voltary)
            self.check_input()
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.get_controlador().DOWN_KEY:
            if self.__state == "Teste":
                self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
                self.__state = "Voltar"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__testex + self.get_offset(), self.__testey)
                self.__state = "Teste"
        if self.get_controlador().UP_KEY:
            if self.__state == "Teste":
                self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
                self.__state = "Voltar"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__testex + self.get_offset(), self.__testey)
                self.__state = "Teste"
        if self.get_controlador().MOUSE:
            if self.__botao_teste.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__testex + self.get_offset(), self.__testey)
                self.__state = "Teste"
            elif self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__voltarx + self.get_offset(), self.__voltary)
                self.__state = "Voltar"
    
    def check_input(self):
        self.move_cursor()
        if self.get_controlador().BACK_KEY:
            self.set_run_display(False)
            self.get_controlador().set_menu_atual(self.get_controlador().get_menu_principal())
        if self.__state == "Teste":
            if (self.__botao_teste.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                return True
        if self.__state == "Voltar":
            if (self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.set_run_display(False)
                self.get_controlador().set_menu_atual(self.get_controlador().get_menu_principal())
