from CC3501Utils import *
from models.bomb import *

class Vista:
    def dibujar(self, bomberman, place_bomb, moveRight, moveLeft, moveUp, moveDown, fondo, dt):
        ##############################################
        # MOVIMIENTO DE CAMARA SOBRE PERSONAJE
        ##############################################
        # IMPORTANTE: Tengo un bug con el dt, por alguna razon al usar el dt entre iteraciones
        # el programa corre ULTRA lento, asi que preferi elegir un valor de tiempo
        # conveniente para que tenga sentido jugar el juego. (0.4)
        bomberman.mover(0.4, moveRight, moveLeft, moveUp, moveDown)

        # Genera un marco donde la pera no mueve la camara
        ##############################################
        # INTERACCION PLATAFORMAS
        ##############################################

        ########################################
        # SE INICIA DIBUJO
        ########################################
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        fondo.dibujar()
        if place_bomb:
            bomb = bomberman.bombs.pop()
            bomb.dibujar()
        bomberman.dibujar()
