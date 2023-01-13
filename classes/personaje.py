from classes.objeto import Modulo_De_Objeto


class Modulo_De_Barra_De_Vida(Modulo_De_Objeto):
    def __init__(self,nombre,posicion):
        Modulo_De_Objeto.__init__(nombre,posicion)
        self.habilidad = None
        self.velocidad = None
        self.animacion_con_caminar = None
        self.animacion_con_correr = None
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
    def cambiar_animacion_con_caminar(self, nueva_animacion):
        self.animacion_con_caminar = nueva_animacion
    def cambiar_animacion_con_correr(self, nueva_animacion):
        self.animacion_con_correr = nueva_animacion
    def cambiar_animacion_de_muerte(self,nueva_animacion):
        self.animacion_de_muerte = nueva_animacion
    def cambiar_animacion_de_habilidad(self, nueva_animacion):
        self.animacion_de_habilidad = nueva_animacion
    def cambiar_sonido_de_muerte(self, nuevo_sonido):
        self.sonido_de_muerte = nuevo_sonido
    def cambiar_sonido_de_habilidad(self, nuevo_sonido):
        self.sonido_de_habilidad = nuevo_sonido