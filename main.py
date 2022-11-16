import pygame
from entities.menu_principal import Menu
from entities.game_runner import Game_runner
from cronometro import Cronometro

if __name__ == '__main__':
    pygame.init()
    # Menu()
    Game_runner.run(Cronometro())