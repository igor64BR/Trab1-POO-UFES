from typing import Dict
import pygame as pg


class Common_actions:
    def get_command(dict):
        keys = pg.key.get_pressed()
        
        for key, action in dict.items():
            if keys[key]:
                action()
        
        