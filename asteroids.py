import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        rvector = self.velocity.rotate(angle)
        rvector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS


        Asteroids(self.position.x, self.position.y, new_radius).velocity = rvector * 1.2
        Asteroids(self.position.x, self.position.y, new_radius).velocity = rvector2 * 1.2
        