from CC3501Utils import *
import time


class Bomb(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 10
        self.place_time = time.time()
        self.active = True
        self.exploding = False
        self.w = 0
        self.h = 0
        super().__init__(pos, rgb)

    def figura(self):
        if not self.exploding:
            self.bomb()
        else:
            self.explosion()

    def bomb(self):
        self.w = 3 * self.a
        self.h = 4 * self.a

        glBegin(GL_POLYGON)
        a = self.a
        # head
        glColor3f(0, 0, 0)
        glVertex2f(1 * a, 0 * a)
        glVertex2f(0 * a, 1 * a)
        glVertex2f(0 * a, 2 * a)
        glVertex2f(1 * a, 3 * a)
        glVertex2f(2 * a, 3 * a)
        glVertex2f(3 * a, 2 * a)
        glVertex2f(3 * a, 1 * a)
        glVertex2f(2 * a, 0 * a)

        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        self.rect(2, 1, 0.5, 1)

        self.rect(1.5, 2, 0.5, 0.5)

        glColor3f(0.5, 0.5, 0.5)
        self.rect(1, 3, 0.5, 0.5)
        self.rect(1.5, 3.5, 0.5, 0.5)
        glColor3f(1, 0, 0)
        self.rect(2, 3.5, 0.5, 0.5)

        glEnd()

    def rect(self, x1, y1, w, h):
        a = self.a

        glVertex2f(x1 * a, y1 * a)
        glVertex2f(x1 * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, y1 * a)

    def explode(self, timeout=1):
        self.crear()
        if time.time() - self.place_time > timeout:
            self.place_time = time.time()
            if self.exploding:
                self.active = False
            self.exploding = True

    def explosion(self):
        self.a = 15
        self.bomb()


