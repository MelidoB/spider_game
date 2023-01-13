from pygame import image

class modelo_de_objeto:
    def __init__(self, nombre,posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.imagen = None
        self.obstaculo = False

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