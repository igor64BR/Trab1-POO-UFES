import pygame as pg

from entities.sprites.sprite import Sprite
from entities.configs import *
from entities.sprites.characters.saci import *
from entities.sprites.characters.mula import *
from entities.sprites.characters.curupira import *
from entities.sprites.characters.cuca import *


class Player_base(Sprite):
    def __init__(self,
                 game,
                 x: int,
                 y: int,
                 character: str) -> None:
        super().__init__(game, x, y, layer=PLAYER_LAYER)

        self.controllable = True
        
        self.choose_character(character)
        self.set_enemy_sprite_collection()
        self.set_command()

    def update(self, *args, **kwargs) -> None:
        if self.controllable:
            self.get_all_commands()
            
        self.character.update()

    def get_all_commands(self):
        self.get_movement_commands()
        self.get_combat_commands()

    def get_movement_commands(self):
        self.get_commands(self.move_commands)

        self.rect.x += self.x_current_speed
        self.check_all_collisions('x')

        self.rect.y += self.y_current_speed
        self.check_all_collisions('y')

        self.reset_speed_changes()

    def get_combat_commands(self):
        self.get_commands(self.combat_commands)

    def get_commands(self, commands: dict):
        keys = pg.key.get_pressed()

        for key, action in commands.items():
            if keys[key]:
                action()

    def check_all_collisions(self, direction: str):
        self.check_collision(direction, self.game.block_sprites)
        self.check_collision(direction, self.enemy_sprite)
        self.check_collision(direction, self.game.minion_sprites)

    def move_up(self):
        self.move(UP, False, -1)

    def move_down(self):
        self.move(DOWN, False)

    def move_right(self):
        self.move(RIGHT, True)

    def move_left(self):
        self.move(LEFT, True, -1)

    def move(self, facing: str, x_speed_change: bool, magnitude: int = 1):
        self.facing = facing

        if x_speed_change:
            self.x_current_speed += magnitude * self.SPEED
        else:
            self.y_current_speed += magnitude * self.SPEED

    def choose_character(self, character: str):
        if character == SACI:
            self.character = Saci(self)

        if character == CUCA:
            self.character = Cuca(self)

        if character == CURUPIRA:
            self.character = Curupira(self)

        if character == MULA_SEM_CABECA:
            self.character = Mula(self)

    def set_enemy_sprite_collection(self):
        raise NotImplementedError(
            "'set_enemy_sprite' method not Implemented on Player class")

    def set_command(self):
        self.commands = {}
        raise NotImplementedError(
            "'set_command' method not Implemented on Player class")
