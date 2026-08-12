import pygame

import asteroidfield
import constants
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    _ = pygame.init()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) #noqa
    asteroid_field = AsteroidField() #noqa creating asteroid field object

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
