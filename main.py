import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shoot import Shoot


def main():
  pygame.init()
  clock = pygame.time.Clock()

  dt = 0

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shoots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable, )
  Shoot.containers = (shoots, drawable, updatable )

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill((0, 0, 0))
    updatable.update(dt)


    for asteroid in asteroids:
      for shot in shoots:
        if shot.colisionCheck(asteroid):
          asteroid.split()
          shot.kill()
          print("BOOOM!")

    for asteroid in asteroids:
      if asteroid.colisionCheck(player):
        print("Gave Over!")
        return


    for thing in drawable:
      thing.draw(screen)

    pygame.display.flip()

    clock.tick(60)
    dt = clock.tick(60) / 1000.0
    #print(dt)



if __name__ == "__main__":
  main()