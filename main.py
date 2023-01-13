import pygame
from close_game import close_game_function


def main():
    #Pasare todo lo que se valla ah dibujar aqui
    todo_para_dibujar = []
    
    pygame.init()
    gameDisplay = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()

    while True:
        close_game_function()
        gameDisplay.fill((255, 255, 255))
                         
        #Dibujare todo lo que se valla ah dibujar aqui
	for i in todo_para_dibujar:
		x,y = i.posicion
		gameDisplay.blit(i.image, (x, y))
							
        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
