import pygame as pg
from constants import *

def main():
    """
    Initializes the game window and runs the main game loop.
    Sets up the display surface, processes user events (such as quitting the game),
    clears the screen each frame, and updates the display.
    """
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        screen.fill("black")
        pg.display.flip()


        



if __name__ == "__main__":
    pg.init()
    main()
