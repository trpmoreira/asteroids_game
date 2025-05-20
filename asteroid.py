import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)


  def draw(self, screen):
    #print(f"Desenhar asteroid em {self.position}")
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, self.position, self.radius, 2)

  def move(self, dt):
    self.position += self.velocity * dt
    #print(f"Posição: {self.position}")

  def split(self):
    self.kill()

    if self.radius < ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle = random.uniform(20, 50)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      asteroid_a_direction = self.velocity.rotate(random_angle)
      asteroid_b_direction = self.velocity.rotate(-random_angle)

      asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_a.velocity += asteroid_a_direction * 1.2
      asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_b.velocity += asteroid_b_direction * 1.2



  def update (self, dt):
    self.move(dt)
