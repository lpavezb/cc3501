from CC3501Utils import *


class Vista:
    def dibujar(self, players, fondo, walls, breakable_walls, power_ups, all_bombs):
        # delete not active objects
        clean(all_bombs)
        clean(breakable_walls)
        clean(power_ups)
        clean(players)

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
        for player in players:
            player.dibujar()
