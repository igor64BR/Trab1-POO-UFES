import time
from entities.characters_lib import Character_enum, Characters_lib
from entities.player import *
import pygame as pg
from entities.constants.screen import Display_Infos


def main():
    pg.init()

    screen = pg.display.set_mode(
        (Display_Infos.SCREEN_WIDTH, Display_Infos.SCREEN_HEIGHT))

    Commander.screen = screen

    player1 = Player(Player.Player1, screen,
                     (
                         Characters_lib.characters[Character_enum.Mage1],
                         Characters_lib.characters[Character_enum.Shooter1],
                         Characters_lib.characters[Character_enum.Support1],
                         Characters_lib.characters[Character_enum.Tank1],
                         Characters_lib.characters[Character_enum.Warrior1],
                     ))

    player2 = Player(Player.Player2, screen,
                     (
                         Characters_lib.characters[Character_enum.Mage2],
                         Characters_lib.characters[Character_enum.Shooter2],
                         Characters_lib.characters[Character_enum.Support2],
                         Characters_lib.characters[Character_enum.Tank2],
                         Characters_lib.characters[Character_enum.Warrior2],
                     ))

    # TODO: Fix p2 commands
    while True:
        Commander.get_pause()
        Commander.get_exit()

        if Commander.game_is_paused:
            continue

        screen.fill(Display_Infos.BG_COLOR)

        player1.execute()
        player2.execute()

if __name__ == '__main__':
    main()
