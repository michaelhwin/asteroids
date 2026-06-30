import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt