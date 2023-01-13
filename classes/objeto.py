from pygame import image

class Modulo_De_Objeto:
    def __init__(self, nombre,posicion,capacidad):
        self.nombre = nombre
        self.posicion = posicion
        self.imagen = None
        self.obstaculo = False
        self.cantidad_de_vida = capacidad
        self.capacidad_de_vida = capacidad

    def cambiar_cantidad_de_vida(self, valor):
        self.cantidad_de_vida = valor
    def cambiar_capacidad_de_vida(self, valor):
        self.capacidad_de_vida = valor
    def obtener_porcentaje_lleno(self):
        return self.lleno / self.capacidad

    def es_un_obstaculo(self):
        self.obstaculo = True
    def cambiar_posicion(self,posicion):
        self.posicion = posicion
    def cambiar_imagen(self, img):
        self.imagen = image.load(f'Images/{img}')
    def obtener_ancho(self):
        return self.imagen.get_width()
    def obtener_largo(self):
        return self.imagen.get_height()