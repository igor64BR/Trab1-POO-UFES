from dataclasses import dataclass
from typing import Tuple
import pygame as pg
from entities.screen import Screen


@dataclass
class Character:

    screen: Screen
    strength: int
    hability_power: int

    __max_stamina: int = 100
    __max_life: int = 100

    color: Tuple[int] = (250, 250, 250, 1)

    def __post_init__(self):
        self.current_life = self.__max_life
        self.current_stamina = self.__max_stamina

        self.size = self.__max_life // 10
        self.speed = 10 / self.size

    def set_initial_position(self, initial_position: Tuple[float]):
        self.x = initial_position[0]
        self.y = initial_position[1]

        self.__set_limits()

    def draw(self):
        pg.draw.circle(
            surface=self.screen.display,
            color=self.color,
            center=(self.x, self.y),
            radius=self.size,
            width=0
        )

    def move_up(self):
        self.__set_limits()
        if self.top > self.screen.SCREEN_TOP:
            self.y -= self.speed

    def move_down(self):
        self.__set_limits()
        if self.bottom < self.screen.SCREEN_BOTTOM:
            self.y += self.speed

    def move_right(self):
        self.__set_limits()
        if self.right < self.screen.SCREEN_RIGHT:
            self.x += self.speed

    def move_left(self):
        self.__set_limits()
        if self.left > self.screen.SCREEN_LEFT:
            self.x -= self.speed

    def __set_limits(self):
        self.top = self.y - self.size
        self.bottom = self.y + self.size

        self.right = self.x + self.size
        self.left = self.x - self.size
