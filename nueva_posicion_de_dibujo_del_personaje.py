

def determinar_nueva_posicion_de_dibujo_del_personaje(posicion_actual_del_dibujo,cantidad_de_pixeles): #
    """it will move depending on which of the 4 direction key is press"""
    x,y = posicion_actual_del_dibujo

    if key_pressed[ord('a')]:
        #Cuando presiono a debo cambiar todas las imagenes de reserva  en #self.dibujos_con_caminar
        x -= cantidad_de_pixeles
    if key_pressed[ord('d')]:
        x += cantidad_de_pixeles
    if key_pressed[ord('w')]:  # [0,1,2,3] Derecha,Abajo,Izquierda,Arriba
        y -= cantidad_de_pixeles
    if key_pressed[ord('s')]:
        y += cantidad_de_pixeles
    return x,y

