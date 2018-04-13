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
                self._matrix[y, x] = 3

            # cuarta seccion: montana 1
            elif x < p4[0]:
                y = f(p3, p4, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[nieve, x] = 3
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[y, x] = 3
            # quinta seccion: valle

            elif x < p5[0]:
                y = f(p4, p5, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[nieve, x] = 3
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[y, x] = 3
            # sexta seccion: montana 2

            elif x < p6[0]:
                y = f(p5, p6, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[nieve, x] = 3
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[y, x] = 3

            else:
                y = f(p6, p7, x)
                if y > nieve:
                    self._geo[0:nieve, x] = 3
                    self._geo[nieve:y, x] = 4
                    self._matrix[nieve, x] = 3
                    self._matrix[y, x] = 4
                else:
                    self._geo[0:y, x] = 3
                    self._matrix[y, x] = 3

        fig = plt.figure()
        ax = fig.add_subplot(111)
        # colorbar customization
        cmap = color.ListedColormap(['cyan', 'blue', 'red', 'brown', 'white'])
        bounds = [0, 1, 2, 3, 4, 5]
        norm = color.BoundaryNorm(bounds, cmap.N)
        cax = plt.imshow(self._geo, origin="lower", interpolation='none', cmap=cmap, norm=norm)
        cb = fig.colorbar(cax, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0.5, 1.5, 2.5, 3.5, 4.5])
        cb.ax.set_yticklabels(['cielo', 'agua', 'fabrica', 'tierra', 'nieve'])

        plt.show()

    def cb(self, t):
        # puntos
        cielo = 0
        mar = 1
        fabrica = 2
        montana = 3
        nieve = 4

        # temperaturas
        t_mar = 0
        if t < 8:
            t_mar = 4
        elif t < 16:
            t_mar = f([8, 4], [16, 20], t)
        else:
            t_mar = f([16, 20], [24, 4], t)

        for i in range(self._h):  # filas
            for j in range(self._w):  # columnas
                if self._matrix[i, j] == mar:
                    self._temp = t_mar

    def plot(self):
        """
        Grafica
        :return: None
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Se agrega grafico al plot
        cax = ax.imshow(self._matrix, interpolation='none')
        fig.colorbar(cax)
        plt.show()

    def show_map(self):

        """
        Grafica el mapa del rio (pilares y contornos)
        :return: None
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # # Se agrega grafico al plot

        cax = plt.imshow(self._geo, cmap='Greys', interpolation='nearest')

        # grillas diferenciales
        for k in range(1, self._w):
            plt.axvline(x=k - 0.5, color=(0, 0, 0, 0.5), linestyle='--', lw=0.5)

        for m in range(1, self._h):
            plt.axhline(y=m - 0.5, color=(0, 0, 0, 0.5), linestyle='--', lw=0.5)

        # coordenadas en metros
        for i in range(1, int(self._largo) + 1):
            plt.axvline(x=i / self._dh - 0.5, color='k', linestyle='--', lw=1.0)

        for j in range(1, int(self._ancho) + 1):
            plt.axhline(y=j / self._dh - 0.5, color='k', linestyle='--', lw=1.0)

        # Bordes del rio
        plt.axvline(x=self._w - 0.5, color='r', linestyle='--', lw=1.0)
        plt.axvline(x=-0.5, color='r', linestyle='--', lw=1.0)

        plt.axhline(y=self._h - 0.5, color='r', linestyle='--', lw=1.0)
        plt.axhline(y=0 - 0.5, color='r', linestyle='--', lw=1.0)

        # fig.colorbar(cax)
        plt.show()


def f(p1, p2, x):
    n = p1[1]
    m = (float(p2[1] - p1[1]) / (p2[0] - p1[0]))
    y = ((m * (x - p1[0])) + n)
    return int(y)


def main():
    t = Tarea()
    t.set_geo()


def medir_presiones(rio, pos_x):
    """
    Recibe un rio y una coordenada en X
    :param rio:
    :param pos_x:
    :return: None
    """

    presion_rio_abajo = []
    pos = []
    rio.reset()

    for pos_y in range(0, rio._h):

        a = rio.addPilar(pos_x, pos_y)
        if not (a):
            continue

        rio.old_cb(1)
        rio.start()
        presion_rio_abajo.append(rio.get_presion())
        pos.append(pos_y * rio._dh)
        rio.reset()

    graph = plt.plot(pos, presion_rio_abajo, color='red', marker='o', linestyle='none', linewidth=2, markersize=12,
                     label="presion desembocadura rio ")
    vert_line = plt.axvline(x=rio._ancho / 2.0, label="centro del rio")
    plt.xlabel('Distancia de Borde Superior a Centro de Pilar[ m ]')
    plt.ylabel('Presion Promedio en Boca del Rio [ Pascal(?) ]')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, borderaxespad=0)
    print(presion_rio_abajo)
    plt.show()


if __name__ == '__main__':
    main()
