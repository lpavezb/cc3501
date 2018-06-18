from CC3501Utils import *


class Bomb(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 20
        super().__init__(pos, rgb)

    def figura(self):
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