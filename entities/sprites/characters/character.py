import pygame as pg

from cronometro import Cronometro


class Character:
    def __init__(self, player, img: str, name: str, speed: int = 3, max_life: int = 100, damage: int = 5) -> None:
        self.set_player_attributes(player, img, name, speed, max_life, damage)
        self.init_skill()
        self.init_basic_attack()
        self.init_mutate()

    def init_mutate(self):
        """Sets mutate character skill initial statuses"""
        self.mutate_skill_is_running = False
        self.mutate_character_start_moment = None
        self.mutate_last_cast_moment = None

        self.LIFE_DEBUFF = 70 / 100
        self.AUTO_ATTACK_BUFF = 120 / 100

    def init_basic_attack(self):
        """Sets basic attack initial statuses"""
        self.basic_attack_start_moment = None
        self.basic_attack_is_running = False

    def init_skill(self):
        """Sets skill initial statuses"""
        self.skill_is_running = False
        self.skill_start_moment = None
        self.skill_last_cast_moment = None

    def set_player_attributes(self, player, img, name, speed, max_life, damage):
        self.game = player.game
        self.player = player

        self.player.name = name
        self.player.SPEED = speed

        self.player.attack_damage = damage
        self.player.MAX_LIFE = max_life
        self.player.current_life = self.player.MAX_LIFE

        sprite = pg.image.load(img)
        self.player.image.blit(sprite, (0, 0))

        self.cronometro = Cronometro()

    def update(self):
        self.update_mutate_character()
        # self.update_skill()
        # self.update_basic_attack()

    def basic_attack(self):
        raise NotImplementedError(
            f"'basic_attack' method not implemented on character")

    def start_mutate_character(self):
        self.mutate_skill_is_running = True

        self.mutated_character = self.choose_character()

        self.mutated_character.player.MAX_LIFE *= self.LIFE_DEBUFF
        self.mutated_character.player.current_life *= self.LIFE_DEBUFF

        self.mutated_character.player.attack_damage *= self.AUTO_ATTACK_BUFF

        self.mutation_initial_time = self.cronometro.start_new_reference_time()

    def end_mutate_character(self):
        self.mutate_skill_is_running = False

        self.mutated_character.player.MAX_LIFE /= self.LIFE_DEBUFF
        self.mutated_character.player.current_life /= self.LIFE_DEBUFF

        self.mutated_character.player.attack_damage /= self.AUTO_ATTACK_BUFF

        self.mutate_last_cast_moment = self.cronometro.start_new_reference_time()

        self.mutated_character = None
        self.mutation_initial_time = None

    def update_mutate_character(self):
        if not self.mutate_skill_is_running:
            return

        MUTATION_DURATION = 5  # seconds
        time_spent = self.cronometro.get_time_spent(self.mutation_initial_time)

        if time_spent > MUTATION_DURATION:
            self.end_mutate_character()

    def try_start_mutation_skill(self):
        SKILL_COOL_DOWN = 10  # seconds

        skill_in_cool_down = self.cronometro.get_time_spent(self.mutate_last_cast_moment) <= SKILL_COOL_DOWN

        if self.mutate_last_cast_moment != None and skill_in_cool_down:
            return

        if not self.mutate_skill_is_running:
            self.start_mutate_character()

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
