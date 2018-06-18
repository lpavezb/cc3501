from vista import *
from models.bomberman import *
from models.fondo import *
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
    bomberman = Bomberman()
    fondo = Fondo()
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
        if keys[pygame.K_UP]:
            move_up= True

        move_down = False
        if keys[pygame.K_DOWN]:
            move_down = True

        move_right = False
        if keys[pygame.K_RIGHT]:
            move_right = True

        move_left = False
        if keys[pygame.K_LEFT]:
            move_left = True

        if keys[pygame.K_q]:
            run = False

        place_bomb = False
        if keys[pygame.K_SPACE]:
            bomberman.place_bomb()
            place_bomb = True

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
        vista.dibujar(bomberman, place_bomb, move_right, move_left, move_up, move_down, fondo, dt)
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

        # el tiempo inicial de la siguiente iteracion es el tiempo final de esta iteracion
        t0 = t1

    pygame.quit()


main()
