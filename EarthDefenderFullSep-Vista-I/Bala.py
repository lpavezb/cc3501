# -*- coding: iso-8859-1 -*-


from Vector2D import *
from OpenGL.GL import *

class Bala:
    def __init__(self, p, v):
        self.r = 5 # "radio" aprox de la bala
        self.p = p
        self.v = v
        self.vive = True # marca para poder eliminar ...

    def mover(self,dt,a):
        self.v=sumar(self.v,ponderar(dt,a))
        self.p=sumar(self.p,ponderar(dt,self.v))

    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p.x(),self.p.y(),0.0)
        glRotatef(self.v.anguloG(),0.0,0.0,1.0)
        glColor4f(1.0,1.0,0.0,1.0)

        glBegin(GL_POLYGON)

        glVertex2f(0,5.0)
        glVertex2f(10.0,0)
        glVertex2f(0,-5.0)

        glEnd()
        glPopMatrix()


