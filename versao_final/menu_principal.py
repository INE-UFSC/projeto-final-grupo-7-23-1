import pygame
from button import Button

class MenuPrincipal:
    def __init__(self, screen):
        self.__font = "assets/font.ttf"

    def update(self, screen):
        running = True
        while running:
            cursor = pygame.mouse.get_pos()

            menu_titulo = pygame.font.SysFont(self.__font, 100).render("MENU PRINCIPAL", True, "#b68f40")
            menu_rect = menu_titulo.get_rect(center=(640, 100))

            botao_jogar = Button(image=None, pos=(640, 250), 
                                text_input="JOGAR", font=pygame.font.SysFont(self.__font, 75), base_color="#d7fcd4", hovering_color="White")
            botao_opcoes = Button(image=None, pos=(640, 400), 
                                text_input="OPÇÕES", font=pygame.font.SysFont(self.__font, 75), base_color="#d7fcd4", hovering_color="White")
            botao_sair = Button(image=None, pos=(640, 550), 
                                text_input="SAIR", font=pygame.font.SysFont(self.__font, 75), base_color="#d7fcd4", hovering_color="White")
            
            screen.blit(menu_titulo, menu_rect)

            for button in [botao_jogar, botao_opcoes, botao_sair]:
                button.changeColor(cursor)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_jogar.checkForInput(cursor):
                        pass
                    if botao_opcoes.checkForInput(cursor):
                        pass
                    if botao_sair.checkForInput(cursor):
                        pygame.quit()

            pygame.display.update()
