import pygame

from classes.personaje import Modulo_De_Personaje
from close_game import close_game_function


def main():
    # Pasare todo lo que se valla ah dibujar aqui
    todo_para_dibujar = []

    # Lo primero que voy a dibujar es el personaje
    personaje = Modulo_De_Personaje()


    pygame.init()
    gameDisplay = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()

    while True:
        close_game_function()
        gameDisplay.fill((255, 255, 255))  # Dibujare la negro en toda la pantalla

        # Dibujare sobre el negro todo lo que se valla ah dibujar aqui
        for i in todo_para_dibujar:
            x, y = i.obtener_posicion()
            gameDisplay.blit(i.imagen, (x, y))

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()