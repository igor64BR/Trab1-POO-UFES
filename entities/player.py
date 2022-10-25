from dataclasses import dataclass
from operator import indexOf
from typing import Any, ClassVar, Dict, Tuple
import pygame as pg
from entities.commander import Commander

from entities.constants.screen import Display_Infos
from entities.character import Character

@dataclass
class Player:
    Player1: ClassVar[int] = 0
    Player2: ClassVar[int] = 1
    
    Player1_initial_position: ClassVar[Tuple[float]] = (Display_Infos.PX, Display_Infos.PX)
    Player2_initial_position: ClassVar[Tuple[float]] = (
        Display_Infos.SCREEN_WIDTH - Display_Infos.PX, 
        Display_Infos.SCREEN_HEIGHT - Display_Infos.PX, 
    )
    
    __player: int
    screen: Any
    character: Character
    
    def __post_init__(self):
        
        self.ininitial_position = (Player.Player1_initial_position, Player.Player2_initial_position)[self.__player]
            
        self.character.set_initial_position(self.ininitial_position)
        
        self.__set_commands()
    
    def execute(self):
        self.character.draw(self.screen)
        Commander.get_command(self.commands)
    
    def __set_commands(self):
        self._P1_COMMANDS: Dict = {
            pg.K_w: self.character.move_up,
            pg.K_s: self.character.move_down,
            pg.K_a: self.character.move_left,
            pg.K_d: self.character.move_right
        }
        
        self._P2_COMMANDS: Dict = {
            pg.K_i: self.character.move_up,
            pg.K_k: self.character.move_down,
            pg.K_j: self.character.move_left,
            pg.K_l: self.character.move_right
        }
        
        self.commands = (self._P1_COMMANDS, self._P2_COMMANDS)[self.__player]
        