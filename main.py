import pygame
from constants import *
import player

def main():
    """
    Initializes the game window and runs the main game loop.
    Sets up the display surface, processes user events (such as quitting the game),
    clears the screen each frame, and updates the display.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pl = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pl.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000  # Frame rate is set to 60 FPS


if __name__ == "__main__":
    main()
