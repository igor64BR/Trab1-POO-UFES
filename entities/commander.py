import sys
import time
from turtle import screensize
import pygame as pg


class Commander:
    screen = None
    game_is_paused = False

    def get_exit():
        for event in pg.event.get():
            quit_events = [
                event.type == pg.QUIT,
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE,
                pg.key.get_pressed()[pg.K_ESCAPE]
            ]

            if any(quit_events):
                print("Encerrando o programa.")
                sys.exit(0)

    def get_pause():
        command = { pg.K_SPACE: Commander.toggle_pause, }

        Commander.get_command(command)

    def get_command(dict) -> bool:
        keys = pg.key.get_pressed()
        
        for key, action in dict.items():
            if keys[key]:
                action()
                pg.display.flip()
                time.sleep(0.1)
        

    def toggle_pause():
        Commander.game_is_paused = not Commander.game_is_paused
        