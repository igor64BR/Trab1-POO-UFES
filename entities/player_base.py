import pygame as pg

from entities.sprite import Sprite
from entities.configs import *


class Player_base(Sprite):
    def __init__(self, game, x: int, y: int, color: tuple[int]) -> None:
        super().__init__(game, x, y, color, layer=PLAYER_LAYER, speed=3)

        self.set_command()
        self.set_enemy_sprite()

    def update(self, *args, **kwargs) -> None:
        self.get_movement_commands()

    def get_movement_commands(self):
        keys = pg.key.get_pressed()

        for key, action in self.commands.items():
            if keys[key]:
                action()

        self.rect.x += self.x_current_speed
        self.check_all_collisions('x')

        self.rect.y += self.y_current_speed
        self.check_all_collisions('y')

        self.reset_speed_changes()

    def check_all_collisions(self, direction: str):
        self.check_collision(direction, self.game.block_sprites)
        self.check_collision(direction, self.enemy_sprite)
        self.check_collision(direction, self.game.minion_sprites)

    def reset_speed_changes(self):
        self.x_current_speed = 0
        self.y_current_speed = 0

    def move_up(self):
        self.move(UP, False, -1)

    def move_down(self):
        self.move(DOWN, False)

    def move_right(self):
        self.move(RIGHT, True)

    def move_left(self):
        self.move(LEFT, True, -1)

    def move(self, facing: str, x_speed_change: bool, magnitude: int = 1):
        self.facing = facing

        if x_speed_change:
            self.x_current_speed += magnitude * self.SPEED
        else:
            self.y_current_speed += magnitude * self.SPEED

    def set_enemy_sprite(self):
        raise NotImplementedError("'set_enemy_sprite' method not Implemented on Player class")

    def set_command(self):
        raise NotImplementedError("'set_command' method not Implemented on Player class")