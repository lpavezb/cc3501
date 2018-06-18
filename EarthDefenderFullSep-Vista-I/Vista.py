# -*- coding: iso-8859-1 -*-


from OpenGL.GL import *
from utils import *

class Vista:
    def dibujar(self,nave,ms,bs,tierra,dt,a,w,h,Rmin,Rmax):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # dibuja la tierra
        tierra.dibujar()

        # itera los meteoritos
        for m in ms:
            # mueve el meteorito
            m.mover(dt/60.0,a)

            # chequea si estan afuera de la pantalla, los elimina de ser asi.
            fuera(m,w,h)

            # dibuja el meteorito
            m.dibujar()

            # chequea impactos con la tierra y actua en concecuencia.
            impacto(tierra,m,Rmin,Rmax,w)

        # itera las balas
        for b in bs:
            b.mover(dt/60.0,a)
            fuera(b,w,h)
            b.dibujar()

            # chequea colisiones con los meteoritos
            for m in ms:
                # de haber colision, destruye ambos.
                if estanChocando(m,b):
                    m.vive = False
                    b.vive = False


        #elimina las balas y meteoritos.
        limpiar(bs)
        limpiar(ms)

        # dibuja la nave
        nave.dibujar()

        glLoadIdentity()

