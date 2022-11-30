from entities.characters.character import Character
from entities.configs import *


class Mula(Character):
    def __init__(self, player) -> None:
        self.player = player
        self.player.name = MULA_SEM_CABECA
        self.player.SPEED = 6
