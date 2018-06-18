# -*- coding: iso-8859-1 -*-

from Circulo import *
import math
from Vector2D import *


class Tierra:
    def __init__(self,w):
        self.c = Circulo(800,Vector(w/2,-700),Vector(0,0),[0,0,1],50)
        self.vida = 1000.0

    def dibujar(self):
        self.c.dibujar()

    def impactar(self,x):
        self.vida = self.vida-x

        # valor entre 0 y 1.
        # 0 = cero vidas = rojo
        # 1 = 1000 vidas = azul
        p=self.vida/1000.0

        # cambia el color de azul a rojo al disminuir p.
        self.c.rgb=[1-p,self.c.rgb[1],p]

