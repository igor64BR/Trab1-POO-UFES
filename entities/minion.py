from entities.sprite import Sprite
from entities.configs import *


class Minion(Sprite):
    def __init__(self, game, x: int, y: int) -> None:
        super().__init__(game, x, y, MINION_COLOR, MINION_LAYER)

        self.reset_speed_changes()

    def reset_speed_changes(self):
        self.x_current_speed = 0
        self.y_current_speed = 0

    def update(self):
        self.rect.x += self.x_current_speed
        self.rect.y += self.y_current_speed

        self.reset_speed_changes()

    def set_groups(self, game):
        self.game = game
        self.groups = self.game.all_sprites, self.game.minion_sprites
        