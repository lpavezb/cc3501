# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: glutfigures_01_colores.py
----------------
Dibuja figuras GLUT en la escena.

Control del programa:
SPACE: cambiar figura
1: visualiza o no los ejes de coordenadas
2: visualiza o no como malla de alambre
3: cambia el color de la figura visualizada333332
ESC: terminar
"""

import pygame
from pygame.locals import *

from AuxiliaryFunctions import *

from random import uniform


#####################################################################
from bronzor import *


def init_pygame(w, h, title=""):
    pygame.init()
    pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)
    pygame.display.set_caption(title)


def init_opengl(w, h):
    reshape(w, h)
    init()


def init():
    # setea el color de fondo
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # se habilitan las transparencias
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    # el color debe incluir la cuarta componente, alpha
    # alpha=1  --> objeto totalmente opaco
    # alpha=0  --> opbjeto totalmente transparente

    glShadeModel(GL_SMOOTH)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)


def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width) / float(height), 0.1, 20000.0)
    # glOrtho(-w,w,-h,h,1,20000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


#####################################################################

W = 640  # ancho de ventana
H = 480  # alto de ventana

# inicializando ...
init_pygame(W, H, "bronzor")
init_opengl(W, H)

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
axes = axesList(100000)

# variables del programa
rgb = [0.0, 0.0, 0.0, 1.0]
fig = 0

show_axes = True
fill_polygons = True
camPos = Vector(0, 0, 4000)  # posicion de la camara
camAt = Vector(14140, -200, -328000)  # posicion que se enfoca
# configuración de camara
glLoadIdentity()
gluLookAt(2000.0, 2000.0, 2000.0,
          0.0, 0.0, 0.0,
          0.0, 0.0, 1.0)

# permite conocer fabricante y version de OpenGL utilizada
print(glGetString(GL_VENDOR))
print(glGetString(GL_VERSION))
b = Bronzor()
run = True
while run:
    # 0: CONTROL DEL TIEMPO

    # 1: MANEJAMOS EVENTOS DE ENTRADA (TECLADO, MOUSE, ETC.)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    # obtener teclas presionadas
    pressed = pygame.key.get_pressed()

    if pressed[K_UP]:
        camPos = sumar(ponderar(100, normalizar(camAt)), camPos)
    if pressed[K_DOWN]:
        camPos = sumar(ponderar(-100, normalizar(camAt)), camPos)
    if pressed[K_RIGHT]:
        camPos = sumar(ponderar(-100, rotarFi(normalizar(camAt), 90)), camPos)
    if pressed[K_LEFT]:
        camPos = sumar(ponderar(100, rotarFi(normalizar(camAt), 90)), camPos)

    if pressed[K_w]:
        camAt = sumar(Vector(0, 0, 1000), camAt)
    if pressed[K_s]:
        camAt = sumar(Vector(0, 0, -1000), camAt)
    if pressed[K_d]:
        camAt = rotarFi(camAt, 0.1)
    if pressed[K_a]:
        camAt = rotarFi(camAt, -0.1)

    if pressed[K_1]:
        camPos = Vector(0, 0, 4000)
        camAt = Vector(14140, -200, -328000)

    if pressed[K_2]:
        camPos = Vector(1926.700, 1926.700, 104.30)
        camAt = Vector(-10000, -10000, -2000)

    if pressed[K_3]:
        camPos = Vector(0, 0, -4000)
        camAt = Vector(-14140, 200, 328000)

    if pressed[K_ESCAPE]:
        run = False

    # 2: EJECUTAMOS LOGICA DE LA APLICACION

    # 3: DIBUJAMOS LOS ELEMENTOS
    # limpia la pantalla (buffer de color y de profundidad)
    glutInit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # posibilidad de pintar o no los polígonos
    if fill_polygons:
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)

    # posibilidad de mostrar o no los ejes
    if show_axes:
        glCallList(axes)

    glColor4fv(rgb)

    b.dibujar()
    glLoadIdentity()
    gluLookAt(camPos.x, camPos.y, camPos.z,  # posicion
              camAt.x, camAt.y, camAt.z,  # mirando hacia
              0.0, 0.0, 1.0)  # inclinacion
    pygame.display.flip()  # vuelca el dibujo a la pantalla
    pygame.time.wait(int(1000 / 30))  # ajusta para trabajar a 30 fps.

#####################################################################
