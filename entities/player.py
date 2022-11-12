from __future__ import annotations
from typing import ClassVar, Dict, List
from dataclasses import dataclass
import pygame as pg
from entities.commander import Commander
from entities.character import Character
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

        self.character.set_initial_position(self.ininitial_position)

        Character.characters.append(self.character)
        self.__set_commands()

    def execute(self):
        self.character.draw()
        Commander.get_command(self.commands)

    def __set_commands(self):
        self._P1_COMMANDS: Dict = {
            pg.K_w: self.character.move_up,
            pg.K_s: self.character.move_down,
            pg.K_a: self.character.move_left,
            pg.K_d: self.character.move_right,
            pg.K_f: self.character.attack
        }

        self._P2_COMMANDS: Dict = {
            pg.K_i: self.character.move_up,
            pg.K_k: self.character.move_down,
            pg.K_j: self.character.move_left,
            pg.K_l: self.character.move_right,
            pg.K_h: self.character.attack
        }

        self.commands = (self._P1_COMMANDS, self._P2_COMMANDS)[self.__player]
