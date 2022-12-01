import pygame as pg
from entities.configs import *


class Sprite(pg.sprite.Sprite):
    def __init__(self,
                 game,
                 x: int,
                 y: int,
                 layer: int,
                 img: str = 'img/Unknown.png',
                 speed: int = 0
                 ) -> None:
        self.set_groups(game)
        self._layer = layer

        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        coordinates = [self.width, self.height]

        sprite = pg.image.load(img)
        self.image = pg.Surface(coordinates)
        self.image.set_colorkey(PINK)
        self.image.blit(sprite, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.set_speed(speed)

    def set_groups(self, game):
        raise NotImplementedError(
            "'set_groups' method not implemented at sprite")

    def set_speed(self, speed: int):
        self.SPEED = speed
        self.reset_speed_changes()

    def reset_speed_changes(self):
        self.x_current_speed = 0
        self.y_current_speed = 0

    def check_collision(self, direction, sprite_group, dokill: bool = False):
        hits = pg.sprite.spritecollide(self, sprite_group, dokill)

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
