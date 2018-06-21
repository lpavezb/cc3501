from CC3501Utils import *


class Vista:
    def dibujar(self, bomberman, fondo, walls, breakable_walls, power_ups, enemies, all_bombs):
        # delete not active objects
        clean(all_bombs)
        clean(breakable_walls)
        clean(power_ups)
        clean(enemies)

        for bomb in all_bombs:
            bomb.explode()

        ########################################
        # SE INICIA DIBUJO
        ########################################
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        fondo.dibujar()

        for wall in walls:
            wall.dibujar()
        for p in power_ups:
            p.dibujar()
        for wall in breakable_walls:
            wall.dibujar()
        for bomb in all_bombs:
            bomb.dibujar()
        for enemy in enemies:
            enemy.dibujar()
        bomberman.dibujar()


def collide(o1, o2):
    return collide_up(o1, o2) or collide_down(o1, o2) or collide_left(o1, o2) or collide_right(o1, o2)