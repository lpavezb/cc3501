import os

from CC3501Utils import *


####################################################
# Clase Pajaro
####################################################

class Pajaro(Figura):
    def __init__(self, a: int, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = a
        super().__init__(pos, rgb)

    def figura(self):
        # Se dibuja la pera
        glBegin(GL_QUADS)
        glColor3f(0.38, 0.19, 0.14)

        # Parte cafe
        a = self.a

        glVertex2f(0 * a, 0 * a)
        glVertex2f(-8 * a, 0 * a)
        glVertex2f(-8 * a, 2 * a)
        glVertex2f(0 * a, 2 * a)

        glVertex2f(0 * a, 2 * a)
        glVertex2f(-4 * a, 2 * a)
        glVertex2f(-4 * a, 3 * a)
        glVertex2f(0 * a, 3 * a)

        glVertex2f(-8 * a, 0 * a)
        glVertex2f(-9 * a, 0 * a)
        glVertex2f(-9 * a, 1 * a)
        glVertex2f(-8 * a, 1 * a)

        glVertex2f(-13 * a, -4 * a)
        glVertex2f(-21 * a, -4 * a)
        glVertex2f(-21 * a, -3 * a)
        glVertex2f(-13 * a, -3 * a)

        glVertex2f(-14 * a, -5 * a)
        glVertex2f(-20 * a, -5 * a)
        glVertex2f(-20 * a, -4 * a)
        glVertex2f(-14 * a, -4 * a)

        # Parte gris

        glColor3f(0.7, 0.7, 0.7)

        glVertex2f(-4 * a, 2 * a)
        glVertex2f(-7 * a, 2 * a)
        glVertex2f(-7 * a, 3 * a)
        glVertex2f(-4 * a, 3 * a)

        glVertex2f(-1 * a, 3 * a)
        glVertex2f(-6 * a, 3 * a)
        glVertex2f(-6 * a, 4 * a)
        glVertex2f(-1 * a, 4 * a)

        glVertex2f(-2 * a, 4 * a)
        glVertex2f(-5 * a, 4 * a)
        glVertex2f(-5 * a, 5 * a)
        glVertex2f(-2 * a, 5 * a)

        glVertex2f(0 * a, 0 * a)
        glVertex2f(-1 * a, 0 * a)
        glVertex2f(-1 * a, -1 * a)
        glVertex2f(0 * a, -1 * a)

        glVertex2f(-1 * a, -1 * a)
        glVertex2f(-2 * a, -1 * a)
        glVertex2f(-2 * a, -2 * a)
        glVertex2f(-1 * a, -2 * a)

        glVertex2f(-2 * a, -2 * a)
        glVertex2f(-5 * a, -2 * a)
        glVertex2f(-5 * a, -5 * a)
        glVertex2f(-2 * a, -5 * a)

        glVertex2f(-3 * a, -5 * a)
        glVertex2f(-6 * a, -5 * a)
        glVertex2f(-6 * a, -7 * a)
        glVertex2f(-3 * a, -7 * a)

        glVertex2f(-6 * a, -6 * a)
        glVertex2f(-7 * a, -6 * a)
        glVertex2f(-7 * a, -7 * a)
        glVertex2f(-6 * a, -7 * a)

        glVertex2f(-3 * a, -7 * a)
        glVertex2f(-14 * a, -7 * a)
        glVertex2f(-14 * a, -8 * a)
        glVertex2f(-3 * a, -8 * a)

        glVertex2f(-4 * a, -8 * a)
        glVertex2f(-13 * a, -8 * a)
        glVertex2f(-13 * a, -9 * a)
        glVertex2f(-4 * a, -9 * a)

        glVertex2f(-5 * a, -9 * a)
        glVertex2f(-12 * a, -9 * a)
        glVertex2f(-12 * a, -10 * a)
        glVertex2f(-5 * a, -10 * a)

        # Parte blanca

        glColor3f(1, 1, 1)

        glVertex2f(-1 * a, 0 * a)
        glVertex2f(-7 * a, 0 * a)
        glVertex2f(-7 * a, -1 * a)
        glVertex2f(-1 * a, -1 * a)

        glVertex2f(-2 * a, -1 * a)
        glVertex2f(-5 * a, -1 * a)
        glVertex2f(-5 * a, -2 * a)
        glVertex2f(-2 * a, -2 * a)

        # Parte negra
        glColor3f(0, 0, 0)
        glVertex2f(1 * a, 1 * a)
        glVertex2f(-1 * a, 1 * a)
        glVertex2f(-1 * a, 0 * a)
        glVertex2f(1 * a, 0 * a)

        glVertex2f(-2 * a, 2 * a)
        glVertex2f(-3 * a, 2 * a)
        glVertex2f(-3 * a, 1 * a)
        glVertex2f(-2 * a, 1 * a)

        # Ala

        glColor3f(0.6, 0.35, 0.28)

        glVertex2f(-16 * a, -3 * a)
        glVertex2f(-7 * a, -3 * a)
        glVertex2f(-7 * a, -6 * a)
        glVertex2f(-16 * a, -6 * a)

        glVertex2f(-12 * a, -2 * a)
        glVertex2f(-7 * a, -2 * a)
        glVertex2f(-7 * a, -3 * a)
        glVertex2f(-12 * a, -3 * a)

        glColor3f(0.38, 0.19, 0.14)

        glVertex2f(-7 * a, -1 * a)
        glVertex2f(-10 * a, -1 * a)
        glVertex2f(-10 * a, 0 * a)
        glVertex2f(-7 * a, 0 * a)

        glVertex2f(-5 * a, -2 * a)
        glVertex2f(-8 * a, -2 * a)
        glVertex2f(-8 * a, -1 * a)
        glVertex2f(-5 * a, -1 * a)

        glVertex2f(-10 * a, -2 * a)
        glVertex2f(-11 * a, -2 * a)
        glVertex2f(-11 * a, -1 * a)
        glVertex2f(-10 * a, -1 * a)

        glVertex2f(-11 * a, -3 * a)
        glVertex2f(-13 * a, -3 * a)
        glVertex2f(-13 * a, -2 * a)
        glVertex2f(-11 * a, -2 * a)

        glVertex2f(-8 * a, -3 * a)
        glVertex2f(-10 * a, -3 * a)
        glVertex2f(-10 * a, -2 * a)
        glVertex2f(-8 * a, -2 * a)

        glVertex2f(-6 * a, -4 * a)
        glVertex2f(-8 * a, -4 * a)
        glVertex2f(-8 * a, -3 * a)
        glVertex2f(-6 * a, -3 * a)

        glVertex2f(-5 * a, -5 * a)
        glVertex2f(-6 * a, -5 * a)
        glVertex2f(-6 * a, -2 * a)
        glVertex2f(-5 * a, -2 * a)

        glVertex2f(-6 * a, -4 * a)
        glVertex2f(-7 * a, -4 * a)
        glVertex2f(-7 * a, -6 * a)
        glVertex2f(-6 * a, -6 * a)

        glVertex2f(-7 * a, -5 * a)
        glVertex2f(-8 * a, -5 * a)
        glVertex2f(-8 * a, -7 * a)
        glVertex2f(-7 * a, -7 * a)

        glVertex2f(-16 * a, -6 * a)
        glVertex2f(-8 * a, -6 * a)
        glVertex2f(-8 * a, -7 * a)
        glVertex2f(-16 * a, -7 * a)

        glVertex2f(-17 * a, -4 * a)
        glVertex2f(-16 * a, -4 * a)
        glVertex2f(-16 * a, -6 * a)
        glVertex2f(-17 * a, -6 * a)

        glVertex2f(-16 * a, -3 * a)
        glVertex2f(-15 * a, -3 * a)
        glVertex2f(-15 * a, -5 * a)
        glVertex2f(-16 * a, -5 * a)

        glVertex2f(-15 * a, -3 * a)
        glVertex2f(-13 * a, -3 * a)
        glVertex2f(-13 * a, -4 * a)
        glVertex2f(-15 * a, -4 * a)

        glColor3f(0.8, 0.8, 0.8)

        glVertex2f(-7 * a, -2 * a)
        glVertex2f(-10 * a, -2 * a)
        glVertex2f(-10 * a, -1 * a)
        glVertex2f(-7 * a, -1 * a)

        glVertex2f(-6 * a, -3 * a)
        glVertex2f(-8 * a, -3 * a)
        glVertex2f(-8 * a, -2 * a)
        glVertex2f(-6 * a, -2 * a)

        glEnd()
