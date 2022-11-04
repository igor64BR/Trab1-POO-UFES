import sys, pygame, main
from button import Button
from pygame import mixer
from entities.characters_lib import Character_enum, Characters_lib
from entities.player import *
from entities.screen import Screen

pygame.init()

SCREEN = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("Menu")

mixer.init()
mixer.music.load("img\magic-forest-95823.mp3")
mixer.music.play()

BG = pygame.image.load("img/capa-3.jpg")


def get_font(size): 
    return pygame.font.Font("img/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        
        main()
       
            

        pygame.display.update()


def options():
    while True:
       
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("GUERRAS FOLCLORICAS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("img/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(640, 400),
                                text_input="OPÇÕES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("img/Quit Rect.png"), pos=(640, 550),
                             text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()