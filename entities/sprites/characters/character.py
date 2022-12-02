import pygame as pg

class Character:
    def __init__(self, player, img: str, name: str, speed: int = 3) -> None:
        self.game = player.game
        self.player = player
        self.player.name = name
        self.player.SPEED = speed

        sprite = pg.image.load(img)
        self.player.image.blit(sprite, (0,0))

    def basic_attack(self):
        raise NotImplementedError(
            f"'basic_attack' method not implemented on character")

    def start_mutate_character(self):
        # self.player.game.game_is_paused = True
        # self.character_mutation = True
        pass

    def end_mutate_character(self):
        pass

    def update_mutate_character(self):
        pass

    def start_skill(self):
        raise NotImplementedError(
            f"'start_skill' method not implemented on character")

    def end_skill(self):
        raise NotImplementedError(
            f"'end_skill' method not implemented on character")

    def update_skill(self):
        raise NotImplementedError(
            f"'update_skill' method not implemented on character")

