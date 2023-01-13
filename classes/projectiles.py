from classes.objeto import Modulo_De_Objeto


class Modulo_De_Projectiles(Modulo_De_Objeto):
    def __init__(self,nombre,posicion):
        Modulo_De_Objeto.__init__(nombre,posicion)
        self.animacion_de_movimiento = None
        self.animacion_de_muerte = None
        self.sonido_de_muerte = None

    def cambiar_animacion_de_movimiento(self, nueva_animacion):
        self.animacion_de_movimiento = nueva_animacion

    def cambiar_animacion_de_muerte(self, nueva_animacion):
        self.animacion_de_muerte = nueva_animacion

    def cambiar_sonido_de_muerte(self, nuevo_sonido):
        self.sonido_de_muerte = nuevo_sonido
