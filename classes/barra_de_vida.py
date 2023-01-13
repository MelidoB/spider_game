from classes.objeto import Modulo_De_Objeto


class Modulo_De_Barra_De_Vida(Modulo_De_Objeto):
    def __init__(self,nombre,posicion,capacidad):
        Modulo_De_Objeto.__init__(nombre,posicion,capacidad)
        self.animacion_de_cambio = None
        self.sonidos_de_cambio = None

    def cambiar_animacion_de_cambio(self, nueva_animacion):
        self.animacion_de_cambio = nueva_animacion
    def cambiar_sonidos_de_cambio(self, nuevo_sonido):
        self.sonidos_de_cambio = nuevo_sonido
