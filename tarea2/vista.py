from CC3501Utils import *
from models.bomb import *


class Vista:
    def dibujar(self, bomberman, move_right, move_left, move_up, move_down, fondo, walls):
        ##############################################
        # MOVIMIENTO DE CAMARA SOBRE PERSONAJE
        ##############################################
        # IMPORTANTE: Tengo un bug con el dt, por alguna razon al usar el dt entre iteraciones
        # el programa corre ULTRA lento, asi que preferi elegir un valor de tiempo
        # conveniente para que tenga sentido jugar el juego. (0.4)
        for wall in walls:
            if move_left:
                move_left = not bomberman.collide_left(wall)
            if move_right:
                move_right = not bomberman.collide_right(wall)
            if move_up:
                move_up = not bomberman.collide_up(wall)
            if move_down:
                move_down = not bomberman.collide_down(wall)
        bomberman.mover(0.4, move_right, move_left, move_up, move_down)
        # delete exploded bombs
        for bomb in bomberman.bombs:
            if not bomb.active:
                index = bomberman.bombs.index(bomb)
                bomberman.bombs.pop(index)

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
        bomberman.explode_bomb()
        for wall in walls:
            wall.dibujar()
        for bomb in bomberman.bombs:
            if bomb.active:
                bomb.dibujar()
        bomberman.dibujar()
