import os

from CC3501Utils import *


####################################################
# Clase Liana
####################################################

class Liana(Figura):
    def __init__(self, a: int, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = a
        super().__init__(pos, rgb)

    def figura(self):
        # Se dibuja la pera
        glBegin(GL_QUADS)
        a = self.a
        b = abs(a)

        # Liana
        glColor3f(0.53, 0.68, 0.4)
        glColor3f(0.33, 0.64, 0.19)

        glVertex2f(5 * a, 0 * b)
        glVertex2f(0 * a, 0 * b)
        glVertex2f(0 * a, 2 * b)
        glVertex2f(5 * a, 2 * b)

        glVertex2f(8 * a, 0 * b)
        glVertex2f(5 * a, 0 * b)
        glVertex2f(5 * a, 1 * b)
        glVertex2f(8 * a, 1 * b)

        glVertex2f(10 * a, -1 * b)
        glVertex2f(8 * a, -1 * b)
        glVertex2f(8 * a, 0 * b)
        glVertex2f(10 * a, 0 * b)

        glVertex2f(12 * a, -2 * b)
        glVertex2f(10 * a, -2 * b)
        glVertex2f(10 * a, -1 * b)
        glVertex2f(12 * a, -1 * b)

        glColor3f(0.33, 0.64, 0.19)
        glVertex2f(34 * a, -3 * b)
        glVertex2f(12 * a, -3 * b)
        glVertex2f(12 * a, -2 * b)
        glVertex2f(34 * a, -2 * b)

        # Sombra plantas
        glColor3f(0.30, 0.47, 0.23)
        glColor3f(0.15, 0.31, 0.08)

        glVertex2f(5 * a, -1 * b)
        glVertex2f(0 * a, -1 * b)
        glVertex2f(0 * a, 0 * b)
        glVertex2f(5 * a, 0 * b)

        glVertex2f(8 * a, -1 * b)
        glVertex2f(5 * a, -1 * b)
        glVertex2f(5 * a, 0 * b)
        glVertex2f(8 * a, 0 * b)

        glVertex2f(10 * a, -2 * b)
        glVertex2f(8 * a, -2 * b)
        glVertex2f(8 * a, -1 * b)
        glVertex2f(10 * a, -1 * b)

        glVertex2f(12 * a, -3 * b)
        glVertex2f(9 * a, -3 * b)
        glVertex2f(9 * a, -2 * b)
        glVertex2f(12 * a, -2 * b)

        glColor3f(0.53, 0.13, 0.01)
        glVertex2f(34 * a, -4 * b)
        glVertex2f(12 * a, -4 * b)
        glVertex2f(12 * a, -3 * b)
        glVertex2f(34 * a, -3 * b)

        glEnd()
