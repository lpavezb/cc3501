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
from crearObjetos import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


def main():
    global gVer, gHor
    gVer = Vector(0, -10.0)
    gHor = Vector(3.0, 0)
    ancho = 800
    alto = 600
    init(ancho, alto, "Not Icy Pera Tower")
    vista = Vista()

    # Esta funcion crea todos los objetos que usare
    resultado = crearObjetos()
    figuras = resultado[0]
    decoracion = resultado[1]
    nubes = resultado[2]
    lianas = resultado[3]
    pajaros = resultado[4]
    reloj = resultado[5]
    fondo = resultado[6]
    #########################################
    # PERSONAJE
    #########################################
    pera = Pera(7, Vector(0, 0), Vector(200, 150))

    ########################################
    # PROGRAMA PRINCIPAL
    ########################################

    pera.flotando = True
    run = True
    # se empieza a medir el tiempo
    t0 = pygame.time.get_ticks()
    dt = 0
    tiempo_caida = 0
    while run:
        if pera.flotando == True:
            tiempo_caida = tiempo_caida + dt
        else:
            tiempo_caida = 0
        posicion_antigua_pera = pera.pos

        ########################################
        # CONTROLADOR DE EVENTOS
        ########################################

        keys = pygame.key.get_pressed()

        moverDer = False
        if keys[pygame.K_RIGHT]:
            moverDer = True

        moverIzq = False
        if keys[pygame.K_LEFT]:
            moverIzq = True

        for event in pygame.event.get():

            if event.type == QUIT:  # cerrar ventana
                run = False
            if event.type == KEYDOWN:

                if event.key == K_SPACE and pera.saltos > 0:
                    pera.vel = Vector(pera.vel.x, 50 + abs(pera.vel.x) / 3)
                    pera.saltos = pera.saltos - 1

                    pera.flotando = True

                if event.key == K_s:
                    run = False

        # que cada objeto actue durante el intervalo de tiempo tardado
        t1 = pygame.time.get_ticks()  # mide el tiempo final
        dt = (t1 - t0) / 1000

        # El juego acaba cuando cai por mucho tiempo
        if tiempo_caida > 5:
            run = False

        if pera.pos.y <= 0:
            run = False

        vista.dibujar(pera, moverDer, moverIzq, posicion_antigua_pera, reloj, figuras, lianas, nubes, pajaros, fondo,
                      decoracion, dt)
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

        # el tiempo inicial de la siguiente iteracion es el tiempo final de esta iteracion
        t0 = t1

    pygame.quit()


main()
