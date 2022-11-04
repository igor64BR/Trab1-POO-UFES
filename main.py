from entities.characters_lib import Character_enum, Characters_lib
from entities.player import *
from entities.screen import Screen
import pygame as pg


def main():
    pg.init()
    screen = Screen()
    Commander.screen = screen.display
    player1 = Player(Player.Player1, screen, Character(10, 10))
    player2 = Player(Player.Player2, screen, Character(10, 10, 200, 200, (250, 0, 0, 1)))

    while True:
        pg.display.update()

        for event in pg.event.get():
            Commander.get_exit(event)
            Commander.get_pause(event)

        if Commander.game_is_paused:
            screen.show_pause()
            continue

        screen.reset_display()

        player1.execute()
        player2.execute()


if __name__ == '__main__':
    main()
