from entities.sprites.characters.character import Character
from entities.configs import *


class Curupira(Character):
    def __init__(self, player) -> None:
        super().__init__(player, CURUPIRA_PATH, CURUPIRA, 3)
