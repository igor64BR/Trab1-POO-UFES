from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Dict

from entities.abilities import Ability

class Ability_enum(Enum):
    Magic1 = 1
    Magic2 = 2
    Shield1 = 3
    Shield2 = 4
    Rage1 = 5
    Rage2 = 6
    Heal1 = 7
    Heal2 = 8
    Fire1 = 9
    Fire2 = 10
    

@dataclass
class Abilitys_lib:
    Abilitys: ClassVar[Dict[Ability_enum, Ability]] = {
        Ability_enum.magic1: Ability(2, 9, 100, (250, 0, 250, 1)),
        Ability_enum.magic2: Ability(2, 9, 100, (0, 0, 250, 1)),
        Ability_enum.shield1: Ability(2, 9, 100, (0, 250, 0, 1)),
        Ability_enum.shield2: Ability(2, 9, 100, (0, 0, 250, 1)),
        Ability_enum.rage1: Ability(2, 9, 100, (250, 0, 0, 1)),
        Ability_enum.rage2: Ability(2, 9, 100, (0, 0, 250, 1)),
        Ability_enum.heal1: Ability(2, 9, 100, (250, 250, 250, 1)),
        Ability_enum.heal2: Ability(2, 9, 100, (0, 0, 250, 1)),
        Ability_enum.fire1: Ability(2, 9, 100, (250, 0, 250, 1)),
        Ability_enum.fire2: Ability(2, 9, 100, (0, 0, 250, 1))
    }