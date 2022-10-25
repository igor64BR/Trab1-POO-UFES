from entities.characters_lib import Character_enum, Characters_lib
from entities.player import *
import pygame as pg
from entities.constants.screen import Display_Infos


def main():
    pg.init()

    screen = pg.display.set_mode(
        (Display_Infos.SCREEN_WIDTH, Display_Infos.SCREEN_HEIGHT))

    font = pg.font.SysFont('courier new', 50, True)
    pause_text = font.render("PAUSED", True, (250, 250, 250), (0, 0, 0))
    pause_text_area = pause_text.get_rect()
    pause_text_area.center = (
        Display_Infos.SCREEN_WIDTH // 2, Display_Infos.SCREEN_HEIGHT // 2)

    Commander.screen = screen

    player1 = Player(Player.Player1, screen,
                     Characters_lib.characters[Character_enum.Mage1])

    player2 = Player(Player.Player2, screen,
                     Characters_lib.characters[Character_enum.Mage2])

    # TODO: Fix p2 commands
    while True:
        pg.display.update()

        for event in pg.event.get():
            Commander.get_exit(event)
            Commander.get_pause(event)

        if Commander.game_is_paused:
            screen.blit(pause_text, pause_text_area)
            continue

        screen.fill(Display_Infos.BG_COLOR)

        player1.execute()
        player2.execute()


if __name__ == '__main__':
    main()
