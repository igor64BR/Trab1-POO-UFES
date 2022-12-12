import sys
import pygame
from pygame import mixer
from pygame.font import Font
from entities.button_selecao_personagem import Button
from entities.configs import *
from entities.game import Game


class Selection_screen:
    HEIGHT = 1200
    WIDTH = 720

    BUTTONS = {
        CURUPIRA: Button(
            image=pygame.image.load("img/name-box.png"),
            pos=(400, 300),
            text_input=CURUPIRA,
            base_color=TEXT_COLOR,
            hovering_color="White"
        ),

        CUCA: Button(
            image=pygame.image.load("img/name-box.png"),
            pos=(900, 300),
            text_input=CUCA,
            base_color=TEXT_COLOR,
            hovering_color="White"
        ),

        SACI: Button(
            image=pygame.image.load("img/name-box.png"),
            pos=(400, 600),
            text_input=SACI,
            base_color=TEXT_COLOR,
            hovering_color="White"
        ),

        MULA_SEM_CABECA: Button(
            image=pygame.image.load("img/name-box.png"),
            pos=(900, 600),
            text_input=MULA_SEM_CABECA,
            base_color=TEXT_COLOR,
            hovering_color="White"
        ),
    }

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.background_image = pygame.image.load(
            "img/background.png")
        pygame.display.set_caption("Menu")
        self.__open_select()

    def __exit_game(self):
        pygame.quit()
        sys.exit(0)

    def __open_select(self):
        characters = []

        for loop in range(2):
            while True:
                self.__blit_images(character=loop + 1)
                choice = self.__get_choice()
                pygame.display.update()

                if choice != None:
                    characters.append(choice)
                    break

        self.chosen_character1 = characters[0]
        self.chosen_character2 = characters[1]
        self.__run_game()

    def __get_choice(self):
        mouse_pos = pygame.mouse.get_pos()

        for _, button in Selection_screen.BUTTONS.items():
            button.changeColor(mouse_pos)
            button.update(self.screen)

        for event in pygame.event.get():
            self.__check_exit(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.__get_character(mouse_pos)

        return None

    def __get_character(self, mouse_pos: tuple):
        if Selection_screen.BUTTONS[SACI].checkForInput(mouse_pos):
            return SACI

        if Selection_screen.BUTTONS[CURUPIRA].checkForInput(mouse_pos):
            return CURUPIRA

        if Selection_screen.BUTTONS[MULA_SEM_CABECA].checkForInput(mouse_pos):
            return MULA_SEM_CABECA

        if Selection_screen.BUTTONS[CUCA].checkForInput(mouse_pos):
            return CUCA

        return None

    def __check_exit(self, event):
        if event.type == pygame.QUIT:
            self.__exit_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.__exit_game()

    def __run_game(self):
        game = Game()

        game.run(
            self.chosen_character1,
            self.chosen_character2
        )

        self.__exit_game()

    def __blit_images(self, character: int):
        MENU_TEXT = Font("img/font.ttf", 20).render(
            f"Escolha sua {character}a lenda", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 30))
        PROPORTIONS = (0, 0, 100, 100)

        curupira = pygame.image.load("img/Curupira1.png")
        saci = pygame.image.load("img/Saci-menu.png")
        cuca = pygame.image.load("img/Cuca1.png")
        mula = pygame.image.load("img/MulaSemCabeca-menu.png")

        LEFT_X_POSITION = 355
        RIGHT_X_POSITION = 850
        TOP_Y_POSITION = 120
        BOTTOM_Y_POSITION = 420

        self.screen.blit(MENU_TEXT, MENU_RECT)
        self.screen.blit(curupira, (LEFT_X_POSITION, TOP_Y_POSITION), PROPORTIONS)
        self.screen.blit(cuca, (RIGHT_X_POSITION, TOP_Y_POSITION), PROPORTIONS)
        self.screen.blit(saci, (LEFT_X_POSITION, BOTTOM_Y_POSITION), PROPORTIONS)
        self.screen.blit(mula, (RIGHT_X_POSITION, BOTTOM_Y_POSITION), PROPORTIONS)
