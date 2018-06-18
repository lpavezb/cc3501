# -*- coding: iso-8859-1 -*-

import math 
from Vector2D import *
from OpenGL.GL import *

class Circulo: 
    def __init__(self, r, p, v, rgb, nt):
        
        self.r = r
        self.p = p
        self.v = v
        self.rgb = []
        self.rgb.append(rgb[0])
        self.rgb.append(rgb[1])
        self.rgb.append(rgb[2])

        self.t = []
            
        a=2*math.pi/nt

        for i in range(nt):
            ai=a*i
            self.t.append(VectorPolar(1.0,ai))
    
        # se guardan los vertices en un arreglo,
        # para no calcularlos en cada iteracion.

    def mover(self,dt):
        self.v=sumar(self.v,ponderar(dt,g))
        self.p=sumar(self.p,ponderar(dt,self.v))
                
    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p.x(),self.p.y(),0.0)
        glScalef(self.r,self.r,0.0)
        glColor4f(self.rgb[0],self.rgb[1],self.rgb[2],1.0)

        glBegin(GL_POLYGON)
            
        glVertex4f( 0.0, 0.0, 0.0 , 1.0)
        
        for v in self.t:
            glVertex4f( v.x(), v.y(), 0.0 , 1.0)

        glVertex4f(self.t[0].x(),self.t[0].y(), 0.0 , 1.0)

        glEnd()
        glPopMatrix()



