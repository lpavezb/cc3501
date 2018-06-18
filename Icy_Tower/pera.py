import os

from CC3501Utils import *

global gVer, gHor, MIN_VEL
MIN_VEL = -56
gVer = Vector(0, -15.0)
gHor = Vector(6.0, 0)


####################################################
# Clase Pera
####################################################
class Pera(Figura):
    def __init__(self, a: int, vel=Vector(4, 0), pos=Vector(0, 0), flotando=False, saltos=10, rgb=(1.0, 1.0, 1.0)):
        self.a = 7  # Factor de escala
        self.vel = vel
        self.flotando = flotando
        super().__init__(pos, rgb)

    def figura(self):
        # Se dibuja la pera
        glBegin(GL_QUADS)
        glColor3f(0.53, 0.77, 0.23)

        # Forma de la pera
        a = self.a

        # horizontal 0
        glVertex2f(2 * a, -4 * abs(a))
        glVertex2f(-3 * a, -4 * abs(a))
        glVertex2f(-3 * a, -5 * abs(a))
        glVertex2f(2 * a, -5 * abs(a))

        # horizontal 1
        glVertex2f(3 * a, 0 * abs(a))
        glVertex2f(-4 * a, 0 * abs(a))
        glVertex2f(-4 * a, -4 * abs(a))
        glVertex2f(3 * a, -4 * abs(a))

        # horizontal 2
        glVertex2f(2 * a, 0 * abs(a))
        glVertex2f(-3 * a, 0 * abs(a))
        glVertex2f(-3 * a, 1 * abs(a))
        glVertex2f(2 * a, 1 * abs(a))

        # horizontal 3
        glVertex2f(1 * a, 1 * abs(a))
        glVertex2f(-2 * a, 1 * abs(a))
        glVertex2f(-2 * a, 3 * abs(a))
        glVertex2f(1 * a, 3 * abs(a))

        # Colores
        # Parte de Sombra
        glColor3f(0.45, 0.64, 0.21)

        # horizontal 0
        glVertex2f(-3 * a, -3 * abs(a))
        glVertex2f(-4 * a, -3 * abs(a))
        glVertex2f(-4 * a, -4 * abs(a))
        glVertex2f(-3 * a, -4 * abs(a))

        # horizontal 1
        glVertex2f(2 * a, -4 * abs(a))
        glVertex2f(-3 * a, -4 * abs(a))
        glVertex2f(-3 * a, -5 * abs(a))
        glVertex2f(2 * a, -5 * abs(a))

        # horizontal 2
        glVertex2f(3 * a, -3 * abs(a))
        glVertex2f(1 * a, -3 * abs(a))
        glVertex2f(1 * a, -4 * abs(a))
        glVertex2f(3 * a, -4 * abs(a))

        # horizontal 3
        glVertex2f(3 * a, -2 * abs(a))
        glVertex2f(3 * a, -2 * abs(a))
        glVertex2f(2 * a, -3 * abs(a))
        glVertex2f(2 * a, -3 * abs(a))

        # Parte iluminada
        glColor3f(0.7, 0.93, 0.29)

        # horizontal 0
        glVertex2f(1 * a, 0 * abs(a))
        glVertex2f(-2 * a, 0 * abs(a))
        glVertex2f(-2 * a, -1 * abs(a))
        glVertex2f(1 * a, -1 * abs(a))

        # horizontal 1
        glVertex2f(2 * a, 1 * abs(a))
        glVertex2f(0 * a, 1 * abs(a))
        glVertex2f(0 * a, 0 * abs(a))
        glVertex2f(2 * a, 0 * abs(a))

        # horizontal 2
        glVertex2f(0 * a, 2 * abs(a))
        glVertex2f(1 * a, 2 * abs(a))
        glVertex2f(1 * a, 1 * abs(a))
        glVertex2f(0 * a, 1 * abs(a))

        # horizontal 3
        glVertex2f(-1 * a, 3 * abs(a))
        glVertex2f(1 * a, 3 * abs(a))
        glVertex2f(1 * a, 2 * abs(a))
        glVertex2f(-1 * a, 2 * abs(a))

        # Parte cafe
        glColor3f(0.5, 0.29, 0.05)

        # horizontal 0
        glVertex2f(-1 * a, -4 * abs(a))
        glVertex2f(0 * a, -4 * abs(a))
        glVertex2f(0 * a, -5 * abs(a))
        glVertex2f(-1 * a, -5 * abs(a))

        # vertical 1
        glVertex2f(-1 * a, 5 * abs(a))
        glVertex2f(0 * a, 5 * abs(a))
        glVertex2f(0 * a, 3 * abs(a))
        glVertex2f(-1 * a, 3 * abs(a))

        # horizontal 2
        glVertex2f(0 * a, 6 * abs(a))
        glVertex2f(1 * a, 6 * abs(a))
        glVertex2f(1 * a, 5 * abs(a))
        glVertex2f(0 * a, 5 * abs(a))

        # -------- Ojos ----------
        a = a * (7 / 10)
        glColor3f(1.0, 1.0, 1.0)

        # Ojo izquierdo
        glVertex2f(-3 * a, -1 * abs(a))
        glVertex2f(-1 * a, -1 * abs(a))
        glVertex2f(-1 * a, 2 * abs(a))
        glVertex2f(-3 * a, 2 * abs(a))

        # Ojo derecho
        glVertex2f(1 * a, -1 * abs(a))
        glVertex2f(3 * a, -1 * abs(a))
        glVertex2f(3 * a, 2 * abs(a))
        glVertex2f(1 * a, 2 * abs(a))

        # -------- Pupilas ----------
        glColor3f(0, 0, 0)

        # Pupila izquierda
        glVertex2f(-2 * a, -1 * abs(a))
        glVertex2f(-1 * a, -1 * abs(a))
        glVertex2f(-1 * a, 1 * abs(a))
        glVertex2f(-2 * a, 1 * abs(a))

        # Pupila derecha
        glVertex2f(2 * a, -1 * abs(a))
        glVertex2f(3 * a, -1 * abs(a))
        glVertex2f(3 * a, 1 * abs(a))
        glVertex2f(2 * a, 1 * abs(a))

        glEnd()

    def mover(self, dt, moverDer, moverIzq, flotando):

        if moverDer == True:
            # modificamos la velocidad con la aceleracion
            self.vel = sumar(self.vel, ponderar(dt, gHor))
            if flotando == True:
                self.vel = sumar(self.vel, ponderar(dt, gVer))

        if moverIzq == True:
            self.vel = sumar(self.vel, ponderar(-1 * dt, gHor))
            if flotando == True:
                self.vel = sumar(self.vel, ponderar(dt, gVer))

        if ((moverIzq == False and moverDer == False) or (moverIzq == True and moverDer == True)) and flotando:
            self.vel = sumar(self.vel, ponderar(dt, gVer))

        if self.vel.y < MIN_VEL:
            self.vel.y = MIN_VEL

        # modificamos la posicion con la velocidad
        self.pos = sumar(self.pos, ponderar(dt, self.vel))
        print(self.vel)

        if estaChocandoMuroDer(self):
            self.pos = Vector(700 + self.a, self.pos.y)
            self.vel = Vector(0, self.vel.y)

        if estaChocandoMuroIzq(self):
            self.pos = Vector(100, self.pos.y)
            self.vel = Vector(0, self.vel.y)


