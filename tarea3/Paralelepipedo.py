# -*- coding: utf-8 -*-
from CC3501Utils import *


class Paralelepipedo:
    # Crea un paralelepipedo centrado en 0 con las dimensiones especificadas
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

        self.pos = Vector(0, 0, 0)
        self.angulo = 0

        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)



        # poliedro definido desde el vertice superior izquierdo en sentido antihorario
        # p1-p4 cara superior
        # p5-p8 cara inferior
        p1 = Vector(-self.largo / 2.0, -self.ancho / 2.0, self.alto / 2.0)
        p2 = Vector(-self.largo / 2.0, self.ancho / 2.0, self.alto / 2.0)
        p3 = Vector(self.largo / 2.0, self.ancho / 2.0, self.alto / 2.0)
        p4 = Vector(self.largo / 2.0, -self.ancho / 2.0, self.alto / 2.0)
        p5 = Vector(-self.largo / 2.0, -self.ancho / 2.0, -self.alto / 2.0)
        p6 = Vector(-self.largo / 2.0, self.ancho / 2.0, -self.alto / 2.0)
        p7 = Vector(self.largo / 2.0, self.ancho / 2.0, -self.alto / 2.0)
        p8 = Vector(self.largo / 2.0, -self.ancho / 2.0, -self.alto / 2.0)

        glBegin(GL_TRIANGLES)
        color = [28, 195, 204]  # cafe
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]

        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])  # amarillo
        cuadrilatero(p1, p4, p3, p2)
        cuadrilatero(p5, p6, p7, p8)
        cuadrilatero(p1, p2, p6, p5)
        cuadrilatero(p2, p3, p7, p6)
        cuadrilatero(p3, p4, p8, p7)
        cuadrilatero(p4, p1, p5, p8)

        glEnd()
        glEndList()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.angulo, 0, 0, 1)  # Rotacion en torno a eje Z
        glCallList(self.lista)
        glPopMatrix()
