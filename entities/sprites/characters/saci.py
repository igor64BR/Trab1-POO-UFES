import math
import time
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

    def try_start_skill(self):
        SKILL_COOL_DOWN = 0  # seconds
        # SKILL_COOL_DOWN = 5  # seconds

        self.try_start_action(
            SKILL_COOL_DOWN,
            self.skill_last_cast_moment,
            self.skill_is_running,
            self.start_skill
        )

    def start_skill(self):
        self.skill_is_running = True

        self.set_speeds()

        self.player.controllable = False

        self.skill_initial_time = self.cronometro.start_new_reference_time()

    def end_skill(self):
        print('skill_ended')
        self.skill_is_running = False
        self.player.controllable = True
        self.player.reset_speed_changes()

        self.skill_last_cast_moment = self.cronometro.start_new_reference_time()

    def update_skill(self):
        SKILL_DURATION = 1  # seconds

        if not self.skill_is_running:
            return

        self.try_end_action(
            SKILL_DURATION,
            self.skill_initial_time,
            self.end_skill
        )

        self.move_involuntarily()

    def move_involuntarily(self):
        player = self.player

        player.rect.x += player.x_current_speed
        self.check_collision_with_enemy()
        player.check_all_collisions('x')

        player.rect.y += player.y_current_speed
        self.check_collision_with_enemy()
        player.check_all_collisions('y')

    def check_collision_with_enemy(self):
        if self.player.check_collision('x', self.player.enemy_sprite) or \
                self.player.check_collision('y', self.player.enemy_sprite):
            self.end_skill()

    def set_speeds(self):
        player = self.player

        enemy = player.enemy_sprite.sprites()[0]

        x_distance = player.rect.x - enemy.rect.x
        y_distance = player.rect.y - enemy.rect.y

        player.reset_speed_changes()
        
        if x_distance != 0:
            player.x_current_speed = player.SPEED 
            player.x_current_speed *= -(x_distance / abs(x_distance))
            player.x_current_speed *= 3

        if y_distance != 0:
            player.y_current_speed = player.SPEED 
            player.y_current_speed *= -(y_distance / abs(y_distance)) 
            player.y_current_speed *= 3
