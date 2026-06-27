import pygame
import constants
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            pygame.display.flip()

            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
