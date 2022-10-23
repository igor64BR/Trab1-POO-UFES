from entities.player import *
import pygame as pg
from constants.screen import Display_Infos

def main():
    pg.init()

    screen = pg.display.set_mode((Display_Infos.SCREEN_WIDTH, Display_Infos.SCREEN_HEIGHT))

    player1 = Player(0, screen)
    player2 = Player(1, screen)

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
        
        pg.display.flip()
            
            
if __name__ == '__main__':
    main()
