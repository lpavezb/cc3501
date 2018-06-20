from CC3501Utils import *
from models.enemy import Enemy


class Vista:
    def dibujar(self, bomberman, move_right, move_left, move_up, move_down, fondo, walls, breakable_walls, power_ups):
        ##############################################
        # MOVIMIENTO DE CAMARA SOBRE PERSONAJE
        ##############################################
        # IMPORTANTE: Tengo un bug con el dt, por alguna razon al usar el dt entre iteraciones
        # el programa corre ULTRA lento, asi que preferi elegir un valor de tiempo
        # conveniente para que tenga sentido jugar el juego. (0.4)
        bomberman.mover(0.4, move_right, move_left, move_up, move_down)

        all_walls = walls + breakable_walls
        for wall in all_walls:
            if move_left and collide_left(bomberman, wall):
                move_left = False
                bomberman.stop_left(wall)
            if move_right and collide_right(bomberman, wall):
                move_left = False
                bomberman.stop_right(wall)
            if move_up and collide_up(bomberman, wall):
                move_up = False
                bomberman.stop_up(wall)
            if move_down and collide_down(bomberman, wall):
                move_down = False
                bomberman.stop_down(wall)

        for power_up in power_ups:
            if move_left and collide_left(bomberman, power_up):
                power_up.trigger(bomberman)
            if move_right and collide_right(bomberman, power_up):
                power_up.trigger(bomberman)
            if move_up and collide_up(bomberman, power_up):
                power_up.trigger(bomberman)
            if move_down and collide_down(bomberman, power_up):
                power_up.trigger(bomberman)

        for bomb in bomberman.bombs:
            if move_left and collide_left(bomberman, bomb) and not bomb.invincible:
                move_left = False
                bomberman.stop_left(bomb)
            if move_right and collide_right(bomberman, bomb) and not bomb.invincible:
                move_left = False
                bomberman.stop_right(bomb)
            if move_up and collide_up(bomberman, bomb) and not bomb.invincible:
                move_up = False
                bomberman.stop_up(bomb)
            if move_down and collide_down(bomberman, bomb) and not bomb.invincible:
                move_down = False
                bomberman.stop_down(bomb)

        for bomb in bomberman.bombs:
            if bomb.exploding and collide(bomberman, bomb):
                bomberman.alive = False
            if bomb.exploding and collide(bomberman, bomb.destroy_range_up()):
                bomberman.alive = False
            if bomb.exploding and collide(bomberman, bomb.destroy_range_down()):
                bomberman.alive = False
            if bomb.exploding and collide(bomberman, bomb.destroy_range_left()):
                bomberman.alive = False
            if bomb.exploding and collide(bomberman, bomb.destroy_range_right()):
                bomberman.alive = False

        for wall in breakable_walls:
            for bomb in bomberman.bombs:
                if bomb.exploding and collide(bomb, wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_up(), wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_down(), wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_left(), wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_right(), wall):
                    wall.active = False
        # delete not active objects
        clean(bomberman.bombs)
        clean(breakable_walls)
        clean(power_ups)

        # Genera un marco donde la pera no mueve la camara
        ##############################################
        # INTERACCION PLATAFORMAS
        ##############################################

        ########################################
        # SE INICIA DIBUJO
        ########################################
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        # dibujar figuras
        fondo.dibujar()
        bomberman.explode_bomb()
        for wall in walls:
            wall.dibujar()
        for p in power_ups:
            p.dibujar()
        for wall in breakable_walls:
            wall.dibujar()
        for bomb in bomberman.bombs:
            bomb.dibujar()
        Enemy(pos=Vector(40, 30)).dibujar()
        bomberman.dibujar()


def collide(o1, o2):
    return collide_up(o1, o2) or collide_down(o1, o2) or collide_left(o1, o2) or collide_right(o1, o2)