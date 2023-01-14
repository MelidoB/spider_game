def dibuja_todo(todo_para_dibujar, gameDisplay):  #dibuja todo lo de todo_para_dibujar en gameDisplay
    for i in todo_para_dibujar:
        x, y = i.obtener_posicion()
        gameDisplay.blit(i.imagen, (x, y))