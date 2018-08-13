from Paralelepipedo import *


class Pasto:

    def __init__(self, pos=Vector(0, 0, 0)):
        self.pos = pos

        self.angulo = 0

        self.lista = 0

        self.crear()

    def crear(self):
        self.lista = glGenLists(1)

        glNewList(self.lista, GL_COMPILE)

        glBegin(GL_QUADS)

        glColor4f(28 / 255.0, 119 / 255.0, 17 / 255.0, 1.0)

        glVertex4f(-10000, -10000, 0.0, 1.0)

        glVertex4f(-10000, 10000, 0.0, 1.0)

        glVertex4f(10000, 10000, 0.0, 1.0)

        glVertex4f(10000, -10000, 0.0, 1.0)

        glEnd()

        glEndList()

    def dibujar(self):
        glDisable(GL_LIGHTING)

        glPushMatrix()

        glCallList(self.lista)

        glPopMatrix()

        glEnable(GL_LIGHTING)
