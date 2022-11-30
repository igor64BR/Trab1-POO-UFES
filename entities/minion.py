import math
from entities.player_base import Player_base
from entities.sprite import Sprite
from entities.configs import *


class Minion(Sprite):
    def __init__(self, game, x: int, y: int) -> None:
        super().__init__(game, x, y, MINION_COLOR, layer=MINION_LAYER, speed=1)

    def update(self):
        self.move_to_closest_player()

    def set_groups(self, game):
        self.game = game
        self.groups = self.game.all_sprites, self.game.minion_sprites

    def set_other_minions(self):
        self.other_minions_sprites = pg.sprite.LayeredUpdates()
        
        other_minions = [sprite for sprite in self.game.minion_sprites.sprites() if sprite != self]
        self.other_minions_sprites.add(other_minions)

    def get_closest_player(self):
        players = self.game.player_sprites.sprites()

        distances = {}

        for player in players:
            distance = self.get_distance_from(player)
            distances[distance] = player

        return distances[min(distances.keys())]

    def get_distance_from(self, player: Player_base):
        x_distance = self.rect.x - player.rect.x
        y_distance = self.rect.y - player.rect.y

        return math.sqrt(x_distance ** 2 + y_distance ** 2)

    def check_all_collisions(self, direction: str):
        self.check_collision(direction, self.game.block_sprites)
        self.check_collision(direction, self.game.player_sprites)
        self.check_collision(direction, self.other_minions_sprites)

    def move_to_closest_player(self):
        player = self.get_closest_player()

        x_distance = self.rect.x - player.rect.x
        y_distance = self.rect.y - player.rect.y

        if x_distance != 0:
            self.x_current_speed = self.SPEED * -(x_distance / abs(x_distance))

        if y_distance != 0:
            self.y_current_speed = self.SPEED * -(y_distance / abs(y_distance))

        self.rect.x += self.x_current_speed
        self.check_all_collisions('x')
        self.rect.y += self.y_current_speed
        self.check_all_collisions('y')

        self.reset_speed_changes()
