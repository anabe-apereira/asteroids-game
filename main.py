import os
# para não aparecer mensagem de importação do pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():

    # prints iniciais de teste
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver }")
    # print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 1
    
    # Create groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Set containers before creating player
    Player.containers = (updatable, drawable)
    
    # Now create player (it will automatically add to groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000        



if __name__ == "__main__":
    main()
