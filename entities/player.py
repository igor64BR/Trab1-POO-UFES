from dataclasses import dataclass
from operator import indexOf
from typing import Any, ClassVar, Dict, Tuple
import pygame as pg
from entities.common_actions import Common_actions

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
    
    player: int
    screen: Any
    characters: Tuple[Character]
    
    def __post_init__(self):
        
        for character in self.characters:
            initial_positions = (Player.Player1_initial_position, Player.Player2_initial_position)
            
            character.set_initial_position(initial_positions[self.player])
        
        self.current_character = self.characters[0]
        
        self.set_commands()
    
    def execute(self):
        self.swap_character()
        
        Common_actions.get_command(self.commands)
        self.draw_characters()
        
    def get_previous_character(self):
        self.get_character()
        
    def get_next_character(self):
        self.get_character(next=True)
    
    def get_character(self, next: bool = False):
        char_index = self.get_new_char_index(next)
        
        self.current_character = self.characters[char_index]
        
        self.set_commands()
        
        pass
    
    def swap_character(self):
        p1_swap_commands = {
            pg.K_q: self.get_previous_character,
            pg.K_e: self.get_next_character
        }
        
        p2_swap_commands = {
            pg.K_u: self.get_previous_character,
            pg.K_o: self.get_next_character
        }
        
        swap_commands = (p1_swap_commands, p2_swap_commands)
        
        Common_actions.get_command(swap_commands[self.player])
        pass
    
    def set_commands(self):
        self._P1_COMMANDS: Dict = {
            pg.K_w: self.current_character.move_up,
            pg.K_s: self.current_character.move_down,
            pg.K_a: self.current_character.move_left,
            pg.K_d: self.current_character.move_right
        }
        
        self._P2_COMMANDS: Dict = {
            pg.K_i: self.current_character.move_up,
            pg.K_k: self.current_character.move_down,
            pg.K_j: self.current_character.move_left,
            pg.K_l: self.current_character.move_right
        }
        
        self.commands = (self._P1_COMMANDS, self._P2_COMMANDS)[self.player]
        
    def draw_characters(self):
        for character in self.characters:
            character.draw(self.screen)

    def get_new_char_index(self, next) -> int:
        last_index = len(self.characters) - 1

        char_index = self.characters.index(self.current_character)
        
        if not next:
            return char_index - 1
        
        if char_index < last_index:
            return char_index + 1

        FIRST_ITEM_INDEX = 0
        
        return FIRST_ITEM_INDEX
    