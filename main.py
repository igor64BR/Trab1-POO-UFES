import time
from entities.characters_lib import Character_enum, Characters_lib
from entities.player import *
import pygame as pg
from entities.constants.screen import Display_Infos

def main():
    pg.init()

    screen = pg.display.set_mode((Display_Infos.SCREEN_WIDTH, Display_Infos.SCREEN_HEIGHT))

    player1 = Player(Player.Player1, screen, 
        (
            Characters_lib.characters[Character_enum.Mage1],
            Characters_lib.characters[Character_enum.Shooter1],
            Characters_lib.characters[Character_enum.Support1],
            Characters_lib.characters[Character_enum.Tank1],
            Characters_lib.characters[Character_enum.Warrior1],
        )
    )
    
    player2 = Player(Player.Player2, screen, 
        (
            Characters_lib.characters[Character_enum.Mage2],
            Characters_lib.characters[Character_enum.Shooter2],
            Characters_lib.characters[Character_enum.Support2],
            Characters_lib.characters[Character_enum.Tank2],
            Characters_lib.characters[Character_enum.Warrior2],
        )
    )

    while True:
        for event in pg.event.get():
            quit_events = [
                event.type == pg.QUIT,
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE,
                pg.key.get_pressed()[pg.K_ESCAPE]
            ]

            if any(quit_events):
                print("Encerrando o programa.")
                return
        
        screen.fill(Display_Infos.BG_COLOR)
        
        player1.execute()
        player2.execute()
        
        time.sleep(0.01)
        pg.display.flip()
            
            
if __name__ == '__main__':
    main()
