import os
# para não aparecer mensagem de importação do pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
def main():

    # prints iniciais de teste
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver }")
    # print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000        



if __name__ == "__main__":
    main()
