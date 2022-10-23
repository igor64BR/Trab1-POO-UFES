from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Dict

from entities.character import Character

class Character_enum(Enum):
    Mage1 = 1
    Mage2 = 2
    Tank1 = 3
    Tank2 = 4
    Warrior1 = 5
    Warrior2 = 6
    Support1 = 7
    Support2 = 8
    Shooter1 = 9
    Shooter2 = 10
    

@dataclass
class Characters_lib:
    characters: ClassVar[Dict[Character_enum, Character]] = {
        Character_enum.Mage1: Character(2, 9, 100, (0, 0, 250, 1)),
        Character_enum.Mage2: Character(2, 9, 100, (0, 0, 250, 1)),
        Character_enum.Tank1: Character(2, 9, 100, (0, 250, 0, 1)),
        Character_enum.Tank2: Character(2, 9, 100, (0, 0, 250, 1)),
        Character_enum.Warrior1: Character(2, 9, 100, (250, 0, 0, 1)),
        Character_enum.Warrior2: Character(2, 9, 100, (0, 0, 250, 1)),
        Character_enum.Support1: Character(2, 9, 100, (250, 250, 250, 1)),
        Character_enum.Support2: Character(2, 9, 100, (0, 0, 250, 1)),
        Character_enum.Shooter1: Character(2, 9, 100, (250, 0, 250, 1)),
        Character_enum.Shooter2: Character(2, 9, 100, (0, 0, 250, 1))
    }