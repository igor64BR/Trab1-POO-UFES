from ast import Dict
from varname import nameof
from cronometro import Cronometro
from entities.characters.character_phisics import Character_body
from entities.characters.character import Character
from entities.screen import Screen

class Saci(Character):
    def __init__(self, screen: 'Screen', player_index: int) -> None:
        Character.__init__(self)

        self.body = Character_body(
            screen=screen,
            player=player_index,
            strength=1,
            attack_range=100,
            hability_power=10,
            max_stamina=50)

        self.ORIGINAL_CHARACTER_SPEED = self.body.speed
        self.ORIGINAL_CHARACTER_ATTACK_RANGE = self.body.attack_range

        self.skill_duration = 4
        self.skill_cooldown = 3

    def run_skill(self):
        """
        Saci se transforma em um tornado, ganhando velocidade,
        se impossibilitando de atacar e dando dano a todos aqueles
        que encosta
        """

        self.set_skill_on()

        SPEED_INCREMENT = 3

        self.body.speed *= SPEED_INCREMENT
        self.body.attack_range = self.body.size


    def end_skill(self):
        print('skill ended')

        self.body.speed = self.ORIGINAL_CHARACTER_SPEED
        self.body.attack_range = self.ORIGINAL_CHARACTER_ATTACK_RANGE

        self.set_skill_of()

    def update_skill(self):
        super().update_skill()

        if not self.skill_is_running:
            return

        self.body.attack()
