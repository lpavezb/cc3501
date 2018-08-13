# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: cubos_02_lighting.py
----------------------------
Dibuja 4 cubos rotando con distintos efectos de iluminación.

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
    #glOrtho(-2*width,2*width,-2*height,2*height,1,20000)
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

def listaCuboFlat():
    
    a = [-0.5,-0.5,-0.5]
    b = [ 0.5,-0.5,-0.5]
    c = [ 0.5,-0.5, 0.5]
    d = [-0.5,-0.5, 0.5]
    e = [-0.5, 0.5,-0.5]
    f = [ 0.5, 0.5,-0.5]
    g = [ 0.5, 0.5, 0.5]
    h = [-0.5, 0.5, 0.5]
    
    n1 = [0,-1,0]
    n2 = [1,0,0]
    n3 = [0,1,0]
    n4 = [-1,0,0]
    n5 = [0,0,1]
    n6 = [0,0,-1]
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glBegin(GL_QUADS)
    
    draw4Vertexfvn(a,b,c,d,n1)
    draw4Vertexfvn(b,f,g,c,n2)
    draw4Vertexfvn(f,e,h,g,n3)
    draw4Vertexfvn(e,a,d,h,n4)
    draw4Vertexfvn(d,c,g,h,n5)
    draw4Vertexfvn(a,e,f,b,n6)
    
    glEnd()
    
    glEndList()
    
    return lista
    
def listaCuboSmooth():
    
    a = [-0.5,-0.5,-0.5]
    b = [ 0.5,-0.5,-0.5]
    c = [ 0.5,-0.5, 0.5]
    d = [-0.5,-0.5, 0.5]
    e = [-0.5, 0.5,-0.5]
    f = [ 0.5, 0.5,-0.5]
    g = [ 0.5, 0.5, 0.5]
    h = [-0.5, 0.5, 0.5]
    
    n1 = [0,-1,0]
    n2 = [1,0,0]
    n3 = [0,1,0]
    n4 = [-1,0,0]
    n5 = [0,0,1]
    n6 = [0,0,-1]
    
    na = meanList([n1,n4,n6])
    nb = meanList([n1,n2,n6])
    nc = meanList([n1,n2,n5])
    nd = meanList([n1,n4,n5])
    ne = meanList([n3,n4,n6])
    nf = meanList([n2,n3,n6])
    ng = meanList([n2,n3,n5])
    nh = meanList([n3,n4,n5])
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glBegin(GL_QUADS)
    
    draw4Vertexfvn4(a,b,c,d,na,nb,nc,nd)
    draw4Vertexfvn4(b,f,g,c,nb,nf,ng,nc)
    draw4Vertexfvn4(f,e,h,g,nf,ne,nh,ng)
    draw4Vertexfvn4(e,a,d,h,ne,na,nd,nh)
    draw4Vertexfvn4(d,c,g,h,nd,nc,ng,nh)
    draw4Vertexfvn4(a,e,f,b,na,ne,nf,nb)
    
    glEnd()
    
    glEndList()
    
    return lista

#####################################################################

W=640 #ancho de ventana
H=480 #alto de ventana

# inicializando ...
init_pygame((W,H),"cubos_02_lighting")
init_opengl((W,H))

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
cubo = listaCuboFlat()
cubo_s = listaCuboSmooth()

axes = axesList(100000)
 
# variables del programa
o = 30
w = 0.1

show_axes = True
fill_polygons = True

# configuración de camara
glLoadIdentity()
gluLookAt( 2000.0, 1000.0, 2000.0, \
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
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0,0.0,0.0,1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0,0.0,0.0,1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR,[1.0,1.0,1.0,1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [10.0])
    glMaterialfv(GL_FRONT, GL_EMISSION, [0.0,0.0,0.0,1.0])
    
    glShadeModel(GL_FLAT)    
    drawList(cubo,pos = [0,-1000,0],o = o,rot = [0,0,1],sz = [700,700,700])
    drawList(cubo_s,pos = [0,-2000,0],o = o,rot = [0,0,1],sz = [700,700,700])
    
    glShadeModel(GL_SMOOTH)
    drawList(cubo,pos = [0,1000,0],o = o,rot = [0,0,1],sz = [700,700,700])
    drawList(cubo_s,pos = [0,0,0],o = o,rot = [0,0,1],sz = [700,700,700])
    
    pygame.display.flip()       # vuelca el dibujo a la pantalla
    # pygame.time.wait(1000/30)   # ajusta para trabajar a 30 fps.
    pygame.time.wait(1000)
#####################################################################
