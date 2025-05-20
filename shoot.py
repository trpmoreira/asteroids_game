import pygame
from circleshape import CircleShape
from constants import *

class Shoot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)
    self.radius = SHOT_RADIUS

  def draw(self, screen):
    #print(f"Desenhar asteroid em {self.position}")
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, self.position, self.radius, 2)

  def move(self, dt):
    self.position += self.velocity * dt
    #print(f"Posição: {self.position}")

  def update (self, dt):
    self.move(dt)