from cronometro import Cronometro
from entities.characters.character_phisics import Character_body
from entities.screen import Screen

class Character:
    cronometro: 'Cronometro'

    def __init__(self) -> None:
        self.skill_is_running = False
        self.skill_start_moment = None
        self.last_skill_usage_time = None

    def try_run_skill(self):
        if self.skill_is_running:
            return

        if self.last_skill_usage_time != None:
            last_skill_usage_time = Character.cronometro.get_time_spent(self.last_skill_usage_time)
            
            if last_skill_usage_time <= self.skill_cooldown:
                print('skill em cooldown')
                return

        self.run_skill()
    
    def run_skill(self):
        raise NotImplementedError("Habilidade não implementada")

    def end_skill(self):
        raise NotImplementedError("Habilidade não implementada")

    def update_skill(self):
        raise NotImplementedError("Método não implementado")

    def set_skill_on(self) -> bool:
        self.skill_start_moment = Character.cronometro.start_new_reference_time()
        self.skill_is_running = True

    def set_skill_of(self):
        self.last_skill_usage_time = Character.cronometro.start_new_reference_time()
        self.skill_is_running = False

    def update_skill(self):
        if self.skill_start_moment is None:
            return

        time_spent = Character.cronometro.get_time_spent(self.skill_start_moment)

        if self.skill_is_running and time_spent >= self.skill_duration:
            self.end_skill()
