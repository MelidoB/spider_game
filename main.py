import pygame
from pygame import key

from classes.personaje import Modulo_De_Personaje
from close_game import close_game_function
from dibuja_todo import dibuja_todo
from nueva_posicion_de_dibujo_del_personaje import determinar_nueva_posicion_de_dibujo_del_personaje

def main():

    todo_para_dibujar = set() #guardare todo lo que se valla ah dibujar en un set llamado todo_para_dibujar. Lo mismo que una lista
                              #pero no puedo acceder el index.


    #1. Lo primero que voy a dibujar es la araña
    araña = Modulo_De_Personaje() #Creo la araña
    araña.cambiar_nombre("araña") #el nombre de la araña sera araña
    araña.cambiar_imagen("araña/0.png") #Su dibujo sera 0.png de la carpeta araña
    araña.cambiar_posicion((20,20)) #La posicion del dibujo es x=20 y=20
    todos_los_dibujos = [] #Creo un contenedor, llamado todos_los_dibujos, para guardar los differentes dibujos que puede usar el araña
    for i in range(3):
        todos_los_dibujos.append(f"araña/{i}.png") #guardo 3 dibujos de la carpeta araña. Se llaman 0.png,1.png,2.png. Van en orden porque los dibujos van en sequencia.
    araña.cambiar_dibujos_con_caminar(todos_los_dibujos) #Guardo los dibujos guardados en todos_los_dibujos en el contenedor del araña llamado self.dibujos_con_caminar

    araña.cambiar_cantidad_de_vida(200) #la vida del araña sera 200
    araña.cambiar_velocidad(10) #La velocidad del araña sera 10.

    todo_para_dibujar.add(araña) #pasando la informacion del araña para que se pueda dibujar luego

    #2. Ahora dibujare al enemigo
    enemigo = Modulo_De_Personaje()  # Creo el enemigo
    enemigo.cambiar_nombre("araña")  # el nombre del enemigo sera enemigo_a
    enemigo.cambiar_imagen("araña/0.png")  # Su dibujo sera 0.png de la carpeta enemigo_a
    enemigo.cambiar_posicion((600, 20))  # La posicion del dibujo es x=600 y=20
    todos_los_dibujos = []  # Creo un contenedor, llamado todos_los_dibujos, para guardar los differentes dibujos que puede usar el enemigo
    for i in range(3):
        todos_los_dibujos.append(
            f"araña/{i}.png")  # guardo 3 dibujos de la carpeta araña. Se llaman 0.png,1.png,2.png. Van en orden porque los dibujos van en sequencia.
    enemigo.cambiar_dibujos_con_caminar(
        todos_los_dibujos)  # Guardo los dibujos guardados en todos_los_dibujos en el contenedor del enemigo llamado self.dibujos_con_caminar

    enemigo.cambiar_cantidad_de_vida(100)  # la vida del enemigo sera 100
    enemigo.cambiar_velocidad(5)  # La velocidad del enemigo sera 5.

    todo_para_dibujar.add(enemigo)  # pasando la informacion del enemigo para que se pueda dibujar luego

    # pasando el enemigo para que se pueda dibujar luego
    pygame.init()
    gameDisplay = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()

    while True:
        close_game_function()
        gameDisplay.fill((255, 255, 255))  # Dibujare la blanco en toda la pantalla

        # Dibujare sobre el blanco  todas las imagenes de los personajes en sus posiciones
        dibuja_todo(todo_para_dibujar, gameDisplay) #dibuja todo lo de todo_para_dibujar en gameDisplay

        #Dale instrucciones al dibujante
        #Si se presiona una tecla la posicion el dibujo
        posicion_actual_del_dibujo = araña.obtener_posicion() #se guardara la posicion actual del dibujo
        cantidad_de_pixeles = araña.velocidad

        # Obtengo la tecla que se presione y la pongo en key_pressed
        key_pressed = key.get_pressed()

        #Si la tecla en key_pressed es a o d roto el dibujo para la izquierda o la derecha
        if key_pressed:
            pass
        #Si la tecla es w o s cambio la posicion del dibujo dependiendo del angulo del dibujo


        nueva_posicion = determinar_nueva_posicion_de_dibujo_del_personaje(posicion_actual_del_dibujo, cantidad_de_pixeles) #Se pasa la posicion y determina una nueva basado en la tecla que presiones y la velocidad (o cantidad de pixeles).
        araña.cambiar_posicion(nueva_posicion) #Esta nueva posicion se usara para dibujar al personaje de nuevo


        clock.tick(60)
        pygame.display.update()




if __name__ == '__main__':
    main()