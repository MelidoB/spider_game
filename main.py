import pygame

from classes.personaje import Modulo_De_Personaje
from close_game import close_game_function


def main():
    # Pasare todo lo que se valla ah dibujar aqui
    todo_para_dibujar = []


    #1. Lo primero que voy a dibujar es el personaje
    personaje = Modulo_De_Personaje() #Creo el personaje
    personaje.cambiar_nombre("araña") #Se va a llamar
    personaje.cambiar_imagen("araña/0.png") #Esta va ah ser la imagen que sera dibujada
    todos_los_dibujos = [] #esto guardara todos los dibujos para cuando este caminando
    for i in range(3):
        todos_los_dibujos.append(f"araña/{i}.png") #Tiene 3 dibujos de 0 a 2
    personaje.cambiar_dibujos_con_caminar(todos_los_dibujos) #Estos dibujos se le pasan al personaje para poder usarlos luego

    personaje.cambiar_posicion((20,20)) #Esta sera la posicion en la que la imagen sera dibujada
    personaje.cambiar_cantidad_de_vida(200) #El total de vida del personaje
    personaje.cambiar_velocidad(5) #La velocidad para usarla en el movimiento del personaje
    #pasando el personaje para que se pueda dibujar luego
    todo_para_dibujar.append(personaje)

    #2. Ahora dibujare al enemigo


    pygame.init()
    gameDisplay = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()

    while True:
        close_game_function()
        gameDisplay.fill((255, 255, 255))  # Dibujare la blanco en toda la pantalla

        # Ahora dibujo el personaje con la imagen en la posicion

        # Dibujare sobre el blanco  todas las imagenes de los personajes en sus posiciones
        for i in todo_para_dibujar:
            x, y = i.obtener_posicion()
            gameDisplay.blit(i.imagen, (x, y))

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()