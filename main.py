import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Group-ish
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0


    while True:
        # Close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw background
        screen.fill("black")

        updatable.update(dt)
        for drawie in drawable:
            drawie.draw(screen)
        for asteroid in asteroids:
            if player.colliding(asteroid):
                print("Game over!")
                exit(0)
            
            for shot in shots:
                if shot.colliding(asteroid):
                    asteroid.split()
                    shot.kill()
                    

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()