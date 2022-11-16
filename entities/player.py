from __future__ import annotations
from typing import ClassVar, Dict, List
from dataclasses import dataclass
import pygame as pg
from entities.commander import Commander
from entities.characters.character import Character
from entities.characters.character_phisics import Character_body
from entities.screen import Screen


@dataclass
class Player:
    Player1: ClassVar[int] = 0
    Player2: ClassVar[int] = 1

    players: ClassVar[List[Player]]

    __player: int
    __screen: Screen
    character: Character

    def __post_init__(self):

        self.ininitial_position = self.__screen.get_initial_positions(
            self.__player)

        self.character.body.set_initial_position(self.ininitial_position)

        Character_body.characters.append(self.character.body)
        self.__set_commands()

    def execute(self):
        self.character.update_skill()
        self.character.body.draw()
        Commander.get_continuous_commands(self.commands)

        # TODO: Fix: not working
        # Commander.get_keydown_commands(self.combat_commands)

    def __set_commands(self):
        self._P1_COMMANDS: Dict = {
            pg.K_w: self.character.body.move_up,
            pg.K_s: self.character.body.move_down,
            pg.K_a: self.character.body.move_left,
            pg.K_d: self.character.body.move_right,

            # TODO: Move to combat_commands
            pg.K_f: self.character.body.attack,
            pg.K_e: self.character.try_run_skill
        }

        self._P1_COMBAT_COMMANDS = {
            # pg.K_f: self.character.body.attack,
            # pg.K_c: self.character.body.skill_start
        }

        self._P2_COMMANDS: Dict = {
            pg.K_i: self.character.body.move_up,
            pg.K_k: self.character.body.move_down,
            pg.K_j: self.character.body.move_left,
            pg.K_l: self.character.body.move_right,

            # TODO: Move to combat_commands
            pg.K_h: self.character.body.attack,
            pg.K_u: self.character.try_run_skill
        }

        self._P2_COMBAT_COMMANDS = {
            # pg.K_h: self.character.body.attack,
            # pg.K_n: self.character.body.skill_start
        }

        player = self.__player
        self.commands = (self._P1_COMMANDS, self._P2_COMMANDS)[player]
        self.combat_commands = (self._P1_COMBAT_COMMANDS, self._P2_COMBAT_COMMANDS)[player]
