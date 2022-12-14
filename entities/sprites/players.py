import pygame as pg

from entities.sprites.player_base import Player_base


class Player1(Player_base):
    def set_groups(self, game):
        self.game = game
        self.groups = self.game.all_sprites, self.game.player1_sprite, self.game.player_sprites

    def set_enemy_sprite_collection(self):
        self.enemy_sprite = self.game.player2_sprite

    def set_command(self):
        self.move_commands = {
            pg.K_w: self.move_up,
            pg.K_s: self.move_down,
            pg.K_d: self.move_right,
            pg.K_a: self.move_left,
        }

        self.combat_commands = {
            pg.K_q: self.character.try_start_mutation_skill,
            pg.K_e: self.character.try_start_skill,
        }


class Player2(Player_base):
    def set_groups(self, game):
        self.game = game
        self.groups = self.game.all_sprites, self.game.player2_sprite, self.game.player_sprites

    def set_enemy_sprite_collection(self):
        self.enemy_sprite = self.game.player1_sprite

    def set_command(self):
        self.move_commands = {
            pg.K_i: self.move_up,
            pg.K_k: self.move_down,
            pg.K_l: self.move_right,
            pg.K_j: self.move_left,
        }

        self.combat_commands = {
            pg.K_u: self.character.try_start_mutation_skill,
            pg.K_o: self.character.try_start_skill,
        }
