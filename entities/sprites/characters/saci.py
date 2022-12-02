from entities.sprites.characters.character import Character
from entities.configs import *


class Saci(Character):
    def __init__(self, player) -> None:
        super().__init__(
            player,
            img=SACI_PATH,
            name=SACI,
            speed=3
        )
