from vista import *
from models.bomberman import *
from models.fondo import *
from models.wall import *
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


def main():
    global gVer, gHor
    gVer = Vector(0, -10.0)
    gHor = Vector(3.0, 0)
    ancho = 800
    alto = 600
    init(ancho, alto, "Bomberman")
    vista = Vista()

    ########################################
    # PROGRAMA PRINCIPAL
    ########################################
    bomberman = Bomberman(pos=Vector(40, 30))
    fondo = Fondo()

    # create walls
    w = Wall().w
    walls = []
    # walls.append(Wall(pos=Vector(100, 100)))
    for i in range(0, int(800 / w)):
        walls.append(Wall(pos=Vector(i * w, 0)))
        walls.append(Wall(pos=Vector(i * w, 600 - w)))
    for i in range(0, int(600 / w)):
        walls.append(Wall(pos=Vector(0, i * w)))
        walls.append(Wall(pos=Vector(800 - w, i * w)))
    wi_x = 3 * w
    wi_y = 3 * w
    while wi_y < 600:
        while wi_x < 800:
            walls.append(Wall(pos=Vector(wi_x, wi_y)))
            walls.append(Wall(pos=Vector(wi_x + w, wi_y)))
            walls.append(Wall(pos=Vector(wi_x, wi_y + w)))
            walls.append(Wall(pos=Vector(wi_x + w, wi_y + w)))
            wi_x = wi_x + 4 * w
        wi_x = 3 * w
        wi_y = wi_y + 4 * w

    # se empieza a medir el tiempo
    t0 = pygame.time.get_ticks()
    dt = 0
    run = True
    while run:
        ########################################
        # CONTROLADOR DE EVENTOsdgsdgfS
        ########################################
        keys = pygame.key.get_pressed()

        move_up = False
        move_down = False
        move_right = False
        move_left = False

        # move keys
        if keys[pygame.K_UP]:
            move_up = True

        if keys[pygame.K_DOWN]:
            move_down = True

        if keys[pygame.K_RIGHT]:
            move_right = True

        if keys[pygame.K_LEFT]:
            move_left = True

        if keys[pygame.K_q]:
            run = False

        # two keys pressed
        if move_up and move_left:
            move_up = False

        if move_up and move_right:
            move_up = False

        if move_down and move_left:
            move_down = False

        if move_down and move_right:
            move_down = False

        # place bomb
        if keys[pygame.K_a]:
            bomberman.place_bomb()

        for event in pygame.event.get():

            if event.type == QUIT:  # cerrar ventana
                run = False
            if event.type == KEYDOWN:

                if event.key == K_s:
                    run = False

        # que cada objeto actue durante el intervalo de tiempo tardado
        t1 = pygame.time.get_ticks()  # mide el tiempo final
        dt = (t1 - t0) / 1000

        # El juego acaba cuando cai por mucho tiempo
        vista.dibujar(bomberman, move_right, move_left, move_up, move_down, fondo, walls)
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

        # el tiempo inicial de la siguiente iteracion es el tiempo final de esta iteracion
        t0 = t1

    pygame.quit()


main()
