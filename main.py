import pygame
from close_game import close_game_function


def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()

    while True:
        close_game_function()
        gameDisplay.fill((255, 255, 255))

#Hello

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
