from dataclasses import dataclass
import pygame as pg

from entities.screen import Screen
from entities.commander import Commander
from entities.player import Player
from entities.character import Character


@dataclass
class Game_runner:
    @staticmethod
    def run():
        screen = Screen()
        screen.set_pause_display()

        Commander.screen = screen.display
        player1 = Player(
            Player.Player1,
            screen,
            Character(
                screen=screen, 
                strength=1,
                attack_range=100, 
                hability_power=10, 
                max_stamina=50)
        )

        player2 = Player(
            Player.Player2,
            screen,
            Character(
                screen=screen,
                strength=20,
                hability_power=10,
                max_stamina=200,
                max_life=200,
                color=(250, 0, 0, 1)
            )
        )

        Player.players = [player1, player2]

        while True:
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