def estaChocandoPlataformaNube(pera, plat):
    if plat == None:
        return False
    else:
        altura_plat = plat.pos.y + 3 * plat.a
        borde_izq_plat = plat.pos.x
        borde_der_plat = plat.pos.x + 22 * plat.a

        tope_izq = pera.pos.x - 4 * pera.a
        tope_der = pera.pos.x + 2 * pera.a
        tope_inf = pera.pos.y - 5 * pera.a
        distancia = altura_plat - tope_inf

        return abs(distancia) <= abs(1 * pera.a) and borde_izq_plat <= tope_der and tope_izq <= borde_der_plat


def estaChocandoPlataformaLiana(pera, plat):
    if plat == None:
        return False
    else:
        altura_plat = plat.pos.y - 3 * abs(plat.a)
        signo_escala = plat.a / abs(plat.a)
        if signo_escala > 0:
            borde_izq_plat = plat.pos.x + 12 * plat.a
            borde_der_plat = plat.pos.x + 34 * plat.a
        else:
            borde_der_plat = plat.pos.x + 12 * plat.a
            borde_izq_plat = plat.pos.x + 34 * plat.a

        tope_izq = pera.pos.x - 4 * pera.a
        tope_der = pera.pos.x + 2 * pera.a
        tope_inf = pera.pos.y - 5 * pera.a
        distancia = abs(altura_plat - tope_inf)
        return distancia <= abs(1 * pera.a) and borde_izq_plat <= tope_der and tope_izq <= borde_der_plat


def estaChocandoPlataformaPajaro(pera, plat):
    if plat == None:
        return False
    else:
        altura_plat = plat.pos.y - 3 * plat.a
        borde_izq_plat = plat.pos.x - 21 * plat.a
        borde_der_plat = plat.pos.x - 13 * plat.a

        tope_izq = pera.pos.x - 4 * pera.a
        tope_der = pera.pos.x + 2 * pera.a
        tope_inf = pera.pos.y - 5 * pera.a
        distancia = abs(altura_plat - tope_inf)
        return distancia <= abs(1 * pera.a) and borde_izq_plat <= tope_der and tope_izq <= borde_der_plat


def estaChocandoMuroDer(pera):
    return 700 + pera.a - pera.pos.x < 0


def estaChocandoMuroIzq(pera):
    return pera.pos.x - 100 < 0
