from entities.sprites.characters.character import Character
from entities.configs import *


class Mula(Character):
    def __init__(self, player) -> None:
        super().__init__(
            player,
            img=MULA_SEM_CABECA_PATH,
            name=MULA_SEM_CABECA,
            speed=6
        )
