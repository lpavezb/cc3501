# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: glutfigures_02_listas.py
----------------
Dibuja figuras GLUT en la escena utilizando listas.

Control del programa:
SPACE: crea nueva figura en posición aleatoria
1: visualiza o no los ejes de coordenadas
2: visualiza o no como malla de alambre
ESC: terminar 
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from AuxiliaryFunctions import *

from random import uniform

#####################################################################

def init_pygame((w,h), title=""):
    pygame.init()
    pygame.display.set_mode((w,h), OPENGL|DOUBLEBUF)
    pygame.display.set_caption(title)

def init_opengl((w,h)):
    reshape((w,h))
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
	
def reshape((width, height)):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width)/float(height), 0.1, 20000.0)
    #glOrtho(-w,w,-h,h,1,20000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#####################################################################

def listaTeapot(sz, rgb = None, pos = [0.0,0.0,0.0],o = 0.0,rot = None):
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glPushMatrix()
    
    glTranslatef(pos[0],pos[1],pos[2])
        
    if (rot != None):
        glRotatef(o,rot[0],rot[1],rot[2])
    
    if (rgb != None):
        glColor4fv(rgb)
    
    glutSolidTeapot(sz)
    
    glPopMatrix()
    
    glEndList()
    
    return lista
    
def randomTeapot():
    rgb = [uniform(0,1),uniform(0,1),uniform(0,1),1.0]
    pos = [uniform(-2000,2000),uniform(-2000,2000),uniform(-2000,2000)]
    sz = uniform(50,200)
    
    return listaTeapot(sz,rgb = rgb,pos = pos,o = uniform(-90,90),rot = [0,0,1])
#####################################################################

W=640 #ancho de ventana
H=480 #alto de ventana

# inicializando ...
init_pygame((W,H),"glutfigures_02_listas")
init_opengl((W,H))

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
axes=axesList(100000)

# variables del programa
teapots = [randomTeapot(),randomTeapot(),randomTeapot()]

show_axes = True
fill_polygons = True

# configuración de camara
glLoadIdentity()
gluLookAt( 2000.0, 2000.0, 2000.0, \
          0.0, 0.0, 0.0, \
          0.0, 0.0, 1.0)

run = True
while run:
    # 0: CONTROL DEL TIEMPO
	
    # 1: MANEJAMOS EVENTOS DE ENTRADA (TECLADO, MOUSE, ETC.)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_1:
                show_axes = not show_axes
            if event.key == K_2:
                fill_polygons = not fill_polygons
            if event.key == K_SPACE:
                teapots.append(randomTeapot())
				
    # 2: EJECUTAMOS LOGICA DE LA APLICACION
	
    # 3: DIBUJAMOS LOS ELEMENTOS
    # limpia la pantalla (buffer de color y de profundidad)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    
    #posibilidad de pintar o no los polígonos
    if fill_polygons:
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)
    
    # posibilidad de mostrar o no los ejes
    if show_axes:
        glCallList(axes)
    
    for t in teapots:
        glCallList(t)
    
    pygame.display.flip()       # vuelca el dibujo a la pantalla
    pygame.time.wait(1000/30)   # ajusta para trabajar a 30 fps.


#####################################################################
