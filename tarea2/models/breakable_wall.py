from CC3501Utils import *


class BreakableWall(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 50
        self.w = self.h = self.a
        self.active = True
        super().__init__(pos, rgb)

    def figura(self):
        a = self.a
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        rect(0, 0, 1, 0.1, a)
        rect(0, 0.3, 1, 0.1, a)
        rect(0, 0.6, 1, 0.1, a)
        rect(0, 0.9, 1, 0.1, a)

        rect(0, 0.1, 0.5, 0.1, a)
        rect(0, 0.4, 0.5, 0.1, a)
        rect(0, 0.7, 0.5, 0.1, a)

        rect(0.6, 0.2, 0.4, 0.1, a)
        rect(0.6, 0.5, 0.4, 0.1, a)
        rect(0.6, 0.8, 0.4, 0.1, a)

        glEnd()

        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(0, 0)
        glVertex2f(0, a)

        glVertex2f(0, a)
        glVertex2f(a, a)

        glVertex2f(a, a)
        glVertex2f(a, 0)

        glVertex2f(a, 0)
        glVertex2f(0, 0)
        glEnd()