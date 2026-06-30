from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def collides_with(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        new_velocity_1 = self.velocity.rotate(angle)
        new_velocity_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_2 = Asteroid(self.position.x, self.position.y, new_radius)

        child_1.velocity = new_velocity_1 * 1.2
        child_2.velocity = new_velocity_2 * 1.2
        