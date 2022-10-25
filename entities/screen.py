from dataclasses import dataclass
import pygame as pg


@dataclass
class Screen:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    BORDER = 20

    BG_COLOR = (0, 0, 0, 1)

    def __post_init__(self):
        self.display = pg.display.set_mode(
            (Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))

        self.__set_pause_display()
    
    def show_pause(self):
        self.display.blit(self.pause_text, self.pause_text_area)

    def reset_display(self):
        self.display.fill(Screen.BG_COLOR)

    def get_initial_positions(player: int):
        player1_position = (Screen.BORDER, Screen.BORDER)
        player2_position = (
            Screen.SCREEN_WIDTH - Screen.BORDER, 
            Screen.SCREEN_HEIGHT - Screen.BORDER, 
        )

        return [player1_position, player2_position][player]

    def __set_pause_display(self):
        font = pg.font.SysFont('courier new', 50, True)

        self.pause_text = font.render("PAUSED", True, (250, 250, 250), (0, 0, 0))

        self.pause_text_area = self.pause_text.get_rect()

        self.pause_text_area.center = (
            Screen.SCREEN_WIDTH // 2, Screen.SCREEN_HEIGHT // 2)
