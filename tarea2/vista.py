from CC3501Utils import *


class Vista:
    def dibujar(self, bomberman, enemies, fondo, walls, breakable_walls, power_ups, all_bombs):
        # delete not active objects
        clean(all_bombs)
        clean(breakable_walls)
        clean(power_ups)
        clean(enemies)

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
        for player in enemies:
            player.dibujar()
        bomberman.dibujar()

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
