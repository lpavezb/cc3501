# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: cubos_03_textura.py
----------------------
Dibuja un paralelepipedo texturizado rotando. No utiliza iluminación

Control del programa:
1: Visualiza o no los ejes de coordenadas
2: Pinta o no los polígonos
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

    # para utilizar texturas    
    glLightModeli(GL_LIGHT_MODEL_COLOR_CONTROL, GL_SEPARATE_SPECULAR_COLOR)
    glEnable(GL_TEXTURE_2D)
	
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

def listaCuboTex(texture):
    
    a = [-0.5,-0.5,-0.5]
    b = [ 0.5,-0.5,-0.5]
    c = [ 0.5,-0.5, 0.5]
    d = [-0.5,-0.5, 0.5]
    e = [-0.5, 0.5,-0.5]
    f = [ 0.5, 0.5,-0.5]
    g = [ 0.5, 0.5, 0.5]
    h = [-0.5, 0.5, 0.5]
    
    t1 = [0,0]
    t2 = [1,0]
    t3 = [1,1]
    t4 = [0,1]
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glBegin(GL_QUADS)
    
    tdraw4Vertexfv(a,b,c,d,t1,t2,t3,t4)
    tdraw4Vertexfv(b,f,g,c,t1,t2,t3,t4)
    tdraw4Vertexfv(f,e,h,g,t1,t2,t3,t4)
    tdraw4Vertexfv(e,a,d,h,t1,t2,t3,t4)
    tdraw4Vertexfv(d,c,g,h,t1,t2,t3,t4)
    tdraw4Vertexfv(a,e,f,b,t1,t2,t3,t4)
    
    glEnd()
    
    glDisable(GL_TEXTURE_2D)
    
    glEndList()
    
    return lista

#####################################################################

W=640 #ancho de ventana
H=480 #alto de ventana

# inicializando ...
init_pygame((W,H),"cubos_03_textura")
init_opengl((W,H))

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
tex = generarTex("ladrillo.jpg",False,False)

cubo = listaCuboTex(tex)

axes = axesList(100000)

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

#observar que al agregar iluminación se ven los objetos negros...
#glEnable(GL_LIGHTING)

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
        glCallList(axes)
    
    drawList(cubo,pos = [0,0,0],o = o,rot = [0,0,1],sz = [1000,1000,500])
    
    pygame.display.flip()       # vuelca el dibujo a la pantalla
    pygame.time.wait(1000/30)   # ajusta para trabajar a 30 fps.


#####################################################################
