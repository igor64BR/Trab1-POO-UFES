from dataclasses import dataclass
from typing import ClassVar, Tuple
import pygame as pg

from cronometro import Cronometro


@dataclass
class Screen:
    BG_COLOR: ClassVar[Tuple[int]] = (0, 0, 0, 1)
    cronometro: 'Cronometro'

    __SCREEN_WIDTH: int = 1280
    __SCREEN_HEIGHT: int = 720
    BORDER: int = 20

    def __post_init__(self):
        self.SCREEN_TOP = 0
        self.SCREEN_BOTTOM = self.__SCREEN_HEIGHT
        self.SCREEN_LEFT = 0
        self.SCREEN_RIGHT = self.__SCREEN_WIDTH

        self.display = pg.display.set_mode(
            (self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT))

        self.set_pause_display()
        self.set_cronometer_display()

    def show_pause(self):
        self.display.blit(self.pause_text, self.pause_text_area)

    def show_time(self):
        self.update_time()
        self.display.blit(self.time_text, self.time_text_area)

    def reset_display(self):
        self.display.fill(Screen.BG_COLOR)

    def get_initial_positions(self, player: int):
        player1_position = (self.BORDER, self.BORDER)
        player2_position = (
            self.__SCREEN_WIDTH - self.BORDER,
            self.__SCREEN_HEIGHT - self.BORDER,
        )

        return [player1_position, player2_position][player]

    def set_pause_display(self):
        font = pg.font.SysFont('courier new', 50, True)

        self.pause_text = font.render(
            "PAUSED", True, (250, 250, 250), Screen.BG_COLOR)

        self.pause_text_area = self.pause_text.get_rect()

        self.pause_text_area.center = (
            self.__SCREEN_WIDTH // 2, self.__SCREEN_HEIGHT // 2)

    def set_cronometer_display(self):
        font = pg.font.SysFont('courier new', 20, True)

        self.time_text = font.render(
            self.cronometro.get_display_time(), True, (250, 250, 250), Screen.BG_COLOR)

        self.time_text_area = self.time_text.get_rect()

        self.time_text_area.center = (
            self.__SCREEN_WIDTH // 2, self.__SCREEN_HEIGHT // 10
        )

    def update_time(self):
        self.set_cronometer_display()

    def draw_circle(self, color: Tuple[int], center: Tuple[float], radius: int, width: int = 0):
        pg.draw.circle(
            surface=self.display,
            color=color,
            center=center,
            radius=radius,
            width=width
        )
