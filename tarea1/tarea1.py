#!/usr/bin/env python
# coding=utf-8
"""
Esto hace tarea
@version 1.1
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color

import time
import tqdm
import numpy as np
import math


class Tarea:
    def __init__(self, ancho=2000, largo=4000, dh=0.08, factor=0.005):
        self._ancho = ancho
        self._largo = largo

        self._factor = factor
        self._dh = dh
        self._adh = self._factor / self._dh

        self._h = int(self._ancho * self._adh)
        self._w = int(self._largo * self._adh)

        self._t = 0  # hora
        self._temp = np.zeros((self._h, self._w))
        self._cb = np.zeros((self._h, self._w))
        self._geo = np.zeros((self._h, self._w))

        # RUT = 19401577-1
        self._RRR = 577.0 / 1000
        self._rho = False

    def set_geo(self):
        # Puntos de interes
        mar = [1200 + 400.0 * self._RRR, 0.0]
        planta = [mar[0] + 120, 0.0]
        inicio_cordillera = [mar[0] + 400, 400 / 3.0]
        cima1 = [mar[0] + 1200, 1500 + 200 * self._RRR]
        valle = [mar[0] + 1500, 1300 + 200 * self._RRR]
        cima2 = [mar[0] + 2000, 1850 + 100 * self._RRR]
        fin = [4000.0, 1850 + 100 * self._RRR]

        nieve = int(1800.0 * self._adh)

        # Transformar puntos de interes a puntos en la grilla
        p1 = (int(mar[0] * self._adh), int(mar[1] * self._adh))
        p2 = (int(planta[0] * self._adh), int(planta[1] * self._adh))
        p3 = (int(inicio_cordillera[0] * self._adh), int(inicio_cordillera[1] * self._adh))
        p4 = (int(cima1[0] * self._adh), int(cima1[1] * self._adh))
        p5 = (int(valle[0] * self._adh), int(valle[1] * self._adh))
        p6 = (int(cima2[0] * self._adh), int(cima2[1] * self._adh))
        p7 = (int(fin[0] * self._adh), int(fin[1] * self._adh))

        # puntos
        # cielo = 0
        # mar = 1
        # fabrica = 2
        # montana = 3
        # nieve = 4

        # Setear geografia

        for x in range(self._w):
            # primera seccion: mar
            if x < p1[0]:
                self._geo[0, x] = 1
                self._cb[0, x] = 1

            # segunda seccion: fabrica
            elif x < p2[0]:
                self._geo[0, x] = 2
                self._cb[0, x] = 2

            # tercera seccion: inicio montana 1
            elif x < p3[0]:
                y = f(p2, p3, x)
                self._geo[0:y, x] = 3
                self._cb[0:y, x] = np.nan
                self._temp[0:y, x] = np.nan
                self._cb[y, x] = 3

            # cuarta seccion: montana 1
            elif x < p4[0]:
                y = f(p3, p4, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 4
                    self._temp[0:y, x] = np.nan
                else:
                    self._geo[0:y, x] = 3
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 3
                    self._temp[0:y, x] = np.nan

            # quinta seccion: valle
            elif x < p5[0]:
                y = f(p4, p5, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 4
                    self._temp[0:y, x] = np.nan
                else:
                    self._geo[0:y, x] = 3
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 3
                    self._temp[0:y, x] = np.nan

            # sexta seccion: montana 2
            elif x < p6[0]:
                y = f(p5, p6, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 4
                    self._temp[0:y, x] = np.nan
                else:
                    self._geo[0:y, x] = 3
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 3
                    self._temp[0:y, x] = np.nan

            else:
                y = f(p6, p7, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 4
                    self._temp[0:y, x] = np.nan
                else:
                    self._geo[0:y, x] = 3
                    self._cb[0:y, x] = np.nan
                    self._cb[y, x] = 3
                    self._temp[0:y, x] = np.nan

    def cb(self, t):
        self._t = t

        # puntos
        cielo = 0
        mar = 1
        fabrica = 2
        montana = 3
        nieve = 4

        # temperaturas
        if t < 8:
            t_mar = 4
        elif t < 16:
            t_mar = f([8, 4], [16, 20], t)
        else:
            t_mar = f([16, 20], [24, 4], t)

        arg = (math.pi / 12.0) * t
        t_fab = 450 * (math.cos(arg) + 2)

        for i in range(self._h):  # filas
            for j in range(self._w):  # columnas
                # cb mar
                if self._cb[i, j] == mar:
                    self._temp[i, j] = t_mar
                elif self._cb[i, j] == cielo:
                    t_atm = f([0, t_mar], [1000 * self._adh, t_mar - 6], i)
                    self._temp[i, j] = t_atm
                elif self._cb[i, j] == montana:
                    self._temp[i, j] = 20
                elif self._cb[i, j] == nieve:
                    self._temp[i, j] = 0
                elif self._cb[i, j] == fabrica:
                    self._temp[i, j] = t_fab

    def mean(self):
        aux = []
        m = self._temp
        for i in range(self._h):
            for j in range(self._w):
                value = m[i][j]
                if not np.isnan(value):
                    aux.append(value)
        return np.mean(aux)

    def plot_geo(self):
        fig = plt.figure()

        cmap = color.ListedColormap(['c', 'b', 'k', 'brown', 'w'])
        bounds = [0, 1, 2, 3, 4, 5]
        norm = color.BoundaryNorm(bounds, cmap.N)
        cax = plt.imshow(self._geo, origin="lower", cmap=cmap, norm=norm)
        cb = fig.colorbar(cax, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0.5, 1.5, 2.5, 3.5, 4.5])
        cb.ax.set_yticklabels(['atmosfera', 'mar', 'fabrica', 'montana', 'nieve'])
        plt.title("Geografia")
        plt.xlabel("Ancho [m]")
        plt.ylabel("Altura [m]")
        plt.show()

    def plot_temp(self):
        fig = plt.figure()
        cax = plt.imshow(self._temp, origin="lower")
        fig.colorbar(cax)
        if self._rho:
            plt.title("Temperatura a las " + str(self._t) + ":00 hrs (rho != 0)")
        else:
            plt.title("Temperatura a las " + str(self._t) + ":00 hrs (rho = 0)")
        plt.xlabel("Ancho [m]")
        plt.ylabel("Altura [m]")
        plt.show()

    def get_cb_matrix(self):
        return self._cb

    def get_temp_matrix(self):
        return self._temp

    def get_geo_matrix(self):
        return self._geo

    def iterate_with_it_number_and_w(self, b=False, iterations=1000, w_r=1.96):
        self._rho = b
        e = 0
        w = self._w
        h = self._h
        now = time.time()
        for _ in tqdm.tqdm(range(iterations)):
            for j in range(w):
                for i in range(h):
                    (self._temp[i][j], e) = sobreRS(self._temp, i, j, w_r, e, w - 1, h - 1,
                                                    self._dh, rho, b)
        later = time.time()
        return int(later - now)

    def iterate(self, b=False):
        self._rho = b  # valor para el titulo del grafico
        epsilon = 0.001
        e = 0  # error
        w = self._w
        h = self._h
        w_r = get_w(w, h)
        for _ in tqdm.tqdm(range(2000)):
            max_e = 0
            for j in range(w):
                for i in range(h):
                    (self._temp[i][j], e) = sobreRS(self._temp, i, j, w_r, e, w - 1, h - 1,
                                                    self._dh, rho, b)
                    if max_e < e: max_e = e
            print max_e
            if max_e < epsilon:
                break

    def doTarea(self, hora=0, rho=False):
        self.set_geo()
        self.cb(hora)
        self.iterate(b=rho)
        self.plot_temp()

    def doTarea2(self, w_r=1.96):
        self.set_geo()
        self.cb(0)
        return self.iterate_with_it_number_and_w(iterations=1000, w_r=w_r)


# Funcion copiada de https://github.com/ppizarror/01-tarea-computagrafica/blob/master/lib.py
# Funcion que retorna true si hay un NAN en torno a a[i][j]
def nearNAN(a, i, j):
    if np.isnan(a[i - 1][j]):
        return True
    if np.isnan(a[i + 1][j]):
        return True
    if np.isnan(a[i][j - 1]):
        return True
    if np.isnan(a[i][j + 1]):
        return True
    return False


# Funcion basada en https://github.com/ppizarror/01-tarea-computagrafica/blob/master/lib.py
# se agregaron algunas condiciones que no estaban en la funcion "copiada"
def sobreRS(matriz, i, j, w, e, width, height, h, rho, b=False):
    if b:
        ro = rho(i, j)
    else:
        ro = 0
    if np.isnan(matriz[i][j]):
        return matriz[i][j], e
    if 0 < i < height and 0 < j < width:
        if nearNAN(matriz, i, j):
            if np.isnan(matriz[i][j + 1]):  # derecha
                if np.isnan(matriz[i + 1][j]):  # derecha y abajo
                    n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i - 1][j] + 2 * matriz[i][j - 1] -
                                                    4 * matriz[i][j] - (h ** 2) * ro) * w
                else:
                    if np.isnan(matriz[i - 1][j]):  # derecha y arriba
                        if np.isnan(matriz[i][j - 1]):  # derecha, arriba y izquierda
                            n = matriz[i][j] + (1.0 / 4) * (4 * matriz[i + 1][j] - 4 * matriz[i][j] -
                                                            (h ** 2) * ro) * w

                        else:
                            n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i + 1][j] + 2 * matriz[i][j - 1] -
                                                            4 * matriz[i][j] - (h ** 2) * ro) * w

                    else:
                        n = matriz[i][j] + (1.0 / 4) * (matriz[i + 1][j] + matriz[i - 1][j] +
                                                        2 * matriz[i][j - 1] - 4 * matriz[i][j] - (h ** 2) * ro) * w

            elif np.isnan(matriz[i + 1][j]):  # abajo
                if np.isnan(matriz[i][j - 1]):  # izquierda
                    n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i - 1][j] + 2 * matriz[i][j + 1] -
                                                    4 * matriz[i][j] - (h ** 2) * ro) * w

                else:
                    n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i - 1][j] + matriz[i][j + 1] + matriz[i][j - 1] -
                                                    4 * matriz[i][j] - (h ** 2) * ro) * w

            elif np.isnan(matriz[i][j - 1]):  # izquierda
                if np.isnan(matriz[i - 1][j]):
                    n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i + 1][j] + 2 * matriz[i][j + 1] -
                                                    4 * matriz[i][j] - (h ** 2) * ro) * w

                else:
                    n = matriz[i][j] + (1.0 / 4) * (matriz[i + 1][j] + matriz[i - 1][j] + 2 * matriz[i][j + 1] -
                                                    4 * matriz[i][j] - (h ** 2) * ro) * w

            else:  # arriba
                n = matriz[i][j] + (1.0 / 4) * (matriz[i + 1][j] + matriz[i][j - 1] + 2 *
                                                matriz[i][j + 1] - 4 * matriz[i][j] - (h ** 2) * ro) * w

        else:
            n = matriz[i][j] + (1.0 / 4) * (matriz[i + 1][j] + matriz[i - 1][j] + matriz[i][j + 1] + matriz[i][j - 1] -
                                            4 * matriz[i][j] - (h ** 2) * ro) * w
    else:
        # Esquinas
        if i == 0 and j == 0:  # esquina superior izquierda
            n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i + 1][j] + 2 * matriz[i][j + 1] - 4 * matriz[i][j]
                                            - (h ** 2) * ro) * w

        elif i == 0 and j == width:  # esquina superior derecha
            n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i + 1][j] + 2 * matriz[i][j - 1] - 4 * matriz[i][j]
                                            - (h ** 2) * ro) * w

        elif i == height and j == 0:  # esquina inferior izquierda
            n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i - 1][j] + 2 * matriz[i][j + 1] - 4 * matriz[i][j]
                                            - (h ** 2) * ro) * w

        elif i == height and j == width:  # esquina inferior derecha
            n = matriz[i][j] + (1.0 / 4) * (2 * matriz[i - 1][j] + 2 * matriz[i][j - 1] - 4 * matriz[i][j]
                                            - (h ** 2) * ro) * w
        # Bordes
        else:
            return matriz[i][j], e  # Como son dirichlet no se hace nada

    if n == matriz[i][j]:
        return matriz[i][j], e
    else:
        e = abs(matriz[i][j] - n)
    return n, e


def rho(x, y):
    return 1 / (x ** 2 + y ** 2 + 120) ** 0.5


def f(p1, p2, x):
    n = p1[1]
    m = (float(p2[1] - p1[1]) / (p2[0] - p1[0]))
    y = ((m * (x - p1[0])) + n)
    return int(y)


def get_w(m, n):
    pi = math.pi
    a = math.cos(pi / (n - 1))
    b = math.cos(pi / (m - 1))
    c = (a + b) ** 2
    w = 4.0 / (2 + math.sqrt(4 - c))
    return w


def plot_mid_t(x, y):
    plt.plot(x, y, '-ro')
    plt.title("Temperatura media segun la hora")
    plt.xlabel("Hora [hrs]")
    plt.ylabel("Temperatura media [C]")
    plt.show()


def main():
    t = Tarea(dh=0.08, factor=0.005)
    t.doTarea(hora=0, rho=False)


if __name__ == '__main__':
    main()
