from entities.sprites.characters.character import Character
from entities.configs import *


class Saci(Character):
    def __init__(self, player) -> None:
        self.player = player
        self.player.name = SACI
        self.player.SPEED = 3
