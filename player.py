import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.timer = 0

    # Take in values to calculate the 3 points for a triangle (needed for the Draw method)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Actually draw yourself
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # A rotate function to ensure player can make turns
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # A move function to ensure player can move back/forth
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # This takes keypress commands, I suppose?
    def update(self, dt):
        # Retrieve a value from keypress, then go over some IF statements to see which key it was
        keys = pygame.key.get_pressed()
        
        # Ensure the cooldown timer is lowered by our dt clock on each and every update
        self.timer -= dt

        # Turning keys: a, d
        if keys[pygame.K_a]:
            inverted_dt = dt * -1
            self.rotate(inverted_dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # Moving keys: s, w
        if keys[pygame.K_s]:
            inverted_dt = dt * -1
            self.move(inverted_dt)
        if keys[pygame.K_w]:
            self.move(dt)
        # Shooting key: space
        if keys[pygame.K_SPACE]:
            # Ensure cooldown timer has passed < 0
            if self.timer <= 0:
                self.shoot()
                # Reset the timer/cooldown
                self.timer = PLAYER_SHOOT_COOLDOWN

    # Add a method for shooting
    def shoot(self):
        # Create an instance of shot, store it in an easy accessable var: shot
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        # Assign a var velocity to it, so we can move it in our update() - otherwise the shot would be static/not moving
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED