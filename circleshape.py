import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other):
        # If (r1 + r2) < (distance between centers of circle) = collision
        if (self.radius + other.radius) > self.position.distance_to(other.position):
            # Little Debug:
            # print(f"self radius: {self.radius} , and other radius: {other.radius}, and calculated distance: {self.position.distance_to(other.position)}")
            return True
        return False