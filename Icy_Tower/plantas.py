import os

from CC3501Utils import *


####################################################
# Clase Plantas
####################################################

class Plantas(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):
        # Se dibuja la pera
        glBegin(GL_QUADS)
        a = 5
        # Plantas
        glColor3f(0.33, 0.64, 0.19)

        glVertex2f(1 * a, 15 * a)
        glVertex2f(0 * a, 15 * a)
        glVertex2f(0 * a, 16 * a)
        glVertex2f(1 * a, 16 * a)

        glVertex2f(2 * a, 14 * a)
        glVertex2f(1 * a, 14 * a)
        glVertex2f(1 * a, 15 * a)
        glVertex2f(2 * a, 15 * a)

        glVertex2f(3 * a, 13 * a)
        glVertex2f(2 * a, 13 * a)
        glVertex2f(2 * a, 14 * a)
        glVertex2f(3 * a, 14 * a)

        glVertex2f(4 * a, 10 * a)
        glVertex2f(3 * a, 10 * a)
        glVertex2f(3 * a, 13 * a)
        glVertex2f(4 * a, 13 * a)

        # Planta 2

        glVertex2f(1 * a, 0 * a)
        glVertex2f(0 * a, 0 * a)
        glVertex2f(0 * a, 2 * a)
        glVertex2f(1 * a, 2 * a)

        glVertex2f(2 * a, 2 * a)
        glVertex2f(1 * a, 2 * a)
        glVertex2f(1 * a, 4 * a)
        glVertex2f(2 * a, 4 * a)

        glVertex2f(4 * a, 4 * a)
        glVertex2f(2 * a, 4 * a)
        glVertex2f(2 * a, 5 * a)
        glVertex2f(4 * a, 5 * a)

        # Sombra plantas
        glColor3f(0.15, 0.31, 0.08)

        glVertex2f(1 * a, 14 * a)
        glVertex2f(0 * a, 14 * a)
        glVertex2f(0 * a, 15 * a)
        glVertex2f(1 * a, 15 * a)

        glVertex2f(2 * a, 13 * a)
        glVertex2f(1 * a, 13 * a)
        glVertex2f(1 * a, 14 * a)
        glVertex2f(2 * a, 14 * a)

        glVertex2f(3 * a, 12 * a)
        glVertex2f(2 * a, 12 * a)
        glVertex2f(2 * a, 13 * a)
        glVertex2f(3 * a, 13 * a)

        glVertex2f(4 * a, 9 * a)
        glVertex2f(3 * a, 9 * a)
        glVertex2f(3 * a, 11 * a)
        glVertex2f(4 * a, 11 * a)

        # Sombra planta 2

        glVertex2f(1 * a, -1 * a)
        glVertex2f(0 * a, -1 * a)
        glVertex2f(0 * a, 1 * a)
        glVertex2f(1 * a, 1 * a)

        glVertex2f(2 * a, 1 * a)
        glVertex2f(1 * a, 1 * a)
        glVertex2f(1 * a, 2 * a)
        glVertex2f(2 * a, 2 * a)

        glVertex2f(4 * a, 3 * a)
        glVertex2f(2 * a, 3 * a)
        glVertex2f(2 * a, 4 * a)
        glVertex2f(4 * a, 4 * a)

        glEnd()
