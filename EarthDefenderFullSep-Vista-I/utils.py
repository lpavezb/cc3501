# -*- coding: iso-8859-1 -*-


from Vector2D import *
from random import uniform
from Meteorito import *


def estanChocando(c1, c2):
    return distancia(c1.p, c2.p) < (c1.r + c2.r)


def fuera(c, w, h):
    # elimina el objeto c si es que esta fuera de la pantalla.
    if c.p.x() > w + 300 or c.p.x() < -300 or c.p.y() > h + 300 or (c.p.y() < 100 and c.p.x() < 0 and c.p.x() > w):
        c.vive = False


def impacto(tierra, m, Rmin, Rmax, w):
    # si hay impacto del meteorito con la tierra, la danna y elimina el meteorito
    if m.p.y() < 100 and m.p.x() > 0 and m.p.x() < w:
        tierra.impactar(10.0 + 40.0 * (m.r - Rmin) / (Rmax - Rmin))
        m.vive = False


#####################################################################

def crearMeteorito(w, h, Rmin, Rmax):
    # crea un meteorito aleatorio
    r = uniform(Rmin, Rmax)
    p = Vector(uniform(0, w), h + Rmax)
    v = Vector(0, 0)
    o = uniform(0, 360)
    v_ang = uniform(-5.0, 5.0)
    return Meteorito(r, p, v, o, v_ang)


def limpiar(cs):
    # saca los objetos destruidos del contenedor cs.
    n = len(cs)
    aux = []
    for i in range(n):
        c = cs.pop(0)
        if c.vive:
            aux.append(c)
    for a in aux:
        cs.append(a)
