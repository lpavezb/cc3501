from OpenGL.GL import *
from CC3501Utils import *
from pera import *


class Vista:
    def dibujar(self, pera, moverDer, moverIzq, pos_antigua, reloj, figuras, lianas, nubes, pajaros, fondo, decoracion,
                dt):
        ##############################################
        # MOVIMIENTO DE CAMARA SOBRE PERSONAJE
        ##############################################
        # IMPORTANTE: Tengo un bug con el dt, por alguna razon al usar el dt entre iteraciones
        # el programa corre ULTRA lento, asi que preferi elegir un valor de tiempo
        # conveniente para que tenga sentido jugar el juego. (0.4)
        pera.mover(0.4, moverDer, moverIzq, pera.flotando)

        posicion_actual_pera = pera.pos
        desplazamiento_pera = posicion_actual_pera - pos_antigua

        # Genera un marco donde la pera no mueve la camara
        if posicion_actual_pera.y <= 100 or posicion_actual_pera.y >= 500:
            pera.pos.y = pos_antigua.y
        else:
            desplazamiento_pera = Vector(0, 0)

        for i in range(0, len(figuras)):
            figuras[i].pos.y = figuras[i].pos.y - desplazamiento_pera.y

        ##############################################
        # INTERACCION PLATAFORMAS
        ##############################################
        nube = None
        liana = None
        pajaro = None
        for i in range(0, len(nubes)):
            if estaChocandoPlataformaNube(pera, nubes[i]) and pera.vel.y < 0:
                nube = nubes[i]

        for i in range(0, len(lianas)):
            if estaChocandoPlataformaLiana(pera, lianas[i]) and pera.vel.y < 0:
                liana = lianas[i]

        for i in range(0, len(pajaros)):
            if estaChocandoPlataformaPajaro(pera, pajaros[i]) and pera.vel.y < 0:
                pajaro = pajaros[i]

        if estaChocandoPlataformaNube(pera, nube) and pera.vel.y <= 0:
            altura_plat = nube.pos.y + 3 * nube.a
            pera.pos = Vector(pera.pos.x, altura_plat + 4.5 * pera.a)
            pera.vel = Vector(pera.vel.x, 0)
            pera.flotando = False
            pera.saltos = 10

        elif estaChocandoPlataformaLiana(pera, liana) and pera.vel.y <= 0:
            altura_plat = liana.pos.y - 3 * abs(liana.a)
            pera.pos = Vector(pera.pos.x, altura_plat + 5 * pera.a)
            pera.vel = Vector(pera.vel.x, 0)
            pera.flotando = False
            pera.saltos = 10

        elif estaChocandoPlataformaPajaro(pera, pajaro) and pera.vel.y <= 0:
            altura_plat = pajaro.pos.y - 3 * pajaro.a
            pera.pos = Vector(pera.pos.x, altura_plat + 5 * pera.a)
            pera.vel = Vector(pera.vel.x, 0)
            pera.flotando = False
            pera.saltos = 10
        else:
            pera.flotando = True

        ########################################
        # SE INICIA DIBUJO
        ########################################
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        fondo.dibujar()
        for fig in figuras:
            fig.dibujar()
        for dec in decoracion:
            dec.dibujar()
        pera.dibujar()
        for rel in reloj:
            rel.dibujar()
