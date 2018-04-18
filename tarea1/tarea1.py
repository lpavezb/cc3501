#!/usr/bin/env python
# coding=utf-8
"""
Esto hace tarea
@version 1.1
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color

import tqdm
import numpy as np
import math


class Tarea:
    def __init__(self, ancho=2000, largo=4000, dh=1):
        """
        Constructor
        :param ancho: Ancho
        :param largo: Largo
        :param dh: Tamaño grilla diferencial
        :type ancho: int,float
        """
        self._ancho = ancho  # privada
        self._largo = largo
        self._dh = dh

        self._t = 0  # hora

        self._h = int(float(ancho) / dh)
        self._w = int(float(largo) / dh)

        self._temp = np.zeros((self._h, self._w))
        self._matrix = np.zeros((self._h, self._w))
        self._geo = np.zeros((self._h, self._w))

        # RUT = 19401577-1
        self._RRR = 577.0 / 1000

    def set_geo(self):
        # Puntos de interes
        mar = [1200 + 400.0 * self._RRR, 0.0]
        planta = [mar[0] + 120, 0.0]
        inicio_cordillera = [mar[0] + 400, 400 / 3.0]
        cima1 = [mar[0] + 1200, 1500 + 200 * self._RRR]
        valle = [mar[0] + 1500, 1300 + 200 * self._RRR]
        cima2 = [mar[0] + 2000, 1850 + 100 * self._RRR]
        fin = [4000.0, 1850 + 100 * self._RRR]

        nieve = int(1800.0 / self._dh)

        # Transformar puntos de interes a puntos en la grilla
        p1 = (int(mar[0] / self._dh), int(mar[1] / self._dh))
        p2 = (int(planta[0] / self._dh), int(planta[1] / self._dh))
        p3 = (int(inicio_cordillera[0] / self._dh), int(inicio_cordillera[1] / self._dh))
        p4 = (int(cima1[0] / self._dh), int(cima1[1] / self._dh))
        p5 = (int(valle[0] / self._dh), int(valle[1] / self._dh))
        p6 = (int(cima2[0] / self._dh), int(cima2[1] / self._dh))
        p7 = (int(fin[0] / self._dh), int(fin[1] / self._dh))

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
                self._matrix[0, x] = 1

            # segunda seccion: fabrica
            elif x < p2[0]:
                self._geo[0, x] = 2
                self._matrix[0, x] = 2

            # tercera seccion: inicio montana 1
            elif x < p3[0]:
                y = f(p2, p3, x)
                self._geo[0:y, x] = 3
                self._matrix[0:y, x] = np.nan
                self._temp[0:y, x] = np.nan
                self._matrix[y, x] = 3

            # cuarta seccion: montana 1
            elif x < p4[0]:
                y = f(p3, p4, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 3

            # quinta seccion: valle
            elif x < p5[0]:
                y = f(p4, p5, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 3

            # sexta seccion: montana 2
            elif x < p6[0]:
                y = f(p5, p6, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 3

            else:
                y = f(p6, p7, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[0:y, x] = np.nan
                    self._temp[0:y, x] = np.nan
                    self._matrix[y, x] = 3

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
                if self._matrix[i, j] == mar:
                    self._temp[i, j] = t_mar
                elif self._matrix[i, j] == cielo:
                    t_atm = f([0, t_mar], [1000, t_mar - 6], i)
                    self._temp[i, j] = t_atm
                elif self._matrix[i, j] == montana:
                    self._temp[i, j] = 20
                elif self._matrix[i, j] == nieve:
                    self._temp[i, j] = 0
                elif self._matrix[i, j] == fabrica:
                    self._temp[i, j] = t_fab

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
        plt.title("Temperatura a las " + str(self._t) + ":00 hrs")
        plt.xlabel("Ancho [m]")
        plt.ylabel("Altura [m]")
        plt.show()

    def get_cb_matrix(self):
            return self._matrix

    def get_temp_matrix(self):
        return self._temp

    def get_geo_matrix(self):
        return self._geo

    def iterate(self, b=False):
        epsilon = 0.001
        e = 0  # error
        e0 = 0  # error inicial
        ni = 0  # numero de iteraciones
        w = self._w
        h = self._h
        for _ in tqdm.tqdm(range(1000)):
            for j in range(w):
                for i in range(h):
                    (self._temp[i][j], e) = sobreRS(self._temp, i, j, get_w(w - 1, h - 1), e, w - 1, h - 1,
                                                    self._dh, rho, b)
            print(e)
            if e < epsilon:
                break
            if e0 == 0:
                e0 = e
            ni += 1  # numero de iteraciones


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
                n = matriz[i][j] + (1.0 / 4) * (matriz[i + 1][j] + matriz[i][j-1] + 2 *
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
    return 1 / (x**2 + y**2 + 120)**0.5


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


def main():
    t = Tarea(dh=10)
    t.set_geo()
    t.cb(0)
    t.iterate(b=True)
    t.plot_temp()
    print(np.shape(t.get_temp_matrix()))
    t.cb(8)
    t.iterate(b=True)
    t.plot_temp()
    t.cb(12)
    t.iterate(b=True)
    t.plot_temp()
    t.cb(16)
    t.iterate(b=True)
    t.plot_temp()
    t.cb(20)
    t.iterate(b=True)
    t.plot_temp()


if __name__ == '__main__':
    main()
