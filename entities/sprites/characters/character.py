import pygame as pg

from cronometro import Cronometro


class Character:
    def __init__(self, player, img: str, name: str, speed: int = 3, max_life: int = 100) -> None:
        self.set_player_attributes(player, img, name, speed, max_life)
        self.init_skill()
        self.init_basic_attack()
        self.init_mutate()

    def init_mutate(self):
        """Sets mutate character skill initial statuses"""
        self.mutate_skill_is_running = False
        self.mutate_character_start_moment = None
        self.mutate_last_cast_moment = None

    def init_basic_attack(self):
        """Sets basic attack initial statuses"""
        self.basic_attack_start_moment = None
        self.basic_attack_is_running = False

    def init_skill(self):
        """Sets skill initial statuses"""
        self.skill_is_running = False
        self.skill_start_moment = None
        self.skill_last_cast_moment = None

    def set_player_attributes(self, player, img, name, speed, max_life):
        self.game = player.game
        self.player = player

        self.player.name = name
        self.player.SPEED = speed

        self.player.MAX_LIFE = max_life
        self.current_life = self.player.MAX_LIFE

        sprite = pg.image.load(img)
        self.player.image.blit(sprite, (0, 0))

        self.cronometro = Cronometro()

    def basic_attack(self):
        raise NotImplementedError(
            f"'basic_attack' method not implemented on character")

    def start_mutate_character(self):
        self.mutate_skill_is_running = True

        self.chosen_mutated_character = self.choose_character()

    def end_mutate_character(self):
        self.mutate_skill_is_running = False
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

    def choose_character(self):
        """
            Pauses the screen. 
            The user must choose with the mouse which player
            will get the buffs and debuffs
        """
        return self
