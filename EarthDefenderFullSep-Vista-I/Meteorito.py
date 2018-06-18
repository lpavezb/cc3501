# -*- coding: iso-8859-1 -*-

from Vector2D import *
from OpenGL.GL import *

class Meteorito:
    def __init__(self, r, p, v, o, w):
        self.r = r # "radio" aprox del meteorito
        self.p = p # posicion
        self.v = v # velocidad
        self.o = o # orientacion en grados del meteorito.
        self.w = w # velocidad angular del meteorito.
        self.vive = True # marca para poder eliminar ...
        self.rgb=[0.7,0.5,0.04,0.0]

    def mover(self,dt,a):
        # cinematica,
        # acelera la velocidad.
        self.v=sumar(self.v,ponderar(dt,a))
        # modifica la posicion con la velocidad instantanea.
        self.p=sumar(self.p,ponderar(dt,self.v))

        # rotar 
        self.o += self.w * dt

    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p.x(),self.p.y(),0.0)
        glScalef(self.r,self.r,0.0)
        glRotatef(self.o,0.0,0.0,1)
        glColor4f(self.rgb[0],self.rgb[1],self.rgb[2],1.0)

        glBegin(GL_POLYGON)

        glVertex2f(-143/150.0,-26/150.0)
        glVertex2f(-154/150.0,86/150.0)
        glVertex2f(-66/150.0,167/150.0)
        glVertex2f(142/150.0,110/150.0)
        glVertex2f(175/150.0,-44/150.0)
        glVertex2f(155/150.0,-108/150.0)
        glVertex2f(53/150.0,-108/150.0)
        glVertex2f(-39/150.0,-149/150.0)
        glVertex2f(-162/150.0,-121/150.0)

        glEnd()
        glPopMatrix()
