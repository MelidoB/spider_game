from classes.objeto import Modulo_De_Objeto
from pygame import image


class Modulo_De_Personaje(Modulo_De_Objeto):
    def __init__(self):
        Modulo_De_Objeto.__init__(self)
        self.habilidad = None
        self.velocidad = None
        self.dibujos_con_caminar = None
        self.animaciones_con_correr = None
        self.animacion_de_muerte = None
        self.animacion_de_habilidad = None
        self.sonido_de_muerte = None
        self.sonido_de_habilidad =None

    def cambiar_habilidad(self, nueva_habilidad):
        self.habilidad = nueva_habilidad
    def cambiar_velocidad(self, nuevo_valor):
        self.velocidad = nuevo_valor
    def obtener_velocidad(self):
        return self.velocidad
    def cambiar_dibujos_con_caminar(self, nuevos_dibujos):
        #recibire todos los dibujos
        #Ire por cada uno y los pondre juntos.
        todos_los_dibujos = []
        for i in nuevos_dibujos:
            #Pondre cada dibujo en el formato de pygame
            dibujo_en_nuevo_formato = image.load(f'imagenes/{i}')
            todos_los_dibujos.append(i)

        #guardare todos los dibujos en mi personaje
        self.dibujos_con_caminar = todos_los_dibujos.copy()

    def cambiar_animacion_con_correr(self, nuevas_animaciones):
        self.animaciones_con_correr = nuevas_animaciones
    def cambiar_animacion_de_muerte(self,nueva_animacion):
        self.animacion_de_muerte = nueva_animacion
    def cambiar_animacion_de_habilidad(self, nueva_animacion):
        self.animacion_de_habilidad = nueva_animacion
    def cambiar_sonido_de_muerte(self, nuevo_sonido):
        self.sonido_de_muerte = nuevo_sonido
    def cambiar_sonido_de_habilidad(self, nuevo_sonido):
        self.sonido_de_habilidad = nuevo_sonido