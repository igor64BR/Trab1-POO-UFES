from entities.characters.character import Character
from entities.configs import *


class Curupira(Character):
    def __init__(self, player) -> None:
        self.player = player
        self.player.name = CURUPIRA
        self.player.SPEED = 3
