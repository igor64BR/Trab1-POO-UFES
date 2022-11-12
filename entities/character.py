from __future__ import annotations
from dataclasses import dataclass
from math import sqrt
from typing import ClassVar, List, Tuple
import pygame as pg
from entities.screen import Screen


@dataclass
class Character:
    characters: ClassVar[List[Character]] = []
    ATTACK_BORDER_COLOR: ClassVar[Tuple[int]] = (0, 250, 0, 1)

    screen: Screen
    strength: int
    hability_power: int

    attack_range: int = None
    max_stamina: int = 100
    max_life: int = 100

    color: Tuple[int] = (250, 250, 250, 1)

    def __post_init__(self):
        self.attack_damage = self.strength // 10
        self.current_life = self.max_life
        self.current_stamina = self.max_stamina

        self.size = self.max_life // 10
        self.speed = 10 / self.size
        self.attack_range = self.attack_range or self.size * 2

    def set_initial_position(self, initial_position: Tuple[float]):
        self.x = initial_position[0]
        self.y = initial_position[1]

        self.__set_limits()

    def draw(self):
        self.screen.draw_circle(
            color=self.color, 
            center=self.__get_position(), 
            radius=self.size
        )

    def take_damage(self, damage: int):
        print(f'character {Character.characters.index(self) + 1} took {damage} of damage')

        self.current_life -= damage

        print(f'Damaged player\'s life: {self.current_life}')

    def attack(self):
        enemy = self.__get_enemy()

        self.screen.draw_circle(
            color=Character.ATTACK_BORDER_COLOR,
            center=self.__get_position(),
            radius=self.attack_range,
            width=2
        )

        if self.__enemy_in_attack_range(enemy):
            enemy.take_damage(self.attack_damage)

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

    def __get_position(self):
        return (self.x, self.y)

    def __enemy_in_attack_range(self, enemy: Character) -> bool:
        center_dist = self.__get_dist_from_enemy(enemy)

        return center_dist <= enemy.size + self.attack_range

    def __set_limits(self):
        self.top = self.y - self.size
        self.bottom = self.y + self.size

        self.right = self.x + self.size
        self.left = self.x - self.size

    def __get_enemy(self):
        return [character for character in Character.characters if character != self][0]

    def __get_dist_from_enemy(self, enemy: Character):
        """Gets the distance from self and enemy's centers"""

        x_dist = abs(self.x - enemy.x)
        y_dist = abs(self.y - enemy.y)

        return sqrt(x_dist ** 2 + y_dist ** 2)
