import sys
import pygame
from pygame import mixer
from pygame.font import Font
from entities.game import Game
from entities.button import Button
from entities.configs import *


class Menu:
    BUTTONS = {
        'play': Button(image=pygame.image.load("img/Play Rect.png"), pos=(640, 250),
                       text_input="PLAY", base_color="#d7fcd4", hovering_color="White"),

        'options': Button(image=pygame.image.load("img/Options Rect.png"), pos=(640, 400),
                          text_input="OPÇÕES", base_color="#d7fcd4", hovering_color="White"),

        'quit': Button(image=pygame.image.load("img/Quit Rect.png"), pos=(640, 550),
                       text_input="SAIR", base_color="#d7fcd4", hovering_color="White")
    }

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(MENU_DIMENSIONS)
        self.background_image = pygame.image.load("img/capa-3.jpg")
        pygame.display.set_caption("Menu")

        mixer.init()
        mixer.music.load("img\magic-forest-95823.mp3")
        mixer.music.play()

        self.__open_main_menu()

    def __open_main_menu(self):
        MENU_TEXT = Font("img/font.ttf", 50).render(
            "GUERRAS FOLCLORICAS", True, "#b68f40")

        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        
        while True:
            self.screen.blit(self.background_image, (0, 0))

            self.screen.blit(MENU_TEXT, MENU_RECT)

            self.__execute_command()

            pygame.display.update()

    def __execute_command(self):
        mouse_pos = pygame.mouse.get_pos()

        for _, button in Menu.BUTTONS.items():
            button.changeColor(mouse_pos)
            button.update(self.screen)

        for event in pygame.event.get():
            if event.type == pg.QUIT:
                self.__exit_game()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.__exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Menu.BUTTONS['play'].checkForInput(mouse_pos):
                    self.__play()

                if Menu.BUTTONS['options'].checkForInput(mouse_pos):
                    self.__options()

                if Menu.BUTTONS['quit'].checkForInput(mouse_pos):
                    self.__exit_game()

    def __play(self):
        pygame.display.set_caption('UFC - Ultimate Folclore Championship')
        self.__run_game()

    def __options(self):
        return

    def __run_game(self):
        game = Game()
        # game.intro_screen()
        game.start_new_game()
        while game.game_is_running:
            game.main()
            # game.game_over()

        self.__exit_game()

    def __exit_game(self):
        pg.quit()
        sys.exit(0)
