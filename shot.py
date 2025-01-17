import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    # Construct with super values as default
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Shots are circular, so draw a circle shape, default width = 2 (hence the int value)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Shots move in a steady constant speed
    def update(self, dt):
        self.position += (self.velocity * dt)