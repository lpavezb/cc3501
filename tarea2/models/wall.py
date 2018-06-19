from CC3501Utils import *


class Wall(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 25
        self.w = self.h = self.a
        super().__init__(pos, rgb)

    def figura(self):
        a = self.a
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        self.rect(0, 0, 1, 1)
        glColor3f(0.5, 0.5, 0.5)
        self.rect(0.05, 0.05, 0.9, 0.9)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(0 * a, 1 * a)
        glVertex2f(1 * a, 0 * a)

        glVertex2f(0 * a, 0 * a)
        glVertex2f(1 * a, 1 * a)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.6, 0.6, 0.6)
        self.rect(0.3, 0.3, 0.4, 0.4)
        glEnd()

    def rect(self, x1, y1, w, h):
        a = self.a

        glVertex2f(x1 * a, y1 * a)
        glVertex2f(x1 * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, y1 * a)