import pygame as pg
from entities.configs import *


class Sprite(pg.sprite.Sprite):
    def __init__(self,
                 game,
                 x: int,
                 y: int,
                 color: tuple[int],
                 layer: int
                 ) -> None:
        self.set_groups(game)
        self._layer = layer

        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        coordinates = [self.width, self.height]

        self.image = pg.Surface(coordinates)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_groups(self, game):
        raise NotImplementedError(
            "'set_groups' method not implemented at sprite")
