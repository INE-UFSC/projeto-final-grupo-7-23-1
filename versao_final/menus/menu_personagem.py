from pygame import Rect, transform, image
from menus.menu import Menu
from constantes import *

class MenuPersonagem(Menu):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__state = "Personagem1"
        self.__escolhido = 1
        self.__p1x, self.__p1y = 260, TELA_HEIGHT / 2 + 30
        self.__p2x, self.__p2y = TELA_WIDTH / 2, TELA_HEIGHT / 2 + 30
        self.__p3x, self.__p3y = 1020, TELA_HEIGHT / 2 + 30
        self.__voltarx, self.__voltary = TELA_WIDTH / 2, TELA_HEIGHT - 100
        self.__offset_p = -82.5
        self.__offset_voltar = -150
        self.__rect_borda = Rect(0, 0, 110, 210)
        self.__rect_fundo = Rect(0, 0, 100, 200)
        self.__personagem1 = [[image.load(CAMINHO_ASSETS + "saci1.png"), image.load(CAMINHO_ASSETS + "saci2.png"),
                              image.load(CAMINHO_ASSETS + "saci3.png"), image.load(CAMINHO_ASSETS + "saci4.png")],
                              [image.load(CAMINHO_ASSETS + "saciagachado.png")]]
        self.__personagem2 = [image.load(CAMINHO_ASSETS + "box1.png"), image.load(CAMINHO_ASSETS + "box2.png")]
        self.__personagem3 = [image.load(CAMINHO_ASSETS + "powerup.png")]
        self.__imagem_p1 = transform.scale(self.__personagem1[0][0], (100, 200))
        self.__imagem_p2 = transform.scale(self.__personagem2[0], (100, 200))
        self.__imagem_p3 = transform.scale(self.__personagem3[0], (100, 200))
        self.__cor_padrao = "white"
        self.__cor_selecionado = "green"
        self.__cor_borda_p1 = self.__cor_selecionado
        self.__cor_borda_p2 = self.__cor_padrao
        self.__cor_borda_p3 = self.__cor_padrao
        self.get_cursor_rect().midtop = (self.__p1x + self.__offset_p, self.__p1y)
    
    def display_menu(self):
        self.set_run_display(True)
        while self.get_run_display():
            self.get_controlador().check_events()
            self.get_controlador().update_mouse()
            self.get_controlador().get_display().fill("black")
            self.get_controlador().draw_image(self.get_image_bg(), TELA_WIDTH / 2, TELA_HEIGHT / 2)
            self.get_controlador().draw_text("ESCOLHA SEU", 60, TELA_WIDTH/ 2, 100, "blue")
            self.get_controlador().draw_text("PERSONAGEM", 60, TELA_WIDTH/ 2, 180, "green")
            self.__botao_p1 = self.get_controlador().draw_rect(self.__rect_borda, self.__p1x, self.__p1y, self.__cor_borda_p1)
            self.__botao_p2 = self.get_controlador().draw_rect(self.__rect_borda, self.__p2x, self.__p2y, self.__cor_borda_p2)
            self.__botao_p3 = self.get_controlador().draw_rect(self.__rect_borda, self.__p3x, self.__p3y, self.__cor_borda_p3)
            self.get_controlador().draw_rect(self.__rect_fundo, self.__p1x, self.__p1y, "blue")
            self.get_controlador().draw_rect(self.__rect_fundo, self.__p2x, self.__p2y, "blue")
            self.get_controlador().draw_rect(self.__rect_fundo, self.__p3x, self.__p3y, "blue")
            self.get_controlador().draw_image(self.__imagem_p1, self.__p1x, self.__p1y)
            self.get_controlador().draw_image(self.__imagem_p2, self.__p2x, self.__p2y)
            self.get_controlador().draw_image(self.__imagem_p3, self.__p3x, self.__p3y)
            self.get_controlador().draw_text("Escolhido", 15, self.__p1x + (self.__escolhido - 1) * (self.__p2x - self.__p1x), self.__p1y - 125, "green")
            self.get_controlador().draw_text("Saci-pererê", 25, self.__p1x, self.__p1y + 145, "white")
            self.get_controlador().draw_text("Curupira", 25, self.__p2x, self.__p2y + 145, "white")
            self.get_controlador().draw_text("Personagem 3", 25, self.__p3x, self.__p3y + 145, "white")
            self.__botao_voltar = self.get_controlador().draw_text("VOLTAR", 40, self.__voltarx, self.__voltary)
            self.check_input()
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.get_controlador().DOWN_KEY or self.get_controlador().UP_KEY:
            if self.__state == "Personagem1" or self.__state == "Personagem2" or self.__state == "Personagem3":
                self.get_cursor_rect().midtop = (self.__voltarx + self.__offset_voltar, self.__voltary)
                self.__state = "Voltar"
            elif self.__state == "Voltar":
                self.get_cursor_rect().midtop = (self.__p1x + self.__offset_p, self.__p1y)
                self.__state = "Personagem1"
        if self.get_controlador().LEFT_KEY:
            if self.__state == "Personagem1":
                self.get_cursor_rect().midtop = (self.__p3x + self.__offset_p, self.__p3y)
                self.__state = "Personagem3"
            elif self.__state == "Personagem2":
                self.get_cursor_rect().midtop = (self.__p1x + self.__offset_p, self.__p1y)
                self.__state = "Personagem1"
            elif self.__state == "Personagem3":
                self.get_cursor_rect().midtop = (self.__p2x + self.__offset_p, self.__p2y)
                self.__state = "Personagem2"
        if self.get_controlador().RIGHT_KEY:
            if self.__state == "Personagem1":
                self.get_cursor_rect().midtop = (self.__p2x + self.__offset_p, self.__p2y)
                self.__state = "Personagem2"
            elif self.__state == "Personagem2":
                self.get_cursor_rect().midtop = (self.__p3x + self.__offset_p, self.__p3y)
                self.__state = "Personagem3"
            elif self.__state == "Personagem3":
                self.get_cursor_rect().midtop = (self.__p1x + self.__offset_p, self.__p1y)
                self.__state = "Personagem1"
        if self.get_controlador().MOUSE:
            if self.__botao_p1.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__p1x + self.__offset_p, self.__p1y)
                self.__state = "Personagem1"
            if self.__botao_p2.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__p2x + self.__offset_p, self.__p2y)
                self.__state = "Personagem2"
            if self.__botao_p3.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__p3x + self.__offset_p, self.__p3y)
                self.__state = "Personagem3"
            elif self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS):
                self.get_cursor_rect().midtop = (self.__voltarx + self.__offset_voltar, self.__voltary)
                self.__state = "Voltar"
    
    def check_input(self):
        self.move_cursor()
        if self.get_controlador().BACK_KEY:
            self.set_run_display(False)
            self.get_controlador().set_menu_atual(self.get_controlador().get_menu_principal())
        if self.__state == "Personagem1":
            self.__cor_borda_p1 = self.__cor_selecionado
            self.__cor_borda_p2 = self.__cor_padrao
            self.__cor_borda_p3 = self.__cor_padrao
            if (self.__botao_p1.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.__escolhido = 1
        if self.__state == "Personagem2":
            self.__cor_borda_p1 = self.__cor_padrao
            self.__cor_borda_p2 = self.__cor_selecionado
            self.__cor_borda_p3 = self.__cor_padrao
            if (self.__botao_p2.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.__escolhido = 2
        if self.__state == "Personagem3":
            self.__cor_borda_p1 = self.__cor_padrao
            self.__cor_borda_p2 = self.__cor_padrao
            self.__cor_borda_p3 = self.__cor_selecionado
            if (self.__botao_p3.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.__escolhido = 3
        if self.__state == "Voltar":
            self.__cor_borda_p1 = "white"
            self.__cor_borda_p2 = "white"
            self.__cor_borda_p3 = "white"
            if (self.__botao_voltar.collidepoint(self.get_controlador().MOUSE_POS)
                    and self.get_controlador().MOUSE_CLICK or self.get_controlador().START_KEY):
                self.get_cursor_rect().midtop = (self.__p1x + self.__offset_p, self.__p1y)
                self.__state = "Personagem1"
                self.set_run_display(False)
                self.get_controlador().set_menu_atual(self.get_controlador().get_menu_principal())

    def get_personagem(self):
        if self.__escolhido == 1:
            return self.__personagem1
        elif self.__escolhido == 2:
            return self.__personagem2
        return self.__personagem3
