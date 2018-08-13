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

W=640 #ancho de ventana
H=480 #alto de ventana

# inicializando ...
init_pygame((W,H),"glutfigures_01_colores")
init_opengl((W,H))

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
axes=axesList(100000)

# variables del programa
rgb = [0.0,0.0,0.0,1.0]
fig = 0;

show_axes = True
fill_polygons = True

# configuración de camara
glLoadIdentity()
gluLookAt( 2000.0, 2000.0, 2000.0, \
          0.0, 0.0, 0.0, \
          0.0, 0.0, 1.0)

# permite conocer fabricante y version de OpenGL utilizada
print glGetString(GL_VENDOR)
print glGetString(GL_VERSION)

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
                fig += 1
                print "fig = ",fig
            if event.key == K_3:
                rgb = [uniform(0,1),uniform(0,1),uniform(0,1),1.0]
                print "rgb = ",rgb
				
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
    
    glColor4fv(rgb)
    
    if fig == 0:
        glutSolidSphere(500,100,100)
    elif fig == 1:
        glutSolidTeapot(800)
    elif fig == 2:
        glutSolidCube(800)
    elif fig == 3:
        glutSolidCone(500,1000,100,100)
    elif fig == 4:
        glutSolidTorus(100,700,100,100)
        
    elif fig == 5:
        glutWireSphere(500,10,10)
    elif fig == 6:
        glutWireTeapot(800)
    elif fig == 7:
        glutWireCube(800)
    elif fig == 8:    
        glutWireCone(500,1000,100,100)
    elif fig == 9:
        glutWireTorus(100,700,100,100)
        
    elif fig >=10:
        glPushMatrix()
        glScalef(600,600,600)
        
        if fig == 11:
            glutSolidDodecahedron() # tiene radio 3 por defecto
        elif fig == 12:
            glutSolidOctahedron()  # tiene radio 1 por defecto
        elif fig == 13:
            glutSolidTetrahedron() # tiene radio 3 por defecto
        elif fig == 14:
            glutSolidIcosahedron()  # tiene radio 1 por defecto
    
        elif fig == 11:
            glutWireDodecahedron() # tiene radio 3 por defecto
        elif fig == 12:
            glutWireOctahedron()  # tiene radio 1 por defecto
        elif fig == 13:
            glutWireTetrahedron() # tiene radio 3 por defecto
        elif fig == 14:
            glutWireIcosahedron()  # tiene radio 1 por defecto
            
        elif fig == 15:
            fig = 0
    
        glPopMatrix() 
    
    pygame.display.flip()       # vuelca el dibujo a la pantalla
    pygame.time.wait(1000/30)   # ajusta para trabajar a 30 fps.


#####################################################################
