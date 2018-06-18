# -*- coding: iso-8859-1 -*-

from Vector2D import *
from OpenGL.GL import *



class Nave:
    def __init__(self):
        self.r = 30 # "radio" aprox de la nave
        self.p = Vector(0.0,100.0)  # posicion de la nave
        self.sp = 10 # cantidad de ataques especiales

    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p.x(),self.p.y(),0.0)
        glColor4f(1.0,1.0,1.0,1.0)

        glBegin(GL_POLYGON)

        glVertex2f(0,100)
        glVertex2f(30,0)
        glVertex2f(-30,0)

        glEnd()
        glPopMatrix()


