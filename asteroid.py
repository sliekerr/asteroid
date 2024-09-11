import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    # Construct with super values as default
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Asteroids are circular, so draw a circle shape, default width = 2 (hence the int value)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Asteroids move in a steady constant speed
    def update(self, dt):
        self.position += (self.velocity * dt)

    # In case they're hit, we need to be able to split them
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            print("Killed asteroid!")
        else:
            random_angle = random.uniform(20,50)
            velocity_one = self.velocity.rotate(random_angle)
            velocity_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = velocity_one * 1.2
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two.velocity = velocity_two * 1.2
            self.kill()
        
