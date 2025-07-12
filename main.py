import pygame
from constants import *
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidsGroup = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroidsGroup, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroids_field = AsteroidField()


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroidsGroup:
            if obj.check_collision(player):
                print("Game over!")
                # Handle collision logic here, e.g., reduce player health or end game
        
        pygame.display.flip()

        dt = clock.tick(60)/1000  # Frame rate is set to 60 FPS


if __name__ == "__main__":
    main()
