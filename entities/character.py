from dataclasses import dataclass
from typing import Dict, Tuple
import pygame as pg


@dataclass
class Character:
    # TODO: Swap below props from ClassVar -> ObjectVar
    size = 10
    speed = 5
    
    # Attributes
    strength: int
    mobility: int
    stamina: int
    
    # Shape
    color: Tuple[int]
        
    def __post_init__(self):
        pass
    
    def set_initial_position(self, initial_position: Tuple[float]):
        self.x = initial_position[0]
        self.y = initial_position[1]
        
    def draw(self, screen):
        pg.draw.circle(
            surface=screen,
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
        