import pygame, random
from logger import log_state, log_event 

from circleshape import CircleShape

from constants import *

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a = self.velocity.rotate(angle)
            b = self.velocity.rotate(-angle)
            Split1 = Asteroid(self.position.x, self.position.y, new_radius)
            Split2 = Asteroid(self.position.x, self.position.y, new_radius)
            Split1.velocity = a * 1.2
            Split2.velocity = b * 1.2
