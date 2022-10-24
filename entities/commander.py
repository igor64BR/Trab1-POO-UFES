import sys
import time
from typing import Any, Callable, Dict
import pygame as pg


class Commander:
    screen = None
    game_is_paused = False

    def get_exit(event):
        quit_events = [
            event.type == pg.QUIT,
            event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE,
            pg.key.get_pressed()[pg.K_ESCAPE]
        ]

        if any(quit_events):
            print("Encerrando o programa.")
            sys.exit(0)

    def get_pause(event):
        if event.type != pg.KEYDOWN:
            return
            
        if event.key == pg.K_SPACE:
            Commander.game_is_paused = not Commander.game_is_paused  # toggle pause

    def get_command(dict):
        keys = pg.key.get_pressed()

        for key, action in dict.items():
            if keys[key]:
                action()
                pg.display.flip()

    def toggle_pause():
        Commander.game_is_paused = not Commander.game_is_paused
