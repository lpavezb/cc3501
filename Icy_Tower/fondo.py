import os

from CC3501Utils import *


####################################################
# Clase Fondo
####################################################

class Fondo(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)

        glColor3f(103 / 255.0, 193 / 255.0, 182 / 255.0)

        glVertex2f(800, 0)
        glVertex2f(0, 0)
        glVertex2f(0, 600)
        glVertex2f(800, 600)
        glEnd()
