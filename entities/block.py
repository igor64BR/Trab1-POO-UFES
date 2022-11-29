import pygame as pg

from entities.configs import *
from entities.sprite import Sprite


class Block(Sprite):
    def __init__(self, game, x, y) -> None:
        super().__init__(game, x, y, GREEN)

    def set_groups(self, game):
        self.game = game
        self.groups = self.game.all_sprites, self.game.block_sprites
