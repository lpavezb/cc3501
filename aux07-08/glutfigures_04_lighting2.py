# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: glutfigures_04_lighting2.py
----------------
Dibuja la Tetera de Utah rotando. Utiliza iluminación y listas.

Control del programa:
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
    glClearColor(0.0, 0.0, 0.0, 1.0)
	
    # se habilitan las transparencias
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    # el color debe incluir la cuarta componente, alpha
    # alpha=1  --> objeto totalmente opaco
    # alpha=0  --> opbjeto totalmente transparente
 
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    #glDepthFunc(GL_LESS)    
        
#    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    
    # normaliza las normales luego del escalamiento.
    glEnable(GL_NORMALIZE)
	
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

def initLight():
    
	glLightfv(GL_LIGHT0, GL_POSITION, [ 3000.0, 0.0, 0.0, 1.0 ])
	glLightfv(GL_LIGHT0, GL_AMBIENT , [ 0.2, 0.2, 0.2, 1.0])
	glLightfv(GL_LIGHT0, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0])
	glLightfv(GL_LIGHT0, GL_DIFFUSE , [ 1.0, 1.0, 1.0, 1.0])
 
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
	glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
 
	glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 180.0)
	glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [ -1.0, 0.0, 0.0])
	glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 0.0)
 
	glEnable(GL_LIGHT0)

#####################################################################

def listaTeapotMaterial(sz, rgb, pos = [0.0,0.0,0.0],o = 0.0,rot = None):
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glPushMatrix()
    
    glTranslatef(pos[0],pos[1],pos[2])
        
    if (rot != None):
        glRotatef(o,rot[0],rot[1],rot[2])
        
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0,0.0,0.0,1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, rgb)
    glMaterialfv(GL_FRONT, GL_SPECULAR,[1.0,1.0,1.0,1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [10.0])
    glMaterialfv(GL_FRONT, GL_EMISSION, [0.0,0.0,0.0,1.0])
    
    glutSolidTeapot(sz)
    
    glPopMatrix()
    
    glEndList()
    
    return lista

#####################################################################

W=640 #ancho de ventana
H=480 #alto de ventana

# inicializando ...
init_pygame((W,H),"glutfigures_04_lighting2")
init_opengl((W,H))

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
axes=axesList(100000)
teapot = listaTeapotMaterial(800, [1,0,0,1], pos = [0.0,0.0,0.0])

# variables del programa
o = 30
w = 0.1

show_axes = True
fill_polygons = True

# configuración de camara
glLoadIdentity()
gluLookAt( 2000.0, 2000.0, 2000.0, \
          0.0, 0.0, 0.0, \
          0.0, 0.0, 1.0)
          
# habilita iluminación
glEnable(GL_LIGHTING)

# configura fuentes de luz
initLight()

# medida de tiempo inicial
t0 = pygame.time.get_ticks()

run = True
while run:
    # 0: CONTROL DEL TIEMPO
    t1 = pygame.time.get_ticks()    # tiempo actual
    dt = (t1 - t0)                  # diferencial de tiempo asociado a la iteración
    t0 = t1                         # actualizar tiempo inicial para siguiente iteración
    
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
				
    # 2: EJECUTAMOS LOGICA DE LA APLICACION
    o += w*dt
	
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
        glDisable(GL_LIGHTING)
        glCallList(axes)
        glEnable(GL_LIGHTING)
    
    drawList(teapot,o = o,rot = [1,0,0])
    
    pygame.display.flip()       # vuelca el dibujo a la pantalla
    pygame.time.wait(1000/30)   # ajusta para trabajar a 30 fps.


#####################################################################
