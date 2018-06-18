import os

from CC3501Utils import *


####################################################
# Clase Nube
####################################################

class Nube(Figura):
    def __init__(self, a: int, vel=Vector(0, 0), pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = a
        self.vel = vel
        super().__init__(pos, rgb)

    def figura(self):
        # Se dibuja la nube
        glBegin(GL_QUADS)
        glColor3f(0.9, 0.9, 0.9)
        a = self.a

        # Rectangulo principal
        glVertex2f(22 * a, 0 * a)
        glVertex2f(0 * a, 0 * a)
        glVertex2f(0 * a, 6 * a)
        glVertex2f(22 * a, 6 * a)

        # Rectangulos
        glVertex2f(0 * a, 1 * a)
        glVertex2f(-1 * a, 1 * a)
        glVertex2f(-1 * a, 6 * a)
        glVertex2f(0 * a, 6 * a)

        glVertex2f(-1 * a, 2 * a)
        glVertex2f(-2 * a, 2 * a)
        glVertex2f(-2 * a, 5 * a)
        glVertex2f(-1 * a, 5 * a)

        glVertex2f(22 * a, 5 * a)
        glVertex2f(2 * a, 5 * a)
        glVertex2f(2 * a, 6 * a)
        glVertex2f(22 * a, 6 * a)

        glVertex2f(19 * a, 6 * a)
        glVertex2f(3 * a, 6 * a)
        glVertex2f(3 * a, 8 * a)
        glVertex2f(19 * a, 8 * a)

        glVertex2f(19 * a, 8 * a)
        glVertex2f(6 * a, 8 * a)
        glVertex2f(6 * a, 9 * a)
        glVertex2f(19 * a, 9 * a)

        glVertex2f(18 * a, 9 * a)
        glVertex2f(7 * a, 9 * a)
        glVertex2f(7 * a, 10 * a)
        glVertex2f(18 * a, 10 * a)

        glVertex2f(17 * a, 10 * a)
        glVertex2f(8 * a, 10 * a)
        glVertex2f(8 * a, 11 * a)
        glVertex2f(17 * a, 11 * a)

        glVertex2f(16 * a, 11 * a)
        glVertex2f(9 * a, 11 * a)
        glVertex2f(9 * a, 12 * a)
        glVertex2f(16 * a, 12 * a)

        glVertex2f(23 * a, 1 * a)
        glVertex2f(22 * a, 1 * a)
        glVertex2f(22 * a, 5 * a)
        glVertex2f(23 * a, 5 * a)

        glVertex2f(24 * a, 2 * a)
        glVertex2f(23 * a, 2 * a)
        glVertex2f(23 * a, 4 * a)
        glVertex2f(24 * a, 4 * a)

        # Luces

        glColor3f(1.0, 1.0, 1.0)

        glVertex2f(-1 * a, 2 * a)
        glVertex2f(-2 * a, 2 * a)
        glVertex2f(-2 * a, 5 * a)
        glVertex2f(-1 * a, 5 * a)

        glVertex2f(3 * a, 5 * a)
        glVertex2f(-1 * a, 5 * a)
        glVertex2f(-1 * a, 6 * a)
        glVertex2f(3 * a, 6 * a)

        glVertex2f(3 * a, 6 * a)
        glVertex2f(2 * a, 6 * a)
        glVertex2f(2 * a, 7 * a)
        glVertex2f(3 * a, 7 * a)

        glVertex2f(4 * a, 7 * a)
        glVertex2f(3 * a, 7 * a)
        glVertex2f(3 * a, 9 * a)
        glVertex2f(4 * a, 9 * a)

        glVertex2f(7 * a, 8 * a)
        glVertex2f(4 * a, 8 * a)
        glVertex2f(4 * a, 9 * a)
        glVertex2f(7 * a, 9 * a)

        glVertex2f(8 * a, 9 * a)
        glVertex2f(7 * a, 9 * a)
        glVertex2f(7 * a, 10 * a)
        glVertex2f(8 * a, 10 * a)

        glVertex2f(9 * a, 10 * a)
        glVertex2f(8 * a, 10 * a)
        glVertex2f(8 * a, 11 * a)
        glVertex2f(9 * a, 11 * a)

        glVertex2f(16 * a, 11 * a)
        glVertex2f(9 * a, 11 * a)
        glVertex2f(9 * a, 12 * a)
        glVertex2f(16 * a, 12 * a)

        # Sombra
        glColor3f(0.8, 0.8, 0.8)

        glVertex2f(22 * a, 5 * a)
        glVertex2f(19 * a, 5 * a)
        glVertex2f(19 * a, 6 * a)
        glVertex2f(22 * a, 6 * a)

        glVertex2f(23 * a, 4 * a)
        glVertex2f(22 * a, 4 * a)
        glVertex2f(22 * a, 5 * a)
        glVertex2f(23 * a, 5 * a)

        glVertex2f(24 * a, 2 * a)
        glVertex2f(23 * a, 2 * a)
        glVertex2f(23 * a, 4 * a)
        glVertex2f(24 * a, 4 * a)

        glVertex2f(23 * a, 1 * a)
        glVertex2f(22 * a, 1 * a)
        glVertex2f(22 * a, 3 * a)
        glVertex2f(23 * a, 3 * a)

        glVertex2f(22 * a, 0 * a)
        glVertex2f(21 * a, 0 * a)
        glVertex2f(21 * a, 2 * a)
        glVertex2f(22 * a, 2 * a)

        glVertex2f(21 * a, 0 * a)
        glVertex2f(15 * a, 0 * a)
        glVertex2f(15 * a, 1 * a)
        glVertex2f(21 * a, 1 * a)

        # Donde pisar
        glColor3f(0.67, 0.75, 0.76)

        glVertex2f(22 * a, 2 * a * (3 / 4))
        glVertex2f(0 * a, 2 * a * (3 / 4))
        glVertex2f(0 * a, 3 * a * (3 / 4))
        glVertex2f(22 * a, 3 * a * (3 / 4))

        glEnd()
