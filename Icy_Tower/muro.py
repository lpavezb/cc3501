import os

from CC3501Utils import *


####################################################
# Clase Muro
####################################################


class Muro(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):
        # Se dibuja la pera
        glBegin(GL_QUADS)

        glColor3f(0.60, 0.20, 0.08)

        # Forma de la pera
        a = 5

        # vertical 0
        glVertex2f(2 * a, 24 * a)
        glVertex2f(0 * a, 24 * a)
        glVertex2f(0 * a, 0 * a)
        glVertex2f(2 * a, 0 * a)

        # vertical 1
        glColor3f(0.53, 0.13, 0.01)
        glColor3f(0.33, 0.07, 0.00)

        glVertex2f(4 * a, 24 * a)
        glVertex2f(2 * a, 24 * a)
        glVertex2f(2 * a, 0 * a)
        glVertex2f(4 * a, 0 * a)

        # Luces
        glColor3f(0.74, 0.23, 0.07)
        glColor3f(0.53, 0.13, 0.01)

        # Vertical 0
        glVertex2f(3 * a, 0 * a)
        glVertex2f(2 * a, 0 * a)
        glVertex2f(2 * a, 2 * a)
        glVertex2f(3 * a, 2 * a)

        glVertex2f(2 * a, 1 * a)
        glVertex2f(1 * a, 1 * a)
        glVertex2f(1 * a, 5 * a)
        glVertex2f(2 * a, 5 * a)

        glVertex2f(3 * a, 4 * a)
        glVertex2f(2 * a, 4 * a)
        glVertex2f(2 * a, 9 * a)
        glVertex2f(3 * a, 9 * a)

        glVertex2f(2 * a, 8 * a)
        glVertex2f(1 * a, 8 * a)
        glVertex2f(1 * a, 11 * a)
        glVertex2f(2 * a, 11 * a)

        glVertex2f(3 * a, 11 * a)
        glVertex2f(1 * a, 11 * a)
        glVertex2f(1 * a, 14 * a)
        glVertex2f(3 * a, 14 * a)

        glVertex2f(4 * a, 13 * a)
        glVertex2f(3 * a, 13 * a)
        glVertex2f(3 * a, 14 * a)
        glVertex2f(4 * a, 14 * a)

        glVertex2f(3 * a, 14 * a)
        glVertex2f(2 * a, 14 * a)
        glVertex2f(2 * a, 18 * a)
        glVertex2f(3 * a, 18 * a)

        glVertex2f(2 * a, 17 * a)
        glVertex2f(1 * a, 17 * a)
        glVertex2f(1 * a, 22 * a)
        glVertex2f(2 * a, 22 * a)

        glVertex2f(3 * a, 21 * a)
        glVertex2f(2 * a, 21 * a)
        glVertex2f(2 * a, 24 * a)
        glVertex2f(3 * a, 24 * a)

        glVertex2f(1 * a, 19 * a)
        glVertex2f(0 * a, 19 * a)
        glVertex2f(0 * a, 20 * a)
        glVertex2f(1 * a, 20 * a)

        glEnd()
