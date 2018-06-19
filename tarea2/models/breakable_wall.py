from CC3501Utils import *


class WallBreak(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 50
        self.w = self.h = self.a
        self.active = True
        super().__init__(pos, rgb)

    def figura(self):
        a = self.a
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        self.rect(0, 0, 1, 1)

        glColor3f(0, 0, 0)
        self.rect(0, 0.2, 0.6, 0.1)
        self.rect(0.5, 0.1, 0.5, 0.1)

        self.rect(0, 0.5, 0.6, 0.1)
        self.rect(0.5, 0.4, 0.5, 0.1)

        self.rect(0, 0.8, 0.6, 0.1)
        self.rect(0.5, 0.7, 0.5, 0.1)
        glEnd()

    def rect(self, x1, y1, w, h):
        a = self.a

        glVertex2f(x1 * a, y1 * a)
        glVertex2f(x1 * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, y1 * a)