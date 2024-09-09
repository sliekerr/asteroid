import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

    # Create two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Add the Player class to both groups - note: only after this, you should instantiate the Player Objects (so they can be added)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create Objects
    player = Player(x, y, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    color = (0,0,0) # Black
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Progress time
        dt = clock.tick(60) / 1000

        # Draw the screen
        screen.fill(color, rect=None, special_flags=0)
        
        # Draw the player
        # old: player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        # Update for keystrokes
        # old: player.update(dt)
        for obj in updatable:
             obj.update(dt)

        # Check for collisions of Asteroids /w Player Object
        for obj in asteroids:
             # If it returns True, means there was collision:
             if obj.check_collision(player):
                  print("Game Over!")
                  # pygame.QUIT  ??
                  return


        # Render the screen
        pygame.display.flip() # This updates the display (after drawing player...)

        # Delay before restarting the loop
        clock.tick(60)
        


if __name__ == "__main__":
	main()
