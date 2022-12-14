import pygame as pg

# screen
SCREEN_WIDTH = 672
SCREEN_HEIGHT = 480
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

MENU_WIDTH = 1280
MENU_HEIGHT = 720
MENU_DIMENSIONS = (MENU_WIDTH, MENU_HEIGHT)

FRAMERATE = 60

TILE_SIZE = 32  # pixels

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 0, 208)

MINION_COLOR = (0, 255, 255)

TEXT_COLOR = '#d7fcd4'

# layers
PLAYER_LAYER = 4
MINION_LAYER = 3
ABILITIES_LAYER = 2
BLOCK_LAYER = 1

# directions
RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

# character names
SACI = 'Saci'
CUCA = 'Cuca'
CURUPIRA = 'Curupira'
MULA_SEM_CABECA = 'Mula-sem-cabeça'

# character paths
SACI_PATH = 'img/Saci.png'
CUCA_PATH = 'img/Cuca.png'
CURUPIRA_PATH = 'img/Curupira.png'
MULA_SEM_CABECA_PATH = 'img/MulaSemCabeca.png'
MINION_PATH = 'img/Cacador.png'

ALL_CHARACTERS = [SACI, CUCA, CURUPIRA, MULA_SEM_CABECA]

# B = block, 1 = player 1, 2 = player 2, M = minion
TILE_MAP = [
    'BBBBBBBBBBBBBBBBBBBBB',
    'B...................B',
    'B.1.................B',
    'B...................B',
    'B....BBB.......M....B',
    'B......B............B',
    'B......B....BBB.....B',
    'B......B......B.....B',
    'B.............B.....B',
    'B...........BBB.....B',
    'B...................B',
    'B.....M.............B',
    'B.................2.B',
    'B...................B',
    'BBBBBBBBBBBBBBBBBBBBB',
]
