import pygame as pg

from entities.sprite import Sprite
from entities.configs import *


class Player_base(Sprite):
    def __init__(self, game, x: int, y: int, color: tuple[int]) -> None:
        super().__init__(game, x, y, color)

        self.SPEED = 3

        self.x_current_speed = 0
        self.y_current_speed = 0

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
        self.collide_blocks('x')
        self.collide_enemy('x')

        self.rect.y += self.y_current_speed
        self.collide_blocks('y')
        self.collide_enemy('y')

        self.reset_speed_changes()

    def collide_enemy(self, direction: str):
        hits = pg.sprite.spritecollide(self, self.enemy_sprite, False)

        if not hits:
            return
        
        if direction == 'x':
            self.check_x_collision(hits)

        elif direction == 'y':
            self.check_y_collision(hits)

    def collide_blocks(self, direction: str):
        hits = pg.sprite.spritecollide(self, self.game.block_sprites, False)

        if not hits:
            return

        if direction == 'x':
            self.check_x_collision(hits)

        elif direction == 'y':
            self.check_y_collision(hits)

    def check_y_collision(self, hits):
        if self.y_current_speed > 0:  # Going to down
            self.rect.y = hits[0].rect.top - self.rect.height

        elif self.y_current_speed < 0:  # Going to up
            self.rect.y = hits[0].rect.bottom

    def check_x_collision(self, hits):
        if self.x_current_speed > 0:  # Going to left
            self.rect.x = hits[0].rect.left - self.rect.width

        elif self.x_current_speed < 0:  # Going to right
            self.rect.x = hits[0].rect.right

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