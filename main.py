import pygame
from constants import *


def main():
  pygame.init()
  clock = pygame.time.Clock()

  dt = 0

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000.0
    print(dt)



if __name__ == "__main__":
  main()