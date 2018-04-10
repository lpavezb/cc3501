#!/usr/bin/env python
# coding=utf-8
"""
Esto hace tarea
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import matplotlib.colors as color
import tqdm
import numpy as np


class Rio:
    def __init__(self, dh = 1):
        """
        Constructor
        :param dh: Tamaño grilla diferencial
        """
        self._ancho = 2000  # privada
        self._largo = 4000
        self._dh = dh

        #geografia
        # RUT = 19401577-1
        self._RRR = 577.0/1000

        self._mar = [1200 + 400.0 * self._RRR, 0.0]
        self._planta = [self._mar[0] + 120, 0.0]
        self._inicio_cordillera = [self._mar[0] + 400, 400/3.0]
        self._cima1 = [self._mar[0] + 1200, 1500 + 200 * self._RRR]
        self._valle = [self._mar[0] + 1500, 1300 + 200 * self._RRR]
        self._cima2 = [self._mar[0] + 2000, 1850 + 100 * self._RRR]
        self._fin = [4000.0, 1850 + 100 * self._RRR]

        self._h = int(float(self._ancho) / dh)
        self._w = int(float(self._largo) / dh)

        self._snow = int(1800/self._dh)

        self._matrix = np.zeros((self._h, self._w))
        self._geo = np.zeros((self._h, self._w))

        self._adh = int(float(1) / dh)

    def create_geo(self):
        # setear puntos con respecto a grilla
        p1 = (int(self._mar[0] / self._dh), int(self._mar[1] / self._dh))
        p2 = (int(self._planta[0] / self._dh), int(self._planta[1] / self._dh))
        p3 = (int(self._inicio_cordillera[0] / self._dh), int(self._inicio_cordillera[1] / self._dh))
        p4 = (int(self._cima1[0] / self._dh), int(self._cima1[1] / self._dh))
        p5 = (int(self._valle[0] / self._dh), int(self._valle[1] / self._dh))
        p6 = (int(self._cima2[0] / self._dh), int(self._cima2[1] / self._dh))
        p7 = (int(self._fin[0] / self._dh), int(self._fin[1] / self._dh))

        fab_h = int(20.0 / self._dh)
        #pintar
        for x in range(0,self._w):
            if x < p1[0]:
                self._geo[0, x] = 1  # Agua

            elif x < p2[0]:
                self._geo[0:fab_h, x] = 2  # fabrica, altura 20 m

            elif x < p3[0]:
                n = p2[1]
                m = float(p3[1] - p2[1]) / float(p3[0] - p2[0])
                y = int(n + m * (x - p2[0]))
                self._geo[0:y, x] = 3  # Tierra

            elif x < p4[0]:
                n = p3[1]
                m = float(p4[1] - p3[1]) / float(p4[0] - p3[0])
                y = int(n + m * (x - p3[0]))
                self._geo[0:y, x] = 3  # Tierra

            elif x < p5[0]:
                n = p4[1]
                m = float(p5[1] - p4[1]) / float(p5[0] - p4[0])
                y = int(n + m * (x - p4[0]))
                self._geo[0:y, x] = 3  # Tierr


            elif x < p6[0]:
                n = p5[1]
                m = float(p6[1] - p5[1]) / float(p6[0] - p5[0])
                y = int(n + m * (x - p5[0]))
                if y > self._snow:
                    self._geo[self._snow:y, x] = 4  # Nieve
                    self._geo[0:self._snow, x] = 3  # Tierra
                else:
                    self._geo[0:y, x] = 3  # Tierr

            else:
                n = p6[1]
                m = float(p7[1] - p6[1]) / float(p7[0] - p6[0])
                y = int(n + m * (x - p6[0]))
                if y > self._snow:
                    self._geo[self._snow:y, x] = 4  # Nieve
                    self._geo[0:self._snow, x] = 3  # Tierra
                else:
                    self._geo[0:y, x] = 3  # Tierr

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

        return

def main():
    # Instancia rio

    r = Rio().create_geo()


if __name__ == '__main__':
    main()