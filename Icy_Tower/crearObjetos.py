import os
import random
from CC3501Utils import *

from pera import *
from pajaro import *
from muro import *
from nube import *
from plantas import *
from liana import *
from reloj import *
from fondo import *
from vista import *


def crearObjetos():
    figuras = []
    decoracion = []
    nubes = []
    lianas = []
    pajaros = []
    reloj = []

    fondo = Fondo(Vector(0, 0))

    # Creacion de primera nube
    nube = Nube(8, Vector(0, 0), Vector(100, 80))
    figuras.append(nube)
    nubes.append(nube)

    esp = 100
    i = 1
    # Creacion random de objetos
    while i < 90:
        # Creacion de nubes
        v = random.randint(esp * i, esp * (i + 1))
        h = random.randint(150, 550)
        s = random.randint(2, 9)
        nube = Nube(s, Vector(0, 0), Vector(h, v))
        figuras.append(nube)
        nubes.append(nube)
        # Creacion de pajaros
        v = random.randint(esp * (i + 1), esp * (i + 2))
        h = random.randint(100, 700)
        s = random.randint(6, 7)
        pajaro = Pajaro(s, Vector(h, v))
        figuras.append(pajaro)
        pajaros.append(pajaro)

        # Creacion de lianas
        v = random.randint(esp * (i + 2), esp * (i + 3))
        h = random.randint(30, 730)
        s = random.randint(5, 6)
        liana = Liana(s, Vector(60, v))
        figuras.append(liana)
        lianas.append(liana)

        # Creacion de lianas con otra orientacion
        v = random.randint(esp * (i + 3), esp * (i + 4))
        h = random.randint(30, 730)
        s = random.randint(5, 6)
        liana = Liana(-1 * s, Vector(740, v))
        figuras.append(liana)
        lianas.append(liana)

        i = i + 4

    for j in range(0, 3):
        for i in range(0, 5):
            muro = Muro(Vector(20 * j, 120 * i))
            decoracion.append(muro)
        for i in range(0, 10):
            planta = Plantas(Vector(20 * j, 100 * i + 27 * j))
            decoracion.append(planta)

    for j in range(0, 4):
        for i in range(0, 5):
            muro = Muro(Vector(800 - 20 * j, 120 * i))
            decoracion.append(muro)
        for i in range(0, 10):
            planta = Plantas(Vector(800 - 20 * j, 100 * i + 27 * j))
            decoracion.append(planta)

    #########################################
    # Reloj
    #########################################

    c = Circulo1(50, Vector(80, 530), (132 / 255.0, 7 / 255.0, 88 / 255.0))
    reloj.append(c)

    c = Circulo1(40, Vector(80, 530), (239 / 255.0, 227 / 255.0, 91 / 255.0))
    reloj.append(c)

    m = Manecilla(0, Vector(80 - 5, 530 - 5))
    reloj.append(m)

    resultado = [figuras, decoracion, nubes, lianas, pajaros, reloj, fondo]
    return resultado
