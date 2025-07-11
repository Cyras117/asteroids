import pygame as pg
from constants import *

def main():
    """
    Initializes the game window and runs the main game loop.
    Sets up the display surface, processes user events (such as quitting the game),
    clears the screen each frame, and updates the display.
    """
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        pg.display.flip()
        dt = clock.tick(60)/1000  # Frame rate is set to 60 FPS


if __name__ == "__main__":
    

    main()
