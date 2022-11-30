import pygame as pg

import sys
from entities.block import Block

from entities.configs import *
from entities.minion import Minion
from entities.players import Player1, Player2


class Game:
    def __init__(self) -> None:
        pg.init()

        self.screen = pg.display.set_mode(SCREEN_DIMENSIONS)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('courier new', 32)

        self.game_is_running = True

    def run(self):
        # game.intro_screen()
        self.start_new_game()
        while self.game_is_running:
            self.main()
            # game.game_over()

    def start_new_game(self):
        self.user_is_playing = True

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.player1_sprite = pg.sprite.LayeredUpdates()
        self.player2_sprite = pg.sprite.LayeredUpdates()
        self.player_sprites = pg.sprite.LayeredUpdates()
        
        self.minion_sprites = pg.sprite.LayeredUpdates()

        self.block_sprites = pg.sprite.LayeredUpdates()
        self.projectile_sprites = pg.sprite.LayeredUpdates()

        self.p1 = pg.sprite.LayeredUpdates()
        self.p2 = pg.sprite.LayeredUpdates()

        self.create_tile_map()
        
        [minion.set_other_minions() for minion in self.minion_sprites.sprites()]

    def create_tile_map(self):
        BLOCK = 'B'
        PLAYER1 = '1'
        PLAYER2 = '2'
        MINION = 'M'

        for i, row in enumerate(TILE_MAP):
            for j, field in enumerate(row):
                if field == BLOCK:
                    Block(self, j, i)

                elif field == PLAYER1:
                    Player1(self, j, i, RED)

                elif field == PLAYER2:
                    Player2(self, j, i, BLUE)

                elif field == MINION:
                    Minion(self, j, i)

    def main(self):
        while self.user_is_playing:
            self.get_events()
            self.update()
            self.draw()

        self.game_is_running = False

    def get_events(self):
        for event in pg.event.get():
            clicked_x_button = event.type == pg.QUIT
            pressed_ESC = event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE

            if clicked_x_button or pressed_ESC:
                self.game_is_running = False
                self.user_is_playing = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FRAMERATE)
        pg.display.update()
