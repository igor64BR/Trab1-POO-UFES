from imp import init_builtin
from mimetypes import common_types
from turtle import screensize
from typing import Dict
import pygame as pg

from constants.screen import Display_Infos

class Player:
    PLAYER_COLORS = {
        0: (250, 0, 0, 1),
        1: (0, 250, 0, 1)
    }
    
    INITIAL_POSITIONS = {
        0: (Display_Infos.PX, Display_Infos.PX),
        1: (Display_Infos.SCREEN_WIDTH - Display_Infos.PX, Display_Infos.SCREEN_HEIGHT - Display_Infos.PX)
    }
    
    def __init__(self, player: int, screen) -> None:
        self.screen = screen
        self.color = Player.PLAYER_COLORS[player]
        
        self.initial_position = Player.INITIAL_POSITIONS[player]
        self.x = self.initial_position[0]
        self.y = self.initial_position[1]
        
        self.P1_COMMANDS: Dict = {
            pg.K_w: self.move_up,
            pg.K_s: self.move_down,
            pg.K_a: self.move_left,
            pg.K_d: self.move_right
        }
        
        self.P2_COMMANDS: Dict = {
            pg.K_i: self.move_up,
            pg.K_k: self.move_down,
            pg.K_j: self.move_left,
            pg.K_l: self.move_right
        }
        
        self.commands = (self.P1_COMMANDS, self.P2_COMMANDS)[player]
        
        # Attributes
        self.size = 20
        self.speed = 1
    
    def execute(self):
        self.get_command()
        self.draw()
    
    def get_command(self):
        keys = pg.key.get_pressed()
        
        for tecla, action in self.commands.items():
            if keys[tecla]:
                action()
        
    def draw(self):
        pg.draw.circle(
            surface=self.screen,
            color=self.color,
            center=(self.x, self.y),
            radius=self.size,
            width=0
        )
    
    def move_up(self):
        self.y -= self.speed
        
    def move_down(self):
        self.y += self.speed
    
    def move_right(self):
        self.x += self.speed
    
    def move_left(self):
        self.x -= self.speed
    

