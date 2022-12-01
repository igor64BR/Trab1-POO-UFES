from entities.sprites.characters.character import Character
from entities.configs import *


class Mula(Character):
    def __init__(self, player) -> None:
        self.player = player
        self.player.name = MULA_SEM_CABECA
        self.player.SPEED = 6

        sprite = pg.image.load(MULA_SEM_CABECA_PATH)
        self.player.image.blit(sprite, (0,0))