from CC3501Utils import *
import time


class Bomb(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0), sound=None):
        self.a = 50
        self.place_time = time.time()
        self.active = True
        self.exploding = False
        self.invincible = True
        self.invincible_time = time.time()
        self.explode_time = 3
        self.w = 0.6 * self.a
        self.h = 0.8 * self.a
        self.explosion_sound = sound
        super().__init__(pos, rgb)

    def figura(self):
        if not self.exploding:
            self.bomb()
        else:
            self.explosion()

    def bomb(self, tx=0, ty=0):
        glBegin(GL_POLYGON)
        a = self.a
        # head
        glColor3f(0, 0, 0)
        glVertex2f((0.2 + tx) * a, (0 + ty) * a)
        glVertex2f((0 + tx) * a, (0.2 + ty) * a)
        glVertex2f((0 + tx) * a, (0.4 + ty) * a)
        glVertex2f((0.2 + tx) * a, (0.6 + ty) * a)
        glVertex2f((0.4 + tx) * a, (0.6 + ty) * a)
        glVertex2f((0.6 + tx) * a, (0.4 + ty) * a)
        glVertex2f((0.6 + tx) * a, (0.2 + ty) * a)
        glVertex2f((0.4 + tx) * a, (0 + ty) * a)

        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        rect(0.4+tx, 0.2+ty, 0.1, 0.2, a)

        rect(0.3+tx, 0.4+ty, 0.1, 0.1, a)

        glColor3f(0.5, 0.5, 0.5)
        rect(0.2+tx, 0.6+ty, 0.1, 0.1, a)
        rect(0.3+tx, 0.7+ty, 0.1, 0.1, a)
        glColor3f(1, 0, 0)
        rect(0.4+tx, 0.7+ty, 0.1, 0.1, a)

        glEnd()

    def explode(self):
        self.crear()
        if time.time() - self.invincible_time > 0.3:
            self.invincible = False
        if time.time() - self.place_time > self.explode_time:
            if not self.exploding:
                self.explosion_sound.play(0)
            self.explode_time = 1
            self.place_time = time.time()
            if self.exploding:
                self.active = False
            self.exploding = True

    def explosion(self):
        self.bomb()
        self.bomb(tx=self.w/self.a)
        self.bomb(tx=-self.w/self.a)
        self.bomb(ty=-self.h/self.a)
        self.bomb(ty=self.h/self.a)

    def destroy_range_up(self):
        b = Bomb(pos=Vector(self.pos.x, self.pos.y + self.h))
        b.invincible = False
        return b

    def destroy_range_down(self):
        b = Bomb(pos=Vector(self.pos.x, self.pos.y - self.h))
        b.invincible = False
        return b

    def destroy_range_right(self):
        b = Bomb(pos=Vector(self.pos.x + self.w, self.pos.y))
        b.invincible = False
        return b

    def destroy_range_left(self):
        b = Bomb(pos=Vector(self.pos.x - self.w, self.pos.y))
        b.invincible = False
        return b
