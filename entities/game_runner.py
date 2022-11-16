from dataclasses import dataclass
import pygame as pg
from cronometro import Cronometro

from entities.screen import Screen
from entities.commander import Commander
from entities.player import Player
from entities.characters.character import Character
from entities.characters.saci import Saci


@dataclass
class Game_runner:
    @staticmethod
    def run(cronometro: 'Cronometro'):
        
        screen = Screen(cronometro)

        Commander.screen = screen.display
        player1 = Player(
            Player.Player1,
            screen,
            Saci(screen, Player.Player1)
        )

        player2 = Player(
            Player.Player2,
            screen,
            Saci(screen, Player.Player2)
        )

        Player.players = [player1, player2]

        Character.cronometro = cronometro

        while True:
            screen.show_time()

            pg.display.update()

            for event in pg.event.get():
                Commander.get_exit(event)
                Commander.get_pause(event)

            if Commander.game_is_paused:
                screen.show_pause()
                continue

            screen.reset_display()

            for player in Player.players:
                player.execute()
