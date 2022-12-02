from entities.sprites.characters.character import Character
from entities.configs import *


class Cuca(Character):
    def __init__(self, player) -> None:
        super().__init__(player, CUCA_PATH, CUCA, 4)
