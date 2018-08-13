from Pasto import *
from bronzor import *
from initializers import *
from Eje import *
from random import uniform
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


class Arbol:
    def __init__(self, pos=Vector(0, 0, 0)):
        self.pos = pos
        self.angulo = 0

        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        glEnable(GL_COLOR_MATERIAL)

        glBegin(GL_TRIANGLES)

        # Tronco
        color = [90, 50, 35]  # cafe
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(20, 100, Vector(0, 0, 0))  # tronco

        # copa
        color = [33, 86, 41]  # verde
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])  # negro
        cono(50, 80, Vector(0, 0, 100))

        glEnd()

        glEndList()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.angulo, 0, 0, 1)  # Rotacion en torno a eje Z
        glCallList(self.lista)
        glPopMatrix()


def main():
    # inicializar
    ancho = 800
    alto = 600
    init(ancho, alto, "ejemplo aux")

    # crear objetos
    clock = pygame.time.Clock()

    # camara
    camPos = Vector(0, 0, 4000)  # posicion de la camara
    camAt = Vector(14140, -200, -328000)  # posicion que se enfoca

    # luz
    light = GL_LIGHT0
    l_position = Vector(1000.0, 100.0, 500.0)

    # crear una luz coherente con su color base
    l_diffuse = [1.0, 1.0, 1.0, 1.0]
    l_ambient = [0.2, 0.2, 0.2, 1]
    l_specular = [1.0, 1.0, 1.0, 1.0]

    # otros valores estandar
    l_constant_attenuation = 1.5
    l_linear_attenuation = 0.5
    l_quadratic_attenuation = 0.2

    l_spot_cutoff = 60.0
    l_spot_direction = Vector(-1.0, -1.0, 0.0)  # direccion de rebote de luz
    l_spot_exponent = 2.0

    eje = Eje(400.0)  # R,G,B = X,Y,Z
    pasto = Pasto(Vector(0, 0, 0))
    arboles = []
    for i in range(0, 50):
        x = uniform(-2000, 2000)
        y = uniform(-2000, 2000)
        p = Arbol(Vector(x, y, 0))
        arboles.append(p)
    b = Bronzor()
    # variables de tiempo
    fps = 30
    dt = 1.0 / fps
    run = True
    while run:
        # manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # obtener teclas presionadas
        pressed = pygame.key.get_pressed()

        if pressed[K_UP]:
            camPos = sumar(ponderar(100, normalizar(camAt)), camPos)
        if pressed[K_DOWN]:
            camPos = sumar(ponderar(-100, normalizar(camAt)), camPos)
        if pressed[K_RIGHT]:
            camPos = sumar(ponderar(-100, rotarFi(normalizar(camAt), 90)), camPos)
        if pressed[K_LEFT]:
            camPos = sumar(ponderar(100, rotarFi(normalizar(camAt), 90)), camPos)

        if pressed[K_w]:
            camAt = sumar(Vector(0, 0, 1000), camAt)
        if pressed[K_s]:
            camAt = sumar(Vector(0, 0, -1000), camAt)
        if pressed[K_d]:
            camAt = rotarFi(camAt, 0.1)
        if pressed[K_a]:
            camAt = rotarFi(camAt, -0.1)

        if pressed[K_r]:
            l_position = Vector(uniform(0, 1000), uniform(0, 1000), uniform(0, 1000))

        if pressed[K_1]:
            l_position = Vector(1000.0, 100.0, 500.0)
            camPos = Vector(0, 0, 4000)
            camAt = Vector(14140, -200, -328000)

        if pressed[K_2]:
            camPos = Vector(-1926.7001808016196, -1926.7001808016196, 104.30468009208232)
            camAt = Vector(10000, 10000, -2000)

        if pressed[K_3]:
            l_position = Vector(1000.0, 100.0, -500.0)
            camPos = Vector(0, 0, -4000)
            camAt = Vector(14140, -200, 328000)

        if pressed[K_ESCAPE]:
            run = False

        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # dibujar objetos
        eje.dibujar()
        # for a in arboles:
        #     a.dibujar()
        b.dibujar()
        # camara
        glLoadIdentity()
        gluLookAt(camPos.x, camPos.y, camPos.z,  # posicion
                  camAt.x, camAt.y, camAt.z,  # mirando hacia
                  0.0, 0.0, 1.0)  # inclinacion

        # luz
        glLightfv(light, GL_POSITION, l_position.cartesianas())
        glLightfv(light, GL_AMBIENT, l_ambient)
        glLightfv(light, GL_SPECULAR, l_specular)
        glLightfv(light, GL_DIFFUSE, l_diffuse)
        glLightf(light, GL_CONSTANT_ATTENUATION, l_constant_attenuation)
        glLightf(light, GL_LINEAR_ATTENUATION, l_linear_attenuation)
        glLightf(light, GL_QUADRATIC_ATTENUATION, l_quadratic_attenuation)
        glLightf(light, GL_SPOT_CUTOFF, l_spot_cutoff)
        glLightfv(light, GL_SPOT_DIRECTION, l_spot_direction.cartesianas())
        glLightf(light, GL_SPOT_EXPONENT, l_spot_exponent)

        glEnable(light)

        pygame.display.flip()  # cambiar imagen
        clock.tick(fps)  # esperar 1/fps segundos

    pygame.quit()
    return


main()
