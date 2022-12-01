from entities.sprites.characters.character import Character
from entities.configs import *


class Cuca(Character):
    def __init__(self, player) -> None:
        self.player = player
        self.player.name = CUCA
        self.player.SPEED = 4

        sprite = pg.image.load(CUCA_PATH)
        self.player.image.blit(sprite, (0,0))