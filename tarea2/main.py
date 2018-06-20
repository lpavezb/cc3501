from models.breakable_wall import WallBreak
from models.power_up import *
from vista import *
from models.bomberman import *
from models.fondo import *
from models.wall import *
from random import *
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


def create_walls(w):
    walls = []
    for i in range(0, int(800 / w)):
        walls.append(Wall(pos=Vector(i * w, 0)))
        walls.append(Wall(pos=Vector(i * w, 600 - w)))
    walls.pop(32)
    walls.pop(30)
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
    return walls


def create_breakable_walls(r, w):
    breakable_walls = []
    available_pos = []
    wi_x = 5 * w
    wi_y = w
    while wi_y < 600:
        while wi_x < 800 - 2 * w:
            pos = Vector(wi_x, wi_y)
            if random() < r:
                breakable_walls.append(WallBreak(pos=pos))
            available_pos.append(pos)
            wi_x = wi_x + 2 * w
        wi_x = w
        wi_y = wi_y + 4 * w
    wi_x = 5 * w
    wi_y = 3 * w
    while wi_y < 600 - 2 * w:
        while wi_x < 800 - 2 * w:
            pos = Vector(wi_x, wi_y)
            if random() < r:
                breakable_walls.append(WallBreak(pos=pos))
            available_pos.append(pos)
            wi_x = wi_x + 4 * w
        wi_x = w
        wi_y = wi_y + 4 * w

    breakable_walls.append(WallBreak(pos=Vector(15 * w, -w)))

    return breakable_walls, available_pos


def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "Bomberman")
    vista = Vista()
    ########################################
    # PROGRAMA PRINCIPAL
    ########################################
    bomberman = Bomberman(pos=Vector(40, 30))
    fondo = Fondo()
    power_ups = []
    # create walls
    w = Wall().w
    walls = create_walls(w)

    r = 0.2  # breakable_wall creation probability
    breakable_walls, available_pos = create_breakable_walls(r, w)
    r = randint(0, len(available_pos)-1)
    power_ups.append(VelPowerUp(pos=available_pos[r]))
    available_pos.pop(r)
    r = randint(0, len(available_pos) - 1)
    power_ups.append(BombPowerUp(pos=available_pos[r]))
    available_pos.pop(r)

    # se empieza a medir el tiempo
    t0 = pygame.time.get_ticks()
    dt = 0
    run = True
    while run:
        ########################################
        # CONTROLADOR DE EVENTOS
        ########################################
        if bomberman.win:
            run = False

        if not bomberman.alive:
            run = False

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

        # que cada objeto actue durante el intervalo de tiempo tardado
        t1 = pygame.time.get_ticks()  # mide el tiempo final
        dt = (t1 - t0) / 1000

        # El juego acaba cuando cai por mucho tiempo
        vista.dibujar(bomberman, move_right, move_left, move_up, move_down, fondo, walls, breakable_walls, power_ups)
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

        # el tiempo inicial de la siguiente iteracion es el tiempo final de esta iteracion
        t0 = t1

    pygame.quit()


main()
