import os

from CC3501Utils import *


####################################################
# Clase Reloj
####################################################

class Circulo1(Figura):
    def __init__(self, radio: int, pos=Vector(0, 0), rgb=(132 / 255.0, 7 / 255.0, 88 / 255.0)):
        self.radio = radio
        super().__init__(pos, rgb)

    def figura(self):
        # reloj
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0.0, 0.0)

        # radio = 50
        ang = 2 * pi / 12
        for i in range(12):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * self.radio, sin(ang_i) * self.radio)

        glVertex2f(1.0 * self.radio, 0.0)

        glEnd()


class Manecilla(Figura):
    def __init__(self, ang=0, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.ang = ang
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)
        ang = self.ang

        glColor3f(0 / 255.0, 0 / 255.0, 0 / 255.0)
        # Vectores a rotar
        v1 = Vector(35, 0)
        v2 = Vector(0, 0)
        v3 = Vector(0, 10)
        v4 = Vector(35, 10)

        # rotaciones
        rot1 = rotar(v1, ang)
        rot2 = rotar(v2, ang)
        rot3 = rotar(v3, ang)
        rot4 = rotar(v4, ang)

        glVertex2f(rot1.x, rot1.y)
        glVertex2f(rot2.x, rot2.y)
        glVertex2f(rot3.x, rot3.y)
        glVertex2f(rot4.x, rot4.y)

        glVertex2f(10, 0)
        glVertex2f(0, 0)
        glVertex2f(0, 25)
        glVertex2f(10, 25)
        glEnd()
