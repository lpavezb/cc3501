from CC3501Utils import *


class VelPowerUp(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 50
        self.w = self.h = self.a
        self.active = True
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(0, 1, 1)
        rect(0.25, 0.25, 0.5, 0.5, self.a)
        glEnd()

    def trigger(self, bomberman):
        bomberman.set_vel(40)
        self.active = False


class BombPowerUp(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 50
        self.w = self.h = self.a
        self.active = True
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(1, 0, 1)
        rect(0.25, 0.25, 0.5, 0.5, self.a)
        glEnd()

    def trigger(self, bomberman):
        bomberman.set_bomb_place_time(bomberman.can_place_bomb_timeout/2)
        self.active = False
