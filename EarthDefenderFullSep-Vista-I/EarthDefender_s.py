# -*- coding: iso-8859-1 -*-

#####################################################################
# Daniel Calderón S.
# CC3501
#####################################################################

# EarthDefender_s.py
# ---------------
# Juego completo,
# incluye sonido
# al presionar enter, cambia la gravedad
# al presionar backspace, los meteoritos se generan mas rápido.
# ---------------

# Implementación testeada con:
## Python 2.6
## PyOpenGL 3.0.1
## PyGame 1.9.1

#####################################################################

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import uniform
import math
from Vector2D import *
from Nave import *
from Meteorito import *
from Bala import *
from Tierra import *
from Circulo import *
from utils import *
from Vista import *


#####################################################################
# Funciones de graficos
#####################################################################

def init_pygame((w, h), title=""):
    pygame.init()
    pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)
    pygame.display.set_caption(title)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)


def reshape((width, height)):
    if height == 0:
        height = 1
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_opengl((w, h)):
    init()
    reshape((w, h))


#####################################################################
# Programa principal Controlador
#####################################################################

def main(argv):
    # imprime en consola
    print 'Earth Defender'

    Rmax = 200.0  # "radio" maximo meteoritos
    Rmin = 30.0  # "radio" minimo meteoritos
    w = 900  # ancho
    h = 600  # alto
    t = 0  # tiempo de conteo para generar meteoritos

    # si se desea utilizar argumentos del programa...
    # if len(argv) > 1:
    # var1 = argv[1]
    # var2 = int(argv[2])

    v0 = Vector(0, 30)  # velocidad balas
    a = Vector(0.0, -0.5)  # aceleración de gravedad
    T = 600  # periodo de aparicion de meteoritos

    ms = []  # contenedor de meteoritos
    bs = []  # contenedor de balas
    nave = Nave()
    tierra = Tierra(w)
    vista = Vista()
    # inicializando ...
    init_pygame((w, h), "Earth Defender")
    init_opengl((w, h))

    # sonidos
    sound_shoot = pygame.mixer.Sound("laser.wav")
    sound_shoot.set_volume(0.2)

    # música de fondo
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1, 0.0)

    # medida de tiempo inicial
    t0 = pygame.time.get_ticks()

    run = True
    while run:
        # 0: CONTROL DEL TIEMPO
        t1 = pygame.time.get_ticks()  # tiempo actual
        dt = (t1 - t0)  # diferencial de tiempo asociado a la iteración
        t0 = t1  # actualizar tiempo inicial para siguiente iteración

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            nave.p = Vector(mouse_pos[0], 100)

            # disparar
            if event.type == MOUSEBUTTONDOWN:
                bs.append(Bala(nave.p, v0))
                sound_shoot.play()

            # cerrar
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                # ataque especial
                if event.key == K_SPACE:
                    if nave.sp - 1 >= 0:
                        bs.append(Bala(nave.p, v0))
                        bs.append(Bala(nave.p, rotar(v0, math.pi / 12)))
                        bs.append(Bala(nave.p, rotar(v0, -math.pi / 12)))
                        bs.append(Bala(nave.p, rotar(v0, math.pi / 6)))
                        bs.append(Bala(nave.p, rotar(v0, -math.pi / 6)))
                        bs.append(Bala(nave.p, rotar(v0, math.pi / 4)))
                        bs.append(Bala(nave.p, rotar(v0, -math.pi / 4)))
                        nave.sp = nave.sp - 1

                # cambia la aceleración del nivel
                if event.key == K_RETURN:
                    a = Vector(uniform(-0.5, 0.5), uniform(-1.0, 0))
                    print "a = ", a.cartesianas()

                # genera meteoritos más rápido
                if event.key == K_BACKSPACE:
                    T -= T * 0.1
                    print "T = ", T

                # cerrar
                if event.key == K_ESCAPE:
                    run = False

        # si se acaban las vidas termina el programa.
        if tierra.vida <= 0:
            print 'GAME OVER'
            run = False

        # efecua las acciones necesarias de manera proporcional a dt
        vista.dibujar(nave, ms, bs, tierra, dt, a, w, h, Rmin, Rmax)

        # si supero el periodo de creacion de meteoritos
        # creo un meteorito, y reinicio el tiempo
        t = t + dt
        if t > T:
            t = t - T
            ms.append(crearMeteorito(w, h, Rmin, Rmax))

        # pone el dibujo en la pantalla
        pygame.display.flip()
        # ajusta para trabajar a 30 fps.
        pygame.time.wait(1000 / 30)

    # termina pygame (cerrar ventana)
    pygame.quit()


if __name__ == "__main__":
    import sys

    # sys.argv es una lista de strings con los argumentos que se le dan al interprete,
    # es decir, si llamamos a
    # python EarthDefender_s.py 3 2
    # entonces
    # sys.argv = ["EarthDefender_s.py","3","2"]
    # luego
    # sys.argv[0] = "EarthDefender_s.py"
    # sys.argv[1] = "3"
    # sys.argv[2] = "2"
    main(sys.argv)

#####################################################################
