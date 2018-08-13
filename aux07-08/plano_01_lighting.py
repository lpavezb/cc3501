# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: plano_01_lighting.py
----------------
Dibuja figuras GLUT en la escena utilizando listas.

Control del programa:
UP/DOWN/LEFT/RIGHT: mueven la fuente de luz sobre el plano
q/a: modifican el SPOT_CUTOFF
1: visualiza o no los ejes de coordenadas
2: visualiza o no como malla de alambre
3: alterna entre smooth y flat
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
    
	glLightfv(GL_LIGHT0, GL_POSITION, [ 0.0, 0.0, 1000.0, 1.0 ])
	glLightfv(GL_LIGHT0, GL_AMBIENT , [ 0.2, 0.2, 0.2, 1.0])
	glLightfv(GL_LIGHT0, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0])
	glLightfv(GL_LIGHT0, GL_DIFFUSE , [ 1.0, 1.0, 1.0, 1.0])
 
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
	glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
 
	glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 60.0)
	glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [ 0.0, 0.0, -1.0])
	glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 0.0)
 
	glEnable(GL_LIGHT0)

#####################################################################

def listaPlano(nx,ny,sz,rgb):
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0,0.0,0.0,1.0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb)
    glMaterialfv(GL_FRONT, GL_SPECULAR,[1.0,1.0,1.0,1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [127.0])
    glMaterialfv(GL_FRONT, GL_EMISSION, [0.0,0.0,0.0,1.0])
    
    glPushMatrix()
        
    glBegin(GL_QUADS)
    
    for i in range(-nx/2,nx/2):
        for j in range(-ny/2,ny/2):
            a = [i*sz,j*sz,0,1]
            b = [(i+1)*sz,j*sz,0,1]
            c = [(i+1)*sz,(j+1)*sz,0,1]
            d = [i*sz,(j+1)*sz,0,1]
            
            n = [0,0,1]
            
            draw4Vertexfvn4(a,b,c,d,n,n,n,n)
    
    glEnd()
    
    glPopMatrix()
    
    glEndList()
    
    return lista

#####################################################################

W=640 #ancho de ventana
H=480 #alto de ventana

# inicializando ...
init_pygame((W,H),"plano_01_lighting")
init_opengl((W,H))

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
axes = axesList(100000)
plano = listaPlano(60,80,100,[0,0,1,1])

# variables del programa
px_luz = 0.0
py_luz = 0.0
v = 10.0

s = 0.1
spot_cutoff = 45.0

right = False
left = False
up = False
down = False
t_q = False
t_a = False

show_axes = True
fill_polygons = True
smooth_flat = True

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
            if event.key == K_3:
                smooth_flat = not smooth_flat
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
            if event.key == K_q:
                t_q = True
            if event.key == K_a:
                t_a = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_q:
                t_q = False
            if event.key == K_a:
                t_a = False
				
    # 2: EJECUTAMOS LOGICA DE LA APLICACION
    if left:
        px_luz += v*dt
    if right:
        px_luz -= v*dt
        
    if up:
        py_luz += v*dt
    if down:
        py_luz -= v*dt
        
    if t_q:
        spot_cutoff += s*dt
    if t_a:
        spot_cutoff -= s*dt
        
    if spot_cutoff < 0.0:
        spot_cutoff = 0.0
    elif spot_cutoff > 90.0:
        spot_cutoff = 90.0
 
    # 3: DIBUJAMOS LOS ELEMENTOS
    # limpia la pantalla (buffer de color y de profundidad)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLightfv(GL_LIGHT0, GL_POSITION, [ px_luz, py_luz, 1000.0, 1.0 ])
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, spot_cutoff)    
    
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
    
    if smooth_flat:
        glShadeModel(GL_SMOOTH)
    else:
        glShadeModel(GL_FLAT)
    
    glCallList(plano)
    
    pygame.display.flip()       # vuelca el dibujo a la pantalla
    pygame.time.wait(1000/30)   # ajusta para trabajar a 30 fps.


#####################################################################
